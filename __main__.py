#!/usr/bin/env python3.12
import psutil
import subprocess
from rich import print 

battery = psutil.sensors_battery()
count = 0
while battery.power_plugged:

   if count == 0:
      count=+1
      print("[bold red]   your PC is plugin. unplugin it before shutdown 󰚦 󰚦\n[/bold red]")
   try:
     battery = psutil.sensors_battery()
   except KeyboardInterrupt:
      exit()


try:
   print("[bold green] system now shuting down [/bold green]")
   #print("[blue] yes this shit is working [/ blue]")
   subprocess.run(["systemctl" ,"poweroff"], check=True)
except subprocess.CalledProcessError as e:

   print(e)
