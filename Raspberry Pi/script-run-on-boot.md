# Running a Script on Boot with a Raspberry Pi #
A guide/notes on how to run a script on boot on a raspberry pi.

## Method 1: rc.local ##
Using rc.local is the easiest method for running a script on boot. However, it will limit the programs ability since rc.local runs __before__ X
so, you cannot access any GUI elements.

The Linux OS on the Pi goes through various runlevels while the system boots. Each runlevel executes run control scripts which do various things to the system. This method focuses on one run control script in particular: ```rc.local```. __rc.local__ is executed once all the other services have been setup but before the multiuser runlevel where you would usually log-in. Many linux distributions do not use or need a rc.local, it is a nice method for achieving our end goal of having data collection begin at boot so if the embedded system accidently blinked power, it could recover.

### Getting into rc.local ###
You need sudo level control to access the rc.local file. Use the command: ```sudo nano /etc/rc.local``` to edit the file on the Pi. Once you have access to the file, you can put in the script you want to run on boot. To do so, right before the ```exit 0``` line type in the typical "python" for executing a python script along with the file path. For example, if the file is located in the desktop of the user pi you would type: ```python /home/pi/desktop/script.py.``` However, there is a small thing to note here. If you do not include an __ampersand (&)__ after the script path, the script will block the execution of the rest of the boot process. Without that character, the rc.local script waits for your script to break before continuing. Because of the rc.local placement in the boot process, this would only prevent the user from logging in so it isn't that big of a deal. Addiitionally, considering that we want data to collect for the entire duration the pi is deployed we actually would prefer this functionality. However, we need to figure out when exactly our script should stop.

### When Our Data Collection Script Needs to Stop ###
Our script is in the rc.local file now so on boot the raspberry pi starts collecting data. This is the result we sought after however, the loop is infinite and we need to put some limitations so it can stop and allow user access for when the data needs to be harvested. The best way would be to automatically break the script once a USB cable has been plugged in to the Pi and detected since there is no other reason for a USB cable to be connected. We can specify that inside the script and have it check for USB connectivity every second or so.

### Putting It All Together ###
With this model, on boot the Pi creates a new file for the data to be stored. Once that file has been created, it proceeds to start collecting data. It collects data and after every point collected, looks to see if a USB has been connected. Once the USB connection has been detected, the script breaks and it allows for the user to log-in.

## Method 2: systemd ##
Systemd allows you to specify when a script should run as other services are initializing during boot. This allows for a wide range of customization and specifity at the price of being complex.

### Unit Files ###
Utilizing systemd will require using a unit file. Unit files are text files that provides systemd information about services, devices, and more. For this specific application (embedded accelerometer), we do not need a GUI which will make things easier. However, we will still go over the GUI section just incase it is relevant in the future. A side benefit of using this is the preservation of power which can be extremely useful especially for embedded applications such as this one.

### No GUI ###
Basic scripts such as data collection, datalogging etc. do not need GUIs so, this is for them. Lets get started.

First you need to create a .service file in the systemd directory: ```sudo nano /lib/systemd/scriptName.service```

With the file open and ready for editing, lets enter the necessary information:
```
[Unit]
Description = A Script    # this does not matter. you can make it anything.
After = multi-user.target # this does matter. It tells Linux when our program needs to be executed. In this case it is "After" multi-user.target multi-user.target is a system                                state specifically the state where control is transferred to the user and occurs before the X system begins so no GUI. Using this state will allow                                for the script to run WITHOUT needing to log-in. This is customizable for whatever your needs are.

[Service]
ExecStart = /usr/bin/python3 /home/pi/script.py # ExecStart is the command that executes the script. First we specify where python3 is so Linux doesn't get confused then, we                                                        tell it where the script is so Linux doesn't get lost. Make sure you always use absolute paths otherwise Linux will get lost.

[Install]
WantedBy = multi-user.target  # WantedBytells Linux what target we want our program to be included with. In this case, it is multi-user.target
 ```
 SO, now that we have that file made we need to make sure systemd recognizes it. We do that with the command: ```sudo systemctl daemon-reload```
 
 ***NOTE: you will need to do this command after every edit to the .service file.***
 
 Now, we need to make sure it understands it has to start this on boot. We do that like this: ```sudo systemctl enable scriptName.service```
 
 Reboot the system and see if it worked: ```sudo reboot```

### GUI ###
If the script we are running needs to utilize graphical features we'll have to do it a different way.

Create a new __.service__ file in the __systemd__ directory: ```sudo nano /lib/systemd/system/scriptName.service```

Now we edit the file in a similar way to how we did it before:
```
[Unit]
Description = Does a Thing # Same as before, this part doesn't really matter only for organization.

[Service]                                            # where we specify environmental varibles like last time.
Environment = DISPLAY=:0                             # connects to the primary display
Environment = XAUTHORITY = /home/pi/.Xauthority      # tells our program where to find the proper credentials to use the X system
ExecStart = /usr/bin/python3 /home/pi/scriptName.py  # command that executes the script. We tell it where the python3 is and where our script is. ***USE ABSOLUTE PATHS!***
Restart = always                                     # tells the program to restart if it fails or exits
RestartSec = 10s                                     # sets the reset time to every 10 seconds from the time it failed or exited
KillMode = process                                   # kills all processes associated with our program if it fails or exits. Allows for a clean restart
TimeoutSec = infinity                                # doesn't ever stop the execution of our program

[Install]
WantedBy = graphical.target
```
Once again, we have to tell systemd to recognize our file so we use: ```sudo systemctl daemon-reload```

And, once again, we have to enable the file from boot with: ```sudo systemctl enable scriptName.service```

Reboot to test it out with: ```sudo reboot```
