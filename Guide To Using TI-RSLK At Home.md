# Preface
I'm Jaskin Kabir and this is my guide on how to use your TI-RSLK robot at home. If you have any more questions you can email me at jkabir@charlotte.edu and I'll respond if I'm not drowning in homework/research![[Pasted image 20250614130747.png]]

This guide is assuming you are using a Windows 10/11 computer. I can't write a guide for Mac/Linux users since I've never worked with these robots on those operating systems. However, I believe that on Mac/Linux you can skip installing the drivers and treat the rest of it mostly the same
# Setting Up Your PC/Laptop
## Install the USB Driver
1. Goto tinyurl.com/rslk-driver and save the file
2. Extract the contents of the file![[Pasted image 20250614134620.png]]
3. If your robot is plugged into your computer, unplug it before step 
4. Go into the extracted folder and double-click the shortcut for installing the drivers for a 64-bit system![[Pasted image 20250614134824.png]]
	1. The majority of computers today are not 32-bit systems, but if yours is make sure you install the 32 bit version
5. Give it permission to modify your computer and follow the installation wizard
6. Install and trust any drivers it asks you to check if the installation was successful, plug your robot into your computer with the included micro USB cable![[Pasted image 20250614135117.png]]
7. Open device manager by right-clicking the start button and clicking "Device Manager"
8. ![[Pasted image 20250613172507.png]]
9. Expand the section labeled Ports (COM & LPT)![[Pasted image 20250613172917.png]]
	1. Device manager is a tool for seeing and managing every device connected to your computer
10. If the installation was successful, you should see these two devices in the list![[Pasted image 20250614135337.png]]
	1. If you don't, you could try a different USB cable
11. Now, your computer knows how to talk to your robot over USB
## Install Energia
1. Goto https://energia.nu/download/ and download the appropriate zip file for your OS![[Pasted image 20250614135836.png]]
2. Click on the file in the explorer and click extract all
3. This time, instead of extracting into your downloads folder, click browse and point it somewhere you will remember. I have a folder on my second hard drive specifically for programs like this. You can just put it on your desktop though if you wanted to. Make sure "Show extracted files when complete is checked"![[Pasted image 20250614140355.png]]
4. Within the extracted files, find energia.exe (it may just be called energia for you). Hold shift and right click it. Then click "Send to"->"Desktop". This will create a shortcut to the energia code editor on your desktop![[Pasted image 20250614141307.png]]
5. You should now have this shortcut on your desktop                                                                    ![[Pasted image 20250614141332.png]]
6. Open energia
7. Click "File->Preferences" or CTRL+, (comma)![[Pasted image 20250614143413.png]]
8. Check "Display line numbers"![[Pasted image 20250614143445.png]]
	1. This will make finding and fixing errors much easier in the future
## Install the RSLK Board
1. Open energia
2. Make sure to allow it to access your network if it asks
3. Click "Tools" at the top, then "Board", then "Boards Manager..."![[Pasted image 20250614141628.png]]
4. Install the package for the Energia MSP432 EMT RED boards ![[Pasted image 20250614141913.png]]
	1. This step will take a long time so be patient
	2. Try not to use the computer for anything else while it downloads
5. Make sure that in any new Energia sketches you make, the board selected is the "RED Launchpad w/msp432..." ![[Pasted image 20250614142250.png]]
6. Now, Energia knows how to convert your code into 1s and 0s that your robot can understand.
## Install the RSLK Library
1. Goto tinyurl.com/rslk-lib and save the file
2. In energia, click "Sketch"->"Include Libary"->"Add .ZIP Library..."![[Pasted image 20250614142401.png]]
3. Point it to the zip file you downloaded in step one and open it by double-clicking it or clicking it once and pressing open![[Pasted image 20250614142520.png]]
4. Now you should be able to type `#include <SimpleRSLK.h>` at the beginning of your code, and Energia will know what that means. This library includes all the code used by the CPU in your robot to talk to the motors and other parts of the robot
5. This library also includes 4 pieces of example code![[Pasted image 20250614145512.png]]
# Writing Code
1. Open a new sketch by clicking "File-> New" or CTRL+N                                                              ![[Pasted image 20250614143127.png]]
2. Make sure `#include <SimpleRSLK.h>` is at the beginning of the file
3. Make sure the first line of the `setup()` function is `setupRSLK();`
4. If you want this program to move the robot, make sure the setup function also contains the line `enableMotor(BOTH_MOTORS);`
5. A blank sketch for this robot should look like this![[Pasted image 20250614143324.png]]
6. Remember that the `setup()` function is run once, and the `loop()` function is then run over and over again until the robot is powered off. Any code outside these functions, aside from global variable definitions like wheel speed, will NOT be executed
	1. Code outside these functions will be executed if you define functions and call them within either the setup or loop functions
