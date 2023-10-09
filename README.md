# 0x4067
*A set of Capture-The-Flag tutorials for NTU's Software Security course*

## Overview of Project
This project consists of 5 CTF tutorials, each dealing with a software security topic:
1. **CVE** - vulnerability assessment
2. **Hashbrown** - cryptography
3. **Hexhunt** - binary exploits
4. **Timelapse** - side channels
5. **Wacky Web Woes** - web vulnerabilities

The tutorials can be found under the `/tutorials` folder. The structure is as follows:
```
/CTF Tutorials
    README.md                       --> Overview of the CTF tutorials, with instructions and rules
    README.pdf
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
            SCSE.png                --> Image used in Question 2
            frame.png               --> QR code embedded in SCSE.png
        timelapse.out               --> Executable used in Timelapse (Question 1)
        Timelapse.md                --> Handout for Timelapse in Markdown format
        Timelapse.pdf               --> Handout for Timelapse in PDF format
    /wackywebwoes
        /src
            wackywebwoes_source.py  --> The main Flask web application used in Wacky Web Woes, source code for wackywebwoes.out
            routes.py               --> contains the routes used by wackywebwoes.py
            /static
                /css
                    pico.min.css    --> CSS styling for the Flask application
            /templates              --> folder containing the HTML templates used in the Flask application
        wackywebwoes.out            --> Executable used in Wacky Web Woes
        WackyWebWoes.md             --> Handout for WackyWebWoes in PDF format
        WackyWebWoes.pdf            --> Handout for WackyWebWoes in PDF format
```

## Modifying and Distributing Challenge Code
Challenges that contain some code can be found in their respective `/src` folder.

### CVE

#### Creating a snapshot of the Shodan search results
Use the "Wayback Machine" to create a free snapshot of any webpage. This was necessary for the CVE tutorial as the vulnerabilities listing were removed soon after.

### Timelapse

#### Creating the Steganography Image
Timelapse question 2 uses the `SCSE.png` image. The `frame.png` QR code was embeded into `SCSE.png` via bit plane steganography using `https://stegonline.georgeom.net/`

#### Hosting of files
The images and text files used in Question 2 are hosted on a separate public Github repository. Pastebin is also another common way to publicly host text files.

### Special Compilation Instructions for Hexhunt
The `C` file used in 'hexhunt' should be compiled with security flags removed:
```
gcc -z execstack -fno-stack-protector -no-pie -o hexhunt hexhunt.c
```

### Special Instructions for Hashbrown, Timelapse and Wacky Web Woes
Since the source code is written in `Python`, the `pyinstaller` library is used to package them into an executable.

**Hashbrown**
```
pyinstaller -w -F hashbrown_source.py
```

**Timelapse**
```
pyinstaller -w -F timelapse_source.py
```

**Wacky Web Woes**
```
pyinstaller -w -F --add-data "templates:templates" --add-data "static:static" --add-data "routes.py:." wackywebwoes_source.py
```