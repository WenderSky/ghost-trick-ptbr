# Texturas

As imagens que entraram no patch, e o material usado para montá-las.

| Arquivo | O que é |
| --- | --- |
| `upp_PT.png` | Contador dos quatro minutos. "min. antes" saiu do espanhol, **"morte"** da versão italiana, com escala corrigida em 7,4% e linha de base realinhada. Formato RGBA8 no jogo, então entra sem perda nenhuma. |
| `title_PT.png` | Logotipo com "Detetive fantasma". Partiu do espanhol; o "c" de *Detective* foi removido com a sombra dele e o subtítulo, recentralizado sob o logo. |
| `aviso_PT.png` | Aviso de fotossensibilidade, a única recomposta do zero. A palavra "Aviso" veio do espanhol; as seis linhas foram redesenhadas em Arial 44px, que casa com o peso do original — a Helvetica que vem no jogo só tem o peso **bold**, e o corpo do aviso é regular. |
| `fantasma.png` | O Sissel fantasma recortado do logotipo, com os óculos. Usado na imagem de marca do guia da Steam. |
| `fundo_p2.png` | O relógio das telas de capítulo **sem texto nenhum**, obtido combinando as 162 variantes que existem no jogo (18 capítulos × 9 idiomas) e ficando com o valor mais escuro de cada pixel. Como o texto é claro e muda de posição em cada idioma, ele desaparece. |

As outras 19 texturas não estão aqui porque não foram desenhadas: são o binário
espanhol oficial da Capcom, copiado para o slot do inglês sem recompressão. Elas
saem do próprio jogo — veja a seção "As imagens com texto" no README principal.

## Como aplicar

Com o [AJT-Tools](https://github.com/Aclios/AJT-Tools) e o jogo já extraído:

```python
from AJTTools.plugins.tex.src import Tex
from pathlib import Path

destino = Path('.../cmn_upp_05_iml4.tex.35.en')   # cópia do original
t = Tex(destino)
t.import_file(Path('upp_PT.png'))
t.save(destino)
```

O PNG precisa ter exatamente as mesmas dimensões do original.
