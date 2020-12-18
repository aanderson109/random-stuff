# Running a Script on Boot with a Raspberry Pi #
A guide/notes on how to run a script on boot on a raspberry pi.

## Method 1: rc.local ##
Using rc.local is the easiest method for running a script on boot. However, it will limit the programs ability since rc.local runs BEFORE X
so, you cannot access any GUI elements.

The Linux OS on the Pi goes through various runlevels while the system boots. Each runlevel executes run control scripts which do various things to the system.
This method focuses on one run control script in particular: rc.local. rc.local is executed once all the other services have been setup but before the multiuser runlevel
where you would usually log-in. Many linux distributions do not use or need a rc.local, it is a nice method for achieving our end goal of having data collection begin at
boot so if the embedded system accidently blinked power, it could recover.

### Getting into rc.local ###
You need sudo level control to access the rc.local file. Use the command: sudo nano /etc/rc.local to edit the file on the Pi. Once you have access to the file,
you can put in the script you want to run on boot. To do so, right before the "exit 0" line type in the typical "python" for executing a python script along with
the file path. For example, if the file is located in the desktop of the user pi you would type: "python /home/pi/desktop/script.py." However, there is a small
thing to note here. If you do not include an ampersand (&) after the script path, the script will block the execution of the rest of the boot process. Without
that character, the rc.local script waits for your script to break before continuing. Because of the rc.local placement in the boot process, this would only prevent
the user from logging in so it isn't that big of a deal. Addiitionally, considering that we want data to collect for the entire duration the pi is deployed we actually
would prefer this functionality. However, we need to figure out when exactly our script should stop.

### When Our Data Collection Script Needs to Stop ###
Our script is in the rc.local file now so on boot the raspberry pi starts collecting data. This is the result we sought after however, the loop is infinite and we need
to put some limitations so it can stop and allow user access for when the data needs to be harvested. The best way would be to automatically break the script once a USB
cable has been plugged in to the Pi and detected since there is no other reason for a USB cable to be connected. We can specify that inside the script and have it check
for USB connectivity every second or so.

### Putting It All Together ###
With this model, on boot the Pi creates a new file for the data to be stored. Once that file has been created, it proceeds to start collecting data. It collects data and
after every point collected, looks to see if a USB has been connected. Once the USB connection has been detected, the script breaks and it allows for the user to log-in.

## Method 2: systemd ##
Systemd allows you to specify when a script should run as other services are initializing during boot. This allows for a wide range of customization and specifity at the price of being complex.

### Unit Files ###
Utilizing systemd will require using a unit file. Unit files are text files that provides systemd information about services, devices, and more. For this specific application (embedded accelerometer), we do not need a GUI which will make things easier. However, we will still go over the GUI section just incase it is relevant in the future. A side benefit of using this is the preservation of power which can be extremely useful especially for embedded applications such as this one.

#### No GUI ####