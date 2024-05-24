# Install pep8 pre-commit hook
$HOOK_FILE='./.git/hooks/pre-commit'
if ((-not $null) -or (Select-String -Pattern 'MYCROFT DEV SETUP' -Path $HOOK_FILE)) {
    if ((-not (Test-Path $HOOK_FILE)) -or (Select-String -Pattern 'MYCROFT DEV SETUP' -Path $HOOK_FILE)) {
        Write-Host 'Installing PEP8 check as precommit-hook'
        Add-Content -Path $HOOK_FILE -Value '#! $(command -v python)'
        Add-Content -Path $HOOK_FILE -Value '# MYCROFT DEV SETUP'
        Get-Content ./scripts/pre-commit | Add-Content -Path $HOOK_FILE
        Set-ItemProperty -Path $HOOK_FILE -Name IsReadOnly -Value $false
    }
}

#$PYTHON = python
#$VENV_PATH_FILE="$Env:VIRTUALENV_ROOT\Lib\site-packages\_virtualenv_path_extensions.pth"
#if ((-not (Test-Path $VENV_PATH_FILE)) -or (-not (Select-String -Pattern "$TOP" -Path $VENV_PATH_FILE))) {
 
# Write-Host 'Adding mycroft-core to virtualenv path'
 #   Add-Content -Path $VENV_PATH_FILE -Value "$TOP"
}

# Install required python modules
if (-not (pip install -r requirements/requirements.txt)) {
    Write-Host 'Warning: Failed to install required dependencies. Continue? y/N'
    $continue = Read-Host
    if ($continue -ne 'y') {
        exit 1
    }
}

# Install optional python modules
if (-not (pip install -r requirements/extra-audiobackend.txt) -or
    -not (pip install -r requirements/extra-stt.txt) -or
    -not (pip install -r requirements/extra-mark1.txt)) {
    Write-Host 'Warning: Failed to install some optional dependencies. Continue? y/N'
    $continue = Read-Host
    if ($continue -ne 'y') {
        exit 1
    }
}

if (-not (pip install -r requirements/tests.txt)) {
    Write-Host 'Warning: Test requirements failed to install. Note: normal operation should still work fine...'
}

$SYSMEM = [math]::floor((Get-WmiObject Win32_ComputerSystem | Select-Object -ExpandProperty TotalPhysicalMemory) / 1MB)
$MAXCORES = [math]::floor($SYSMEM / 2202010)
$MINCORES = 1
$CORES = (Get-WmiObject -Class Win32_Processor | Measure-Object -Property NumberOfLogicalProcessors -Sum).Sum

if ($MAXCORES -lt 1) {
    $MAXCORES = $MINCORES
}

if ($CORES -lt 1 -or $CORES -gt $MAXCORES) {
    $CORES = $MAXCORES
}

Write-Host "Building with $CORES cores."

# Build and install pocketsphinx
# Build and install mimic

Set-Location -Path $TOP

if (($build_mimic -eq 'y') -or ($build_mimic -eq 'Y')) {
    Write-Host 'WARNING: The following can take a long time to run!'
    .\scripts\install-mimic.sh -C $CORES
} else {
    Write-Host 'Skipping mimic build.'
}

# Set permissions for common scripts
Get-ChildItem -Path .\bin -Recurse | ForEach-Object { $_.IsReadOnly = $false }

# Store a fingerprint of setup
Get-ChildItem -Path requirements -Recurse -Include *.txt | Get-FileHash | Format-List > .installed

Write-Host 'Mycroft setup complete! Logs can be found at /var/log/mycroft/setup.log'
