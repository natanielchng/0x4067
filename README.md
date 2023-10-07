# 0x4067
*Capture-The-Flag tutorials for NTU's Software Security course*

## Modifying & Building the Challenges

### Catastrophic Vulnerabilities Everywhere (CVE)
There is no code used for CVE, as it is an investigative exercise with information available online!

### Hashbrown

### Hexhunt
The source code for Hexhunt can be found in `/hexhunt/src`. 

`hexhunt.c` is the main challenge; `hexhunt.py` is a sample solution using the `pwn` library.

Compile `hexhunt.c` with the following:
```
gcc -z execstack -fno-stack-protector -no-pie -o hexhunt hexhunt.c
```


### Wacky Web Woes
The source code for Wacky Web Woes can be found in `/wackywebwoes/src`.  

Wacky Web Woes is a simple Flask project. An overview of the project structure is as follows:
```
/src
    wackywebwoes.py     --> The main Flask application
    routes.py           --> contains the routes used by wackywebwoes.py
    /static
        /css
           pico.min.css --> CSS styling for the Flask application
    /templates          --> folder containing the HTML templates used in the Flask application
```

`Pyinstaller` is used to bundle the Flask application into a single executable file. In the Flask project directory of `wackywebwoes.py`, run the following command:
```
pyinstaller -w -F --add-data "templates:templates" --add-data "static:static" --add-data "routes.py:." wackywebwoes.py
```