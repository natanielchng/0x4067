# CE/CZ4067 CTF Tutorial

## Hash Brown
Hello, hacker. 

You've been called upon by an anonymous client to break into a super secret program known as `h45hbr0wn`.

Instructions to use this program are found in `hashbrown_readme.txt`.

These files can be found in the `hashbrown` folder.

If you are successful in breaking into the program, the client will engage you for future assignments.

### Questions
1. The `hashbrown_readme.txt` file contains a mysterious alphanumeric string. What is the originial text contained in this string?
2. What was the message encoded or encrypted with?
3. What is the occurrence when two pieces of data share the same hash value? (Hint: piap kwttqaqwv)
4. The `h45hbr0wn` program requires two files to run. You will have to craft or find files to access the program. What is the flag obtained from this program?

## Catastrophic Vulnerabilities Everywhere
Upon further investigation of the `h45hbr0wn` program, you found that is has been making requests to an IP address `155.69.19.55`.

You decide to to investigate this IP address...

### Questions
1. You start your investigation by checking publicly available information about the IP address. What is this activity called?
2. You decide to use a tool like Shodan.io to get more information about the IP address. What are the vulnerabilities that Shodan has detected? (Hint: https://web.archive.org/web/20230825034205/https://www.shodan.io/host/155.69.19.55)
3. What are the CVSS 3 scores for the vulnerabilities?
4. Who is the ISP tied to the IP address?
5. What is a vulnerability scoring framework developed by Tenable?

## Timelapse

### Questions
1. What is a vulnerability where an attacker can gain information about a system's secret or private data by measuring the time it takes for certain operations to complete?
2. What is the flag obtained from the `71m3l4p53` program?