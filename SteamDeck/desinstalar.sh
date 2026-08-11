#!/usr/bin/env bash
# Remove a tradução PT-BR de Ghost Trick.
set -uo pipefail
PAK="re_chunk_000.pak.patch_001.pak"

printf '\n  Removendo a tradução PT-BR de Ghost Trick\n\n'

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

ACHOU=0
for b in "${CANDIDATAS[@]}"; do
  for alvo in "$b/steamapps/common/Ghost Trick" "$b/common/Ghost Trick"; do
    if [ -f "$alvo/$PAK" ]; then
      rm -f -- "$alvo/$PAK" "$alvo/$PAK.backup"
      printf '  Removido de: %s\n' "$alvo"
      ACHOU=1
    fi
  done
done

printf '\n'
if [ "$ACHOU" -eq 1 ]; then printf '  O jogo voltou ao inglês original.\n\n'
else printf '  Não encontrei nenhuma tradução instalada.\n\n'; fi
