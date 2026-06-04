# BMC
- A Baseboard Management Controller (BMC) is a dedicated processor on server motherboards that lets sysadmins monitor and manage the hardware remotely over its own Ethernet port
- If the server is completely screwed, the BMC will still be ok
## Features
- Monitor fan speeds, temperatures, and power supply health
- Control power (on off, reset etc)
- Blink a little LED so when you're walking around a server room trying to find the one you're working on you can look for the blinking LED `ipmitool chassis identify`
- Mount `.iso`, `.img` or network shares (NFS) and present them as a physical USB storage device. Useful for firmware/OS installation
- Remote KVM: Using the web interface, you can remotely access the desktop environment
# IPMI
- The Intelligent Platform Management Interface (IPMI) is a standard for communicating with the BMC
- The `impitool` linux package sends IPMI commands to the bmc
- Can be used in two ways
	- From the server itself: `ipmitool ARGS`
	- Over LAN: `ipmi tool -I lanplus -H HOSTADDR -u USERNAME -P PASSWORD ARGS`
# Custom BMC Wrapper script
- Instead of typing the long lanplus command, I wrote a script that wraps it
- Located at `/opt/bmc.sh` on scruffy
- Usage:
  ```sh
bmc.sh kif power status  
bmc.sh kif power on  
bmc.sh kif power soft # Requests graceful shutdown  
bmc.sh kif power off # Forces shutdown  
bmc.sh kif power reset # Simulates pressing reset button  
bmc.sh kif power cycle # Simulates unplugging and replugging the PSU
bmc.sh kif sensor # reads out all sensor values
  ```
## bmc.sh Code
```sh
server="$1"
shift

ipmitool -I lanplus -H "${server}_bmc.rcs.uncc.edu" -U rcslab -P "Reconfig2026!" $*
```
