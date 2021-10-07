# ARP-SPOOF-DETECTOR
Hello everyone, this program is designed to find any duplicate MAC addresses which could help detect arp poisining attacks.
All you would need to do is run the program and it checks for duplicate MACs. If there's any, it will inform you on screen and save it to "log.txt" file in the current directory.
You also have the ability to rerun the program and it will check for any additional duplicate MACs.
The log.txt file will also inform you of when the program discovered the duplicate MAC.


To run in Linux:
Python3 must be installed.
After program is installed, make sure program has the execute permision for current user or group. 
Syntax to change permissions: _sudo chmod 777 ARP_Extraction.py_
There are 2 ways to run the program after the execute permission has been given.
Easiest way to run is by the following command: _python3 ./ARP_Extraction.py_ (assuming in the correct and current directory).
The other way to run the program is by first editing the file and adding _#!/usr/bin/python3_ to the top of the python program. Then you could just run the program via _./ARP_Extraction.py_ (assuming in the correct and currrent directory).


To run in Windows:
Python3 must be installed.
After program is installed, double click it.
