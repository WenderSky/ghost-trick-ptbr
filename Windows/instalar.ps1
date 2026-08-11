$ErrorActionPreference = 'Stop'
$OutputEncoding = [Console]::OutputEncoding = [Text.Encoding]::UTF8
$pak  = 're_chunk_000.pak.patch_001.pak'
$aqui = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host ''
Write-Host '  Ghost Trick: Phantom Detective - traducao PT-BR' -ForegroundColor Cyan
Write-Host '  ------------------------------------------------'
Write-Host ''

function Achar-Jogo {
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
    # discos comuns, caso o registro nao ajude
    foreach ($d in (Get-PSDrive -PSProvider FileSystem).Name) {
        $bibliotecas += "${d}:\SteamLibrary", "${d}:\Steam", "${d}:\Program Files (x86)\Steam"
    }
    foreach ($b in ($bibliotecas | Select-Object -Unique)) {
        $alvo = Join-Path $b 'steamapps\common\Ghost Trick'
        if (Test-Path (Join-Path $alvo 're_chunk_000.pak')) { return $alvo }
    }
    return $null
}

$destino = Achar-Jogo
if (-not $destino) {
    Write-Host '  Nao encontrei a pasta do jogo automaticamente.' -ForegroundColor Yellow
    Write-Host '  No Steam: clique com o botao direito em Ghost Trick >'
    Write-Host '  Gerenciar > Procurar arquivos locais, e cole o caminho aqui.'
    Write-Host ''
    $destino = (Read-Host '  Caminho da pasta Ghost Trick').Trim('"'' ')
}

if (-not (Test-Path (Join-Path $destino 're_chunk_000.pak'))) {
    Write-Host ''
    Write-Host "  Isso nao parece a pasta do jogo: $destino" -ForegroundColor Red
    Write-Host '  Deve existir um re_chunk_000.pak la dentro.'
    Write-Host ''
    exit 1
}

Write-Host "  Jogo encontrado em:"
Write-Host "  $destino" -ForegroundColor Green
Write-Host ''

$jaTem = Join-Path $destino $pak
if (Test-Path $jaTem) {
    $bkp = Join-Path $destino "$pak.backup"
    if (-not (Test-Path $bkp)) {
        Copy-Item $jaTem $bkp
        Write-Host '  Ja havia um patch instalado; guardei uma copia como .backup'
    } else {
        Write-Host '  Ja havia um patch instalado; sera substituido.'
    }
}

Copy-Item (Join-Path $aqui $pak) $destino -Force
Write-Host ''
Write-Host '  Pronto! A traducao esta instalada.' -ForegroundColor Green
Write-Host ''
Write-Host '  O jogo ja abre em portugues - nao precisa mexer em opcao nenhuma.'
Write-Host '  Para remover, rode DESINSTALAR.bat (o jogo volta ao ingles).'
Write-Host ''
Read-Host '  Enter para fechar' | Out-Null
