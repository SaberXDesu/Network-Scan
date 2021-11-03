# Network-Scan

Hello viewers! This repository here contains a list of python codes that I've made for network scanning

## advanceScanner.py
This python code attempts to find open TCP ports on your target IP address. To execute this code, do the following:
```
(1) chmod +x advanceScannere.py //Permits code to execute
(2) ./advanceScanner.py -H <targetHost> -P <list of ports> //For example ./advanceScanner.py -H 10.10.15.5 -P 20,40,60,80,255,443
```

## retbanner.py 
This code attempts to get the banner from a target IP address and port numbers within the range 1 - 100. To execute this code, do the following:
```
(1) chmod +x retbanner.py
(2) ./retbanner.py //Enter your target IP after executing the code, as it will prompt a message stating "[*] Enter Target IP: "
```

## vulnScan.py
This code checks whether your target host is vulnerable to your list of vuln in .txt format. However, please note that the port numbers are in a list and can be changed to your likings. To execute this code, do the following:
```
(1) chmod +x vulnScan.py
(2) ./vulnScan.py YourVulnListFile.txt
```
```
Example in YourVulnListFile.txt:
dojnasdfduf
sgpsfigjispfg
SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
dfpidfpweefd
wepgfiwrepgjiwrg
```
