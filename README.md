# Portscanner
Program to scan for open ports on multiple targets without using nmap.

# Requirements
A Linux device to run the program.

# Installation
First update and install git
```
sudo apt-get update
sudo apt install git
```
(If you dont have pip) ``` sudo apt install python3-pip ```
Install colorama
```
pip3 install colorama
```
Then install the package
```
git clone https://github.com/eliran3/projects.git
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
Program to find every reachable ip in the network.

# Requirements
A Linux device to run the program.

# Installation
First update and install git
```
sudo apt-get update
sudo apt install git
```
install netifaces, scapy, colorama modules
```
pip3 install netifaces
sudo python3 -m pip install --pre scapy[complete]
pip3 install colorama
```
(If you dont have pip) ``` sudo apt install python3-pip ```
(If you dont have colorama) ``` pip3 install colorama ```

Next install the package
```
git clone https://github.com/eliran3/projects.git
```
Now enter the directory "projects" and run the following
```
chmod +x ipscanner.py
```
All left to do is run the script!
```
sudo ./ipscanner.py
```
IMPORTANT: After 30s of running the script, It'll print that the script is finished so just press ``` ctrl+c ``` to exit the program.


# Ipscanner_developer_version
Program to find every reachable ip in the network.

# Requirements
A Linux device to run the program.

# Install - Linux
First update and install git
```
sudo apt-get update
sudo apt install git
```
(If you dont have pip) ``` sudo apt install python3-pip ```

Now install the modules called netifaces, scapy
```
pip3 install netifaces
sudo python3 -m pip install --pre scapy[complete]
```
Next install the package
```
git clone https://github.com/eliran3/projects.git
```
Now enter the directory "projects" and run the following
```
chmod +x ipscanner_developer_version.py
```
All left to do is run the script
```
sudo ./ipscanner_developer_version.py
```


# Cryptography
Program to encrypt-decrypt text and files.

# Install - Linux

First update and install git
```
sudo apt-get update
sudo apt install git
```
Next install the package
```
git clone https://github.com/eliran3/projects.git
```
Now enter the directory "projects" and run the following
```
chmod +x cryptograpy.py
```
All left to do is run the script
```
./cryptograpy.py
```

# Install - Windows

install the package
```
git clone https://github.com/eliran3/projects.git
```
All left to do is run the script
```
python3 cryptograpy.py
```
