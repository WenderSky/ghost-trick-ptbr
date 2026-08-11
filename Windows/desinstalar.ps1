$ErrorActionPreference = 'Stop'
$OutputEncoding = [Console]::OutputEncoding = [Text.Encoding]::UTF8
$pak = 're_chunk_000.pak.patch_001.pak'

Write-Host ''
Write-Host '  Removendo a traducao PT-BR de Ghost Trick' -ForegroundColor Cyan
Write-Host ''

$bibliotecas = @()
try {
    $steam = (Get-ItemProperty 'HKCU:\Software\Valve\Steam' -Name SteamPath -ErrorAction Stop).SteamPath
    $bibliotecas += $steam
    $vdf = Join-Path $steam 'steamapps\libraryfolders.vdf'
    if (Test-Path $vdf) {
        foreach ($linha in Get-Content $vdf) {
            if ($linha -match '"path"\s+"(.+?)"') { $bibliotecas += $Matches[1] -replace '\\\\','\' }
        }
    }
} catch {}
foreach ($d in (Get-PSDrive -PSProvider FileSystem).Name) {
    $bibliotecas += "${d}:\SteamLibrary", "${d}:\Steam", "${d}:\Program Files (x86)\Steam"
}

$achou = $false
foreach ($b in ($bibliotecas | Select-Object -Unique)) {
    $alvo = Join-Path $b 'steamapps\common\Ghost Trick'
    $arq  = Join-Path $alvo $pak
    if (Test-Path $arq) {
        Remove-Item $arq -Force
        $bkp = "$arq.backup"
        if (Test-Path $bkp) { Remove-Item $bkp -Force }
        Write-Host "  Removido de: $alvo" -ForegroundColor Green
        $achou = $true
    }
}

Write-Host ''
if ($achou) { Write-Host '  O jogo voltou ao ingles original.' }
else        { Write-Host '  Nao encontrei nenhuma traducao instalada.' -ForegroundColor Yellow }
Write-Host ''
Read-Host '  Enter para fechar' | Out-Null
