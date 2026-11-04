* Concatenate all .md files into one combined.md file with headers indicating the source file.

> Get-Content *.md | Set-Content combined.md


* Use separators to indicate the source file for each section in the combined.md file.

> Get-ChildItem *.md | ForEach-Object {"`n`n---`n# FILE: $($_.Name)`n---`n" | Add-Content combined.md     Get-Content $_ | Add-Content combined.md }