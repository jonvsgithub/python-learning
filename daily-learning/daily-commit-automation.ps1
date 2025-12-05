# Daily Python Learning Commit Automation Script
# This script creates a daily learning file and commits it automatically
# Run this daily to build your GitHub heatmap!

param(
    [string]$WorkspacePath = "C:\Users\HP\OneDrive\Notes\PYTHON",
    [string]$Topic = "Daily Python Learning"
)

# Get today's date
$today = Get-Date -Format "yyyy-MM-dd"
$dayName = Get-Date -Format "dddd"

# Create daily file
$dailyFileName = "daily-learning\learning-$today.py"
$fullPath = Join-Path $WorkspacePath $dailyFileName

$content = @"
# Daily Python Learning - $dayName, $today
# Topic: $Topic

# Today's Learning Focus:
# 1. Review previous concepts
# 2. Learn one new concept
# 3. Practice with exercises
# 4. Build a small project

# Session started at: $(Get-Date -Format "HH:mm:ss")

# Notes:
# - Keep it short and focused
# - Practice consistently
# - Build the heatmap!

print("Learning Python on $today!")
print("Keep grinding! Every commit counts!")
"@

# Write the file
$content | Out-File -FilePath $fullPath -Encoding UTF8

# Add, commit, and push
Push-Location $WorkspacePath
git add .
git commit -m "Daily learning: $dayName, $today - $Topic"
git push origin main 2>$null

Write-Host "✅ Daily commit created and pushed!" -ForegroundColor Green
Write-Host "📅 Date: $today" -ForegroundColor Green
Write-Host "📝 File: $dailyFileName" -ForegroundColor Green

Pop-Location
