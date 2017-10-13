Author: Sangram Grewal
Date: 9/21/17

Python application that uses TCP to transfer a file from a Client to a Server.

NOTE: Python 3 is required.

First run the Server script and decide a port number to listen on. Then get the ip address of
the Server using the following command:
	$/sbin/ifconfig
Then use the port number + ip of the Server machine to start the Client script
on a DIFFERENT machine.
Make sure the file to be transferred is in the same directory as the script.

Upon succesful completion, the file should now be copied onto the Server machine
and saved within the /recv/ directory, a sub-directory of wherever the Server
script is located. If /recv/ didn't exist prior to execution, it is created
automatically.

**IP address of server must be in single quotes when passed to client script**

To run:

On Server Machine: (Run 1st)
$python3 ftps.py <port-number>
	port-number: port on server machine that program will start listening on

On Client machine: (Run 2nd)
$python3 ftpc.py <'ip-address'> <port-number> <filename>
	ip-address: ip of server machine. **Must be in single quotes**
	port-number: port on server machine
	filename: name of file in local directory to be sent