## The C++ Language
(Written by Dr. Shue)
C++ is a programming language, which is a series of special words and commands that translate into instructions for a computer. These special words we refer to as the language's **syntax**. If we write the syntax correctly, a program called the **compiler** will read the text and translate it into the 1's and 0's the computer speaks. Then, we can have a tool, such as Energia, upload the program to the computer and execute it. 

Computer programs work by executing instructions sequentially from the top of the program, which is a list of instructions. Instructions can range from performing operations such as addition or subtraction, to jumping ahead to another place in a program and skipping certain lines. The syntax of our C++ language can be translated into these instructions. While it may be foreign or confusing at first, programming languages make creating programs much easier. If we had to program computers using instruction directly like they had to way back when computers were first invented, we wouldn't be able to create such complex masterpieces today, such as Microsoft internet explorer. 

Energia uses a modified form of C++, which has two main components: setup and loop. The code we place inside of "setup" gets ran once when the microcontroller starts up, and the instructions we place inside of "loop" get ran over and over until the microcontroller loses power or gets reset.
## Tips
### Fixing Errors
- If you make a mistake, the compiler will probably tell you what mistake you made and where to find it. Take a look at this example code![[Pasted image 20250614144230.png]]
- In this example, I made several mistakes and the first time I tried to upload the code, the compiler found two of them. 
	- It says that on line 11, 'i' was not declared in this scope. This means that the compiler was looking for a variable named 'i', but it was never declared. This is because variable declaration in C++ must define the variable's type. The correct line would be `int i = 0`
	- Second, it says that on line 19, it was expecting '}' at the end of the program. This is because I opened a curly brace after the if statement on line 13, but I never closed that curly brace
- After I fix these mistakes, I press upload again and it finds another mistake![[Pasted image 20250614144726.png]]
	- It says that on line 13, it was expecting a ',' or ';' before 'if'.
	- This means I forgot to put a comma or a semicolon somewhere before line 13.
	- Sure enough, I forgot to put a semicolon at the end of line 11
- I fixed these errors and pressed upload, but the compiler found another error![[Pasted image 20250614144959.png]]
	- On line 14, it says 'BOTH_MOTOR' was not declared in this scope
	- This is because I forgot the S at the end and the compiler doesn't know what 'BOTH_MOTOR' means
- Now the code works![[Pasted image 20250614145058.png]]
- As you can see, the compiler error messages at the bottom of the screen are very useful for finding and fixing errors.
- If there is an error you can't figure out, Energia lets you copy the error message so you can paste it into google (or some sort of AI but don't tell anyone I said that)![[Pasted image 20250614145215.png]]
# Links
- https://energia.nu/guide/
	- This is an excellent website. It has a good tutorial on how the C++ language works and how the Energia framework can be used to write code for your robot
- https://energia.nu/reference/
	- This page has a list of functions built into the Energia framework and information about how they all work
- https://fcooper.github.io/Energia-RSLK-Library/_simple_r_s_l_k_8h.html
	- This is a list of all the functions available in the RSLK library and how to use them

# Using The Serial Monitor
- The serial monitor is a way to communicate with your robot over a USB cable
## Using the Serial Monitor on your robot
- Take a look at this example code:
```C++
#include <SimpleRSLK.h>
void setup() {
  // put your setup code here, to run once:
  setupRSLK();
  enableMotor(BOTH_MOTORS);
  Serial.begin(9600);
  while (!Serial) {}
  Serial.println("Setup function works");
  
}
int i = 0;
void loop() {
  if ( i == 0) {
    Serial.println("Loop function works");
    i = 1;
  }
  
}
```
- Let's walk through what it is doing
	- First, we call `Serial.begin(115200)`. This opens serial communication over the USB cable at a rate of 9600 1s and 0s per second.
	- The variable `Serial` will evaluate to `false` while the connection is invalid and `true` while the connection is valid. `while (!Serial) {}` tells the robot to do nothing and wait until the serial connection is established
	- Now, it can call `Serial.println()` which will print messages to the terminal
