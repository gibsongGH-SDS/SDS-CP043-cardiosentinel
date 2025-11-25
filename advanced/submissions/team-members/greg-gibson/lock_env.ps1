<#
=========================================================
 lock_env.ps1 — Create a clean requirements.txt (Windows)
=========================================================
#>

# Stop on first error
$ErrorActionPreference = "Stop"

Write-Host "🔍 Freezing environment..."
pip freeze | Out-File requirements_full.txt -Encoding utf8

# Check if pipdeptree is available
$pipdeptreeExists = (Get-Command pipdeptree -ErrorAction SilentlyContinue) -ne $null

if ($pipdeptreeExists) {
    Write-Host "🧹 Filtering top-level packages with pipdeptree..."
    pipdeptree --warn silence --freeze | Out-File requirements_top.txt -Encoding utf8
}
else {
    Write-Warning "pipdeptree not found. Install with: pip install pipdeptree"
    Write-Host "Falling back to raw requirements list..."
    Copy-Item requirements_full.txt requirements_top.txt -Force
}

# Remove unneeded or low-level packages
Write-Host "🧩 Cleaning up known unneeded packages..."
Get-Content requirements_top.txt |
    Where-Object {
        ($_ -notmatch '^(pip|setuptools|wheel|pkg_resources|typing-extensions|urllib3|certifi|charset-normalizer|idna|requests)')
    } |
    Out-File requirements.txt -Encoding utf8

Write-Host ""
Write-Host "✅ requirements.txt created successfully!"
Write-Host "-----------------------------------"
Get-Content requirements.txt -TotalCount 15
Write-Host "..."
$packageCount = (Get-Content requirements.txt | Measure-Object -Line).Lines
Write-Host "$packageCount packages saved."
Write-Host "-----------------------------------"
Write-Host "Tip: Commit requirements.txt to GitHub (ignore requirements_full.txt and requirements_top.txt)."

# Clean up temp files
Remove-Item requirements_full.txt, requirements_top.txt -ErrorAction SilentlyContinue