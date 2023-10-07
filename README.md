# 0x4067
*Capture-The-Flag tutorials for NTU's Software Security course*

## Modifying & Building the Challenges

### Wacky Web Woes
```
pyinstaller -w -F --add-data "templates:templates" --add-data "static:static" --add-data "routes.py:." wackywebwoes.py
```