## Using the Serial Monitor on Your Computer
1. Goto device manager and look in the Ports section. Find the device labeled "XDS110 Class Application/User UART (COM#)"![[Pasted image 20250614151514.png]]
2. Remember the number at the end of that name
3. In Energia, goto Tools->Port and select the port you just found![[Pasted image 20250614151549.png]]
4. Now, you can click the magnifying glass in the top right to open the Serial Monitor                            ![[Pasted image 20250614150253.png]]
5. 
# Using the Ultrasonic Sensor
This part was written by Dr. Shue for the college level robotics class that uses these robots. If you want to use the ultrasonic sensor, you will have to buy at least 4 jumper cables to connect the pins
## Background

### Rangefinders

A common sensor used in robotics are what we call “range finders”. Range finders are sensors that are able to sense the distance to the nearest object in front of the sensor.Many technologies can be used to build rangefinders, such as:

- Ultrasonic Sound
- Infrared Light
- LIDAR (Infrared Based)

Ultrasonic rangefinders use reflected ultrasonic sound waves to determine distance. An ultrasonic “speaker” is used to create a sound wave and the time it takes for the sound wave to return to a receiver
![[Pasted image 20250614145857.png]]
Since we know the speed of sound, if we divide the time it took the sound to return in half and multiply it by the speed of sound, we get the distance:  Distance = (Time x SpeedOfSound) / 2

### Interfacing the Ultrasonic Sensor

We'll begin by examing how to use the HC-04 Ultrasonic Sensor. This sensor measures distance to the closest object in front of it by measuring the time of flight of an ultrasonic sound wave it emites. Before we can use the sensor, we need to know how to connect it to our microcontroller:
![[Pasted image 20250614145906.png]]
The HC-04 has four pin connections. One is Vcc which is the power pin. This pin needs to be connected to 5 volts on the MSP432 board for power. The ground pin needs to be connected to a ground pin on the MSP432 board as well. The trigger pin is used to generate an ultrasonic pulse. A precisely timed pulse must be sent to this pin to generate the ultrasonic pulse. The Echo Pulse pin goes high when an ultrasonic sound wave is received. These two pins will need to be tied to any GPIO pin on the microcontroller board in order to use them. I'll choose the pins P6_4 for the trigger and P6_5 for the pulse.

Programming the control, timing, and calculating the result can be tricky, so we're going to pull in an external library to do that work for us. Download the zip file containing the library [here](https://drive.google.com/file/d/1lHT3G8WV1OiNkU0rYGKb8O9x7bC-bV1U/view?usp=sharing) https://tinyurl.com/rslk-uss-lib. Once downloaded, go to Sketch->include libary->Add .ZIP library... and navigate to the location where you downloaded this zip file and select it. Once imported, download [this example code](https://tinyurl.com/rslk-uss-code) https://tinyurl.com/rslk-uss-code

This example code will allow us to drive the sensor and read the distance measured by it. This distance is then printed to the Energia terminal using the "Serial.println()" function. To open the terminal, click on the "magnifying glass" icon on the top right corner of the interface.
![[Pasted image 20250614150253.png]]
This will open a window that will print characters sent from the microcontroller.
![[Pasted image 20250614150259.png]]
If you download and run the code, if you open the terminal you should see the distance sensed by the ultrasonic sensor, provided everything is working as expected. If you don't see anything printing on the terminal, try changing the selected serial port under Tools.

Let's take a moment and examine some of this code. At the top of the code, outside of the setup() and loop() functions, we have the line "hcrs04 mySensor(PINTRIG, PINECHO);". This line creates the interface object that we use to interact with the sensor and defines which pins it is attached to. We see that PINTRIG and PINECHO are defined to P6_4 and P6_5 just above. 
![[Pasted image 20250614150306.png]]
In the setup routine we see initialization calls to the serial monitor, which allows us to print messages over USB, and a call to "mySensor.begin()". This is an initialization routine for the ultrasonic sensor and must be called before we can receive measurements from the device.
![[Pasted image 20250614150319.png]]
In the loop we have a variable called "DISTANCE" which is assigned a value from "mySensor.read()". This is the distance value produced by the sensor. We then make calls to "Serial.print()" to print this information to the screen. Finally, a small delay is added to the loop to keep the terminal from printing too many messages.

NOTE: You will need to find some creative way to mount your ultrasonic sensor to your robot.