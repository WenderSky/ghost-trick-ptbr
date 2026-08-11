# Ghost Trick: Phantom Detective — tradução para português do Brasil

Tradução completa e não oficial de *Ghost Trick: Phantom Detective* (versão de PC/Steam, 2023).

**12.197 falas** — roteiro, menus, sistema e a enciclopédia — mais as **22 imagens
que têm texto desenhado dentro**: títulos de capítulo, logotipo, telas de
carregamento e avisos.

<!-- Coloque aqui um print da tela de título de capítulo em português. -->

## Instalação

Baixe o pacote da sua plataforma na página de [**Releases**](../../releases).

**Windows** — dois cliques em `INSTALAR.bat`. Ele procura a pasta do jogo sozinho,
em todas as bibliotecas do Steam, inclusive em outros discos.

**Steam Deck** — copie a pasta para o Deck, entre no Modo Área de Trabalho, abra o
Konsole e rode:

```bash
bash instalar.sh
```

O jogo já abre em português: a tradução ocupa o lugar do inglês, então não há
opção para trocar. Não é preciso mexer em Proton, variável de ambiente ou opção
de inicialização.

Para remover, rode `DESINSTALAR.bat` ou `bash desinstalar.sh`.

## O que esperar

Os nomes dos personagens foram mantidos como no original — Sissel, Lynne,
Missile, Cabanela, Jowd, Kamila, Yomiel e os demais. A tradução foi feita a
partir do texto em inglês do PC, não portada da versão de Nintendo DS.

Os horários das telas de capítulo continuam em AM/PM, como no original.

## Como funciona

O jogo roda em RE Engine e guarda tudo num `re_chunk_000.pak` de 5,9 GB. A
tradução é distribuída como `re_chunk_000.pak.patch_001.pak`, um arquivo separado
que o motor carrega por cima — **o pak original nunca é modificado**. Apagar o
patch devolve o jogo ao inglês, sem reinstalar nada.

Os textos ficam em 77 arquivos `.msg.18`. A tradução ocupa a coluna `English`,
porque o jogo abre nesse idioma por padrão e assim ninguém precisa mexer em
opção nenhuma.

### As texturas

Vinte e duas imagens têm o texto desenhado dentro e não passam pelo sistema de
legendas. O jogo já traz cada uma em nove idiomas, e o espanhol coincide palavra
por palavra com o português em dezenove delas — "Capítulo 1", "Capítulo final" e
o atlas das telas de carregamento saem prontos. Nessas, o binário oficial foi
copiado para o slot do inglês, sem recompressão.

As outras três precisaram de trabalho:

| Imagem | Problema | Solução |
| --- | --- | --- |
| Contador dos 4 minutos | espanhol diz "de muerte" | "morte" recortada da versão **italiana**, com correção de escala e linha de base |
| Logotipo | "Detective" vs. "Detetive" | o "c" removido com sua sombra e o subtítulo recentralizado |
| Aviso de fotossensibilidade | texto inteiramente diferente | recomposto no mesmo corpo, entrelinha e cor do original |

## Refazer a partir da fonte

A pasta [`fonte/`](fonte) tem o material que produz o patch:

- `traducoes/` — os textos em JSON, um arquivo por lote, na forma
  `{"arquivo.csv": {"entrada": "texto"}}`;
- `GLOSSARIO.md` — termos fixos e as decisões de voz de cada personagem;
- `ferramentas/aplicar_traducao.py` — aplica um JSON aos CSVs e valida
  sequência de tags `<TRCK>`, marcadores, escapes e largura de linha;
- `ferramentas/preparar_lote.py` — separa o próximo lote e mostra o andamento.

Extrair e reempacotar o jogo exige o [AJT-Tools](https://github.com/Aclios/AJT-Tools),
que não é redistribuído aqui.

## Aviso

Projeto de fã, sem relação com a Capcom. *Ghost Trick: Phantom Detective* e todo
o material original pertencem à Capcom Co., Ltd. É preciso ter uma cópia legítima
do jogo — nada aqui o substitui ou permite jogá-lo sem comprá-lo.

Verificar a integridade dos arquivos pelo Steam remove a tradução. Se isso
acontecer, rode o instalador de novo.
