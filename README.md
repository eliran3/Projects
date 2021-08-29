# Portscanner
Program to scan for open ports on multiple targets without using nmap.

# Requirements
A Linux device to run the program.

# Install - Linux
First install git
```
sudo apt install git
```
Then install the package
```
git clone https://github.com/eliranCoding/portscanner.git
```
Now enter the directory "portscanner" and run the following
```
chmod +x portscanner.py
```
To run the file just enter
```
./portscanner.py
```
Example:
```
./portscanner.py -t x.x.x.x, www.xyz.com -p {num1}-{num2}
```
