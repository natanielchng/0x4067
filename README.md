# 0x4067
*A Set of Capture-The-Flag tutorials for NTU's Software Security course*

## Overview of Project
This project consists of 5 CTF tutorials, each dealing with a software security topic:
1. **CVE** - vulnerability assessment
2. **Hashbrown** - cryptography
3. **Hexhunt** - binary exploits
4. **Timelapse** - side channels
5. **Wacky Web Woes** - web vulnerabilities

The tutorials can be found under the `/tutorials` folder. The structure is as follows:
```
/tutorials
    /cve
        CVE.md                      --> Handout for CVE in markdown format
        CVE.pdf                     --> Handout for CVE in PDF format
    /hashbrown
        /src
            hashbrown_source.py     --> Source code for hashbrown.out
        hashbrown.out               --> Executable used in Hashbrown (Question 5)
        Hashbrown.md                --> Handout for Hashbrown in Markdown format
        Hashbrown.pdf               --> Handout for Hashbrown in PDF format
    /hexhunt
        /src
            hexhunt_source.c        --> Source code for hexhunt.out
        hexhunt.out                 --> Executable used in Hexhunt (Question 1-3)
        Hexhunt.md                  --> Handout for Hexhunt in Markdown format
        Hexhunt.pdf                 --> Handout for Hexhunt in PDF format
    /timelapse
        /src
            timelapse_source.py     --> Source code for timelapse.out
        timelapse.out               --> Executable used in Timelapse (Question 1)
        Timelapse.md                --> Handout for Timelapse in Markdown format
        Timelapse.pdf               --> Handout for Timelapse in PDF format
    /wackywebwoes
        /src
            wackywebwoes.py         --> The main Flask web application used in Wacky Web Woes, source code for wackywebwoes.out
            routes.py               --> contains the routes used by wackywebwoes.py
            /static
                /css
                    pico.min.css    --> CSS styling for the Flask application
            /templates              --> folder containing the HTML templates used in the Flask application
        wackywebwoes.out            --> Executable used in Wacky Web Woes
        WackyWebWoes.md             --> Handout for WackyWebWoes in PDF format
        WackyWebWoes.pdf            --> Handout for WackyWebWoes in PDF format
```

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
    
```

`Pyinstaller` is used to bundle the Flask application into a single executable file. In the Flask project directory of `wackywebwoes.py`, run the following command:
```
pyinstaller -w -F --add-data "templates:templates" --add-data "static:static" --add-data "routes.py:." wackywebwoes.py
```