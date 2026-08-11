"""Gera um lote de trabalho com o texto em inglês ainda não traduzido.

Considera pendente toda entrada cuja coluna English continua idêntica ao
inglês original guardado em `_ref_en` — comparação exata, sem heurística.
Placeholders #Rejected# e entradas vazias ficam de fora.

Uso:
    python preparar_lote.py st01/st01_0000.msg.18.csv --tamanho 40
    python preparar_lote.py --resumo
"""

import argparse
import csv
import json
import sys
from pathlib import Path

csv.field_size_limit(10_000_000)

MSG_DIR = Path(r"D:\gt_trad\tools\AJT-Tools\msg\gamedesign\text")
REF_DIR = Path(r"D:\gt_trad\_ref_en")
LOTES_DIR = Path(r"D:\gt_trad\lotes")
REVISADAS = Path(r"D:\gt_trad\revisadas.json")


def registro() -> dict[str, list[str]]:
    if not REVISADAS.exists():
        return {}
    return json.loads(REVISADAS.read_text(encoding="utf-8"))


def ler(caminho: Path) -> dict[str, str]:
    with caminho.open(encoding="utf-8-sig", newline="") as f:
        return {l["entry name"]: (l.get("English") or "") for l in csv.DictReader(f)}


def pendentes_de(rel: str) -> tuple[dict[str, str], int, int]:
    """Entradas ainda por traduzir, mais os totais (traduzíveis, prontas)."""
    atual = ler(MSG_DIR / rel)
    original = ler(REF_DIR / rel)
    # entradas cuja tradução ficou igual ao inglês só são reconhecidas pelo registro
    tratadas = set(registro().get(rel, []))

    pendentes, traduziveis, prontas = {}, 0, 0
    for nome, texto_orig in original.items():
        if not texto_orig.strip() or "#Rejected#" in texto_orig:
            continue
        traduziveis += 1
        if nome in tratadas or atual.get(nome, "") != texto_orig:
            prontas += 1
        else:
            pendentes[nome] = texto_orig
    return pendentes, traduziveis, prontas


def resumo() -> None:
    arquivos = sorted(p.relative_to(REF_DIR).as_posix() for p in REF_DIR.rglob("*.csv"))
    tot_trad = tot_pronto = 0
    print(f"{'arquivo':<34} {'total':>6} {'prontas':>8} {'faltam':>7}")
    for rel in arquivos:
        pend, traduziveis, prontas = pendentes_de(rel)
        tot_trad += traduziveis
        tot_pronto += prontas
        marca = "  <-- em andamento" if 0 < prontas < traduziveis else ""
        print(f"{rel:<34} {traduziveis:>6} {prontas:>8} {len(pend):>7}{marca}")
    pct = tot_pronto / tot_trad * 100 if tot_trad else 0
    print(f"\nTOTAL: {tot_pronto}/{tot_trad} entradas ({pct:.1f}%)")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepara um lote de tradução")
    parser.add_argument("arquivo", nargs="?", help="caminho relativo do CSV")
    parser.add_argument("--tamanho", type=int, default=40, help="entradas por lote")
    parser.add_argument("--resumo", action="store_true", help="progresso geral")
    args = parser.parse_args()

    if args.resumo:
        resumo()
        return 0

    if not args.arquivo:
        parser.error("informe o arquivo ou use --resumo")

    if not (REF_DIR / args.arquivo).exists():
        print(f"ERRO: {args.arquivo} não existe")
        return 1

    pendentes, traduziveis, prontas = pendentes_de(args.arquivo)
    selecionadas = dict(list(pendentes.items())[: args.tamanho])

    LOTES_DIR.mkdir(parents=True, exist_ok=True)
    nome = args.arquivo.replace("/", "_").replace(".csv", "")
    destino = LOTES_DIR / f"{nome}_lote.json"
    destino.write_text(
        json.dumps(selecionadas, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"arquivo....: {args.arquivo}")
    print(f"traduzíveis: {traduziveis}")
    print(f"prontas....: {prontas}")
    print(f"pendentes..: {len(pendentes)}")
    print(f"neste lote.: {len(selecionadas)} -> {destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
