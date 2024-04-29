-- This folder contains the files used in our spoofed RIT login page --


Details:
- The spoofed site was set up on an Apache server hosted on a machine on the same network as the victim supplicant, on port 80.
- The stolen credentials were sent to a backend server via POST request.
- The backend server uses json-server, a simple and easy to set up backend server acquired through npm. (https://www.npmjs.com/package/json-server).
- The backend server was hosted on the same machine as the spoofed server on port 8080. 
