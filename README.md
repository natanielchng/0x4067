# ⚒️ Hephaestus 

Smash the stack!

## Introduction 

*Hephaestus is the Greek god of blacksmiths, metalworking, carpenters, craftsmen, artisans, sculptors, metallurgy, fire, and volcanoes.*

This repository contains binary exploitation and reverse engineering examples.

## Code Examples

The code examples are located in the `src` directory.

They are also deployed on Replit as an API of sorts...

| Filename                       | Vulnerability                                   | Deployment Example                                                                |
| ------------------------------ | ----------------------------------------------- | ------------------------------------------------------------------------- |
| [titanium.c](/src/titanium.c) | Buffer overflow to overwrite a variable's value | [![Try with Replit Badge](https://replit.com/badge?caption=Try%20with%20Replit)](https://hephaestus-api.sonicfruit.repl.co/titanium?arg1=aaaaaaaa) |

## Usage

It is recommended to modify this repository from within a sandboxed environment  

Your evironment should have the following:  
- GCC
- Python3

Follow the compilation instructions for each of the C files in `/src`

Install the Python dependencies
```sh
pip install -r requirements.txt
```

Run the Flask application
```
python3 hephaestus_api.py
```



## ⚠️ Disclaimer

Please use caution and discretion when working with this code and always test it in a sandboxed environment. The owner and contributors of this repository are not responsible for any damages or harm caused by the use or misuse of this code.