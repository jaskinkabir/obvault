# Configuration Triple
- CPU
- Manufacturer
- Operating system
- Examples
	- Sparc-sun-solaris2.6
	- i386-pc-wint4.0
## Nowadays No Longer a Triple
- Sometimes obvious to leave out one part
	- i386-linux (manufacturer doesn't matter)
	- sparc-sunos (manufacturer is obviously sun)
- Other times even more detail is necessary
	- An operating system using mostly GNU sw with the linux kernel would be: i86-pc-linix-gnu
	- using all GNU software: i586-oc-hurd-gnu
- Our PowerPC is typically called powerpc-405-linux-gnu
## Vitis Triple
## arm-none-eabi-gcc
- CPU is ARM, but each ARM processor is just called ARM so there really should be more specificity here
- Manufacturer is you lol (None)
- OS is standalone (eabi)
- 
