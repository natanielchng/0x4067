# CE/CZ4067 CTF Tutorial

## Hash Brown
Hello, hacker. 

You've been called upon by an anonymous client to break into a super secret program known as `h45hbr0wn`.

Instructions to use this program are found in `instruction.txt`.

These files can be found in the `hashbrown` folder.

If you are successful in breaking into the program, the client will engage you for future assignments.

### Questions
1. The `instruction.txt` file contains a mysterious string. What is the flag contained in this string?
2. What was the flag encoded or encrypted with? (Hint: Gfxj64)
3. What is the SHA256 sum for the amd64 Kali Linux 2023.3 ISO? (Hint: https://old.kali.org/kali-images/)
4. What is the occurrence when two pieces of data share the same hash value? (Hint: piap kwttqaqwv)
5. The `h45hbr0wn` program requires two files to run. You will have to craft or find files to access the program. What is the flag obtained?

## Catastrophic Vulnerabilities Everywhere
Upon further investigation of the `h45hbr0wn` program, you found that is has been making requests to an IP address `155.69.19.55`.

You decide to to investigate this IP address...

### Questions
1. You start your investigation by checking publicly available information about the IP address. What is this activity called?
2. You decide to use a tool like Shodan.io to get more information about the IP address. What are the vulnerabilities that Shodan has detected? (Hint: https://web.archive.org/web/20230825034205/https://www.shodan.io/host/155.69.19.55)
3. What are the CVSS 3 scores for the vulnerabilities?
4. Who is the ISP tied to the IP address?
5. What is the vulnerability scoring framework developed by Tenable?

## Timeshare
In the previous investigation, one of the requests made to the IP address contained a file.