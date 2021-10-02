### Hi there 👋
#### Development
I'm Eliran from Israel, 17 years old, And I'm a Developer in my free time, I really enjoy developing and learning computer stuff.

Skills: Python, C#, C/C++, BASH, HTML, CSS, Networking

- 🔭 I’m currently working on Finding backdoor in instagram 
- 🌱 I’m currently learning Python, Cyber, Networking... 
- 📫 How to reach me: eliran2109@gmail.com 
- ⚡ Fun fact: Still at High school😄 


[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/eliranCoding)  [<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/dev-dot-to.svg' alt='dev' height='40'>](https://dev.to/elirannissani)  [<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/facebook.svg' alt='facebook' height='40'>](https://www.facebook.com/elirannissani)  [<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/instagram.svg' alt='instagram' height='40'>](https://www.instagram.com/eliran_nissani/)

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
