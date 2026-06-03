# Todo
## DNS Stuff
1. Install Kea
	1. Natively on Ubuntu host or
	2. Podman container with `–network host` to listen to broadcasts
2. Generate TSIG key
3. Add key to `/etc/named.conf`
4. Tell IPA to accept dynamic updates with the key
5. Restart dns service
6. Configure kea dhcp.conf
	1. Send updates true, enable updates true
	2. Qualifying suffix `rcs.uncc.edu`
7. Kea should also have the qualifying suffix rcs.uncc.edu
8. Edit kea-dhcp-ddns.conf
	1. Add secret key
	2. List dns domains

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
# IPA Authentication
- Before doing anything in the FreeIPA container, you must authenticate
- Use the command `kinit admin`
- The password is `micro`

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
## Install software
`apt install freeipa-client nfs-common autofs -y`
## Setup FreeIPA On New Client

```
ipa-client-install --mkhomedir --no-ntp --no-dns-sshfp -U --domain=rcs.uncc.edu --server=scruffy.rcs.uncc.edu --realm=RCS.UNCC.EDU -p admin -w "mciro"
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