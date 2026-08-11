# 👻 Ghost Trick: Phantom Detective — Tradução PT-BR

> Tradução **não-oficial** para **Português do Brasil** de *Ghost Trick: Phantom Detective* (Steam, 2023) — **texto completo + as imagens com texto desenhado dentro**.

<p align="center">
  <img alt="Idioma" src="https://img.shields.io/badge/idioma-Portugu%C3%AAs%20(BR)-009c3b">
  <img alt="Plataforma" src="https://img.shields.io/badge/plataforma-PC%20%2B%20Steam%20Deck-1b2838">
  <img alt="Versão" src="https://img.shields.io/badge/vers%C3%A3o-1.0-c41020">
  <img alt="Cobertura" src="https://img.shields.io/badge/cobertura-100%25-brightgreen">
  <img alt="Uso" src="https://img.shields.io/badge/uso-n%C3%A3o--comercial-important">
</p>

---

## 📜 Sobre

*Ghost Trick* é o jogo do Shu Takumi (o criador de *Ace Attorney*) em que você joga como um fantasma que perdeu a memória e tem **quatro minutos** para mudar o destino de quem acabou de morrer. É um dos melhores roteiros que a Capcom já escreveu — e nunca saiu em português.

Esta tradução leva **todo o texto do jogo** para o português do Brasil: as 12.197 falas do roteiro, os menus, o sistema, a enciclopédia de personagens **e também as 22 imagens que têm o texto desenhado dentro** — os títulos de capítulo, o logotipo, as telas de carregamento e os avisos.

A tradução ocupa o **slot do idioma Inglês**. Como o jogo já abre em inglês por padrão, **não é preciso mexer em opção nenhuma**: instalou, abriu, está em português.

> ⚠️ **Aviso:** esta é uma **tradução amadora**, feita por um fã, e **pode conter erros** — typos, alguma frase com sentido um pouco diferente do original, ou uma quebra de linha imperfeita numa caixa de diálogo. Não é um trabalho profissional/oficial. Se encontrar algum erro, abra uma [*issue*](../../issues) com um print que eu corrijo nas próximas versões. 🙂

---

## 🎮 O que foi traduzido

| Conteúdo | Entradas | Cobertura |
|------|:---:|:---:|
| **Roteiro e diálogos** | 10.913 | ✅ 100% |
| **Enciclopédia de personagens** | 514 | ✅ 100% |
| **Menus e mensagens de sistema** | 512 | ✅ 100% |
| **Nomes de objetos e ações** | 261 | ✅ 100% |
| **Imagens com texto** | 22 | ✅ 100% |

Isso inclui:

- 📖 **História completa** — os 17 capítulos mais o capítulo final, do prólogo ao epílogo
- 💬 Todos os **diálogos**, incluindo as falas opcionais quando você examina cenário
- 🐕 As falas do **Missile**, com o jeitinho dele de nomear as coisas *(o telefone é "aquele 'Alô?' preto")*
- 📚 A **enciclopédia** — todos os personagens e suas descrições
- 🧭 **Menus, opções, salvamento, seleção de capítulo** e mensagens de sistema
- 🔍 **Nomes de todos os objetos** que você possui e das ações que faz neles
- 🖼️ **Títulos de capítulo, logotipo, telas de carregamento e avisos** (veja abaixo)

O texto passou por uma **verificação automática** nos 77 arquivos do jogo: sequência das tags de efeito (`<TRCK>` — som, tremida, flash, pausa), marcadores, escapes e largura máxima de linha de cada arquivo. **0 divergências** no resultado final.

---

## 🖼️ As imagens com texto

Vinte e duas imagens do jogo têm o texto **desenhado dentro** e não passam pelo sistema de legendas. Elas costumam ficar em inglês nas traduções de fã — aqui, não.

O jogo já traz cada uma dessas imagens em **nove idiomas**. O espanhol coincide palavra por palavra com o português em dezenove delas: *"Capítulo 1"*, *"Capítulo final"* e o atlas das telas de carregamento saem prontos. Nessas, o **binário oficial da Capcom** foi copiado para o slot do inglês — sem redesenho e sem recompressão.

As outras três precisaram de trabalho:

| Imagem | O problema | Como foi resolvido |
|---|---|---|
| **Contador dos 4 minutos** | espanhol diz *"de muerte"* | a palavra **"morte"** foi recortada da versão **italiana**, com correção de escala e de linha de base |
| **Logotipo** | espanhol diz *"Detective"* | o **"c"** foi removido com a sombra dele e o subtítulo, recentralizado sob o logo |
| **Aviso de fotossensibilidade** | texto inteiramente diferente | recomposto no mesmo corpo, entrelinha e cor do original |

Nenhuma letra foi redesenhada do zero: até nas três acima, os glifos vieram do próprio jogo, em outros idiomas.

---

## 🚫 O que **não** foi traduzido (de propósito)

| Item | Por quê |
|------|---------|
| Nomes dos personagens (Sissel, Lynne, Missile, Cabanela, Jowd, Kamila, Yomiel...) | Mantidos no original, como na versão internacional |
| O logotipo **Ghost Trick** | É o nome comercial da obra; só o subtítulo virou *"Detetive fantasma"* |
| Horários das telas de capítulo (**7:31 PM**) | Mantidos em AM/PM, como no original, para não ficar meio a meio com o menu de seleção de capítulo |
| Aviso de copyright da Capcom | Texto jurídico, fica como está |

