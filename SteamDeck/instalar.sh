#!/usr/bin/env bash
# Instala a tradução PT-BR de Ghost Trick no Steam Deck (ou qualquer Linux com Steam).
set -uo pipefail

PAK="re_chunk_000.pak.patch_001.pak"
AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

printf '\n  Ghost Trick: Phantom Detective — tradução PT-BR\n'
printf '  ----------------------------------------------\n\n'

if [ ! -f "$AQUI/$PAK" ]; then
  printf '  Não achei o %s aqui do lado.\n' "$PAK"
  printf '  Extraia o pacote inteiro antes de rodar este script.\n\n'
  exit 1
fi

# Bibliotecas Steam: as padrão, as do cartão SD e as declaradas no libraryfolders.vdf
CANDIDATAS=(
  "$HOME/.local/share/Steam"
  "$HOME/.steam/steam"
  "$HOME/.var/app/com.valvesoftware.Steam/data/Steam"
)
for m in /run/media/*/ /run/media/deck/*/ ; do
  [ -d "$m" ] && CANDIDATAS+=("${m%/}")
done
for vdf in "$HOME/.local/share/Steam/steamapps/libraryfolders.vdf" \
           "$HOME/.steam/steam/steamapps/libraryfolders.vdf"; do
  # sed POSIX em vez de grep -oP: -P depende do locale e nem sempre existe
  [ -f "$vdf" ] && while IFS= read -r p; do
    [ -n "$p" ] && CANDIDATAS+=("$p")
  done < <(sed -n 's/.*"path"[[:space:]]*"\(.*\)".*/\1/p' "$vdf" 2>/dev/null)
done

DESTINO=""
for b in "${CANDIDATAS[@]}"; do
  for alvo in "$b/steamapps/common/Ghost Trick" "$b/common/Ghost Trick"; do
    if [ -f "$alvo/re_chunk_000.pak" ]; then DESTINO="$alvo"; break 2; fi
  done
done

if [ -z "$DESTINO" ]; then
  printf '  Não encontrei a pasta do jogo automaticamente.\n'
  printf '  No Steam: Ghost Trick > engrenagem > Propriedades > Arquivos\n'
  printf '  instalados > Procurar, e cole o caminho aqui.\n\n'
  read -r -p '  Caminho da pasta Ghost Trick: ' DESTINO
  DESTINO="${DESTINO%\"}"; DESTINO="${DESTINO#\"}"
fi

if [ ! -f "$DESTINO/re_chunk_000.pak" ]; then
  printf '\n  Isso não parece a pasta do jogo: %s\n' "$DESTINO"
  printf '  Deve existir um re_chunk_000.pak lá dentro.\n\n'
  exit 1
fi

printf '  Jogo encontrado em:\n  %s\n\n' "$DESTINO"

if [ -f "$DESTINO/$PAK" ] && [ ! -f "$DESTINO/$PAK.backup" ]; then
  cp -- "$DESTINO/$PAK" "$DESTINO/$PAK.backup"
  printf '  Já havia um patch instalado; guardei uma cópia como .backup\n'
fi

if cp -- "$AQUI/$PAK" "$DESTINO/$PAK"; then
  printf '\n  Pronto! A tradução está instalada.\n\n'
  printf '  O jogo já abre em português — não precisa mexer em opção nenhuma.\n'
  printf '  Para remover, rode ./desinstalar.sh (o jogo volta ao inglês).\n\n'
else
  printf '\n  Não consegui copiar. Se o jogo está no cartão SD, confira se\n'
  printf '  o cartão não está protegido contra escrita.\n\n'
  exit 1
fi
