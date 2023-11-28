### Updating OS on OnePlus 8 Pro

Patching boot.img won't work, so follow this: 
1. Update OS normally
2. Download latest Magisk APK from [their GitHub](https://github.com/topjohnwu/Magisk/releases/) to your computer
3. Enter fastboot mode and `adb sideload Magisk.apk`

If something goes wrong and you cannot boot into you OS, just enter fastboot mode and flash boot with boot.img from the 
[official LineageOS page](https://download.lineageos.org/devices/instantnoodlep/builds) with `fastboot flash boot boot.img`


### Making SafetyNet work

To chek if the phone is ready download [YASNAC - Yet ANother SafetyNet Attestation Chacker](https://github.com/RikkaW/YASNAC) 
(should be available in PlayStore). For PlayIntegrity check install Play Integrity API Checker.

_Some steps may have been lost, but those are 100% necessary..._
1. Install Systemless Host Magisk Module
2. Install [Universal SafetyNet Fix](https://github.com/kdrag0n/safetynet-fix) Magisk Module or its 
    [modification by Displax](https://github.com/Displax/safetynet-fix/) (the first one doesn't work for me).
3. Since November 2023 Play Integrity feature doesn't work (YASNAC doesn't detect this), so [PlayIntegrityFix](https://github.com/chiteroman/PlayIntegrityFix) should be installed too. 
4. Activate Zygisk (Zygote on Magisk) and add the following apps there:
    - Google Play Store
    - Google Services Framework
    - Google Wallet
    - McDonald's
    - any banking apps
  
At this point it seems to run quite reliably for me, but I remember changing some ID of my device, so it shows up as Android 9 
or something, when in reality it is Android 13. 


### Other useful Magisk Modules

- Magisk Bootloop Protector
- OnePlus DolbyAtmos
