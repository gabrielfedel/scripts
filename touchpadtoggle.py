#a simple script to toggle touchpad
#maybe you need to change your touchpad, to show yout touchpad type use xinput on terminal

import subprocess

a=subprocess.check_output(["xinput","list-props","SynPS/2 Synaptics TouchPad"])
pos=a.find('Enabled')
enabled=a[pos+15]
if enabled=="1":
	subprocess.call(["xinput","set-prop","SynPS/2 Synaptics TouchPad","Device Enabled","0"])
else:
	subprocess.call(["xinput","set-prop","SynPS/2 Synaptics TouchPad","Device Enabled","1"])
