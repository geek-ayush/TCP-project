# TCP-server
A sample for a tcp server application.
# Install the server 
After downloading the files , run the given command in the terminal
```  
    sudo python3 setup.py install
```
# Using the server 
Run the command
```
    sudo tcpserver 
```
or 
```
    sudo tcpserver -p 132 -d -l file.log
```
# Uninstall the server
Runthe command
```
    sudo python3 setup.py instal --record files.txt
    cat files.txt |xargs rm -rf
````