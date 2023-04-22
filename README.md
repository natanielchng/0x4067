# ⚒️ Hephaestus 

Smash the stack!

## Introduction 

*Hephaestus is the Greek god of blacksmiths, metalworking, carpenters, craftsmen, artisans, sculptors, metallurgy, fire, and volcanoes.*

This repository contains binary exploitation and reverse engineering examples.

## Code Examples

The code examples are located in the `src` directory.

They are also deployed on Replit as an API of sorts...

| Filename                            | Vulnerability                                      | Deployment Example                                                                                                                    |
| ----------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| [titanium.c](/src/titanium.c)       | Buffer overflow to overwrite a variable's value    | [![Try with Replit Badge](https://replit.com/badge?caption=Try%20with%20Replit)](https://titanium-hephaestus.0x4067.repl.co/titanium) |
| [cobalt.c](/src/cobalt.c)           | Format string vulnerability                        | [![Try with Replit Badge](https://replit.com/badge?caption=Try%20with%20Replit)](https://cobalt-hephaestus.0x4067.repl.co/cobalt)     |
| [caesium.c](/src/caesium.c)         | Timing side channel attack                         | [![Try with Replit Badge](https://replit.com/badge?caption=Try%20with%20Replit)](https://cobalt-hephaestus.0x4067.repl.co/caesium)    |
| [rehnium.c](/src/rehnium/rehnium.c) | "Reverse engineering"-like of a WebAssembly module |                                                                                                                                       |

## Usage

Each vulnerable code file has a corresponding Python Flask wrapper. For example:
- cobalt.c
- cobalt.py

The Python wrapper allows interacting with the vulnerable binary via HTTP requests. Before that however, the wrapper handles code compilation and setting of environment variables.

## ⚠️ Disclaimer

Please use caution and discretion when working with this code and always test it in a sandboxed environment. The owner and contributors of this repository are not responsible for any damages or harm caused by the use or misuse of this code.