# Preface
I'm Jaskin Kabir and this is my guide on how to use your PicarX robot at home. If you have any more questions you can email me at jkabir@charlotte.edu and I'll respond if I'm not drowning in homework/research
![[Pasted image 20250613232522.png]]
This guide is assuming you are using a Windows 10/11 computer. I can't write a guide for Mac/Linux users since I've never worked with these robots on those operating systems. However, I believe that on Mac/Linux you can skip installing the drivers and treat the rest of it mostly the same
# Setting Up Your PC/Laptop
## Installing Drivers
1. Install the [Bonjour Print Services](https://download.info.apple.com/Mac_OS_X/061-8098.20100603.gthyu/BonjourPSSetup.exe)
	1. Goto https://download.info.apple.com/Mac_OS_X/061-8098.20100603.gthyu/BonjourPSSetup.exe
	2. Run the exe file by double-clicking it in the file explorer![[Pasted image 20250613155122.png]]
	3. Follow the instructions in the installation wizard and be sure to click yes when Windows asks permission to install the driver
2. Install the [RNDIS Driver Package](https://storage-us.xtool.com/resource/static/xcs/driver/rndis.zip) 
	1. Goto https://storage-us.xtool.com/resource/static/xcs/driver/rndis.zip
	2. Open the folder where the file was downloaded
	3. Click on the file and then click extract all and then extract![[Pasted image 20250613174308.png]]
	4. ![[Pasted image 20250613174349.png]]
	5. Open device manager by right-clicking the start button at the bottom of the screen and then clicking device manager![[Pasted image 20250613172507.png]]
	6. Use the micro USB cable included with the red TI-RSLK kit to connect the PicarX to your PC![[Pasted image 20250613172629.png]]
		1. Make sure the cable is plugged into the usb port closer to the back of the robot, as the other usb port is simply for powering the Raspberry Pi
	7. In device manager, expand the section labeled Ports (COM & LPT)![[Pasted image 20250613172917.png]]
	8. Look for the device called USB Serial Device (The number after COM does not matter). This is the robot.![[Pasted image 20250613173023.png]]
		1. If you cannot see this device after plugging in the robot, you may have to wait a few seconds. The device manager screen will flash when it detects the robot.
		2. You can also manually refresh the list by clicking Action->Scan for hardware changes![[Pasted image 20250613173505.png]]
	9. Right-click the USB Serial device and click "Update driver"![[Pasted image 20250613173146.png]]
	10. Click "Browse my computer for drivers"![[Pasted image 20250613173220.png]]
	11. Click Browse![[Pasted image 20250613173533.png]]
	12. Point the installation to the RNDIS folder inside the folder that you extracted the RNDIS package into. Ensure that the "Include subfolders" box is checked. Finally, click "Next"
	13. ![[Pasted image 20250613174903.png]]
	14. If successful, the screen will look like this![[Pasted image 20250613174928.png]]
### What Did You Just Do?
- The way you connect to the Raspberry Pi in the robot is through SSH, which is a tool for controlling computers over the internet
- The SD card I gave you is configured to make the Raspberry Pi treat the USB cable as a network connection
- Installing the RNDIS driver package configures your computer to do the same. Both the Raspberry Pi and your computer now view the USB cable as an internet connection they can communicate over
- The Bonjour Print Services package is used to translate the name of your robot, like `kubi.local` into the actual IP Address of your robot, which would be something like `192.168.1.7`, which you would have to memorize and type every time you wanted to connect to the robot if you didn't use this package
## Installing VSCode
1. Goto https://code.visualstudio.com/download
2. Click the appropriate link for your operating system![[Pasted image 20250613175157.png]]
3. Open the file when it is done downloading, then follow the steps in the installation wizard
4. When you reach this step, check all the boxes![[Pasted image 20250613175626.png]]
	1. This step is not strictly necessary, but it is recommended if you want to use VSCode for other things in the future
5. Launch VSCode and go to the extensions tab![[Pasted image 20250613182159.png]]
6. Download the Python extension and the Remote SSH extension![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfm5-cgwtUBiP3m9GqLNO8bNzjJRudfUWJoIgPl4tKvmV__ZxrRZZ1KWqCShu_ugTfwfl4_fY-5Gm4DixA7alxw99P_nDx6SYrwBwAXSFUevvx9gGWBnZk8WOEVPE-YWjAvoA5K?key=c6k-QZQ4Yx_22nbnOw_i9w)![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeocoayEnqhzhiI-MwxBB-RvQe63ucLgWufmbsZX7kZYlUxA5Wk4cFKiS2Vcoh2ckSHgtHafFEFSG5wVsGFyN8Uj0Iohgigb8s-G7VJ1HWNefm3a8rlWjIdk6SvvigXC5K5Ytuqbw?key=c6k-QZQ4Yx_22nbnOw_i9w)
### What Did You Just Do?
- VSCode is a tool for developing software, and you just installed two important extensions for it. The Python extension allows the code editor to understand Python code and properly display it. The Remote SSH package allows us to write and test code directly on the robot over an SSH connection
# Connecting to the Robot over USB
1. Plug in your robot and open device manager
2. In the "Network Adapters" section, you should be able to find a device called "USB Ethernet Gadget" ![[Pasted image 20250613182426.png]]
	1. If you can't find this, wait a few seconds until the screen flashes or manually refresh the list
3. Open the terminal by right-clicking the start button and clicking "Terminal"
4. ![[Pasted image 20250613182553.png]]
5. Connect to your robot with the following command `ssh pi@[NAME_OF_ROBOT].local`                                                  ![[Pasted image 20250613182803.png]]
	1. If you have a fresh robot, the name of your robot will be kubi
	2. Otherwise it should be the same as the name you had in class
6. Type yes to continue connecting![[Pasted image 20250613182828.png]]
7. The password is `1337`
8. Now you have access to a linux terminal on the robot![[Pasted image 20250613182854.png]]

# Setting Up Passwordless SSH Authentication (Optional)
- Typing in the password every time you want to connect to the robot is annoying. Here's how to make your robot trust your computer:
1. Open a new tab in the terminal![[Pasted image 20250613210444.png]]
2. Generate an ssh key pair 
	1. Type the command `ssh-keygen -t ecdsa` into the new terminal
	2. Keep pressing enter until your terminal looks like this![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc7b_fZcX6Ng31PHmZlzSYk6cp8nC6hgdCZo8JuEGct3JqAotBRekn2lrxZVIPXkF1IObheBWx51hL2hM0xmYYDi8cm2lp5pAkl3JfH8Nq4E-Z4k6gx4lZSCilA9tAA2lxUc21t?key=c6k-QZQ4Yx_22nbnOw_i9w)
3. Transfer the public key onto your Raspberry Pi
	1. Run this command `cat ~/.ssh/id_ecdsa.pub | ssh pi@kubi.local "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"`
		1. If your robot has a different name, make sure you replace "kubi" with the name of your robot
	2. Type the password when it asks for it, which is 1337
4. You should now be able to connect to your robot without typing the password
## What Did You Just Do?
- The SSH Keygen command created a public key and a private key for your computer. The next command copied the public key to the robot
- Look into public-key cryptography if you want to know more
# Connecting the Robot to WiFi
1. In the linux terminal type the command `sudo nmtui`                                                                     ![[Pasted image 20250613183620.png]]
	1. This will open a utility that is navigated using the arrow keys and the enter button. The mouse does not do anything here
	2. The sudo keyword here is short for "Super-User Do", and it allows whatever application is opened by the command to have access to and modify system files. This is necessary to edit the configuration of the system
2. First, I recommend that you delete the network connections used to connect to the networks at EPIC, but this isn't strictly necessary.
	1. Select "Edit a connection" with the arrow keys and press enter![[Pasted image 20250613183841.png]]
	2. Select any saved networks and delete them![[Pasted image 20250613183852.png]]
3. Select "Activate a connection" and press enter![[Pasted image 20250613184625.png]]
4. Select your home WiFi network and enter the password
5. Once the Raspberry Pi is connected you can quit the nmtui utility
6. Check if you have a WiFi connection with the `ifconfig` command. If you are connected to your router, you should see an ip address on the interface labeled `wlan0`![[Pasted image 20250613185914.png]]
	1. If you are still connected to the Pi over USB, note that there is a network interface called `usb0`. This is the 'network' that your computer can use to communicate with your robot over USB
7. You should now be able to wirelessly connect to the Raspberry Pi using the ssh command, so long as your computer is connected to the same network you connected your Raspberry Pi to
8. Check if you have access to the internet with the command `sudo apt update`![[Pasted image 20250613190304.png]]
	1. This command won't make any changes to your system, it will just ask the apt repository servers which software packages installed on the robot can be updated
	2. If the command is successful, you have an internet connection on the Pi, which may be necessary for setting up VSCode
# Renaming the Robot (Optional)
- Execute this command to open the Raspberry Pi configuration utility                                              ![[Pasted image 20250613184951.png]]
	- This is another utility like the nmtui utility that is controlled with the arrow keys and the enter key
- Select "System Options" and press enter![[Pasted image 20250613185028.png]]
- Select "Hostname" and press enter![[Pasted image 20250613185104.png]]
- Take note of the warning that the tool gives you and ensure that the name you give your robot follows its rules. Also note that you will be typing this name a lot so keep it short![[Pasted image 20250613185204.png]]
- Enter your robot's new name and press enter![[Pasted image 20250613185227.png]]
- Select finish and press enter![[Pasted image 20250613185338.png]]
- Reboot the Raspberry Pi by pressing enter![[Pasted image 20250613185345.png]]
- If you still have device manager open, you should see it flash once when the Pi turns itself off, and then once more when it's fully rebooted. Once you see the USB Ethernet/RNDIS Gadget in the list can you unplug the robot or try connecting to it over SSH
# Accessing the Example Code
- When a new SSH session is opened, the terminal is in the user's home directory, which should be `/home/pi`
	- A shortcut for the home directory is the character `~`, which can be typed by holding shift and pressing the backtick key next to the 1 key
	- Executing `cd ~` will transport the terminal session back to the home directory
- you can run the command `ls` to list what files and folders are available in this directory![[Pasted image 20250613190709.png]]
	- `ls` is short for list, and it displays found folders as blue and files as white
- This shows that there is one folder named `picar-x` in the home directory. To enter this directory you use the change directory of `cd` command:![[Pasted image 20250613190954.png]]
	- If you type `cd pi` and then press tab. Linux should automatically figure out what you're trying to type and complete it for you
- Let's do another `ls`![[Pasted image 20250613191012.png]]
	- This directory contains files used to control the robot
- `cd` into the examples directory and do another `ls` to see all the example programs the manufacturer included with this library![[Pasted image 20250613191122.png]]
- To run any of these programs you use the `python3` command. You can type the number of a program and press tab and Linux will complete the name for you.
- ![[Pasted image 20250613191224.png]]
	- You can go to this link to see what each example program does and how they work:
	- https://docs.sunfounder.com/projects/picar-x-v20/en/latest/python/play_with_python.html
# Writing Your Own Code
## Making a New Folder/Directory
- The first thing you need to do is make a folder to put all our code
- You can do this with the make directory or `mdkir` command
- ![[Pasted image 20250613193355.png]]
	- First make sure you are in the home directory
	- Next you can make the new directory
	- After that, `ls` will show there is a new folder in the home directory
	- If you `cd` into it and do another `ls`, you'll see that it's empty

## Using VSCode Remote Development
1. Open VSCode
2. Click the button in the bottom left of your screen![[Pasted image 20250613211254.png]]
3. Select "SSH" and press enter![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdanLTB_JiVLk2rUOVGTREdfwTD41Kz6FVFkAuW758vZpgi1ERmfqw7CulHjGL0jNj53Y9rw1PV9TgPllFG2tx5mcvSi9M88VCxXIcsziTh4jMmr6HEAip7UcFbD4D__ypBXlDk?key=c6k-QZQ4Yx_22nbnOw_i9w)
4. Select "Add New SSH Host..." and press enter![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeHRls_PqmZ2GKMeB4yFZk-LGAIZLpFFOz22hvnuGnh6aBvrBkpdVmt1bHCsIXNoaNxHqHUNW4jjr9Eobc5ufmVjWTLRgy-aST_JLZ57cxU8ZHPxB-qfvTN7yGYLeyP83LGt3CHZw?key=c6k-QZQ4Yx_22nbnOw_i9w)
5. Type the address of your robot and press enter ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcNMF0mwjnyzP9VS-87Z2bSK4i-IBRIBUAAoGZukbzKcQ27fGnu09-fxmIHaTwL0ChMo50ONbj0R3tDYbB9MHvpevTaV_VjHr774Rwkok20ANM5XtOMb0XHqbfSpWBkkCxWWZ0pAA?key=c6k-QZQ4Yx_22nbnOw_i9w)
6. Use the default config file in the `C:\Users` directory![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeSOhiInBlTzo2y_pXFiOqTdRWqnHXeENBQ6bXqLr1NGRLcMsXrtFxXfiu9Y8LB1JqSKxWusRJ3AG_XHPVb2mdVeODQM5yhpgVWdzzENgJcLI8cyl6THIlPV34g9SbCkLQlNeK5Gg?key=c6k-QZQ4Yx_22nbnOw_i9w)
7. Press the button in the bottom left and press connect to host again. You should be able to select your robot and press enter![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdIgPklwOEooMRhcxXvQKBMi1JDaikvuFg8ltyS8yd3Iro6hE3TFcHI4dZ8Mm0oEsz4_ZCkzxeghxozrRSJokFf_Gfw4JDpG4qSifHZnKjUkmGK_iSQ2jLaUSimPLBPpoz5BBKv2Q?key=c6k-QZQ4Yx_22nbnOw_i9w)
8. This should open a new window of VSCode connected to the robot. When it asks which platform your robot is using, select Linux![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfpDB0HhfZ5NoVPo4izhM-wdJ_-Lx_EpLFZA6cuWqvD2X57rcHtH75sSyuq1tRX3JovSAubXOMLCftLdLL6zFXYhKRJZ6FBDz042uauNth2A0R7ehA3-AmwA-4Jj7Nc9Qq0wvA9Cg?key=c6k-QZQ4Yx_22nbnOw_i9w)
9. If you skipped the passwordless authentication step, type the password, which is `1337`
10. If a message like this pops up, just hit retry a couple times. If that doesn't work restart VSCode or your robot. The ssh connection can be finicky.**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd3bLvyNHDFW1KyCJUARPu3RICsIP7yIA1zlAYqDshwo6gOn9hJJWELTS_96Wl7rIRfs4j0yAm-5x9lE0pOJ8xjXtEsDridclVN8KfSus7KjtGgnHnnaodh6VB02DSqCa2cK6juwQ?key=c6k-QZQ4Yx_22nbnOw_i9w)**
11. Once you have a remote window open, click open folder![[Pasted image 20250613214215.png]]
12. Make a new file![[Pasted image 20250613214623.png]]
13. Give it a name ending in `.py` and press enter. Creating a new file could take some time so be patient
14. Now you can start writing code! Write some code and remember to save the file. If there is a white dot next to the file name it means your changes haven't been saved yet![[Pasted image 20250613215239.png]]
15. Note that this isn't like the code for the red TI RSLK robot. There are no setup or loop functions, you make those yourself, and the code will simply start executing from line 1 until the end. Here is some example code:
```python
from picarx import Picarx
from time import sleep 

if __name__ == "__main__":
    px = Picarx()
    try:
        print("First Program!")
        px.forward(30)
        sleep(0.5)
        px.backward(30)
        sleep(0.5)
    finally:
        px.stop()
```
- This program moves the robot forward for half a second, then backward for half a second, then stops
	- If `px.forward()` makes your robot go backwards it means your left motor is plugged into the port on the robot hat for the right motor. You need to switch them
- `if __name__ == "__main__":` is a common pattern in python code to check if the script being executed is the main program or a piece of another program. When writing python, putting this in your main scripts is a good habit to form
- The `try ... finally` pattern is to allow the robot to recover from errors. Everything in the `try` block will be executed, but if any errors occur it will execute the code in the `finally` block before exiting. This patten essentially tells the Python interpreter to call `px.stop()` at the end of the program no matter what, which prevents the motors from being stuck spinning until you restart the Pi.

## Nano
- If you can't access the internet with your Raspberry Pi, then you cannot use Visual Studio Code to connect to your Raspberry Pi
- Unfortunately I'm not experienced enough with this system to help you troubleshoot this, but there are plenty of resources online for the Raspberry Pi Zero 2w, which is the computer inside the robot. If you look up something like "Raspberry Pi Zero 2w cannot connect to internet" then you would probably find some results
- If you still can't connect your Pi to the internet though, there is still the `nano` command, which opens a terminal based text editor
- Executing `nano [FILENAME]` will open the file you specified or create it if it doesn't exist ![[Pasted image 20250613192211.png]]
- ![[Pasted image 20250613192324.png]]
	- At the bottom of the screen are the keyboard shortcuts used to control the editor. A `^` key represents the CTRL button on your keyboard and `M-` represents ALT. 
	- To exit nano press CTRL+X, and to undo press ALT+U
# Running Your Own Code
1. You can open a terminal directly in vscode by clicking on the terminal tab or clicking Terminal->New Terminal on the top toolbar![[Pasted image 20250613215931.png]]
2. This terminal should automatically open in the folder that you wrote your code in. Type `python3 script_name.py` into the terminal and press enter. Make sure to replace "script_name" with the name you chose for your first script
# Links
- https://docs.sunfounder.com/projects/picar-x-v20/en/latest/python/play_with_python.html
	- This is the official documentation of the robot
	- They include good explanations of what their code is doing
- https://github.com/sunfounder/picar-x/blob/v2.0/picarx/picarx.py
	- This is better as a reference. This file contains all the functions available in the picarx library
- https://github.com/sunfounder/vilib/blob/picamera2/vilib/vilib.py
	- This is the file containing all the functions available for use with the camera
- https://docs.sunfounder.com/projects/robot-hat-v4/en/latest/robot_hat_v4/robot_hat_v4.html
	- This is the official documentation of the robot hat module and how to get more granular control of anything plugged into it 
- https://docs.python.org/3/
	- Documentation of the python language
	- Also see https://www.w3schools.com/python/
	- And Geeks For Geeks

# Final Note
- Don't give up!
- If you run into an issue, copy and paste error messages into google and try your best to figure out how to fix it. Eventually you'll be able to read them yourself
- After working with you guys this past week, I know that all of you will be able to figure out any issues you have, and make good use of these robots
- It was great to meet you all. Have fun!

for topic #campsoncampus/byor