# Ceci n'est pas un Cisco.

We've experienced all sorts of things with the Cisco RV325 series. Stability however isn’t one of them when running several heavy traffic IPSec tunnels. 
There’s no remote reboot functionality that I know of. The only pragmatic solution before getting a maintenance window to swap it with different kit was to use selenium and navigate to the console screens and reboot it from a scheduled cron job.  

Works up until Firmware v1.4.2.19
