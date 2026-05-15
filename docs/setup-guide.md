# My Personel Setup

## VBOX image and setting
Download [Oracle Virtual Box](https://www.virtualbox.org/wiki/Downloads) according to your host Operating System

Download the latest [Ubuntu](https://ubuntu.com/download/desktop) LTS version

Host Machine Specs:
- Processor: AMD Rysen 7 3700X 8-Core Processor (3.60 GHz)
- Installed RAM: 48.0 GB
- Graphics Card: NIVIDIA GeForce RTX 5070 Ti (16 GB)
- Storage: about 6.37 TB
- OS: Windows 11

Virtual Box Settings
- OS: Ubuntu 24.04.3 LTS
- System
    - MotherBoard
        - Base Memory: 12288 MB
        - Boot order: Optical, Hard Disk, Floppy
        - Chipset Type: ICH9
        - TPM Version: None
        - Pointing Device: USB Tablet
        - I/O APIC: Enabled
        - Hardware Clock in UTC: Enabled
        - UEFI: Disabled
    - Processor
        - Number of CPUs: 6
        - Processing Cap: 100%
        - PAE/NX: Enabled
    - Acceleration
        - Paravirtualization Interface: KVM
        - HArdware Virtualization: Nesting Paging Enabled
- Display
    - Video Memory: 128 MB
    - Number of Virtual Monitors: 1
    - Scale Factor: 100%
    - Graphics Controller VMSVGA
    - 3D Acceleration: Disabled
- Storage: 60.00 GB Dynamically allocated storage
- Network:
    - Adapter 1: Attached to NAT
    - Adapter 2: Attached to Host-only Adapter
    - Adapter 3: Internal Network
