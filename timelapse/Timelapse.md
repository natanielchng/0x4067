# Timelapse

## Question 1

### (a) What is a vulnerability where an attacker can gain information about a system's secret or private data by measuring the time it takes for certain operations to complete?
### (b) What is the flag obtained from the `timelapse` program?

The `timelapse` program takes in a 4 digit password.
```sh
$ ./timelapse 

  
███████  ██ ███    ███ ██████  ██      ██   ██ ██████  ███████ ██████  
     ██ ███ ████  ████      ██ ██      ██   ██ ██   ██ ██           ██ 
    ██   ██ ██ ████ ██  █████  ██      ███████ ██████  ███████  █████  
   ██    ██ ██  ██  ██      ██ ██           ██ ██           ██      ██ 
   ██    ██ ██      ██ ██████  ███████      ██ ██      ███████ ██████
  
Usage: ./timelapse <password>
Please enter the 4 digit numerical password...
```

There also seems to be a delay when processing the password. Find out if the delay varies with the digits entered.
```
$ ./timelapse 0000

  
███████  ██ ███    ███ ██████  ██      ██   ██ ██████  ███████ ██████  
     ██ ███ ████  ████      ██ ██      ██   ██ ██   ██ ██           ██ 
    ██   ██ ██ ████ ██  █████  ██      ███████ ██████  ███████  █████  
   ██    ██ ██  ██  ██      ██ ██           ██ ██           ██      ██ 
   ██    ██ ██      ██ ██████  ███████      ██ ██      ███████ ██████
  
1.004884958267212
1.005920171737671
1.0057597160339355
1.0117690563201904


Access denied...
```
## Question 2

### (2a) You have been tasked with investgating an image found at the following link: `https://raw.githubusercontent.com/0x4067/KpMU0l0N/main/SCSE.jpg`. Is there any interesting information stored within the image file? If so, what is it and how was it stored?

### (2b) Continue following the trail based off the information found in (2a). What is the second steganography technique used?

### (2c) The flag obtained from (2b) contains a link to a research paper. What is the phone model discussed in the paper?