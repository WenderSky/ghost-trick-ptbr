"""Aplica traduções PT-BR nos CSVs exportados, escrevendo na coluna alvo.

Recebe um JSON no formato:

    {"st01/st01_0000.msg.18.csv": {"st01_0000_m01_0000": "texto traduzido", ...}}

e grava o texto na coluna de idioma escolhida (por padrão English, que é o
slot que o mod sobrescreve).

Validações, todas contra o inglês original guardado em `_ref_en`:

- **tags**: a sequência de `<...>` da tradução tem que ser igual à do original,
  porque são efeitos sincronizados com a fala (som, tremida, flash, pausa).
- **largura**: o limite de cada arquivo é a maior linha que o próprio inglês
  usa ali. Isso adapta ao contexto: diálogo fica em ~37 caracteres, enquanto
  mensagens de sistema em cmn/ e database/ podem passar de 100.
- **quebras**: o jogo usa \\r\\n; \\n solto é convertido automaticamente.

Uso:
    python aplicar_traducao.py traducoes.json [--coluna English] [--conferir]
"""

import argparse
import csv
import io
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

csv.field_size_limit(10_000_000)

MSG_DIR = Path(r"D:\gt_trad\tools\AJT-Tools\msg\gamedesign\text")
REF_DIR = Path(r"D:\gt_trad\_ref_en")
# registro de entradas já tratadas: sem ele, falas que ficam iguais em
# português ("Heh heh.") apareceriam como pendentes para sempre
REVISADAS = Path(r"D:\gt_trad\revisadas.json")
TAG = re.compile(r"<[^>]*>")
# placeholders que o jogo substitui em tempo de execução, ex.: "{0} MB"
CHAVE = re.compile(r"\{[^}]*\}")
# "&<;" e "&>;" são escapes que o jogo desenha como um único caractere (≪ ≫).
# Precisam sair da frente antes de procurar tags, senão o "<" deles é lido
# como início de tag, e contam como 1 caractere ao medir a largura.
ESCAPE = re.compile(r"&[<>];")


def neutralizar(texto: str) -> str:
    return ESCAPE.sub("\x00", texto)


def tags_de(texto: str) -> list[str]:
    return TAG.findall(neutralizar(texto))


def linhas_visiveis(texto: str) -> list[str]:
    """Texto sem tags, quebrado nas linhas que o jogador realmente vê."""
    limpo = TAG.sub("", neutralizar(texto))
    return limpo.replace("\r\n", "\n").split("\n")


@lru_cache(maxsize=None)
def referencia(rel: str) -> tuple[dict[str, str], int]:
    """Devolve o inglês original por entrada e a maior linha usada no arquivo."""
    caminho = REF_DIR / rel
    originais: dict[str, str] = {}
    limite = 0

    with caminho.open(encoding="utf-8-sig", newline="") as f:
        for linha in csv.DictReader(f):
            texto = linha.get("English") or ""
            originais[linha["entry name"]] = texto
            if "#Rejected#" in texto:
                continue
            for visivel in linhas_visiveis(texto):
                limite = max(limite, len(visivel.rstrip()))

    return originais, limite


def avisos(rel: str, entry: str, traduzido: str) -> list[str]:
    originais, limite = referencia(rel)
    original = originais.get(entry)
    problemas = []

    if original is None:
        return [f"{rel}: entrada '{entry}' não existe no inglês original"]

    if tags_de(original) != tags_de(traduzido):
        problemas.append(f"{entry}: a sequência de tags não bate com o original")

    if ESCAPE.findall(original) != ESCAPE.findall(traduzido):
        problemas.append(f"{entry}: os escapes &<; / &>; não foram preservados")

    if sorted(CHAVE.findall(original)) != sorted(CHAVE.findall(traduzido)):
        problemas.append(
            f"{entry}: os placeholders {CHAVE.findall(original)} não foram preservados"
        )

    for i, visivel in enumerate(linhas_visiveis(traduzido), 1):
        tamanho = len(visivel.rstrip())
        if tamanho > limite:
            problemas.append(
                f"{entry}: linha {i} tem {tamanho} caracteres, acima do limite "
                f"{limite} deste arquivo: {visivel!r}"
            )
    return problemas


def main() -> int:
    parser = argparse.ArgumentParser(description="Aplica traduções nos CSVs do jogo")
    parser.add_argument("json", help="arquivo JSON com as traduções")
    parser.add_argument("--coluna", default="English", help="coluna de idioma alvo")
    parser.add_argument(
        "--conferir",
        action="store_true",
        help="só valida tags, largura e quebras, sem gravar nada",
    )
    args = parser.parse_args()

    traducoes = json.loads(Path(args.json).read_text(encoding="utf-8"))
    total = normalizadas = 0
    todos_problemas = []

    registro = (
        json.loads(REVISADAS.read_text(encoding="utf-8"))
        if REVISADAS.exists()
        else {}
    )

    for rel, entradas in traducoes.items():
        caminho = MSG_DIR / rel
        if not caminho.exists():
            todos_problemas.append(f"{rel}: arquivo não existe")
            continue

        with caminho.open(encoding="utf-8-sig", newline="") as f:
            leitor = csv.reader(f)
            cabecalho = next(leitor)
            linhas = list(leitor)

        idx_nome = cabecalho.index("entry name")
        idx_alvo = cabecalho.index(args.coluna)
        pendentes = {}

        # o jogo usa \r\n; aceitamos \n solto no JSON e convertemos aqui
        for nome, texto in entradas.items():
            corrigido = texto.replace("\r\n", "\n").replace("\n", "\r\n")
            if corrigido != texto:
                normalizadas += 1
            pendentes[nome] = corrigido

        tratadas = set(registro.get(rel, []))

        for linha in linhas:
            nome = linha[idx_nome]
            if nome not in pendentes:
                continue
            novo = pendentes.pop(nome)
            todos_problemas += avisos(rel, nome, novo)
            linha[idx_alvo] = novo
            tratadas.add(nome)
            total += 1

        registro[rel] = sorted(tratadas)

        for nome in pendentes:
            todos_problemas.append(f"{rel}: entrada '{nome}' não encontrada no CSV")

        if not args.conferir:
            with io.open(caminho, "w", encoding="utf-8-sig", newline="\n") as f:
                escritor = csv.writer(f, delimiter=",")
                escritor.writerow(cabecalho)
                escritor.writerows(linhas)

    if not args.conferir:
        REVISADAS.write_text(
            json.dumps(registro, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    if todos_problemas:
        print(f"-- {len(todos_problemas)} avisos --")
        for problema in todos_problemas:
            print(f"  {problema}")

    acao = "conferidas" if args.conferir else "aplicadas"
    if normalizadas:
        print(f"{normalizadas} entradas tiveram as quebras normalizadas para \\r\\n.")
    print(f"{total} entradas {acao} na coluna {args.coluna}.")
    return 1 if todos_problemas else 0


if __name__ == "__main__":
    sys.exit(main())
