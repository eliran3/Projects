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
Now enter the directory "projects" and run the following
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


# Ipscanner
Program to find every ip in the network.

# Requirements
A Linux device to run the program.

# Install - Linux
First install git
```
sudo apt install git
```
Now install a module called netifaces
```
pip3 install netifaces
```
(If you dont have pip)
```
sudo apt install python3-pip
```
# Next install the package
```
git clone https://github.com/eliranCoding/ipscanner.git
```
Now enter the directory "projects" and run the following
```
chmod +x ipscanner.py
```
To run the file just enter
```
./ipscanner.py
```
