# Mysterious Boxes

Follow the guidlines listed below as-is if you are using *nix OS. If you are using Windows then replace all the `.sh` files in the following steps with `.bat` files and follow the steps.

## Setup

### Step 1

- Install VirtualBox (preferably 5.0 or later)

### Step 2

- Download the lab setup files and virtual machines available as zip file at following link

[https://archive.org/download/scapy-pc-workshop-32bit/scapy-pc-workshop-32bit.zip](https://archive.org/download/scapy-pc-workshop-32bit/scapy-pc-workshop-32bit.zip)

- Extract the zip file in a directory 

```
unzip scapy-pc-workshop-32bit.zip
```

### Step 3

- Change the directory to the directory where you have extracted the files

- Run the script `import_labs.sh`
        
    - This script will import all the OVA files from the directory into your VirtualBox
    - In the end, this script will list all the VMs available in VirtualBox
    - If you see victim1, victim2, attacker in the VMs list, the importing is successful

- Run the script `start_labs.sh`
    
    - This script will setup and run your lab VMs
    - All the victims will run in the background and only attacker will run in the foreground
    - This script will display list of all the running VMs in the end
    - If you see two victims and an attacker in the list, you are ready!

*Run the script `stop_labs.sh` when done with the labs. This will gracefully shutdown all the lab VMs.*

## Troubleshooting (Windows)

All the scripts assume the VirtualBox installation is at `C:\Program Files\Oracle\VirtualBox`. In case, if the installation is at a different location, edit the following line in script to manually point to the right location.

```
PATH=%PATH%;C:\Program Files\Oracle\VirtualBox
```

All the VMs have host-only interface turned on by default. Windows VirtualBox interface naming convention tend to be inconsistent. In case you are having trouble starting VMs due to network interface name, change the interface name in script manually to match your VirtualBox host-only adapter interface name.

```
vboxmanage modifyvm "victim1" --nic1 hostonly --hostonlyadapter1 <YOUR_INTERFACE_NAME_HERE">
```


## Topology

### Host machine

- Host OS is the primary Operating System on which you are running VirtualBox
- Host OS is on the same sub-net as the VM’s

### Attacker machine

    Username: attacker
    Password: attacker

- The VM displayed after running `start_labs.sh` is our attacker
- This is our base machine for this workshop from where we orchestrate our attacks
- The attacker machine has SSH server running so you can use SSH to login to the machine
- For GUI, you can login using the above credentials in the VM and run `startx` command
- The GUI is openbox based, it is intended to be super minimal so don’t be surprised about lack of "features"
- `readme.txt` file in home directory has more info on tools installed and essential commands etc

### Victim machines

- Bunch of pre-configured VM's
- Configured to run in the background (headless mode)
- Victims have varying operating systems, listening services and security policies

## The Goal

To find as much information as we can about the victim machines using Scapy on attacker machine.

- Fingerprinting OSs
- Find listening services
- Understand security policies
