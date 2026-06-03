# Todo
## Router Config
- Set Scruffy as the DNS server
- Make the router give out fqdns (\*.rcs.uncc.edu)

# Podman commands
```
Start: 
sudo podman start freeipa-server-container

Enter: 
sudo podman exec -ti freeipa-server-container /bin/bash

Stop: 
sudo podman stop freeipa-server-container
```
- `-ti` means create a TTY and use an interactive terminal

# Creating a New Account
## Within FreeIPA Container
```
ipa user-add USERNAME --first=FIRST –-last=LAST --shell=/bin/bash
```
`echo "temp" | ipa passwd USERNAME`
`ipa user-show dummy | grep UID`
``
## On Scruffy
`mkdir -p /mnt/nfs-data/home/USERNAME`
`chown -R UID:UID /mnt/nfs-data/home/USERNAME`
`chmod 700 /mnt/nfs-data/home/USERNAME`

# Enrolling a new machine

## Setup machine
- Ensure DNS server is scruffy: `172.16.0.2`
- Ensure hostname is fully qualified `(host).rcs.uncc.edu`
- Create local root user account with home directory in `/users`
## Install software
`apt install freeipa-client nfs-common autofs -y`
## Setup FreeIPA

```
ipa-client-install --mkhomedir --enable-dns-updates --no-ntp -U --domain=rcs.uncc.edu --server=scruffy.rcs.uncc.edu --realm=RCS.UNCC.EDU -p admin -w "reconfig"
```

`ipa-client-automount –server=scruffy.rcs.uncc.edu --location=default -U`
`sudo systemctl restart sssd`
`sudo systemctl restart autofs`

# Adding DNS Records
`ipa dnsrecord-add rcs.uncc.edu HOSTNAME --a-rec=IP`


`/users` for lab home directories
`/opt` for xilinx tools


Remote power on for kif
magic commands, snmp


for topic #thesis