---

## 🛠️ Como foi feito (resumo técnico)

O jogo roda em **RE Engine** e guarda tudo num `re_chunk_000.pak` de **5,9 GB**.

1. **Desempacotamento** do pak (formato **KPKA v4**) com o [AJT-Tools](https://github.com/Aclios/AJT-Tools), feito para *Ghost Trick* e *Apollo Justice*.
2. Os textos ficam em **77 arquivos `.msg.18`**, com uma coluna por idioma. A tradução ocupa a coluna **English** — o jogo abre nesse idioma por padrão, então o jogador não precisa mexer em nada.
3. **Ferramenta de validação própria**: cada lote traduzido é conferido contra o inglês original antes de gravar — sequência e contagem das tags `<TRCK>`, marcadores `{n}`, escapes e a **largura máxima de linha de cada arquivo** (varia de 27 a 107 caracteres, dependendo da caixa de diálogo).
4. **Texturas**: comparação das nove variantes de idioma de cada imagem para descobrir quais podiam ser reaproveitadas, e recomposição das demais a partir de glifos originais.
5. **Distribuição como patch**: o resultado vira um `re_chunk_000.pak.patch_001.pak`, que o motor carrega por cima. **O pak original nunca é modificado.**

Uma curiosidade do processo: dá para recuperar o **fundo limpo** de uma tela de capítulo — o relógio vermelho sem texto nenhum — combinando as 162 variantes existentes (18 capítulos × 9 idiomas) e ficando com o valor mais escuro de cada pixel. O texto simplesmente desaparece.

### Refazer a partir da fonte

A pasta [`fonte/`](fonte) tem o material que produz a tradução:

- [`traducoes/`](fonte/traducoes) — os textos em JSON, um arquivo por lote
- [`GLOSSARIO.md`](fonte/GLOSSARIO.md) — termos fixos e as decisões de voz de cada personagem
- [`ferramentas/aplicar_traducao.py`](fonte/ferramentas) — aplica um JSON e valida tudo que está no item 3
- [`ferramentas/preparar_lote.py`](fonte/ferramentas) — separa o próximo lote e mostra o andamento

---

## 💾 Instalação

> **Requisitos:** o jogo *Ghost Trick: Phantom Detective* instalado pela **Steam**. Não precisa de Python, nem de mexer em Proton, variável de ambiente ou opção de inicialização.

Baixe o pacote da sua plataforma na página de [**Releases**](../../releases/latest).

### 🪟 Windows

1. Baixe e **descompacte** `GhostTrick_PTBR_Windows.zip`.
2. **Feche o jogo.**
3. Dê **duplo-clique** em `INSTALAR.bat`.
4. Ele encontra a pasta do jogo sozinho, em qualquer biblioteca do Steam, **inclusive em outro disco**. *(Se não achar, ele pergunta o caminho.)*
5. Pronto! Abra o jogo — já está em português.

### 🎮 Steam Deck

1. **Feche o jogo** e vá para o **Modo Área de Trabalho**.
2. Copie a pasta `GhostTrick_PTBR_SteamDeck` para o Deck (ex.: `~/Downloads`).
3. Abra o **Konsole** e rode:
   ```bash
   cd ~/Downloads/SteamDeck
   bash instalar.sh
   ```
4. Ele detecta o jogo no SSD **ou no cartão SD**.
5. Volte ao **Modo Jogo** e abra o jogo — já está em português.

> 💡 Rode com `bash instalar.sh` mesmo, e não `./instalar.sh`: o bit de execução se perde quando o arquivo passa pelo Windows.

---

## ↩️ Como reverter

Rode o `DESINSTALAR.bat` (Windows) ou `bash desinstalar.sh` (Deck).

Ou, na mão: a tradução é **um arquivo só** dentro da pasta do jogo, chamado `re_chunk_000.pak.patch_001.pak`. Apagar ele já devolve o inglês, sem reinstalar nada.

> ⚠️ **Verificar a integridade dos arquivos pelo Steam também remove a tradução** — é o comportamento normal do Steam com arquivos que não são dele. Se isso acontecer, é só rodar o instalador de novo.

A tradução **não encosta nos saves** e não atrapalha as conquistas.

---

## ⚖️ Licença e uso

Esta é uma **tradução de fã**, feita **sem fins lucrativos** e **sem qualquer afiliação** com a Capcom.

- ✅ **Pode** baixar, usar e compartilhar **gratuitamente**.
- ✅ **Pode** repostar, desde que **credite** o autor e **mantenha** este aviso.
- ❌ **É proibido vender, cobrar, monetizar ou lucrar** de qualquer forma com esta tradução.
- ❌ **É proibido distribuir os arquivos do jogo.** Compartilhe **apenas o patch** deste repositório — nunca o `re_chunk_000.pak` original da Capcom.

*Ghost Trick: Phantom Detective* e todos os nomes relacionados são marcas registradas da **Capcom Co., Ltd.** Este projeto não é oficial e não substitui a compra do jogo.

---

## 🙏 Créditos

**Tradução, engenharia reversa e ferramentas:** **Wender_sky** *(Steam)*

Ferramenta de desempacotamento: [AJT-Tools](https://github.com/Aclios/AJT-Tools), de Aclios.

Feito com muito café e respeito por um dos melhores roteiros da Capcom. 🕯️

---

<p align="center"><i>“É o que os cachorrinhos fazem!”</i><br><sub>— Missile</sub></p>
