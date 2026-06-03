# BMC Control
- Shell Script to alias the longer ipmi command
	- `ipmitool -I lanplus -H 10.16.26.13 -U rcslab -P "Reconfig2026!" $*`
	- This stores the password to the BMC account in plaintext. Maybe that needs to change in the future?
- Located at `/users/kif_bmc.sh` on scruffy
- Usage:
  ```sh
kif_bmc.sh power status  
kif_bmc.sh power on  
kif_bmc.sh power soft # Requests graceful shutdown  
kif_bmc.sh power off # Forces shutdown  
kif_bmc.sh power reset # Simulates pressing reset button  
kif_bmc.sh power cycle # Simulates unplugging and replugging the PSU
  ```
# TODO
- Need to give Kif a static IP
- Need to give Kif's BMC a static IP
