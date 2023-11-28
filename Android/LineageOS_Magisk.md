### Updating Lineago OS 23 (Android 13) on OnePlus 8 Pro (IN2020)

> **Caution!** Updates won't work with Company Portal installed. To update your phone you first need to get rid of it (better remove all company apps, but if you don't won't to, you can try openning Company Portal and in the left burger menu there will be option to remove company administration only). After doing so, enable USB Debugging in the Developer Options if it was disabled.

> **Info:** patching `boot.img` won't work on your device, so follow this tutorial instead.

 
1. Update OS normally (through settings).
2. Download latest Magisk APK from [their GitHub](https://github.com/topjohnwu/Magisk/releases/) to your computer
3. Enter **fastboot mode** (recovery mode) and sideload Magisk `adb sideload Magisk.apk` (accept installation from phone, by clicking YES). After installation is successful unplug your phone from the PC.
4. Reboot notmally to the system (After logging in several more reboots will probably happen, just ignore them. If "factory reset window" appears, that means that you most likely some of the Magisk modules installed is conflicting with your phone. At this point just ignore all of the reboots and pop-up windows and when fastboot mode appears, select **try again** option, but when you will be able to use your phone again, don't forget to remove all Zgisk modules installed).
5. Once rebooting sequence finished and you can use your apps - open Magisk (or Better Settings) and install both **App** and **Magisk (then direct installation)** (in the specified order). Once again lots of phone reboots will probably happen, behave the same as in the previous step.
    
    At this point something may go wrong and you won't be able to boot into your system after Magisk installation. Then you just need to enter **fastboot mode** and flash boot with boot.img from the 
    [official LineageOS page](https://download.lineageos.org/devices/instantnoodlep/builds) with `fastboot flash boot boot.img`. After doing so you will end up with bare Lineage OS without root. Now repeat the whole process from the beggining or search for the solution yourself.

6. Turn off all Zygisk modules (SafetyNet Fix, PlayIntegrityFix, etc). Enable zygisk and reboot your phone.
7. After rebooting, enable all the modules back and reboot your phone again. Now Zygisk should work.
8. Perform basic Magisk "hiding": hide app, rename it. Enable battery unrestricted mode in system settings for Magisk (or "Better Options"), it may help reduce number of false alerts. 
9. That's it, your device now should be fully rooted and they may work nice.

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
    - Google Play Services
    - McDonald's
    - any banking apps
  
At this point it seems to run quite reliably for me, but I remember changing some ID of my device, so it shows up as Android 9 or something, when in reality it is Android 13. 


### Other useful Magisk Modules

- Magisk Bootloop Protector
- OnePlus DolbyAtmos
