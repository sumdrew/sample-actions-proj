---
title: RECON Lab Manual
author: Sumuri Forensics
date: March 7, 2023
---

# 1. Introduction

![Figure 1.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/912d8a06-50c0-496f-bc53-1ba733adfc34/Screen1.jpg)

RECON LAB is a full Forensic Suite that supports numerous file systems such as Windows, macOS, Linux, iOS, Android and more. RECON LAB was created to solve multiple problems inherent in other forensic tools and to expedite processing and analysis without sacrificing the quality of the exam.

RECON LAB was designed, developed and runs on macOS. MacOS was the only logical choice for developing a modern forensic tool to support the most common and largest number of file systems and artifacts without losing data.

The most difficult file system and operating system (OS) for most forensic tools to support is macOS. Mac understands itself and can interpret its own artifacts. This is not true of other file systems, operating systems, and other forensic tools as they do not natively support macOS and its artifacts.

In addition to supporting its own file system and artifacts, macOS supports a multitude of other file systems and the artifacts of Windows, Linux, Unix and many more.

RECON LAB is the only full Forensic Suite designed natively on macOS to take full advantage of the power within macOS. Other forensic tools that run on a Mac were ported from other non-Mac operating systems and experience limitations. Instead of utilizing native macOS libraries they rely on reverse engineering and third-party applications which can lead to missed data, improper interpretation of data and slower processing times.

RECON LAB primarily relies on native macOS libraries so support for new macOS file systems and/or artifacts is quick or instantaneous.

RECON LAB comes with one full year of free updates and support.

## 1.1. Why Use a Mac for Forensic Analysis?

Until the release of RECON LAB, no other forensic tool properly processed or utilized the correct timestamps for macOS.

This is only one example of an extremely important artifact that is improperly interpreted or missed completely by other forensic tools.

It is imperative to understand the importance of macOS in forensic exams and what may be missed by other forensic tools.

### 1.1.1. Apple Extended Attributes

Apple Extended Attributes are special metadata created only within macOS to allow searches via the macOS search utility - Spotlight.

Apple Extended Attributes contain extremely valuable information for investigations. This special metadata cannot be seen in Windows. Most Windows forensic tools ignore or have a limited ability to display Apple Extended Attributes as they are not natively supported.

Images and data collected by SUMURI’s RECON ITR and processed by RECON LAB provide the most extensive views of Apple Extended Metadata.

Understanding Apple Extended Metadata is critical to investigations.

### 1.1.2. Viewing Proper Timestamps

Apple’s macOS utilizes Apple Extended Attributes for timestamps in favor of POSIX (Unix) timestamps.

RECON IMAGER, when used with RECON LAB, is the only solution to properly view and utilize the correct macOS timestamps.

### 1.1.3. Viewing Files Natively

There are many file types and artifacts proprietary to macOS. As RECON LAB is designed on macOS it supports all macOS files and artifacts natively.

For example, Applications in macOS are actually “bundle” files. Everything needed for the application to run is found within the bundle file. What looks and appears to a single file to the Mac user is actually thousands of innocuous files and folders. In traditional forensic tools, these bundle files are expanded adding unnecessary artifacts to your case.

RECON LAB also is integrated with macOS’s Quick Look which natively supports viewing hundreds of file types without needing or using the original application. Unlike other forensic tools, the files do not have to be exported first to view saving time.

### 1.1.4. Apple File System (APFS)

Apple File System (APFS) is a proprietary file system from Apple and utilized for macOS, iOS, watchOS, and tvOS. APFS is natively and fully supported on macOS High Sierra (10.13) and above. APFS has limited support in macOS Sierra (10.12). APFS has no support within Windows operating systems. Any support for APFS on Windows and/or Windows forensic tools are using reversed engineered non-native technologies.

SUMURI’s RECON ITR can create forensic images that can be processed and analyzed with RECON LAB natively.

RECON ITR and RECON LAB also automatically supports the imaging and processing macOS 10.15 System and user DATA partitions.

### 1.1.5. Local Time Machine Snapshots (APFS)

Time Machine is a utility in macOS that is used for creating backups. Time Machine must be activated by the user and requires a local or remote disk to store the backups (Time Machine disk). If the Time Machine disk is not available the backups are stored locally. These backups are known as “Local Time Machine Snapshots” in APFS. They are also sometimes referred to as APFS Snapshots.

RECON IMAGER (included with RECON ITR) along with RECON LAB are the only solutions that can display, image, hash and analyze Local Time Machine Snapshots in Macs with T2 Security Chipsets and without.

_Note: An examiner should not expect to find Local Time Machine Snapshots in every case. They will only exist when the conditions above have been met._

### 1.1.6. FileVault

FileVault (version 2) is the macOS full _volume_ encryption of which there are no backdoors. FileVault is mounted and decrypted with the user’s login password or Recovery Key which is created when FileVault was originally enabled.

RECON LAB allows the examiner to decrypt the forensic image of a Mac encrypted with FileVault natively using either the password or Recovery Key.

### 1.1.7. Support for Other File Systems

RECON LAB was designed to harness the power of macOS. Whatever the Mac can mount, RECON LAB can process.

MacOS natively supports APFS, macOS Extended (HFS+), MS-DOS FAT, ExFAT and NTFS (as read-only).

Using freely available open-source FUSE solutions and Paragon Software drivers (included) just about any file system can be mounted and processed with RECON LAB such as Linux ext2, ext3, and ext4.

## 1.2. Hybrid Processing Engine

Unlike any other forensic solution, RECON LAB utilizes a Hybrid Processing Engine.

The Hybrid Processing Engine processes a forensic image both inside RECON LAB and mounted outside RECON LAB using macOS.

The Hybrid Process Engine maximizes the recovery of artifacts and simultaneously increases the speed of processing.

Additionally, this approach uniquely allows RECON LAB to utilize the power of macOS natively.

## 1.3. Three Stage Analysis

RECON LAB offers three-stages of analysis.

**Stage One** – Parse and recovery thousands of artifacts with **Automated Analysis** of Windows, macOS, iOS, AndroidOS, and Google Takeout.

**Stage Two** – Four **Advanced Forensic Viewers** assist in parsing and examining macOS Property Lists (.plist), SQLite Databases, Hex, and the Window’s Registry.

**Stage Three** – Utilize hundreds of features built into RECON LAB make **manual analysis** easier.

## 1.4. Support for Hundreds of Timestamps

RECON LAB currently supports several hundred individual timestamps. These include file systems, Apple Extended Metadata and application-specific timestamps.

These timestamps are integrated throughout RECON LAB to provide “one of a kind” analysis along with exponential reporting options.

Additionally, RECON LAB provides “second to none” chronological analysis and reporting.

## 1.5. Advanced Timelines

With such large support for hundreds of timestamps, RECON LAB can generate both textual and graphical views of events to make analysis easier.

Placing these events in chronological order allows an examiner to see events unfold minute by minute or even second by second.

Having the ability to see events in order based on time allows an examiner to solve cases and render opinions faster and more accurately.

## 1.6. Advanced Data Correlation

In a single day, a person of interest will probably use several devices capable of storing electronic data. For example, they may use a laptop or tablet at home, a mobile phone on their way to work and a desktop computer when they arrive. On each of these devices, our person of interest could use multiple web browsers and messaging apps. To add even more complexity, our person of interest is moving to different locations throughout the day and generating different location artifacts.

To get a clear picture of what our person of interest has done in a day RECON LAB has developed Advanced Data Correlation to collate all of this information into single views regardless of device or application.

Advanced Data Correlation (as **Redefined Results**) along with support for hundreds of timestamps provides an examiner with amazing investigative insight.

## 1.7. Advanced Reporting With Full Control

RECON LAB provides you with exponential reporting options from the granular level (single artifact) to the global level (all artifacts included).

Additionally, RECON LAB includes the first of its kind WYSIWYG (What You See Is What You Get) reporting mode called Story Board.

Story Board allows the user to have full control over the reporting process and is as easy to use as a word processor.

The examiner has the ability to add, remove or annotate bookmarks anywhere in the report at any time.

Story Board also allows you to add your bookmarks and tags in chronological order to make it easier to understand the timeline of events.

# 2. Recommended Minimum Requirements

Macs are unique in doing more with less. That being said, RECON LAB will work on most Macs.

Keep in mind the simple formula: **Processor + RAM = Speed**

The faster the processor and the more RAM that is installed will determine how fast you can process data.

## 2.1. Minimum Recommended Specifications for Running RECON LAB

Any Mac with an i7 Quad-core Processor or M1 equivalent with 16GB of RAM capable of running macOS 10.13 or above.

An Admin user required.

To get faster speeds, even with slower Macs, consider using a Thunderbolt 3 External RAID. Putting both the evidence and case files on the external Thunderbolt 3 RAID will provide an extra boost in the speed of processing.

SUMURI has tested and offers the [ARECA 8-Bay Thunderbolt 3 RAID Storage](https://sumuri.com/product/arc-8050t3-8/) with various storage options.

# 3. Helpful Hints

Before starting a new case with RECON LAB please refer to these helpful tips.

**Use macOS Extended for Evidence Drives**

The macOS can support a variety of file systems, however, in testing, we have the best results with macOS Extended (HFS+).

If you want to mount your macOS Extended evidence drive on Windows use the HFS+ for Windows drivers from Paragon Software that are provided to you with your purchase of RECON LAB.

Additionally, if you are creating logical images of Mac data to any non-Mac file system you will lose the Apple Extended Metadata.

**Use Apple Disk Image Format (.dmg) for Imaging Evidence**

The Apple Disk Image that is created with RECON ITR or PALADIN is a RAW image format that can be loaded into any forensic tool that supports RAW images. The .dmg image is natively supported by the Mac.

Although RECON LAB supports Expert Witness Formats (.E01, .Ex01) it is not native to the Mac and requires the use of FUSE. FUSE acts as an interpreter to mount non-native file systems. Using FUSE adds an additional unnecessary layer between the forensic image and RECON LAB and is not recommended.

**Avoid Segmentation of Forensic Image Files**

RECON LAB supports segmented image files. However, with extremely large disk sizes found in modern devices, thousands of segments can be created which may cause issues. If possible, avoid segmenting forensic images and use a single file.

# 4. Getting Support

Support for RECON LAB is available via our Online Support site and submitting a ticket here:

[https://helpdesk.sumuri.com](https://helpdesk.sumuri.com/)

During regular business hours, we strive to respond in less than one hour but no longer than 24 hours.

SUMURI is based in the state of Delaware, USA (Eastern Time Zone – EST/EDT).

Our office hours are 0900-1700 (9 a.m. – 5 p.m.). SUMURI is closed for US [Federal Holidays](https://www.opm.gov/policy-data-oversight/pay-leave/pay-administration/fact-sheets/holidays-work-schedules-and-pay/).

**Law Enforcement Emergency Support**

If you are law enforcement, and are in need of immediate emergency assistance with any of our products, please contact us anytime at +1 302.570.0015.

# 5. Renewing RECON LAB

RECON LAB comes with one full year of support and updates.  Once RECON LAB expires, its license will need to be renewed in order to continue to receive updates and support.

RECON LAB can be renewed online via our website here:

[https://sumuri.com/product/recon-lab-renewal/](https://sumuri.com/product/recon-lab-renewal/)

Additionally, RECON LAB can be renewed by contacting our office to be assisted by a team member

# 6. Training

SUMURI offers vendor-neutral training on Mac Forensics. SUMURI’s courses teach the concepts and knowledge to use RECON ITR (or other tools) to process Mac artifacts and Mac file systems.

* [Best Practices In Mac Forensics (MFSC-101)](https://sumuri.com/sumuris-macintosh-forensic-survival-course/)
* [Advanced Practices In Mac Forensics (MFSC-201)](https://sumuri.com/macintosh-forensic-survival-course-level-2/)

If interested in hosting a training course at your location and receiving up to two free seats please contact us via the link below.

* [Hosting SUMURI Training](https://sumuri.com/host-training/)

# 7. Installation

RECON LAB includes and relies on native libraries, some third-party applications and utilities to ensure that largest amount of data can be processed and analyzed.

Please install all the recommended applications, in order, and one at a time, using the instructions below.

Due to Mac’s strict adherence to security, you may be asked to provide your password various times during the installation.

Periodically check to make sure that all dependent applications are updated:

Updates for RECON LAB can be downloaded at: [https://sumuri.com/updates/](https://sumuri.com/updates/)

## 7.1. Installing Xcode and Command Line Tools

Xcode is a free development environment provided by Apple. Xcode and Xcode Command Line Tools include additional binaries and applications which are used in RECON LAB.

**Installing Xcode**

1. Apple Xcode is available for free using Apple’s App Store

2. Click the “Get” button to install Xcode on your Mac via the Apple App Store.

3. Be sure to open and fully install the application before going forward.

**Installing Xcode Command Line Tools**

To install or check to see if Xcode Command Line Tools are installed follow the instructions below:

1. Open the Terminal Application – `/Applications/Utilities/Terminal`

2. Type the following command and hit return: `xcode-select --install`

3. Follow the instructions provided by the application.

## 7.2. Installing FUSE for macOS

FUSE for macOS is a free open-source application that acts as an interpreter for non-native file systems. FUSE for macOS assists in loading Expert Witness Format (EWF) forensic images such as .E01 and .Ex01. FUSE for macOS must be installed to mount and process EWF images.

**Installing FUSE for macOS**

1. Navigate to the FUSE for macOS website and download the version that matches your macOS from here: [https://osxfuse.github.io/](https://osxfuse.github.io/)

2. Double-click on the .dmg file downloaded.

3. Double-click on the “FUSE for macOS” icon to install.

4. Follow the application instructions for completing the installation.

## 7.3. Installing Paragon Drivers

SUMURI has partnered with Paragon Software to include helpful file system drivers for both Mac and Windows. You will receive a license code for downloading and activating Paragon Software applications when you purchase a full version of RECON LAB.

To download and install Paragon Software applications follow the instructions below.

**Accessing Paragon Software Applications**

1. Navigate to Paragon Software’s website and create an account if you do not already have one here: [https://my.paragon-software.com/#/login](https://my.paragon-software.com/%23/login)

2. Navigate to “Register New Product” and enter the code provided to you when you purchased RECON LAB.

3. Navigate to “My Products” after entering the code to access and download your applications.

**Installing extFS for Mac by Paragon Software**

1. Download extFS for Mac following the instructions above.

2. Double-click on the .dmg downloaded from Paragon.

3. Double-click on “Install extFS for Mac” to install drivers for Linux file systems.

4. Complete the installation by following the instructions provided.

## 7.4. Installing RECON LAB

Make sure that you have downloaded the most current version of RECON LAB and follow the instructions below to install. Go to Section 7.7 for more information.

![Figure 7.4.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/ed6dc85e-f267-42b5-a0b9-f136d2ac34df/image.png)

Move the RECON LAB installer .dmg to your Desktop and double-click to mount the installer.

![Figure 7.4.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/acee573d-2f09-46b4-b10f-de072cd66ed7/image.png)

A notification window will appear to ask if you want to open the application. Choose “Open”.

RECON LAB will then begin scanning to see if additional packages need to be installed and may prompt you to install extra components.

![Figure 7.4.f3: ](https://t10572667.p.clickup-attachments.com/t10572667/ed9ce377-54e4-4a23-95b6-ad47ef67f914/Screen%20Shot%202022-01-04%20at%204.18.03%20PM.png)

If prompted, select install to install the extra packages.

![Figure 7.4.f4: ](https://t10572667.p.clickup-attachments.com/t10572667/170a81cb-cfc7-46fb-81ec-244b97cb6e33/Screen%20Shot%202022-01-04%20at%204.18.07%20PM.png)

Once that has been completed, the installer will ask you to continue. Select Continue to launch the RECON LAB Installer.

![Figure 7.4.f5: ](https://t10572667.p.clickup-attachments.com/t10572667/4878fdfc-2ce2-45c7-b8fc-b30c76548743/Screen%20Shot%202022-01-04%20at%204.20.15%20PM.png)

The RECON LAB Installer window will now appear.

![Figure 7.4.f6: ](https://t10572667.p.clickup-attachments.com/t10572667/45b662ed-c61f-4d5a-af12-fd8f26505e1c/image.png)

Choose one of the following options:

**Install** – Updates existing RECON LAB installations preserving your settings, examiner and agency information.

**Clean Install** – Use this for first time installs or to reset RECON LAB to its original settings.

**Uninstall** – Use this option to remove RECON LAB from your Mac.

When the installation reports **Done**, quit the installer and eject the RECON LAB Installer disk image (right-click “Eject”).

## 7.5. Granting Privileges

Before launching RECON LAB for the first time, RECON LAB will need to be given Full Disk Access. This allows RECON LAB to gain access to areas and files restricted by standard permissions.

### 7.5.1. Full Disk Access

The following describes how to change the Full Disk Access permissions according to the version of macOS your examiner machine is running.

#### 7.5.1.1. macOS 12 and Below

![Figure 7.5.1.1.f7: ](https://lh6.googleusercontent.com/Jq6N2-XwNL7waTi5kI2pdLbBa19SkbMYR7aJj9Xa1z5PATvrFiUnLeW1mV3UAcg5eefHjhP3lJW2Bnx3C_yD-Z6AJzHsvx-bKiitVKxE9DU3coGHMeVvT7m-vC3WaWIvsncueJQlJEWCCNWzC9PjQ9wOt2pk1TQ4ghllqssF7I84KPz61IpE7GtntAgdew)

To give RECON LAB Full Disk Access on macOS 12 and below, navigate to **System Preferences** using the **Apple Menu** found in the top left corner (Apple Menu – System Preferences).

![Figure 7.5.1.1.f8: ](https://lh6.googleusercontent.com/SYzpxdYdKxbZL7s_j7G_oQ41S1GEvLCCOMQQCFfojISCwDdEF3LJ3u6vbOBdhdIwjF4v8EdXSwtVk43fJXtmu_cc4Yr6mDsppDYh_tpJoHO0YnLJBt_D2Ke7QL6es3YRBHrjKF5HG9AsTQpNUeAaOtK2ixeHhGrXXVxvolQtpM6pYlmwC2E5tifQFoHhaw)

From **System Preferences** select the **Security & Privacy** icon.

Follow the steps below to add RECON LAB to the **Full Disk Access** column.

![Figure 7.5.1.1.f9: ](https://lh6.googleusercontent.com/3yhC561ZrLVBBeaJPCPFZmos5QAOZzNIUPp7AFnfetDKyO3PXeHo7r0f7RTJPfQRnve7Did6PnptJb-y8PmuTZz0bZ3v5rMrguN8owrzCAWzKKMjI6hVw-0iTrD6U5AKNdaWNgziRFPxpnBVj4UR0fcqFdXShU7XctWMGxBvuLoIwMoYIWk9-tl2br1tDA)

1. Click on the lock icon in the bottom left corner and enter the admin password to unlock.

2. Select the **Privacy** tab and then **Full Disk Access** in the sidebar.

3. Click the **“+”** symbol and navigate to the RECON LAB application.

4. Select the **RECON LAB** application to give Full Disk Access permissions.

#### 7.5.1.2. macOS 13 and above

Alongside the release of macOS 13, Apple introduced a change to the tried and true System Preferences to make it more akin to iOS. System Preferences has now been changed to System Settings and includes a new interface.

To give RECON LAB Full Disk Access on macOS 12 and below, navigate to **System Settings** using the **Apple Menu** found in the top left corner (Apple Menu – System Settings).

![Figure 7.5.1.2.f10: ](https://lh3.googleusercontent.com/bviahqAsFcEPpipoWPF8apJEuCp3UpmWfMiHRdxMGnTCKEwCxS5PIFlY8Q-5mK6b7tcwfvqtl36z6QfTywlz7Oz2-Ypa3uVLpvKTz-_5gQolA1dKHb1vRVPjCaAOMNageMVaGqS5-HypLmvr_PqZvUOmXVS1BEkyCwfy0TvURCkmPXdNU16Dz-Q4GVriyA)

From **System Settings** select the **Security & Privacy** icon.

![Figure 7.5.1.2.f11: ](https://lh5.googleusercontent.com/4YD45epB_aG5lIA6uZJsefShqEKkJRQ5dyjxiayBMgeArVUIUEbSc5UiwhZu0eNvpfG-gSy07Z16dHgfzPszeMBTnzwYU0lcDQBg21eMCg2Jak0eMQprJgaN_NPbDAmYZAbSH4e_jn8bZDghMSYc2qLsmZsh1PTVAD6f6hvnsjlsDd5WnuUwZPIXz2cr1Q)

1. Navigate to **Full Disk Access**

2. Scroll to the bottom of the window to locate the **"+"** symbol.

3. Click the **“+”** symbol and enter the **administrator password**.

4. Navigate to the **RECON LAB** application.

5. Select the **RECON LAB** application and enable the switch to give Full Disk Access permissions.

![Figure 7.5.1.2.f12: ](https://t10572667.p.clickup-attachments.com/t10572667/91072f2b-b456-4526-bbbe-081a17ad0e5b/image.png)

## 7.6. Energy and Sleep Settings

Allowing your Mac to go to sleep in the middle of processing a case will most likely cause issues. Make sure that you disable any settings which “Put hard disks to sleep when possible” or that allows the computer to sleep when working with RECON LAB.

These settings can be changed in System Preferences (Apple Menu – System Preferences) in macOS 12 or in System Settings (Apple Menu – System Settings) in macOS 13.

### 7.6.1. macOS 13 (Ventura) and below

![Figure 7.6.1.f13: ](https://t10572667.p.clickup-attachments.com/t10572667/63dc1fe2-1ead-4f6e-8f79-2d6c7bfbbe5e/image.png)

Look for the **Energy Saver** icon.

![Figure 7.6.1.f14: ](https://t10572667.p.clickup-attachments.com/t10572667/812a41ed-bd55-468d-890f-6b2cb1710964/image.png)

Set the “Put hard disks to sleep when possible” setting to “Never.” This should ensure that RECON LAB’s processes will run uninterrupted.

On M1 and M2 laptops (such as the Macbook Pro) this setting may appear as “Battery” instead.

![Figure 7.6.1.f15: ](https://t10572667.p.clickup-attachments.com/t10572667/1ded977f-d533-4448-81cf-da4ffb223c1d/image.png)

![Figure 7.6.1.f16: ](https://t10572667.p.clickup-attachments.com/t10572667/8b9a2cfd-39a0-468d-ab2c-e65ccbf8ca0f/image.png)

Once “Battery” is selected, set the “Put hard disks to sleep when possible” setting to “Never.”

### 7.6.2. macOS 12 (Monterey) and below

![Figure 7.6.2.f17: ](https://t10572667.p.clickup-attachments.com/t10572667/a0310044-beaf-4c13-9834-f957dfecaadc/image.png)

Look for the **Energy Saver** icon. Then check both of the settings for **Battery** and **Power Adapter**.

![Figure 7.6.2.f18: ](https://t10572667.p.clickup-attachments.com/t10572667/9813b92c-f073-4125-8909-b9495786f059/image.png)

Under the **Battery** section, ensure the “Put hard disks to sleep when possible” and the “Enable Power Nap while on battery power” options are disabled in the **Power Adapter** tab. Additionally, be sure that the “Prevent computer from sleeping automatically when the display is off” option is enabled. Finally, make sure that “Turn Display off after:” is also set to “Never”.

![Figure 7.6.2.f19: ](https://t10572667.p.clickup-attachments.com/t10572667/b1276ab8-c2b9-4bbe-8f47-1911901a0579/image.png)

Energy Saver will bring you to the window shown above when working with an Apple machine that does not rely on battery power.

Under the **Power** tab, ensure the “Put hard disks to sleep when possible” and the “Enable Power Nap while on battery power” options are disabled. Also, be sure that the “Prevent computer from sleeping automatically when the display is off” option is enabled and that “Turn Display off after:” is also set to “Never”.

After following these steps, RECON LAB should have all the permissions it needs run uninterrupted.

## 7.7. Updating RECON LAB

Before using RECON LAB, please make sure that you have the latest update.

RECON LAB updates can be found here: [https://goo.gl/wWm2qi](https://goo.gl/wWm2qi)

Download the latest version (highest-numbered) and move the .dmg to your Desktop.

Notifications for new updates will be sent out to the email address that we have on file. If you are not sure if you are on the RECON LAB update list and would like to be notified when updates are released please let us know at [hello@sumuri.com](mailto:hello@sumuri.com).

**Updating with a Renewed License**

When updating RECON LAB, you have the option to point to a new license file. Click “Clean Install” in the Installer window, and you will see the option to replace your License file. Check the box and you can change your license file without losing configuration settings in RECON LAB.

![Figure 7.7.f20: ](https://t10572667.p.clickup-attachments.com/t10572667/61b8a11f-3a4d-4c2c-ae11-55debd22212b/image.png)

Click “Install” in the Installer window, and you will see the option to replace your License file. Make sure it is unchecked, and RECON LAB will update without the need to point to the license file.

# 8. Starting RECON LAB

Once installed, RECON LAB can be found in your **Applications** directory.

For quick access, you can grab the RECON LAB icon and drag it to your dock to create a shortcut.

![Figure 8.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/c91fb411-ac2f-477d-8026-c668835f8348/image.png)

To start RECON LAB, double-click the icon in the Applications folder or single-click if you created a shortcut within the dock.

## 8.1. Adding Your License

When you run RECON LAB for the first time after installation you will be prompted to add your license.

Your license can be found on the RECON LAB USB which also acts as your security dongle. The RECON LAB USB will need to be attached to your Mac in order to run.

If a demo was requested or if RECON LAB was recently renewed the license will be sent by email. Please keep your license some place safe.

![Figure 8.1.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/abcce971-f570-401b-b311-70179ad44a33/image.png)

If you are prompted to add your license choose “Browse” and navigate to your license file.

Select your license file and choose “Open”.

RECON LAB will add your license and restart.

## 8.2. Installing Python

Python, which is a common scripting language used in forensics, is utilized for some features in RECON LAB and should be installed. Make sure that Xcode and its Command Line Tools have been previously installed.

**Installing Python**

1. Download and install the latest version of Python3 for macOS from this link: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open Finder then go to the Applications folder, find the Python application, on the left side of the Python app you will see a dropdown arrow, expand it and double click on "Install Certificates.command”.

3. After installing the certificates open your terminal and run the following command to install additional required libraries: python3 -m pip install lz4 enum34

4. Messages regarding updating “pip” can be ignored.

## 8.3. Admin Password

Upon the first run of RECON LAB you will be prompted to enter your admin password one time. Enter your admin password and click “OK”.

## 8.4. Access Warning Messages

![Figure 8.4.f3: ](https://t10572667.p.clickup-attachments.com/t10572667/f74bf362-1c30-4d4f-b841-28931c4e824d/image.png)

When starting RECON LAB a message window will appear with some important information. This information may change so please review from time to time.

If you do not want the message to appear when you start RECON LAB select “Don’t show this message again”.

## 8.5. RECON LAB Welcome Screen

![Figure 8.5.f4: ](https://t10572667.p.clickup-attachments.com/t10572667/75b76acc-be41-4dcf-a8ea-e649b36499a4/Screen%20Shot%202021-12-30%20at%2010.11.11%20AM.png)

Upon starting RECON LAB you will be presented with the **Welcome Screen**.

The Version of RECON LAB will be found in the title bar.

In the bottom right corner, the Licensee, Purchase Date and Expiration Date are displayed for your reference.

The buttons along the bottom of the Welcome Screen are:

* **About RECON** – Access to RECON LAB’s EULA, change logs, exceptions and/or known issues, special requirements, support and updates information.

* **RECON Config** – Allows the examiner to create persistent settings.

* **Acquire iOS Device** – Opens the RECON LAB iOS Imager interface.

* **New Case** – Starts the New Case Wizard.

* **Load Case** – Allow an examiner to select a RECON LAB Case Folder.

# 9. Configuration

Every examiner will have a unique approach to an examination.

RECON LAB allows an examiner to configure a variety of settings prior to starting a case. Configuration settings are persistent and will automatically be set for each new case.

This approach saves a lot of time. Configuration settings can be overridden at any time if required.

## 9.1. Examiner Details

![Figure 9.1.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/5c27fcae-6143-4958-aba2-dfc0ea548e8e/image.png)

The **Examiner Details** settings allow entry of the following information:

* **Agency Name** – Name of the examination agency.

* **Examiner** – Name of the examiner.

* **Examiner Phone** – Phone number for the examiner.

* **Agency Address** – Agency address.

The agency logo can be changed by selecting the three dots under the current logo.

![Figure 9.1.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/209b6f3b-39d2-42b6-8cac-bb2409d9b871/image.png)

 Any graphic can be selected for the agency logo. RECON LAB supports adding PNG or JPEG image formats.

All information entered in the Examiner Details will automatically be added to any reports generated by RECON LAB.

## 9.2. Artifacts and Plugins

RECON LAB includes hundreds of plugins that recover thousands of artifacts automatically from Windows, macOS, iOS, Android and Google Takeout.

RECON LAB allows an examiner to enable plugins to run on every case and/or create templates for specific investigations.

![Figure 9.2.f3: ](https://t10572667.p.clickup-attachments.com/t10572667/393fb041-cd9d-49d3-9c4c-eec2fcafaf31/image.png)

Above is the interface for RECON LAB’s Plugin and Artifact selection. Columns and dots were added to the interface to help you quickly see if a plugin is supported within a specific platform.

Each plugin can have multiple artifacts. Activating a checkbox will enable the plugin.

On the left side, there are filters at the top for “All Plugins” and specific operating systems (i.e. “winOS”) and platforms (i.e. “Google Takeout”). Selecting any filter on the left-side removes all plugins from the Plugin Window on the right-side except for what is relevant to the operating system or platform selected. For example, if you select the “iOS Plugins” filter on the left you will only see plugins relating to iOS on the right.

 ![](https://t10572667.p.clickup-attachments.com/t10572667/1ef2cfa8-cdda-4943-9763-46ede3c44ccb/Screen%20Shot%202022-01-04%20at%2011.37.00%20AM.png)

Similarly, there is a Plugin Search box in the upper right corner that can be used to quickly filter all plugins. In the example above, the keyword “photo” was used to show all plugins that contained the word “photo” (i.e. Android Photos, Photo Booth).

At the bottom of the window, there is a “Save Template” button. Checking this box and providing a name will make a permanent template that can be used again.

**Saving a Template for Plugins and Artifacts**

![Figure 9.2.f4: ](https://t10572667.p.clickup-attachments.com/t10572667/f6fb1d8f-6169-4e86-9226-6f6185497f10/image.png)

1. Using the example above, the Plugin Search was used to find all plugins with the word “photo”.
2. Each of these plugins was selected using the checkboxes.
3. The “Save Template” box was checked and the name “Photo Search” was given to the template.
4. To save the new template the “Add” button was clicked.
5. The new template can now be selected and applied in the dropdown box at the top of the window.

Remember, settings can always be changed at any time within the case.

## 9.3. User Defined Extensions

User Defined Extension settings allow the examiner to create “buckets” (categories) for various file extensions. These categories will appear in the RECON LAB Sidebar. Any files with a matching file extension included in a Category will automatically be filtered and appear in the “bucket” in RECON LAB’s Sidebar.

![Figure 9.3.f5: ](https://t10572667.p.clickup-attachments.com/t10572667/53055dc1-b021-4763-b446-b14ea6af4e6d/image.png)

In the example above, the category Image contains the file extensions .png, .jpg, .jpeg, .ico and .gif. When a new case is started, any files matching these extensions will automatically be found in the Sidebar in a “bucket” named “Image”.

**Adding or Removing Categories and Extensions**

![Figure 9.3.f6: ](https://t10572667.p.clickup-attachments.com/t10572667/f30b2657-67aa-4e2b-9485-4dd6bb246586/image.png)

To create a new Category or to add an Extension simply click the “+” button. Enter the text and hit return.

To remove a Category or Extension select the item and click the “-” button.

To add multiple extensions at the same time use the “paste” or clipboard button. Make sure that your text is entered as on item per line with a single carriage return. Copy all the text to your Clipboard and then use the “paste” (clipboard) button to add multiple items at the same time.

## 9.4. User Defined File Signatures

User Defined File Signature settings allow the examiner to create “buckets” (categories) using a file’s signature. File signatures help identify files in the absence of extensions or if the file extension is incorrect.

The categories created will appear in the RECON LAB Sidebar. Any files with a matching a file’s signature included in a Category will automatically be filtered and appear in the “bucket” in RECON LAB’s sidebar

![Figure 9.4.f7: ](https://t10572667.p.clickup-attachments.com/t10572667/bd5ce49e-738d-4bbb-9066-f1e10ddef05d/image.png)

In the example above, the category “Financial Database Files” contains the file signatures for Quicken backup and database files. When a new case is started, any files matching these signatures will automatically be found in the Sidebar in a “bucket” named “Financial Database Files”.

**Adding or Removing File Signatures**

![Figure 9.4.f8: ](https://t10572667.p.clickup-attachments.com/t10572667/11c39f1d-13d0-4941-ad51-364e7a15cae2/image.png)

To create a new Category or to add a new File Signature simply click the “+” button.

1. Use the “Label” field to provide a name.

2. Add the signature as HEX or ASCII and select the appropriate button.

3. If the file signature begins at a specific offset add the value in the “Offset” field.

4. Click “Add”.

To remove a Category or File Signature select the time and then click the “-” button.

**Editing a File Signature**

To edit a previously stored File Signature click the “Edit” (pencil icon) button. Make the required changes and click “Add” to save.

## 9.5. Keyword Lists

The Keyword List settings allow the examiner to create lists ahead of time for content-based searches. Various search options will be explained later in this manual.

Keywords can be grouped into categories. Content keywords can be plain text or regular expressions (REGEX) that conform to dtSearch rules.

dtSearch’s Quick Reference Guide can be found here: [http://support.dtsearch.com/Support/forms/iframes\_advanced/default.html](http://support.dtsearch.com/Support/forms/iframes_advanced/default.html)

![Figure 9.5.f9: ](https://t10572667.p.clickup-attachments.com/t10572667/5fdc82ef-d2be-428c-a1ea-28a45144ecbd/image.png)

In the example above a category was created for “Phone Numbers”. Four phone numbers were entered as keywords. The first three are standard text. The last one (“+919876?????”) is an example of a regular expression to find an Indian phone number where we know the first six numbers but we do not know the last five. We checked the “Regex” checkbox to let RECON LAB know that the text entered should be treated as a regular expression.

### 9.5.1. Adding or Removing Categories or Keywords

![Figure 9.5.1.f10: ](https://t10572667.p.clickup-attachments.com/t10572667/877651ee-48c1-4316-8259-b8fd8d1778e3/image.png)

To create a new Category or Keyword simply click the “+” button. Enter the text and hit return.

If the Keyword is to be treated as a regular expression click the “Regex” box.

To remove a Category or Keyword select the entry and click the “-” button.

To add multiple keywords at the same time use the “paste” or clipboard button. Make sure that your text is entered as on item per line with a single carriage return. Copy all the text to your Clipboard and then use the “paste” (clipboard) button to add multiple items at the same time.

### 9.5.2. Editing a Keyword

![Figure 9.5.2.f11: ](https://t10572667.p.clickup-attachments.com/t10572667/fb3a61a0-5456-473d-8b64-fd1fafc47ad5/image.png)

To edit a previously entered keyword click the “Edit” (pencil icon) button. Make the required changes and click “Add” to save.

## 9.6. Text Indexing Filters

RECON LAB has included features to speed up your examination.

Text Indexing Filter settings allow you to set files to index or not index during a case ahead of time.

### 9.6.1. Default Index – No Filter

The default setting for indexing is “No Filter”. Leave this setting if you want to index all files.

![Figure 9.6.1.f12: ](https://t10572667.p.clickup-attachments.com/t10572667/f8a42def-0e16-48fc-834c-f6c8a20ad634/image.png)

### 9.6.2. Indexing Specific Files Only

To speed up processing you can have RECON LAB index only certain file types (based on extension) by selecting “Index these files”.

In the example below, a category was created for “Documents”. In the “Documents” category three file types were added (.rtf, .doc, .pdf). With these settings, RECON LAB will only index RTF, Word Document and PDF files and ignore all other file types.

![Figure 9.6.2.f13: ](https://t10572667.p.clickup-attachments.com/t10572667/28237935-13ec-4f0a-a395-5e9dc01daa76/image.png)

### 9.6.3. Eliminating Files From Indexing

Also, to speed up processing, RECON LAB can ignore indexing specific file types (based on extension) by selecting “Do not index these files”.

 ![](https://t10572667.p.clickup-attachments.com/t10572667/ac452643-d52d-4bb8-b79f-b6019c7de19a/image.png)

In the example above, a category for “Virtual Disk” was created. Within the category the extensions of .iso, .vdi, .vhd, and .vmdk were added. This category will reduce our processing time dramatically as RECON LAB will index all files except for those added to the lists below.

### 9.6.4. Adding or Removing Categories and Extensions

![Figure 9.6.4.f14: ](https://t10572667.p.clickup-attachments.com/t10572667/29546cb7-2268-41bb-aa12-d05d6b874269/image.png)

To create a new Category or to add an Extension simply click the “+” button. Enter the text and hit return.

To remove a Category or Extension select the item and click the “-” button.

To add multiple extensions at the same time use the “paste” or clipboard button. Make sure that your text is entered as on item per line with a single carriage return. Copy all the text to your Clipboard and then use the “paste” (clipboard) button to add multiple items at the same time.

## 9.7. Apple Metadata Filters

RECON LAB is the only forensic suite that is developed on a Mac to utilize macOS libraries natively. This allows RECON LAB to see and fully utilize Apple Extended Metadata. Other solutions do not natively support Apple Extended Metadata and rely on third-party and reversed engineered solutions that may not see or support all the metadata that exists which can lead to missed evidence.

Within the main RECON LAB interface, all Apple Extended Metadata is visible.

For the Apple Metadata Filter settings, we have selected some of the most common and important Apple Extended Metadata attributes which can be set to always show in the RECON LAB sidebar or within reports.

![Figure 9.7.f15: ](https://t10572667.p.clickup-attachments.com/t10572667/da41fd9b-e742-4af5-a771-77e02a0d1213/image.png)

Apple Metadata Filter Column Descriptions

* **D** – Check this box to add this Apple Extended Attribute to the RECON LAB Sidebar. Any files matching selected attributes will automatically be filtered and placed in the Sidebar.

* **R** – Checking this box will include the selected attribute’s metadata automatically to reports.

* **Title** – The common name of the Apple Extended Attribute.

* **Attribute** – The specific name of the Apple Extended Attribute.

* **Description** – The official description of the Apple Extended Attribute.

## 9.8. EXIF Metadata Filters

RECON LAB also parses EXIF metadata. The EXIF Metadata Filters allows an examiner to automatically filter out files with specific EXIF attributes to the RECON LAB Sidebar and/or always include select attributes in reports.

![Figure 9.8.f16: ](https://t10572667.p.clickup-attachments.com/t10572667/722446d9-8ca0-4e55-bf09-8d59f786cee1/image.png)

**EXIF Metadata Filter Column Descriptions**

* **D** – Check this box to add the EXIF Metadata to the RECON LAB Sidebar. Any files matching selected metadata will automatically be filtered and placed in the Sidebar.

* **R** – Checking this box will include the selected EXIF metadata automatically to reports.

* **Title** – The common name of the EXIF Metadata.

* **Description** – The official description of the Apple Extended Attribute.

## 9.9. Volatility Path

RECON LAB supports Volatility for RAM analysis. Volatility can be downloaded from [https://www.volatilityfoundation.org/](https://www.volatilityfoundation.org/)

Once downloaded, Volatility can be configured to work with RECON LAB.

![Figure 9.9.f17: ](https://t10572667.p.clickup-attachments.com/t10572667/9848d0f7-d927-4e69-a7b3-860110a456fb/Screen%20Shot%202022-01-14%20at%2010.34.49%20AM.png)

To use Volatility within RECON LAB select the three dots in the Volatility Path settings. Navigate to and select the “[vol.py](http://vol.py)” file to save the path.

Please refer to Volatility documentation for downloading and setting up Volatility profiles and plugins here: [https://github.com/volatilityfoundation/volatility/wiki](https://github.com/volatilityfoundation/volatility/wiki)

## 9.10. System Password

When you start RECON LAB for the first time or if you reset RECON LAB you will be prompted to enter your Admin password. If you change your password after installing RECON LAB you will have to update it using the System Password settings.

![Figure 9.10.f18: ](https://t10572667.p.clickup-attachments.com/t10572667/3ddf3853-1900-4cb7-bcde-4c3de15c864f/image.png)

To update, click the pencil icon and enter your new password.

## 9.11. External Applications

RECON LAB allows files to be sent to and opened in external applications.

![Figure 9.11.f19: ](https://t10572667.p.clickup-attachments.com/t10572667/5084c514-706a-4112-96bf-e3615a3c3312/image.png)

To add an application select the “Add” button. Navigate to and select the application that you would like to add.

To remove an application, highlight the application to remove and select the “Remove” button.

## 9.12. Highlight User Opened Files

RECON LAB gives examiners the option to highlight files that were opened by a user on the source device. In the configuration menu navigate to Preferences and select “Highlight User Opened Files.” This can be done in the configuration menu before you start a case or after a case has already been started.

![Figure 9.12.f20: ](https://t10572667.p.clickup-attachments.com/t10572667/5415dab8-266b-434d-8836-4c109405f03c/image.png)

Files will be highlighted yellow if they have an entry in the use count in their Apple Extended Attributes metadata.

![Figure 9.12.f21: ](https://t10572667.p.clickup-attachments.com/t10572667/30cd3f05-3480-4ad7-ae5b-a7a9d66b9bef/image.png)

To remove the highlights open RECON Config from the menu bar and deselect “Highlight User Opened Files” then click “Apply.”

## 9.13. Text View Settings

![Figure 9.13.f22: ](https://t10572667.p.clickup-attachments.com/t10572667/eb76fd7c-bea4-48a0-98c1-fcf02267a715/image.png)

To speed up processing RECON LAB allows you to set the Maximum File Size for the Text View. The default setting is 20 MB. To increase or decrease the size, enter any value. Keep in mind the value will be interpreted as megabytes.

## 9.14. Debug Mode

![Figure 9.14.f23: ](https://t10572667.p.clickup-attachments.com/t10572667/b6b7acd7-c16e-47c0-b0be-380c136f9926/image.png)

RECON LAB has the ability to log any errors that cause the application to fail. Using this feature will make our development team aware of the error, and allow them to diagnose and fix the error. This is accomplished by turning on debug mode (as shown above). To turn on debug mode, select “Debug” from the side bar menu on the left side of the screen. After that click the check box next to “Enable Debug Mode.” When the box is checked, “Debug mode” is active

# 10. Starting A New Case

![Figure 10.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/841289ad-5ac2-46b7-bb39-b36e49ceb6b2/Screen%20Shot%202022-01-14%20at%2010.51.47%20AM.png)

To start a case with RECON LAB select “New Case” from the Welcome Screen.

## 10.1. Case Info

When you start a new case with RECON LAB the Case Wizard starts with the Case Info screen.  If any information was added previously in the RECON Configuration settings that info will automatically be included.  The information entered here will be included in RECON LAB reports.  Certain fields are mandatory and must be entered to proceed to the next screen.  These fields are marked with an asterisk.

![Figure 10.1.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/b36ce429-2664-4f86-a125-82270fb4a8e0/Screen%20Shot%202022-01-12%20at%204.07.52%20PM.png)

The following information can be entered into the Case Info window.

* **Case No**. (mandatory) – A unique case number.

* **Case Name** (mandatory) – Name for your case.

* **Location** – Location of the incident or the exam.

* **Case Notes** – free form to add any notes required.

* **Examiner (mandatory)** – Examiner name.

* **Examiner Phone** – Phone number for the examiner.

* **Examiner Email** – Email for the examiner.

* **Agency** – Agency name.

* **Agency Address** – Address for the agency.

After you have entered the mandatory information and any additional information that you want then click “Next”.

## 10.2. Adding Source Data to Process

RECON LAB can accept a variety of sources to process.

![Figure 10.2.f3: ](https://lh6.googleusercontent.com/wzMUszB0bTRulk9LY_OjWViBE4lQOtONig0d0j5XEavW3ieXYDYCRrwRXPrdH05mN71aJwYtWfvmFs28R29otB3Rxvydr5ZRqBUvjanXC8gFdNW1US11A0AUhTN7pJ_rngnhWt92)

To select a source to process use the “Add Source” dropdown and select a source to process.

Options for adding sources are broken down into five categories. Each category has specific image type options, some of which will change the way your image is processed. It is imperative that the correct source type is selected for your image.

![Figure 10.2.f4: ](https://lh4.googleusercontent.com/bId6Clqn4XU-iboSvOZ_NpDMI35GGGPjrQuMgNEo35AhbWogEMGPwdNnr0PNWY_eEiNcLDYn0R1RGZfhquwgu916egD3P0bezWbXIrrCVxIdKxiO7GtytDk_Udm0BQQSocrRaW1y)

* **Physical Evidence** -  includes options for physically attached media and physically acquired forensic images

* **Logical Evidence** -  includes options for logically acquired forensic images, including ones specifically captured with RECON ITR

* **Mobile Evidence** - includes options for different mobile backups and extractions

* **Cloud Evidence** - includes options for cloud production data

* **Network Acquisition** - includes options for acquisitions done over a network

### 10.2.1. Physical Evidence

![Figure 10.2.1.f5: ](https://lh3.googleusercontent.com/HLYyTzSU7d3WTZAAw--gIPbFBWSWfk9RwJ-z4LD7uSY-6NJJfP1yMmwi0zYODDOHSmiLkKe6dbOwRGEyeyw_wQmpbPT5jHTLNxFl_jod3pyodXpxPQdRyUQ3MBCW3oby4tRBINbT)

RECON LAB supports ingesting multiple different types of Physical Evidence from multiple types of sources. From forensic images of macOS, Windows, and Linux, to RAM images and Optical Disc images.

To begin loading physical evidence into your case, select the Physical Evidence icon from the ‘Evidence Type’ menu.

![Figure 10.2.1.f6: ](https://lh4.googleusercontent.com/x3W_Q8D8omZdIs2XYnVoKGZ05CsYZ-YD4Os_Nb3ITyV4gKe4q_FO_ramEG1aWmq0W3k3Yt5FT9L_eoiu72tDEJOejfQ3yTTXmUcq1fg5GfKX0S7wgrZ2RJRKz4zSHO8_kv2kUBkQ)

The ‘Select Image Type’ screen will then load and allow you to choose the type of image you’d like to load.

![Figure 10.2.1.f7: ](https://lh5.googleusercontent.com/TPA6TJAhE_qnB0NlC_MbRE6Zj3nmryVEo3STUwO7FyhgY5zMEZMdflVG-DoS1YkGptelg-53hg8cyo8Oykxl9rrgn-6qU7v8nfA6ZVBC0Z7FXIVxASH9cBZVTZOyxZ-OO5Lwz4Be)

#### 10.2.1.1. Forensics Images

RECON LAB supports just about any forensic image format. This option refers specifically to full physical disk acquisitions.

To begin, select the Forensics Image at the Image Type screen.

![Figure 10.2.1.1.f8: ](https://lh4.googleusercontent.com/PPrwr3uCYAOc72ELRFQFqxioiIofTjBYfbCudBRavi_rA0WYQBET0t7hfGDI7fW6xae2YSr6u5UpLnYzpSNt1J_F9qdWn2XwYj7pzzGPHamH-xRkmkBF-5VCZgPy7UxGVB6jvRvT)

Next, select the Operating System that your image is of.

##### 10.2.1.1.1. Physical Images of macOS

If the image is of a Mac, select the macOS icon to be greeted with the following screen.

![Figure 10.2.1.1.1.f9: ](https://lh4.googleusercontent.com/2sYiE4nK9gux5kraEvPyv_uV9syNjswBFQTGybP__WKHiCqr_yHSra9wDsQE6RjcY1C5EyYkNakglLtrZKpk1Tkv3s3dxFI7OrU3TE-4ip-j0WUXnIorRhsX-_r_HwJ7PKIvnUK_)

From here, you can configure the image as needed.

Select the ‘...’ icon on the right side to open a file browser window, allowing you to navigate to your stored image file.

Currently accepted formats are:

* **RAW Images** – .dd, .000, .00001, .raw

* **Apple Disk Images** – .dmg, .sparsebundle, .sparseimage

* **Expert Witness Format** (EWF) – .E01, .Ex01, .L01, .S01

* **Advanced Forensic File Format** - AFF4

![Figure 10.2.1.1.1.f10: ](https://lh6.googleusercontent.com/yroHSl9Tkd6LM_iD1hxVpwzIVJLrhfoVXmNDR_7IuVjEiyMFg7WSttsyQYy9nGWRBOVeiUqlqXnZUgt-LvGBGWAoI52lPpVVpEgPksrOBK_50Po4yjmHAnyShE_jLZwVubG-TBFh)

Select your image and hit ‘Open’ to continue.

![Figure 10.2.1.1.1.f11: ](https://lh5.googleusercontent.com/X69WqKaz7vFc9GmcfRfS59F5Zzfe-ElwqwRWQK27WP1QN1r4WPIfWg2wKxT2REaEGacMA0rDJkSGcs92l9fYvZeGurZ_kfiIQonwDYfP6F7-pxg7vmkhbem2merh41k5rGk3Xxq5)

If the image is of a FileVaulted Mac, select the ‘Is FileVaulted’ option, then enter the administrator password of the image to automatically decrypt it during processing.

If the image is of a Fusion Drive Mac, ensure that the first image added is of the smaller SSD drive before continuing to the next step. Then, select the ‘Is Fusion Drive’ option, and navigate to the location of the larger HDD image to automatically pair the images together during processing.

##### 10.2.1.1.2. Physical Images of Windows Machines

If you’re loading images of a Windows machine, select the Windows Icon to be greeted with the following screen.

![Figure 10.2.1.1.2.f12: ](https://lh4.googleusercontent.com/NO5Pbp3bI-FGKbOTEEJb0EAelaeHH0cqSldddlSlVRYNm0IHi9lq1sVpJTWJ3vwnDZGu7hMHKIJ9tojv2WyGS_sP7tzsDutRZ-hkfXZf4jVMm0UPjDaGoV4_1v0oxNb2WgZ5tjuJ)

From here, select the ‘...’ icon on the right side to open a File Browser window. This will allow you to navigate to your stored image file.

Select your image and hit ‘Open’ to continue.

![Figure 10.2.1.1.2.f13: ](https://lh5.googleusercontent.com/X69WqKaz7vFc9GmcfRfS59F5Zzfe-ElwqwRWQK27WP1QN1r4WPIfWg2wKxT2REaEGacMA0rDJkSGcs92l9fYvZeGurZ_kfiIQonwDYfP6F7-pxg7vmkhbem2merh41k5rGk3Xxq5)

##### 10.2.1.1.3. Physical Images of Other OS Machines

If you’re loading images of a Windows machine, select the Windows Icon to be greeted with the following screen.

![Figure 10.2.1.1.3.f14: ](https://lh4.googleusercontent.com/NO5Pbp3bI-FGKbOTEEJb0EAelaeHH0cqSldddlSlVRYNm0IHi9lq1sVpJTWJ3vwnDZGu7hMHKIJ9tojv2WyGS_sP7tzsDutRZ-hkfXZf4jVMm0UPjDaGoV4_1v0oxNb2WgZ5tjuJ)

From here, select the ‘...’ icon on the right side to open a File Browser window. This will allow you to navigate to your stored image file.

Select your image and hit ‘Open’ to continue.

![Figure 10.2.1.1.3.f15: ](https://lh5.googleusercontent.com/X69WqKaz7vFc9GmcfRfS59F5Zzfe-ElwqwRWQK27WP1QN1r4WPIfWg2wKxT2REaEGacMA0rDJkSGcs92l9fYvZeGurZ_kfiIQonwDYfP6F7-pxg7vmkhbem2merh41k5rGk3Xxq5)

Select ‘Add’ to add the Image to your case for processing.

#### 10.2.1.2. Mounted Volumes

RECON LAB can add mounted volumes as a source as well.

To add a mounted volume as a source, select the ‘Mounted Volumes’ Icon from the Physical Evidence ‘Select Image Type Menu’.

![Figure 10.2.1.2.f16: ](https://lh3.googleusercontent.com/562U5fKk33HTMC5IrBxpMAaMNZ2IJi9E_ywnOgtK1yDK9WQTMPz2fjrfTaTtASfGe0_qbcJCFsLV69xc6VObS097BJY8YGaOOkC_c_O0IEhqrx1b9DU-xXo0nV3V-XPjgqSX7aTJ)

Selecting Mounted Volumes presents you with a selection box.  Any currently mounted volumes with be displayed.

![Figure 10.2.1.2.f17: ](https://lh6.googleusercontent.com/6YiH-RiUCkGSuKmYbK8VkhQlHYUk-1-cF_RXqiQgDSGD7Bw1kCiaA-spep92vwEChtQwhuzhlTbsv6-npc57LwxCmKbExq5UhuPtBxwaV_fserT1SzVVAh_Y59GUQZ-ksd_SW755)

To add, check the box next to the volume path and then click “Add”.

#### 10.2.1.3. Optical Disc Image

RECON LAB can support Optical Disc image formats as a source.

RECON LAB currently supports .ISO and .cdr Optical Disc formats.

![Figure 10.2.1.3.f18: ](https://lh3.googleusercontent.com/fUt-hEyb_w99CmJtYZmPtCA6gx1HojG1pW2bo7naKYMlSsCfcDfGaWeTPxUi-hLvqvRsULwq2iquzV8rEtLXAdLTjh-N8xpEdUaN0wlJettDGSyJEiLP63An68Wc5-HESmxMPkF3)

Select the ‘Optical Disk Image’ Icon under ‘Select Image Type’.

![Figure 10.2.1.3.f19: ](https://lh4.googleusercontent.com/NUV6WtGdCpEktZLezN1n-EPJyN8lRDMmL4Q4W94GL2dsfWvofhVZBqNfmkdYOkIZ_oJpwHZJFRSjlrHh7HBdQ5OgcSfLSkU-0h-iYF3VxW3qKR6Lk-ZgfjaAkkl4xEgWqF7CtZKl)

From here, select the ‘...’ icon on the right side to open a File Browser window. This will allow you to navigate to your stored image file.

Select your image and click ‘Open’ to continue.

![Figure 10.2.1.3.f20: ](https://lh5.googleusercontent.com/kjeHFY0J5nGKG9vI7EuAC0QrFuOq0az-GBY5Lvn4Rr6JL1QY7vLBo0445cQAxxJVRkRGBYS-ox_WRmhGmskdNJ9_Rjc8Dh3PBAX0HlS0YgD8lV1c50arKCHOruBd51oy8surfNf8)

Select ‘Add’ to add the Optical Disc Image to your case for processing.

#### 10.2.1.4. RAM Image

RECON LAB supports loading RAM images which are usually in raw format.

To load a RAM image, select the ‘RAM Image’ icon in the Physical Evidence ‘Select Image Type’ menu.![](https://lh4.googleusercontent.com/5aIko1Jc3z7c8-CR_KI3g0jrvBWLN_ofaBW0nsZqP9MM0b6akmMeqfLnsQoy000poA5Gjyv5FwIxxidWyNGmN-NI96-zZNVZRXT28WAc_K7koKV6jD09sdWFHR3c2MqkUSp-fK71)

From there, select the ‘...’ icon on the right side to open a File Browser window. This will allow you to navigate to your stored image file.![](https://lh5.googleusercontent.com/1d9t80qrcu_GSVV4UjAJtNhGI1PJ2PasQ2hQeI3Dwe4ppr8JsLk43E4Fhj04ZxbedUS2sdpwcJTFutfbvdInjgzHpMCmR72jq8XMc7fvQOY9PZjKGUy1o8PiXXbfdR1v73wB6PC0)

![Figure 10.2.1.4.f21: ](https://lh5.googleusercontent.com/X69WqKaz7vFc9GmcfRfS59F5Zzfe-ElwqwRWQK27WP1QN1r4WPIfWg2wKxT2REaEGacMA0rDJkSGcs92l9fYvZeGurZ_kfiIQonwDYfP6F7-pxg7vmkhbem2merh41k5rGk3Xxq5)

Select your image and click ‘Open’ to continue.

Select ‘Add’ to add the RAM Image to your case for processing.

#### 10.2.1.5. RECON FS Block Image

![Figure 10.2.1.5.f22: ](https://lh3.googleusercontent.com/eT1-AQFIIqxv-wInyIy8VvY3EoaOaemNOKtIUl1AdWk8WVYxCsIWgYVquQtqWcSPM0vfEjxhCz3ySZQUV5g7JOa8pibOK2ZDWhq5FkZiKvR7FWpB35xePcHjxcN2HWDXV8V_eA11)

FS Block Copy is the primary output format of T2 Macs imaged with RECON ITR.

To select an FS Block Copy image created with RECON ITR, select the RECON FS Block Image icon in the Physical Evidence ‘Select Image Type’ menu.

Once selected, RECON LAB will display the available image formats for a RECON FS Block Image. Choose either sparseimage or DMG depending on what format your image is in.

![Figure 10.2.1.5.f23: ](https://lh4.googleusercontent.com/n5DCd_dlNjueexR6NVYcHat-y2INpfBcxGMkU1ClOJlMq1Nq9CElqav5pJ08bKP4IHeUm0o7tFCuAtwjtfLJK8Tlw_WRtzexclWw-JVWsLptEOccq65SmOt8ryNkvvPiY6Tlr2MZ)

From here, select the ‘...’ icon on the right side to open a File Browser window. This will allow you to navigate to your stored image file.

Select your image and click ‘Open’ to continue.

![Figure 10.2.1.5.f24: ](https://lh3.googleusercontent.com/8RTqOxLcd41qv7iBavJmzjNSLue0aNcNo6uUKlZCExnWFMmuxp84uOH4Vw4MDRrf1wxy4RQ6sF_JkH3GR7qIF4QVZk6ergqTGCkVCruApPxPoSN-BNQF2ns8gOE96fx8R-zMyDx8)

Select ‘Add’ to add the RECON FS Block Image to your case for processing.

### 10.2.2. Logical Evidence

RECON LAB supports multiple kinds of logical acquisitions. It is particularly important to select the correct option when dealing with logical acquisitions. Some features present features that are important when using RECON LAB and RECON ITR together may not function properly if a source is not loaded properly.  ![](https://lh5.googleusercontent.com/7vpwUdTZBzS43jxiWb2c90R7OiuzeMUD0p-dapQirDSWy_y6Fzn9r1ehCIwGFuYZzgXa9uDk7gxbhP7ITEPLcy8T5ANkx2bbnHPk8o7pDlIk4CJpRkv2J2uhByq2x7SEQyYxeRaH)

To begin loading logical evidence into your case, select the Logical Evidence icon from the Evidence Type selection.

![Figure 10.2.2.f25: ](https://lh6.googleusercontent.com/S71JCA0ALQ61Uuhl9Mpdz3YFyO1qyqgQlPUReYG9AmZnB1ArUkT5ZVJL0dBcIg-SoYHUCRvYRySo3cPHo4YKoNf1Lbe2lsQYSdcmxMeXFICvTSLHk4WCM9kY11VYPwPygCS9J0Wb)

From the ‘Select Image Type’ menu, you can select the type of logical evidence you’d like to ingest.

#### 10.2.2.1. Time Machine Backup

![Figure 10.2.2.1.f26: ](https://lh5.googleusercontent.com/1KlDjS71CjQ3JJoCKN1WDVJRo7nNKRjC9KRVrHQGowuWiKgW1FpNk5MCG2j8-4vIQzrZUYkjLYD9HNRTOJZ_8qV9gLfbXYHqBwQ2cosSFVI-hGk49eE-seYqEcBrVUDdmy-Ah7qt)

RECON LAB supports the processing and automated analysis of individual macOS Time Machine Backups.

To begin adding your Time Machine Backups to your case, select the Time Machine Backup icon from the Logical Evidence ‘Image Type’ Menu.

![Figure 10.2.2.1.f27: ](https://lh3.googleusercontent.com/q4bhZhvxAg9eLSU5Iy4aJZmVwWNuRIqSl_RZ8f9eQzqUggcqaQCt0nFpvuAWke8jWczY1HIJ7P4HdQrDzm1e29XpWH8NM4qdyCETkYguEwnTk3YbMaNtQvh2Hh0HYHixzJxJJlUW)

Select the ‘...’ icon and navigate to the directory of the backup in which you would like to process.  Select “Choose” to add the backup directory.

![Figure 10.2.2.1.f28: ](https://lh5.googleusercontent.com/HJqQU_YEklSIRadeq3tdgzB1yXt6o_5WQ_ykkmYIIkB9u6js7UCJANaMYKEu2LJAZASQ_du0V_fZk-rVYOBf_K7Z07raaLa0rKD0qI7xgypz7VzNdOaqWd_Z-tLDQPwrXPLhAnot)

Select ‘Add’ to add the Time Machine Backup to your case for processing.

#### 10.2.2.2. macOS Home Directory

There are many situations in Mac investigations where only a single user’s home directory can be acquired.  RECON LAB supports adding and automatically processing a macOS Home Directory.

![Figure 10.2.2.2.f29: ](https://lh3.googleusercontent.com/8GbN8w4QeXP__qBbJCR2LkcKdte0hhr-iuOMFbaoOaHh7gckeEfP4U0MRX5rCnD_MI3swg6IOfxTGdT7zzEE3sRqsj0w6cpoMx7NqSNfqZb6WBLLJEOGrQL4bEA6n84L18wLpYr2)

To begin loading a macOS Home Directory to your case, select the ‘macOS Home Directory’ icon from the Logical Evidence ‘Select Image Type Menu’.

![Figure 10.2.2.2.f30: ](https://lh5.googleusercontent.com/599i_vherPjiWxNUvqoNS0ekwSbHUaNqMMOhu6coBtVyPhQDzEwLQ86-TSAkDE39v8znnI98Oi4uf3gpVLtjBVFRDGjE2zKAxicqJ6EXsvJ6C7MkC-3xZ27Psbkl_7kfPrsAev_c)

Next, select the ‘...’ icon and navigate to the home directory you’d like to add. Select Choose to continue.

Enter the username of the home directory and select ‘Add’ to the home directory for processing.

#### 10.2.2.3. RECON Logical Image

A RECON Logical image is any logical image that was taken with RECON ITR. There are three supported file formats for RECON Logical images, Sparseimage, DMG, and Folder. A RECON Logical image will utilize a database made at the time of imaging to display the correct Modify, Access and Create Date and Time stamps of a logical image. This database is create any time RECON ITR makes a logical image.

![Figure 10.2.2.3.f31: ](https://lh5.googleusercontent.com/_PZT35uE4JSPmkhmVZx1c579sNJprTatUQhMe4Z_nn1A9X7nmcE-CmxJ_PdOue7G6apjy-eObTxOkn72HxOxLyxYQ4uQJAgDFmB75jBgP-v6reHA7o5iSr2P99KZHd_1dXQa7z8D)

To load a RECON Logical image, navigate to the RECON Logical Image icon in the Logical Evidence ‘Select Image Type’ Menu.

Next, choose the type of RECON Logical Image you’d like to load. Select the icon that matches the format of the image you have.

![Figure 10.2.2.3.f32: ](https://lh3.googleusercontent.com/Y4L2uOCBwziFKLcQWxsbCUi8nelUmpmTfT4G8ZxLcMXhaFr8lcJgwzGYZItp-kt97UgDV7oi3CqZ49dRyHokvp3XqGChN-zVS83NyVRMV2ZPg0JRsAdxxWefMndBf480XxQo8iq2)

Select the ‘...’ icon to browse to your image location and select ‘Open’.

![Figure 10.2.2.3.f33: ](https://lh3.googleusercontent.com/I1PZuoA8j5dEIh9JmxOxRBwchWdzz0QfP1q_d87suACSmwRVIFhuXg6d6Zz8TjORrK7eUEyAaAo8ryHa_ChHRzMIuChUBAoTDejE8pME8x9N39ZdhkGzz5Rh9qv213NtF0OUjqfR)

Select ‘Add’ to add the RECON Logical Image to your case for processing.

#### 10.2.2.4. Encase Logical Image

Access Data has its own proprietary logical container format, popularly known as L01.

RECON LAB has support for ingesting these containers using the Logical Evidence section.

![Figure 10.2.2.4.f34: ](https://lh3.googleusercontent.com/h47N8sjYkaiJqIiAfH_XPlvS0Vg-Foh_CoWUqphCQCJQjhlaMyWjlYGGX8SY3FONetWQcBvn8bUYrtO-X2QwRygAjoy0iNLmjJ_4Z7kxB5iW3bp1KgRHnhXGxaEedljzkK_MXd6S)

To load your L01 in RECON LAB, navigate to the ‘Encase Logical Image’ icon in the Logical Evidence ‘Select Image Type’ Menu.

![Figure 10.2.2.4.f35: ](https://lh3.googleusercontent.com/psaUaB-OGIf9GGsGA-OHNSnc2ytims38Xx-ccez0pdHCZXEmvRocaSdnnb5_dX8VeCRINmAC6D9DFdchtUDp46cysEyA61ogfjhQ9zGAhcFIR9ku2zt7efmp33bALGVqfYy0rLgE)

Select the L01 Icon.

Select the ‘...’ icon to browse to your image file and click ‘Open’ to continue.

![Figure 10.2.2.4.f36: ](https://lh4.googleusercontent.com/lYkrNHzu5EKtrQ2oe1xb6hT-tq5enXmcOAOENq4YoG826i1jwBVtacGiFnbtRlR1caCdE3_wJzs8zZTxqlWwZ1In_VFZ1vrDWwl3e1Xi4JCp0wPjUri_T1F1_4DfZ8mb1LinQnuc)

Select ‘Add’ to add the L01 to your case for processing.

#### 10.2.2.5. Logical Folder

Individual folders can be added as a source to process.

![Figure 10.2.2.5.f37: ](https://lh4.googleusercontent.com/0H9YTiOfDT2t3mzpYWgqToCc37avsJOrFPqCWrU43Om2tyjfQn2q1uBwcy_OAwTkbrenedKvi6YzVorRVqLNQjSWRGjDWNc9RlfHLn81pDfyivS395uziP_azD-pTx2bRPDV1z7B)

To add a folder as a source, navigate to the Folder icon in the Logical Evidence ‘Select Image Type’ menu.

![Figure 10.2.2.5.f38: ](https://lh5.googleusercontent.com/s9ucY3JMvGNgaoiVRrQaSuA_ZcvyIAZDCDLT6ogmvxO2lVsuLBoWYr36gpKgLkhW_N6HCIOtplg1K7u6WKoeZcs2CE4NW498s6cKUSUy96aSfOb3gKZ_cfIgnSDwUpBg0jbRjPxx)

Click the ‘...’ icon to browse to the folder you’d like to add and select ‘Open’.

Select ‘Add’ to add the Folder to your case for processing.

#### 10.2.2.6. Logical File

Individual files can be added as a source to process.

![Figure 10.2.2.6.f39: ](https://lh4.googleusercontent.com/MtI2dAP9FjDDCC5zUFcQo6-MHyssxJMmhQ430RCsXodUT50cWDUytD4jxPsWdut0Baiy1LNoE-g1XDzlDLQsXRJgyW3FsbOWaVjJJiYu5PhTT0tGHbikis8cTGEIirRFqB4jxEAt)

To add a file as a source, navigate to the File icon in the Logical Evidence ‘Select Image Type’ menu.

![Figure 10.2.2.6.f40: ](https://lh5.googleusercontent.com/LFJpzhab0oUrAGR4isfWzKMt5yxwUzwaJLtlhKLIAySbvsqQKIF5f5KxofQWXmFPFJRSgoAlWxzeciSEnTOXGBmPAanC2MohzLh9VAUQc4a5DNFxWXEENnxVue3fjEWhAiZ7quWP)

Click the ‘...’ icon to browse to the folder you’d like to add and select ‘Open’.

Select ‘Add’ to add the File to your case for processing.

### 10.2.3. Mobile Evidence

RECON LAB has support for processing multiple forms of iOS and Android sources, that can all be accessed through the Mobile Evidence section, including support for both Cellebrite iOS backups and ADB Backups.

![Figure 10.2.3.f41: ](https://lh5.googleusercontent.com/SH5hHURPOwoiOrjmXGiShaVytBCLqndmD0aK-RMi86vkqqIDFfddj5d9w2n8jjkvuqQjdPBbv_14FlBUt245xiqvM6qDy8LX-IJCYi4UQwdEOdCFGal2nvnOq_RJ8OJ3JmoDAPbo)

To begin loading Mobile Evidence into RECON LAB, select the Mobile Evidence icon from the ‘Select Evidence Type’ Window.

#### 10.2.3.1. iTunes iOS Backup

RECON LAB supports the analysis of Apple iOS backups.

Most forensic tools that image iOS devices utilize the iTunes engine to create an iTunes backup to process.

RECON LAB also has the ability to image and iOS device and create an iOS backup which is discussed later in this manual.

![Figure 10.2.3.1.f42: ](https://t10572667.p.clickup-attachments.com/t10572667/c4c59ab3-f145-4932-a806-c1ca59ff876f/Screen%20Shot%202022-03-07%20at%204.45.40%20PM.png)

To add an iOS backup as a source navigate to the ‘iTunes iOS Backup’ icon from the Mobile Evidence ‘Select Image Type’ Menu.

Select the ‘…’ icon to browse to the manifest.db file inside the iTunes iOS Backup and select ‘Open’.

Select ‘Add’ to add the backup to your case for processing.

#### 10.2.3.2. Cellebrite iOS Backup

RECON LAB supports ingesting of Cellebrite UFED extractions in the form of unencrypted .tar and UFDR.![](https://t10572667.p.clickup-attachments.com/t10572667/9ed9582b-6d14-49c5-a185-39d48661526a/Screen%20Shot%202022-03-07%20at%204.47.25%20PM.png)

To add an iOS backup as a source navigate to the ‘Cellebrite iOS Backup’ icon from the Mobile Evidence ‘Select Image Type’ Menu.

Select the evidence type that you’d like to ingest, either an unencrypted .tar backup or a UFDR folder.

![Figure 10.2.3.2.f43: ](https://lh6.googleusercontent.com/1pLsUiO6TtJEvxUD4vZ3L6l4ltmSG6ZzuaVTX617GSrzey2iWNtKl3dJImCNx-1bsh1knhOhpeJZxqy5khZeUzNIGLueguwQnY-6MygKAp13z6OBI_yKsemB21WQir53UOXbX08W)

Select the ‘…’ icon to browse to the image file and select ‘Open’.

Select ‘Add’ to add the backup to your case for processing.

#### 10.2.3.3. GrayKey Backup

RECON LAB supports ingesting of GrayKey images in the form of .zip files.

![Figure 10.2.3.3.f44: ](https://t10572667.p.clickup-attachments.com/t10572667/e6f7c30e-2e21-4b22-8dc3-1a6aab5d9626/Screen%20Shot%202022-03-07%20at%203.56.31%20PM.png)

To add an iOS backup as a source navigate to the ‘GrayKey iOS Backup’ icon from the Mobile Evidence ‘Select Image Type’ Menu.

![Figure 10.2.3.3.f45: ](https://t10572667.p.clickup-attachments.com/t10572667/d924b2ab-a373-47e1-845f-1c676302f39a/Screen%20Shot%202022-03-07%20at%203.59.49%20PM.png)

Select the ‘…’ icon to browse to the file and select ‘Open’.

Select ‘Add’ to add the backup to your case for processing.

#### 10.2.3.4. ADB Android Backup

RECON LAB supports processing Android Debug Bridge (ADB) files and backups of Android Devices.![](https://t10572667.p.clickup-attachments.com/t10572667/32d146ba-09a6-4b25-b00b-05f360ebe838/Screen%20Shot%202022-03-07%20at%204.47.34%20PM.png)

To add an ADB Backup as a source navigate to the ‘ADB Android Backup’ icon from the Mobile Evidence ‘Select Image Type’ Menu.![](https://lh6.googleusercontent.com/I26n2vt-QaDBfeLlDLlHN7NPfEzf5wIHM5t_j6OsXImxrFtRlguw66Lt-25VBI4uBQIkePqFhGaYw60lz1Yhjl-D4ydJxTKtRMDsBo2EWYEBC4OeFoEeLKg0Qr7_HzfV64jr69L9)

Select the type of backup you have, either an AB backup or a folder.

![Figure 10.2.3.4.f46: ](https://lh6.googleusercontent.com/9GJvoWyktdxQnEP4e0KmLNQratyf4jDuetG4NX-DvgxLaRBLBa6pKf92Q1-7hMRuDRFHmAYOMopmhef6QibSkDsPqAPxOuiaCnCwpu6VACFckOCPV76TytaIXew3cGtkCQxVBDvP)

Select the ‘…’ icon to browse to the file and select ‘Open’.

Select ‘Add’ to add the backup to your case for processing.

### 10.2.4. Cloud Evidence

RECON LAB supports ingesting evidence related to cloud storage as well. The currently supported format is Google Takeout downloads. These can be added and parsed with RECON LAB by following the section below.

![Figure 10.2.4.f47: ](https://lh5.googleusercontent.com/rPdtZOxd34cl5chkx-6OB66gcKAbuJ0NSmlonwms0LuVoDl7kfytEmTaS8XjKnV-GS6gV-g4-w-fBzfPuUVRvSh5_uraKz6nnFnYNAVNQA7xgluOJuwY2Dt-4srttrJ2OF8jD1sp)

To begin processing Cloud Evidence, select the ‘Cloud Evidence’ Icon from the ‘Select Evidence Type’ Menu.

#### 10.2.4.1. Google Takeout

RECON LAB supports data downloaded from Google Takeout: [https://takeout.google.com](https://takeout.google.com/)

RECON LAB has numerous plugins to automate the analysis of Google Takeout data.

![Figure 10.2.4.1.f48: ](https://lh6.googleusercontent.com/V1PWfQjtLhER83Sav6OJ8iT7JMqJNKqYvOouPRHEyB-IPokhWoG89kL7Iyc9GXZ0GzTe-N-0Kvux5JQ2BolBYH7RbAD7v18S0xomErvPaueUR4NrueLRhH0l9YX22NfO22PyhLrq)

To load data from Google Takeout select the Google Takeout option from the ‘Select Image Type’ Menu.

![Figure 10.2.4.1.f49: ](https://lh5.googleusercontent.com/oGpe0e2kYUzYyxll93VCcUyTwpcdPOMu2GYhDJFnUEVY-3HAERsXVwRgtvbvK5CUGoyX5dONyxXrGElNon-j6ZguF0f9O_ldC9UHvEubyyoZph_bVRqklxo6eSCf_1zi1-YJDjlY)

Then, select the ‘...’ option and navigate to the directory with the Google Takeout data. Then, select ‘Open’ to continue.

Select ‘Add’ to add the Google Takeout to your case for processing.

### 10.2.5. Network Acquisition

Network Acquisition refers to acquisitions performed over a connection like SMB. RECON LAB currently supports one type of Network Acquisition, RECON MAC Sharing Mode.

![Figure 10.2.5.f50: ](https://lh3.googleusercontent.com/HJwPDyrhzpPQXpTswqR0Qt18Y6HN6lYoFiUXR-J9zFIqMPQZBEF0dSYoPMgqwmYAEtTIf9J586rzGlDDAitCTXxJRyVdY7HavSj0bdLj408DI3EpUZ93JfYQLMv-9WguoDsNo8i6)

#### 10.2.5.1. RECON Mac Sharing Mode

RECON ITR supports imaging the new M1 Macs using Apple’s new Sharing Mode. This method of imaging is run over an SMB connection, so the image is created differently than your conventional synthesized disk image.

To begin adding your Sharing Mode image, select the RECON Mac Sharing Mode icon and select the format of your image.

![Figure 10.2.5.1.f51: ](https://t10572667.p.clickup-attachments.com/t10572667/17727700-cdce-4aa4-b28f-7eb0293131bb/image.png)

Next, select the ‘...’ option and navigate to the image. Then, select ‘Open’ to continue.

![Figure 10.2.5.1.f52: ](https://t10572667.p.clickup-attachments.com/t10572667/831ef0e1-b31e-426a-8caa-c085b0d27e88/image.png)

Select ‘Add’ to add the Sharing Mode image to your case for processing.

## 10.3. Adding Source Information

Once a Source has been selected the Source Information window will appear.

![Figure 10.3.f53: ](https://t10572667.p.clickup-attachments.com/t10572667/0eb47145-322a-43d9-b68c-c6bc23d244da/image.png)

Here you can add a unique evidence number (“Evidence No.”) and a description of the evidence.

After entering the information click “Ok”.

## 10.4. Adding Multiple Sources

RECON LAB can process multiple sources at the same time.

![Figure 10.4.f54: ](https://t10572667.p.clickup-attachments.com/t10572667/f479a2e7-9234-4d5a-a2fd-e735fbf79668/Screen%20Shot%202022-01-14%20at%2010.55.59%20AM.png)

To add more than one source use the “Add Source” button.  Additional sources will be listed once added.  To remove a source before processing begins click the “X” button.

## 10.5. Case Directory

After adding your sources to process you have to select the location for your RECON LAB Case Directory.  This directory is used to store everything and can become quite large in size depending on the amount of data to be processed.  Make sure that there is enough space on the media where the Case Directory is placed.

It is recommended to use a macOS Extended (HFS+) formatted drive for the location of the Case Directory.

![Figure 10.5.f55: ](https://t10572667.p.clickup-attachments.com/t10572667/0d792edd-875c-419a-b5ab-5e85c7be9a02/Screen%20Shot%202022-01-14%20at%2010.56.53%20AM.png)

To select the location for the Case Directory click the three dots.  Navigate to the desired location and click “Choose”.

## 10.6. Date and Time Settings

RECON LAB has several options for setting time zones.

![Figure 10.6.f56: ](https://t10572667.p.clickup-attachments.com/t10572667/1c413188-49ab-4e3b-a49e-c0bf630cb55d/Screen%20Shot%202022-01-14%20at%2010.57.38%20AM.png)

* **UTC** – Coordinated Universal Time or +00:00

* **Machine Time Zone** – This is the time zone of your examination system if detected.

* **Other Time Zone** – This dropdown menu will allow you to pick any time zone in the world.

RECON LAB also has several options for the Date Format.  Whatever Date Format is chosen here will take effect globally in RECON LAB.

## 10.7. File System Modules Selection

![Figure 10.7.f57: ](https://t10572667.p.clickup-attachments.com/t10572667/5b027fa5-0498-4406-8326-f598f9410ddf/Screen%20Shot%202022-01-14%20at%2010.59.57%20AM.png)

RECON LAB was designed to give an examiner as much control as possible.  This control can help an examiner complete investigations and analysis faster.

The examiner has the option of enabling or disabling individual File System Modules.

For example, if your case does not require the need for signature analysis then you do not have to activate this module which will save processing time.

### 10.7.1. Apple Metadata Module

![Figure 10.7.1.f58: ](https://t10572667.p.clickup-attachments.com/t10572667/124f5669-08a0-48a3-a99a-b6d0fbc81929/Screen%20Shot%202022-01-14%20at%2011.00.28%20AM.png)

To activate the Apple Metadata module for macOS sources, check the box next to “Extract Apple Metadata”.

If you have previously configured this module your selections will be present.  At this time you can add or remove attributes.

**Apple Metadata Filter Column Descriptions**

* **D** – Check this box to add this Apple Extended Attribute to the RECON LAB Sidebar.  Any files matching selected attributes will automatically be filtered and placed in the Sidebar.

* **R** – Checking this box will include the selected attribute’s metadata automatically to reports.

* **Title** – The common name of the Apple Extended Attribute.

* **Attribute** – The specific name of the Apple Extended Attribute.

* **Description** – The official description of the Apple Extended Attribute.

### 10.7.2. Signature Analysis Module

![Figure 10.7.2.f59: ](https://t10572667.p.clickup-attachments.com/t10572667/733a4ac5-78ba-48fc-bb38-41e28bbd9d81/Screen%20Shot%202022-01-14%20at%2011.02.34%20AM.png)

Selecting “Analyse User Defined File Signatures” run a module to identify files based on the file’s headers (or signature).  The file signatures can be added in the Case Wizard or previously in RECON LAB Configuration.

To learn how to enter or remove a file signature please refer to the previous instruction in the “Configuration” section of this manual.

### 10.7.3. EXIF Metadata Module

![Figure 10.7.3.f60: ](https://t10572667.p.clickup-attachments.com/t10572667/241dca50-9d82-49f4-ac27-cfe1c70261bc/Screen%20Shot%202022-01-14%20at%2011.21.12%20AM.png)

Selecting “Extract Exif Metadata” tells RECON LAB to recover any EXIF metadata selected in this module.

**EXIF Metadata Filter Column Descriptions**

* **D** – Check this box to add the EXIF Metadata to the RECON LAB Sidebar.  Any files matching selected metadata will automatically be filtered and placed in the Sidebar.

* **R** – Checking this box will include the selected EXIF metadata automatically to reports.

* **Title** – The common name of the EXIF Metadata.

* **Description** – The official description of the Apple Extended Attribute.

### 10.7.4. Hashes Module

![Figure 10.7.4.f61: ](https://t10572667.p.clickup-attachments.com/t10572667/1f488c4d-719f-4288-8688-7951e08b4765/Screen%20Shot%202022-01-14%20at%2011.22.34%20AM.png)

If you will be utilizing pre-configured hash sets in your investigation or analysis choose “Analyze Hashes”.

RECON LAB will create hashes of all files within the case.

## 10.8. Artifact Plugin Selection Module

As described previously in the “Configuration” part of this manual, RECON LAB automatically processes and analyzes thousands of artifacts using hundreds of plugins for Windows, macOS, iOS, Android and Google.

Select any plugins or artifacts that you want to run.

![Figure 10.8.f62: ](https://t10572667.p.clickup-attachments.com/t10572667/40ecddc3-eec0-459b-b471-d487f5f5551c/Screen%20Shot%202022-01-14%20at%2011.23.55%20AM.png)

To begin processing of all sources with the selected Filesystem Modules and Automatic Artifact Analysis, click “Start”.

# 11. Timeline Analysis

The ability to sort data by timestamps is found throughout RECON LAB.

RECON LAB includes two special ways to create amazing timelines with support for hundreds of unique timestamps.

1. **Super Timeline** – creates a CSV or SQLite database of standard system timestamps and/or Artifact Plugin timestamps.
2. **Artifacts Timeline** – visual view of events based on timestamps from automated analysis.

## 11.1. Super Timeline

![Figure 11.1.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/d0ae7d02-331d-4f46-8c90-232ab7617f08/Screen%20Shot%202022-01-26%20at%2012.29.06%20PM.png)

The Super Timeline can be activated by selecting Timeline > Super Timeline from the Menu Bar.

![Figure 11.1.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/b55b3290-03ab-4c8e-9d5e-995ac98f5fa8/image.png)

Once selected the Super Timeline configuration window will appear.

The Output Format can either be SQLite (recommended) or CSV.  If you choose CSV the number of records is limited to 1,000,000.

An examiner can choose to include the standard timestamps of File System Records, timestamps of Artifacts Plugin Records or both.

A **Start Time** and an **End Time** can also be provided.

To create the Super Timeline provide a File Name, File Path and click OK.

![Figure 11.1.f3: ](https://t10572667.p.clickup-attachments.com/t10572667/8804e529-bee4-48e2-8ab9-c80156d73bca/image.png)

Once the Super Timeline is created you will be prompted to review the results.

## 11.2. Artifacts Timeline

In order for the Artifacts Timeline to create a timeline make sure that you have run some or all of the Artifacts and Plugin modules for automatic analysis.

![Figure 11.2.f4: ](https://t10572667.p.clickup-attachments.com/t10572667/536bbc68-0ba1-4f28-a9bc-d25f00059498/Screen%20Shot%202022-01-26%20at%2012.29.00%20PM.png)

An Artifact Timeline can be created by selecting Timeline > Artifact Timeline from the Menu Bar.

![Figure 11.2.f5: ](https://t10572667.p.clickup-attachments.com/t10572667/c72c5f0e-8d51-4760-92bf-496bc8408346/image.png)

Start by selecting the artifacts of interest in the Artifacts List and timestamps of interest in the Timestamp List.

![Figure 11.2.f6: ](https://t10572667.p.clickup-attachments.com/t10572667/bf34185c-5d52-4717-b016-be40aaf44932/image.png)

_Note: FS Events artifacts can contain millions of records.  Be aware that this will take time to load._

![Figure 11.2.f7: ](https://t10572667.p.clickup-attachments.com/t10572667/d9e23dc1-381a-4ad9-bd62-a86f71060e90/image.png)

Next, select your Start and End dates and click Apply to create the Timeline.

Once complete you will have a graphical view of all the parsed and selected artifacts along a graphical timeline.

![Figure 11.2.f8: ](https://t10572667.p.clickup-attachments.com/t10572667/9e9b2883-5db7-401a-bd6b-f49a32c86713/image.png)

The timeline can be viewed by Year, Month, Day wise and  Hourly.

To move backward and forward through the timeline pages use the navigation buttons or go directly to a page by using the “Go to Page” option.

![Figure 11.2.f9: ](https://t10572667.p.clickup-attachments.com/t10572667/83910c7a-8c3e-495a-b2bb-70fcdb94e004/image.png)

In the graphical view, you can save a picture of the current graph by clicking the “Save” button.

To export the data into a CSV file click the Export button.

To review the results in a table view click the “Tableview” button.

![Figure 11.2.f10: ](https://t10572667.p.clickup-attachments.com/t10572667/953e6a68-2d34-4c9a-bb50-eeb729ce6a59/image.png)

Each color in the graph represents a different artifact.  Hovering over the color will display a popup window with additional information about the plugin.

![Figure 11.2.f11: ](https://t10572667.p.clickup-attachments.com/t10572667/ac336cce-802f-4069-a26c-0b7eafbf0dc9/image.png)

Double-clicking on a plugin in the graph will open its results in a table view.

![Figure 11.2.f12: ](https://t10572667.p.clickup-attachments.com/t10572667/dc11c9c2-0bce-4ab8-b0d7-9e6bc28cfcbf/image.png)

The results can be exported to a CSV file using the “Export” button.

Selecting the “Save” button will save this table to the Sidebar and can be found under “Artifacts Timeline”.

Clicking the “Close” button will close the graph.

# 12. Redefined Results

Redefined Results are a way to collate data across different devices that use different applications.  It allows a complete picture of events even when a person is using a mobile device, laptop, and a computer in a single day.

Redefined Results are available for **Web History**, **Messaging** and **Location Data**.

![Figure 12.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/fd768206-311a-4728-8794-f9ad78a828cf/image.png)

Redefined Results can be found in the Sidebar and viewed by double-clicking on the result of your choice.

## 12.1. Collated Location History

![Figure 12.1.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/f171a3b2-e1f5-4474-96e2-3bf1ce506bc0/image.png)

Any data containing location data will be collated in the Redefined Results for Location History.

## 12.2. Collated Messaging

Messenger Redefined Results collate different messenger applications from different sources into one.

![Figure 12.2.f3: ](https://t10572667.p.clickup-attachments.com/t10572667/0aae773b-a2af-45ad-958a-c444b221c19e/image.png)

The Event View tab provides a table view of all the data.  The results can be filtered using the Search box.

![Figure 12.2.f4: ](https://t10572667.p.clickup-attachments.com/t10572667/7f12c74a-e6a0-45f7-a549-5c328f3ac7f7/image.png)

A **Start Time** and **End Time** can be applied to the results by clicking the Timeline button.

![Figure 12.2.f5: ](https://t10572667.p.clickup-attachments.com/t10572667/b885f41f-c8f4-4587-ad42-b94ade8d27a2/image.png)

The **Graph View** provides a visual view of the messaging data in a timeline.

![Figure 12.2.f6: ](https://t10572667.p.clickup-attachments.com/t10572667/d82e61ba-a1b6-4656-8894-5e8b4ea5b547/image.png)

The Pie View tab provides another visual analysis of the data based on percentages.

## 12.3. Collated Web History

![Figure 12.3.f7: ](https://t10572667.p.clickup-attachments.com/t10572667/d184e16f-444e-4eb1-bcb2-0fe9e0f5e19f/image.png)

Browser History Redefined Results collate different web browsing applications from different sources into one.

The **Event View** tab provides a table view of all the data.  The results can be filtered using the Search box.

![Figure 12.3.f8: ](https://t10572667.p.clickup-attachments.com/t10572667/0ca623df-fe96-456e-8460-f3d1c417e332/image.png)

A **Start Time** and **End Time** can be applied to the results by clicking the Timeline button.

![Figure 12.3.f9: ](https://t10572667.p.clickup-attachments.com/t10572667/6a133fde-0988-4c4f-9b65-69c9570f940a/image.png)

The **Graph View** provides a visual view of web browser data in a timeline.

![Figure 12.3.f10: ](https://t10572667.p.clickup-attachments.com/t10572667/cd0485cf-1217-45cc-a66e-653840d7a55e/image.png)

The **Top URLs** tab is a graphical view that shows the most visited websites based on frequency.

# 13. RAM Analysis

The RAM Analysis module in RECON LAB contains a Graphical User Interface (GUI) for the Volatility Framework.  The output from Volatility can be bookmarked and used for documentation within RECON LAB.  Currently, RECON LAB supports Volatility (Version 2).

RECON LAB’s RAM Analysis module also includes the ability to carve user and Keychain passwords from RAM images.

The RAM Analysis module supports processing both Windows and macOS RAM images. Supported operating system profiles can be found here:

[https://github.com/volatilityfoundation/volatility/blob/master/README.txt](https://github.com/volatilityfoundation/volatility/blob/master/README.txt)

## 13.1. Setting Up Volatility Framework

Before continuing, please ensure that you have configured the bvolatility framework by following the steps in Section 9.9 Volatility Path.

## 13.2. Selecting a RAM Image to Process

Make sure that RAM images have been added to RECON LAB in raw format as a Source.  A raw RAM image can be created using RECON _ITR_.

 ![](blob:<https://app.clickup.com/fcda8b01-c8b3-42c8-8e7a-80f7572a7034)> Start the **RAM Analysis** module by selecting Process > Super Timeline from the Menu Bar.

![Figure 13.2.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/5324f9f3-c3bc-487c-9ad2-d6ec8134bd75/image.png)

If a RAM image has been added as a source then it can be selected in the **Source** dropdown list.

## 13.3. Carving Passwords from RAM

_Note: Carving passwords from volatile memory is not guaranteed to work.  Many factors can influence successfully carving passwords._

![Figure 13.3.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/727b0d85-1bcb-4a57-9a36-c44965b3110a/image.png)

To run the Carve Password module select a RAM image from the Source dropdown list and click **Carve Password.**

![Figure 13.3.f3: ](https://t10572667.p.clickup-attachments.com/t10572667/a6e5eac6-3afd-4fa9-a572-806114d921b8/image.png)

RECON LAB will utilize three algorithms in an attempt to collect as many passwords as possible.  A counter will increase for each password found.

![Figure 13.3.f4: ](https://t10572667.p.clickup-attachments.com/t10572667/3331528e-42d5-4990-b76d-7fa1bd9bd41d/image.png)

When the Carving Passwords module has completed a prompt will appear asking if you would like to open the list of passwords.

![Figure 13.3.f5: ](https://t10572667.p.clickup-attachments.com/t10572667/12703ad0-0c0b-4729-be1c-91b9b4dabc2c/image.png)

The Main Viewer window will display any passwords carved which can be bookmarked and added to reports.

![Figure 13.3.f6: ](https://t10572667.p.clickup-attachments.com/t10572667/59ae3199-9b9f-4fd9-8397-60b444f3f981/image.png)

Additionally, a dictionary can be created from the recovered passwords by right-clicking on any highlighted password and selecting **Create Word List**.

## 13.4. Using Volatility Framework in RECON LAB

Make sure that the steps have been followed in **Section 29.1** to properly download and install Volatility Framework.  Also, be sure to properly install any profiles that are to be used for analysis.

Start the **RAM Analysis** module by selecting Process > Super Timeline from the Menu Bar.

![Figure 13.4.f7: ](https://t10572667.p.clickup-attachments.com/t10572667/d22303a2-8fa8-48dd-87f9-906de3abb847/image.png)

Next, select the RAM image to be analyzed from the **Source** dropdown list.

![Figure 13.4.f8: ](https://t10572667.p.clickup-attachments.com/t10572667/8bfbf79d-9158-424e-b308-024c19ec2739/image.png)

Finally, select the correct **Operating System**, **Build Version** **and Artifacts** to be analyzed from the remaining dropdown lists and press **Execute**.

![Figure 13.4.f9: ](https://t10572667.p.clickup-attachments.com/t10572667/a0487447-b56d-467b-8f66-eb14e1e5a1bc/image.png)

If successful, the output will be displayed in the **Command Output** window

![Figure 13.4.f10: ](https://t10572667.p.clickup-attachments.com/t10572667/24ffed38-570d-47b3-b983-19621f986766/image.png)

The output can be exported as a text file by clicking the **Export** button.

![Figure 13.4.f11: ](https://t10572667.p.clickup-attachments.com/t10572667/90cdbaab-9c10-4712-b0bc-34534c7c8368/image.png)

Additionally, the output can be saved to the Sidebar under **RAM Analysis Saved** by clicking the **Save** button.

From the RAM Analysis Saved window the output of the RAM Analysis can be bookmarked for reporting.

# 14. Local Time Machine Snapshots (APFS Snapshots)

RECON LAB can identify and perform differential analysis of Local Time Machine Snapshots contain within a forensic image of an APFS if they exist.  Local Time Machine Snapshots are sometimes referred to as APFS Snapshots.  Refer to **Section 1.1.5** of this manual for additional information.

## 14.1. Processing Local Time Machine Snapshots

 ![](https://t10572667.p.clickup-attachments.com/t10572667/bc20bc30-7e18-42ef-ab8e-a5fadeca2fcc/Screen%20Shot%202022-01-19%20at%204.21.35%20PM.png)

Local Time Machine Snapshots only exist in APFS.  To identify if Local Time Machine Snapshots exist in the case right-click on the AFPS volume containing the user data and select **Snapshots**.

![Figure 14.1.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/9a4b9259-c30a-4e50-9b89-873093cee86e/image.png)

If any Local Time Machine Snapshots exist a window will appear listing all of the snapshots.

![Figure 14.1.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/7eba0a04-b4b3-4ebc-9e84-0e5be51d7e57/image.png)

Select the snapshot to be processed and added to the case.

![Figure 14.1.f3: ](https://t10572667.p.clickup-attachments.com/t10572667/df9e5889-8c5f-4821-90ed-99b524ba357c/image.png)

RECON LAB performs a differential analysis of the Local Time Machine Snapshot by comparing with the current state of the image and identifying modified and deleted files.

Analysis of Local Time Machine Snapshots can be repeated for any additional snapshots that exist.

Processed Local Time Machine Snapshots can be found in **Sidebar** under **Snapshots**.

# 15. Acquiring and Processing iOS Devices

In the initial Splash screen, examiners have the ability to acquire an iOS image from an iPhone, iPod, or iPad that is connected to their forensic Mac.  The examiner will need the authentication credentials for the iOS device and the ability to interact with the iOS display (i.e. a functioning screen). iTunes must be installed on the Mac and it must to be up to date.  In macOS 10.15 iTunes has been removed and the functionality of iTunes has been divided into three different applications and integrated into macOS.

## 15.1. Acquiring an iOS Device

![Figure 15.1.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/9e20157b-198b-4b21-8fde-76b757ce1ef0/Screen%20Shot%202022-01-18%20at%205.22.27%20PM.png)

Unlock the iOS device to be acquired.  Start RECON LAB and select the **Acquire iOS Device** button.  The iOS Device window will appear.

![Figure 15.1.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/0ce88813-10ae-4e75-a4be-85629b01d502/image.png)

 Connect the **unlocked** iOS device to the Mac and make sure that the iOS device as been authorized to connect to the Mac by clicking the **Trust** button.  If the Trust button does not appear automatically select the iOS device from the Finder Sidebar.  A prompt to **Trust** may also appear on the iOS device as well.

![Figure 15.1.f3: ](https://t10572667.p.clickup-attachments.com/t10572667/1d4c5150-de3d-42ba-9bf7-9dc4435e9a95/image.png)

Once the device has been authorized click the **Refresh** button to see any connected iOS devices.

Select the iOS device to acquire from the list and click the **Acquire** button.

Select the **Destination** for the output to begin the acquisition.  Once completed a prompt will appear asking if you would like to open the output.

See section 10.2.3.1 iTunes iOS Backup to add the iOS backup as a source to your case.

# 16. Reporting

RECON LAB includes a variety of reporting options from the granular level (single artifacts or plugins) to the global level (all artifacts or plugins included) and anything in-between.

Additionally, RECON LAB includes the first of its kind WYSIWYG (What You See Is What You Get) reporting mode called StoryBoard.  Story Board allows the examiner to have full control over the reporting process and is as easy to use as a word processor.  The examiner has the ability to add, remove or annotate bookmarks anywhere in the report at any time.

Story Board also allows the examiner to add his/her bookmarks and tags in chronological order to make it easier to understand the timeline of events.

## 16.1. Plugin Reports

RECON LAB supports automatically processing thousands of artifacts using hundreds of plugins.  Processed artifacts can be found by expanding **Artifacts** in the Sidebar.

Selecting any **Plugin** category will open a results window.  Every Plugin has the ability to create a variety of reports depending on the type of artifacts recovered.

![Figure 16.1.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/7fae33d6-02b4-4753-8fa1-fad55d0486ab/image.png)

Plugin reports can be generated by selecting a few options found in the upper right-hand corner of the plugin results window.

![Figure 16.1.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/ecad5d4c-0e62-4e8e-8a42-8980f57e3950/image.png)

The **type of report** can be selected from the first dropdown list.  The options are the following:

* **HTML** - Report which can be easily opened with a web browser
* **PDF** - Portable Document Format
* **CSV** - Comma Separated Value (spreadsheet)
* **XML** - Extensible Markup Language
* **KML** - Keyhole Markup Language file used for files that contain geotags

![Figure 16.1.f3: ](https://t10572667.p.clickup-attachments.com/t10572667/4fb7a3e2-d01f-4ccf-be48-d48473f9ed87/image.png)

The second dropdown list allows the examiner to select **what will be included** in the report.  The options are the following:

* **Tags** - a report with only the items that have been bookmarked in the current plugin and its tabs
* **Full** - a report of all artifacts from all tabs of the current plugin
* **Screen Items** - includes what is currently displayed in the list of results including the results of any filters

![Figure 16.1.f4: ](https://t10572667.p.clickup-attachments.com/t10572667/6b28aaf8-9a94-44ac-aac9-229df7497428/image.png)

Any items selected with the previous settings that include exportable data can be included with the report by checking the **Export** checkbox.

![Figure 16.1.f5: ](https://t10572667.p.clickup-attachments.com/t10572667/eeecdb4b-a85c-48d8-90f5-4f1e8f8ab1b7/image.png)

Once all the settings have been selected the report can be generated by clicking the **Report** button.

## 16.2. Global Artifacts Report

The Global Artifacts Report automatically creates reports from bookmarks and tags.

![Figure 16.2.f6: ](https://t10572667.p.clickup-attachments.com/t10572667/a0d93357-7a89-400c-b65e-0da4209fe752/Screen%20Shot%202022-01-19%20at%204.33.12%20PM.png)

To begin creating a Global Artifacts Report and to open the Global Report Case Information window click on the **Global Report icon** from the Top Menu.

### 16.2.1. Case Information Window

![Figure 16.2.1.f7: ](https://t10572667.p.clickup-attachments.com/t10572667/676fe6f6-1233-421e-a3f4-73e44a9ed6e6/image.png)

The **Global Report Case Information** window allows the examiner to adjust and enter additional information to be included in the report.  To proceed to the **Global Report - Report Category** selection click the **Next** button.

### 16.2.2. Customizing Global Reports

The Global Report can be customized using the **Report Scope** and **Report Type** options in the Global Report - Report Category window.

![Figure 16.2.2.f8: ](https://t10572667.p.clickup-attachments.com/t10572667/96bde731-6795-41b1-88f4-4f586e845dbc/image.png)

If **Tags** is selected under **Report Scope** the examiner can then choose any category of bookmarks or tags to include in the report.

![Figure 16.2.2.f9: ](https://t10572667.p.clickup-attachments.com/t10572667/274199f8-6362-4ca1-8aa5-4c5aff298248/image.png)

If **Full** is selected under **Report Scope** then the Report button will change to **Next** to allow the examiner to select individual Plugins to be included in the report.

**Note**: Make sure to set the Report Type, Report Name and Report Path options before proceeding.  These options will be discussed later.

![Figure 16.2.2.f10: ](https://t10572667.p.clickup-attachments.com/t10572667/cc44a3da-911a-4696-ac0b-e30418ffdb3a/image.png)

From the Global Report - Plugin Selection window individual plugins and their artifacts can be selected for inclusion in the report by checking the boxes.

If there are any files that can be exported during report creation the examiner can activate the checkbox under the Export column.

To create a Global Report from the Plugin Selection window just click Report.

### 16.2.3. Global Report Type

![Figure 16.2.3.f11: ](https://t10572667.p.clickup-attachments.com/t10572667/ba22be2e-ae29-459b-aee5-f204b292559a/image.png)

The **Report Type** can be selected in the Global Report - Report Category window.  The following report types are available:

* **Advanced HTML** - Report which can be easily opened with a web browser and have advanced navigation
* **Standard HTML** - Report which can be easily opened with a web browser in a linear format
* **PDF** - Portable Document Format
* **CSV** - Comma Separated Value (spreadsheet)
* **XML** - Extensible Markup Language

![Figure 16.2.3.f12: ](https://t10572667.p.clickup-attachments.com/t10572667/8122da11-8b62-4c35-8728-7e7e91582d24/image.png)

To create the Global Report from the Report Category window select whether or not to **Export Files** by activating the checkbox.

Optionally, the **Report Name** and **Report Path** can be changed.

![Figure 16.2.3.f13: ](https://t10572667.p.clickup-attachments.com/t10572667/470fd0a2-ad42-4e80-a6f0-2113345d7f8c/image.png)

Once all options have been selected click **Report** to generate the report.

## 16.3. Story Board Reports - WYSIWYG Reports

RECON LAB includes the first ever “What you see is what you get” (WYSIWYG) reporting option in a forensic suite called Story Board.  With **Story Board**, the examiner has full control over reporting allowing a user to add text, tags, bookmarks at will.  Additionally, Story Board includes the ability to sort and add bookmarks and tags chronologically.  Chronological reporting is proven to increase understand of factual events.

![Figure 16.3.f14: ](https://t10572667.p.clickup-attachments.com/t10572667/ea97d025-a2fb-4bc3-935d-48116739d8c7/Screen%20Shot%202022-01-19%20at%204.37.47%20PM.png)

To create a report using the Story Board reporting mode click the **Story Board** icon in the Top Menu.

![Figure 16.3.f15: ](https://t10572667.p.clickup-attachments.com/t10572667/308d5853-947f-4e95-ad9f-4cba6ea26dd6/image.png)

Enter a name for the report and click **Create** and the Story Board main interface will open.

![Figure 16.3.f16: ](https://t10572667.p.clickup-attachments.com/t10572667/d189e27f-7cbf-4b68-a249-09cc524dc472/image.png)

The Story Board interface is divided into two sections.  All tags and bookmarks from the case are accessible and found at the top.  The report is found in the bottom section.

### 16.3.1. Editing a Report

![Figure 16.3.1.f17: ](https://t10572667.p.clickup-attachments.com/t10572667/ccaf4203-e5c9-4374-862f-ef4361d9fcfb/image.png)

The Story Board interface includes a word processor with common formatting options which can be found to the right of the report.

* **Edit** - Undo, Redo, Cut, Copy, Paste
* **Font** - Installed Fonts, Font Size, Bold, Italic, Underline, Font Color
* **Alignment** - Left-centered, Centered, Right-centered, Justified, List Options

### 16.3.2. Adding Tags and Bookmarks to a Report

![Figure 16.3.2.f18: ](https://t10572667.p.clickup-attachments.com/t10572667/83fbcbfb-fa01-43b6-a17f-828ff67b43d7/image.png)

To add an item (record) to the Story Board report place the cursor at the location where the item is to be placed.  Right-click on an item from the bookmarks and tags list and select from one of the three options:

* **Add Record** - adds details about the record (bookmark, tag) to the report without the file
* **Add Record with File(s)** - adds both the details of the record to the report with the file (export)
* **Add File(s)** - adds the file only to the report (export)

![Figure 16.3.2.f19: ](https://t10572667.p.clickup-attachments.com/t10572667/8a44a173-abca-49de-a6ab-4c3efec57b44/image.png)

The above is an example of a record added to the report with the file.

### 16.3.3. Adding External Files to a Report

![Figure 16.3.3.f20: ](https://t10572667.p.clickup-attachments.com/t10572667/6ec7c9b3-3881-46db-9793-37c2fb42ec7f/image.png)

To add external files to the Story Board report click the **Add File** button found above the formatting options to the right of the report.

![Figure 16.3.3.f21: ](https://t10572667.p.clickup-attachments.com/t10572667/99caf4de-71ab-4a7b-b910-d4548e33775b/image.png)

Navigate to the file to add and click Open to add the file to the report.

### 16.3.4. Filtering Records In Story Board

![Figure 16.3.4.f22: ](https://t10572667.p.clickup-attachments.com/t10572667/8aa3a6d0-1e47-4ba1-bca6-64cb698203de/Screen%20Shot%202022-01-19%20at%204.48.00%20PM.png)

Categories of records can be selected and filtered by using the dropdown list.

![Figure 16.3.4.f23: ](https://t10572667.p.clickup-attachments.com/t10572667/e09e87c9-8728-4491-872d-be226da83f6f/image.png)

Additionally, records can be filtered by entering a keyword in the **Search** box.

### 16.3.5. Adding Records in Chronological Order

![Figure 16.3.5.f24: ](https://t10572667.p.clickup-attachments.com/t10572667/4c58c784-2a7d-4902-94c4-fffa17168de0/image.png)

Selecting the Timeline tab allows records to be sorted chronologically.  Records can then be added to the report in sequence of occurrence.

### 16.3.6. Blur Image in Report

![Figure 16.3.6.f25: ](https://t10572667.p.clickup-attachments.com/t10572667/9a13928b-0e89-4fe3-94c9-4175fffc1496/image.png)

To blur and image that is to be added to a Story Board report check the **Blur Image** button before adding an image to the report.

### 16.3.7. Saving and Exporting a Story Board Report

![Figure 16.3.7.f26: ](https://t10572667.p.clickup-attachments.com/t10572667/3e9a4142-a6d5-4de3-8174-c2efb5641ef8/image.png)

Use the **Save** button to save the current state of the Story Board report.

![Figure 16.3.7.f27: ](https://t10572667.p.clickup-attachments.com/t10572667/458a50a9-9cec-47c7-beb2-3cecd86d978c/image.png)

To export the report in a HTML, PDF or ODT format click the **Export** button and select one of the options from the dropdown list.

# 17. Shutdown RECON LAB

![Figure 17.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/c01bac84-c217-4478-a2da-ebf927f67160/image.png)

To quit RECON LAB select “Quit RECON\_LAB” from the top menu

# 18. Disk Manager with Write-Block

Disk Manager allows the processing and analysis of connected devices and their volumes by using RECON LAB’s Disk Manager and software write-blocking features.

![Figure 18.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/8375980b-b052-46ce-9006-e078a02a5858/Screen%20Shot%202022-01-18%20at%205.20.54%20PM.png)

Disk Manager can be accessed from the RECON LAB Welcome Screen by clicking the **Disk Manager** button.

![Figure 18.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/4c48e712-cfdf-42d1-961d-f052bd44a9bb/image.png)

The Disk Manger window will open showing all connected disks and volumes that can be accessed by RECON LAB.

## 18.1. Write-Blocking

![Figure 18.1.f3: ](https://t10572667.p.clickup-attachments.com/t10572667/df7a67f6-ad2f-4f53-bca5-aa88aeb5043e/image.png)

Mac computers in Target Disk Mode and other disks can be connected safely (write-block) to RECON LAB by disabling the Disk Arbitration daemon.  To turn off Disk Arbitration click the **Turn Off** button at the bottom right of the Disk Manager.

Once disabled hard disks and Mac computers placed in Target Disk Mode can be connected safely to your examination Mac.

![Figure 18.1.f4: ](https://t10572667.p.clickup-attachments.com/t10572667/65b02dca-10e3-4a3c-91bd-7e5273957dcd/image.png)

If the Mac being connected contains a T2 Security Chipset there will be prompt to enter a password for an active account on the Mac being connected in Target Disk Mode.

![Figure 18.1.f5: ](https://t10572667.p.clickup-attachments.com/t10572667/1861777a-7e7a-4907-8434-80dc3cf75d4a/image.png)

After connecting the device click the Refresh button to show the new devices.

![Figure 18.1.f6: ](https://t10572667.p.clickup-attachments.com/t10572667/54564b27-b071-46a2-a990-7849f0037944/image.png)

With the new devices displayed, the following options exist:

* **Refresh** - re-poll for changes to connected devices
* **Decrypt** - allows an examiner to decrypt FileVault volumes with a password or Recovery Key
* **Unmount** - unmount any previously mounted volume
* **Mount-R** - mounts a volume or disk read-only

## 18.2. Mounting a Device Read-Only

The Disk Manager can be used to mount volumes as read only to ensure that there are no changes to data.

![Figure 18.2.f7: ](https://t10572667.p.clickup-attachments.com/t10572667/fb441bf2-650b-4628-82df-8aa86b6294fe/image.png)

Select the volume in the Disk Manager to mount as read-only and click Mount-R.

![Figure 18.2.f8: ](https://t10572667.p.clickup-attachments.com/t10572667/ac196dd0-7d6f-46d4-bca7-4f3faec11d52/image.png)

**Note**: If you are mounting a Mac in Target Disk Mode with macOS 10.15 or higher you will need to mount both the System and Data partitions as read-only.

![Figure 18.2.f9: ](https://t10572667.p.clickup-attachments.com/t10572667/ccf8e791-69e5-4c69-8a8f-e47b249c7fda/image.png)

Once mounted read-only, the volumes can be added to RECON LAB for processing.

# 19. RECON LAB Case Exporter

RECON LAB’s Case Exporter feature allows examiners to collaborate with one another by using a portable case. This feature gives teams the ability to export all of the important information to a standalone application that can be reviewed by a Windows computer.

## 19.1. Exporting a Case

Exporting a case is a simple process that allows examiners to export findings in a way that can be further analyzed without the need for a RECON LAB license.

![Figure 19.1.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/73469b11-432e-4eae-b235-3c0989214f3a/Screen%20Shot%202022-01-18%20at%205.19.40%20PM.png)

Select Export > **Export Case** in the Menu Bar, and the Export Case window will appear.

![Figure 19.1.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/0605dc9f-2154-41a1-b3bb-00092d52a3eb/image.png)

RECON LAB has two options when exporting a case:

**Quick Mode -** Allows examiners to quickly export data from the case using RECON LAB’s preset configurations from automated plugins

**Custom Export -** Allows examiners to selectively include data for their case from bookmarks and tags

### 19.1.1. Quick Mode

In **Quick Mode**, select the **Category** options with their corresponding automated plugins under **List** to export and analyze in RECON CASE READER.

![Figure 19.1.1.f3: ](https://t10572667.p.clickup-attachments.com/t10572667/981cd8c2-d834-4ff0-8a7b-9ac12f69c954/image.png)

_Note: Automated plugins need to be processed before exporting a case in Quick Mode. For more information about RECON LAB’s automated plugins, see Section 9.2._

### 19.1.2. Custom Mode

In **Custom Mode**, select the specific data marked by tags and bookmarks to export and analyze in RECON CASE READER.

For more information on bookmarking and tagging, see Section 17

![Figure 19.1.2.f4: ](https://t10572667.p.clickup-attachments.com/t10572667/328f6c68-16c5-4cd2-8a83-72d7ac8434b0/image.png)

### 19.1.3. Exported Case Output

Select the desired **Output** directory to export the case, and click **Export**.

![Figure 19.1.3.f5: ](https://t10572667.p.clickup-attachments.com/t10572667/0ffb645d-1e99-442e-ac9f-42630ff47cfc/image.png)

The case will output to a folder named **Export\_Case** in the selected directory and will include a **RECON\_CASE\_READER.exe** and a **Case\_Data** Folder.

![Figure 19.1.3.f6: ](https://t10572667.p.clickup-attachments.com/t10572667/ec1275d5-3d80-4f6a-a6c9-0435f3d3e257/image.png)

# 20. CASE Reader

The RECON\_CASE\_READER.exe is included every time a case is exported. The executable is used to install the RECON LAB Case Reader application onto a Windows machine. The application only needs to be installed one time. After installation, any exported case can be loaded into the RECON LAB Case Reader.

## 20.1. Minimum System Requirements

Windows 10 with Intel i5 processor with 8GB of RAM.

## 20.2. Installation

To install the RECON CASE Reader double click on the RECON\_CASE\_READER.exe. Windows may ask to allow the application to make changes to your device. If so, select yes.

![Figure 20.2.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/fcf3edc2-ea9f-4ba7-8df7-6d60003e5f80/image.png)

The next step in the installation will ask if the examiner wants to create an additional desktop shortcut on the user’s desktop. Check the box to add a desktop shortcut or uncheck it to not add one.

![Figure 20.2.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/7d6b9448-e158-4bb9-aecb-d7b48681faec/image.png)

Click Install to begin installing RECON CASE. The default installation path is C:\\Program Files (x86)> RECON CASE READER

![Figure 20.2.f3: ](https://t10572667.p.clickup-attachments.com/t10572667/31523d4b-ab44-45a5-abf3-e9bb81e2f7cc/image.png)

Click Finish to complete the installation. Keeping the Launch RECON CASE READER box checked will automatically launch the RECON CASE READER once the installation is complete.

![Figure 20.2.f4: ](https://t10572667.p.clickup-attachments.com/t10572667/864ee254-0d04-40d2-95ea-558b14ff051f/image.png)

## 20.3. Loading a case

![Figure 20.3.f5: ](https://t10572667.p.clickup-attachments.com/t10572667/431e1806-f869-4d2e-8869-b8d346f22df6/image.png)

The RECON CASE READER splash screen gives the examiner the option to load any case that is exported from RECON LAB. Clicking **Load Case** will give the option to select previously loaded cases or **Other Case**.

![Figure 20.3.f6: ](https://lh4.googleusercontent.com/UGbpm3es1UEftnK3T7P3zvAM-PvZak_tnei1bjdtCYUGGmH5w5vE0Kii73gYydO3T3nGvTfVcpt2lnKotlG-8dWr5LUKZkWTbY0ecdbEPWs-0IrKjzS0i_SMs_XRS4wQj7fKycvx)

**Other Case** will open a File Explorer window where examiners can navigate to exported RECON LAB case folders. Exported case folders are named Case\_Data by default.

![Figure 20.3.f7: ](https://lh6.googleusercontent.com/o-Dwc0hubds-gmn04mBJI_M1wNg1dlsoW4kkCpJW_458Xj7kX0TWyr7wSLPuiZQNeWUZZDJONZj4WwZ7NY_0qyGkY0QrK8Ai9ENj8Xjk19r0atpt54ihEyqMwj-N5KcMM1QGa92m)

Once a case folder or previously loaded case is selected RECON CASE READER will begin to load results.

## 20.4. RECON CASE Reader Interface

The RECON CASE Reader interface is designed to mirror RECON LAB’s simple and intuitive design. Many features in the RECON CASE READER function the same way as they do in RECON LAB.

![Figure 20.4.f8: ](https://t10572667.p.clickup-attachments.com/t10572667/72bcc97c-43d8-41f4-94fd-63a3142b6a16/image.png)

## 20.5. Case View

Once a case is loaded examiners will be greeted with the Case View Screen. The Case View screen can also be accessed by clicking the “briefcase” icon at the top of the sidebar

![Figure 20.5.f9: ](https://t10572667.p.clickup-attachments.com/t10572667/94f32d33-385c-4885-9402-c005c04cfb51/image.png)

**Case View** displays information about the case including information about the case and the examiner.

**Note** This information is taken from RECON LAB at the time of the export and can not be changed.

The Case Info screen displays the sources used when exporting the case. More information about each source can be found by clicking on the name of the source.

## 20.6. Top Menu

![Figure 20.6.f10: ](https://t10572667.p.clickup-attachments.com/t10572667/f9395408-86a6-479e-ae7d-70d599ec5cd7/image.png)

RECON CASE Readers Top Menu has 3 buttons two of which have sub-menus.

**Artifacts** - contains the “Search Artifacts” and “Artifact Timeline” sub-menus.

**Search Artifacts** - allows the examiner to conduct a single keyword search quickly within all exported artifacts. Section 19.1 has more information about Artifact Keyword searching.

![Figure 20.6.f11: ](https://lh5.googleusercontent.com/QS0J4g83SOB0uDqo5RrNCuMhO7Q6NiR9Ug1ufSFpj9S_0WuXKhaIcekDvCWtgvusYJK0KSsLYfIMAsfjvAN6E27pBkMqAP4ptulEaVu0XSA5jWtXkMTWE0Fw2fm4tXAHouuqNghW)

**Artifacts Timeline** -  Opens the Artifacts Timeline module used for generating timelines and graphs for timestamps recovered from the exported Artifacts and Plugins module. Section 27.2 has more information on Artifacts Timeline.

![Figure 20.6.f12: ](https://t10572667.p.clickup-attachments.com/t10572667/4ce3b1c5-36ea-4ee7-b461-092a29292d67/image.png)

**Generate Report** - contains the “Automated Report” menu

**Automated Report** - automatically generates reports from bookmarks or plugins. Section 32.2 has more information about Global Reports

![Figure 20.6.f13: ](https://t10572667.p.clickup-attachments.com/t10572667/88a5e81b-1ea3-44c9-b100-bb082d194a59/image.png)

**File Search** - Allows for locating files based on a combination of timestamps, file names, extensions, file sizes, and more. Section 19.2 has detailed information about File Search.

![Figure 20.6.f14: ](https://t10572667.p.clickup-attachments.com/t10572667/bcd8df2f-f5ac-4419-8265-a6a2fcf55f11/image.png)

## 20.7. Main Columns

There are two main columns at the top of the Main Window for the RECON CASE READER. These columns can be used for quick navigation.

![Figure 20.7.f15: ](https://lh3.googleusercontent.com/JtkKc5hS9hk6BBxM8i0gUkuSg-fjlGZ74DLy66hwxFuNUm60q1cKA2HaIEq4np5x1XMeKM0Epno-HnUP8EDZqluGz5vY8iYKyWwQKz3OsTnfQODyN-mb57jf1iBkdKH1hz9Z2EEA)

When you navigate to different modules or views these columns will keep a history of these. Clicking on the columns will allow you to return to a previous module or view.

Views or modules can be removed by selecting the “X” button.

![Figure 20.7.f16: ](https://lh5.googleusercontent.com/lyTAINks-O52x71atA2cbUy28OjVBinUHMYSnbzyZSKJvpA09c7t3f7gyCUoUNbX_wOnBMZDosYtABP54_HvNCQtEN0Vy7cQMgfMYUxWs5Dl7nfKQ5h9EKc50cWdDVQb5I9R5dZI)

### 20.7.1. Select Category Column

![Figure 20.7.1.f17: ](https://lh6.googleusercontent.com/nV-noRKd3kFitpqsWSroIPZFid4NWCdaONi5_NPm77L7f_yAvL_IGozrodZay2x9ui6D-O3SZI6SoFfeO0EjNdUBkWVjCoS42SfOGMFcxyCZQRZ_LgsrKBcXpu0f4bj4pYl1uqEh)

The Select Category Column keeps a history of modules and sources previously viewed. Clicking the title of the column will show previous items. Select any item to return to the module or source.

### 20.7.2. Select Feature Column

![Figure 20.7.2.f18: ](https://lh6.googleusercontent.com/XWNM91unM3mvuHL1T5X08JH05pbBDNg3caatsvEsIQ34jndOqhCZ-EYuffWUBrO1_OvAiOvDo_9PJ9uP9zVZkm-RmKkJV8bjh5ieWy3yJcAZo32XG9CZGtyb9uRyqHI0yy7Mc8PD)

The Select Feature Column keeps a history of different windows viewed. Clicking the title of the column will show previous items. Select any item to return to a previous window.

## 20.8. Case Sidebar

![Figure 20.8.f19: ](https://t10572667.p.clickup-attachments.com/t10572667/15c4ce9a-2bb9-48cb-9f32-eba959537a6d/image.png)

The sidebar is used to quickly access data found from processing and analysis. It can also be used to manually navigate through the exported source data.

Clicking the dropdown arrow next to a category or directory will expand it.

The case sidebar is broken up into three sections.

1. **Source - Displays the exported data allowing for manual review and analysis.**
2. **Artifacts - Displays data parsed from artifacts at the time of export as well as artifact keyword search results and artifact timeline results**
3. **File Filters - Displays information about file types and File Search results**

### 20.8.1. Source Tab

![Figure 20.8.1.f20: ](https://t10572667.p.clickup-attachments.com/t10572667/272b4f19-6297-4646-b2a5-65041a7a96a3/image.png)

The source tab shows the exported files in a directory structure. Examiners can easily manually navigate through the directories of the exported data.

### 20.8.2. Artifacts Tab

The artifacts tab displays information from exported artifacts along with the results from Artifact Keyword searches and Artifact Timelines.

![Figure 20.8.2.f21: ](https://t10572667.p.clickup-attachments.com/t10572667/df36b859-8efd-4650-ac2b-bfabd26eaf4e/image.png)

![Figure 20.8.2.f22: ](https://t10572667.p.clickup-attachments.com/t10572667/01f9fad8-b9dc-4d51-a01e-bd913dcb0528/image.png)

### 20.8.3. File Filters

The File Filters tab contains data relating to file extensions and results from file searches. Files will be sorted by extensions or categorized by searched keywords.

![Figure 20.8.3.f23: ](https://t10572667.p.clickup-attachments.com/t10572667/d15f4e8a-1f16-4d7c-88a3-f9a6091fb71c/image.png)

## 20.9. Main Viewer Window

The RECON CASE Reader main view is designed to mirror the interface of RECON LAB. See section 12.6-12.8 for more information about the main view, covering the Details, Hex Viewer, Text Viewer, Apple Metadata, and more.

![Figure 20.9.f24: ](https://t10572667.p.clickup-attachments.com/t10572667/eee92d28-0976-4d55-b046-1d6dfc5b81aa/image.png)

# 21. Importing your Case into RECON LAB

Case folders exported and analyzed in RECON CASE READER can be loaded back into RECON LAB for further analysis or more robust report generation.

Simply select to Load Case when starting RECON LAB and point to the case folder used in the RECON CASE READER.

# 22. Weapon Analysis

The weapon analysis file system module allows RECON LAB to automatically identify and categorize pictures that have firearms in them. Pictures will be categorized as either Guns or Rifles and put into their own category.

## 22.1. Processing for Weapon Analysis

Weapon Analysis is processed as a file system module and is accessed by right-clicking a file or directory in the file system. The screenshot below shows the file system module processing options including Weapon Analysis.

![Figure 22.1.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/137315e9-d28e-484b-9149-0a310023ad86/Screen%20Shot%202022-01-20%20at%204.28.04%20PM.png)

## 22.2. Weapon Analysis Results

Results for weapon analysis are put into their own category on the left menu. The results are broken into two subcategories of Guns or Rifles.

![Figure 22.2.f2: ](blob:<https://app.clickup.com/81f2bd6e-092a-48c1-8dac-b5bb838abaf2)>

After selecting a category results are displayed in the main pane. Results can be viewed as either a list of files or in a gallery view.

![Figure 22.2.f3: ](https://t10572667.p.clickup-attachments.com/t10572667/e977218a-ae94-4ea2-acd9-7f4f599dd83a/Screen%20Shot%202022-01-20%20at%205.13.07%20PM.png)

# 23. Fire Analysis

The Fire Analysis File System Module allows RECON LAB to automatically identify and categorize pictures that have fire in them. Detected pictures will be put into their own category for easy analysis.

## 23.1. Processing for Fire Analysis

Fire Analysis is processed as a file system module and is accessed by right-clicking a file or directory in the file system. The screenshot below shows the file system module processing options including Fire Analysis. ![](https://t10572667.p.clickup-attachments.com/t10572667/c3cc5f22-51b1-49a7-a4df-f3634712244d/image.png)

## 23.2. Fire Analysis Results

Results from Fire Analysis are displayed in their own category in the left menu. After selecting Fire Analysis results are displayed in the main pane and can be viewed in a file list or a gallery view

![Figure 23.2.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/4df9ddda-e078-4b40-9602-25c2f2feb923/image.png)

![Figure 23.2.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/8fcb1177-a96f-4dcc-a5a0-453e12aff9cd/image.png)

# 24. Skin Tone Detection

The Skin Tone Analysis File System Module allows RECON LAB to automatically identify and categorize pictures that have a detected skin tone in them. Detected pictures will be put into their own category for easy analysis.

## 24.1. Processing Skin Tone Detection

Skin Tone Analysis is processed as a file system module and is accessed by right-clicking a file or directory in the file system. The screenshot below shows the file system module processing options including Skin Tone Detection.

![Figure 24.1.f1: ](https://lh5.googleusercontent.com/DviQgUnJtjg8elWCrUGzSIggAP9O-JoWKBrYy7NnES2c8gpwCdH05PHdMKDiJfOPcaWRgyYkjNrOj5CKdaevleFP-dK2NFmOetEMK371xAf5mVInsDd7jvkYYccUFdLfwtcMqEed)

## 24.2. Skin Tone Detection Results

Results from Skin Tone Detection results are displayed in their own category in the left menu. After selecting Skin Tone Detection results are split into different file types.

![Figure 24.2.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/a8e177ba-74b8-4586-b2ba-662d19a71ca7/image.png)

After selecting a file type results are displayed in the main pane and can be viewed in a file list or a gallery view.

![Figure 24.2.f3: ](https://t10572667.p.clickup-attachments.com/t10572667/85d18530-c5f6-43e4-9f62-8add0bbf6901/image.png)

# 25. Face Analysis

The Face Analysis File System Module allows RECON LAB to automatically identify and categorize pictures that have a detected face in them. Detected pictures will be put into their own category for easy analysis. After faces are identified examiners can then search for faces using the Face Search Feature.

## 25.1. Processing for Face Analysis

Face Analysis is processed as a file system module and is accessed by right-clicking a file or directory in the file system. The screenshot below shows the file system module processing options including Face Analysis.

![Figure 25.1.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/224ef9c1-73a8-478d-9c67-415eb0134eed/image.png)

**Note** Faces must be indexed using the Face Analysis Feature before the Face Search Feature can be used.

## 25.2. Face Analysis Results

Results from Face Search are displayed in their own category in the left menu. After selecting Faces all of the detected faces will be displayed in one section. Files can be displayed as either a list of files or a list of faces.

![Figure 25.2.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/e04a937e-cee2-472d-91b0-ab4595821f0b/image.png)

The Faces option for displaying results will show a list of faces and all images associated with each face. Simply click on each face to show a gallery of all images associated with the detected face.

![Figure 25.2.f3: ](https://t10572667.p.clickup-attachments.com/t10572667/55da5bf8-ffcc-45fe-a3a0-82deccde9c32/image.png)

## 25.3. Face Search

After indexing faces with the Face Analysis file system module examiners can import an image and search for any pictures with that face in them.

In the Menu Bar select Search>Recognize Face.

![Figure 25.3.f4: ](https://t10572667.p.clickup-attachments.com/t10572667/07988621-8411-4523-b89c-6525f018c0e9/image.png)

A window will pop up that allows examiners to load a file of their choosing. Click the three dots at the top of the window to open a Finder window and navigate to your desired picture. After the picture is selected click the Extract Faces button to detect the face in the picture.

After the face is detected add a name to save the results as and click Start.

![Figure 25.3.f5: ](https://t10572667.p.clickup-attachments.com/t10572667/b343255e-bcb1-4396-a686-5d4dd68818dd/image.png)

Face Search results will be displayed in the left menu under Face Search.

![Figure 25.3.f6: ](https://t10572667.p.clickup-attachments.com/t10572667/ce81ec16-07cd-4d98-b354-b367ed9b5cdd/image.png)

Results will be displayed as a file list view and can be changed to a gallery view for easy analysis.

![Figure 25.3.f7: ](https://t10572667.p.clickup-attachments.com/t10572667/beb80eba-d12a-436c-9e8b-e6a1a19323c1/image.png)

![Figure 25.3.f8: ](https://t10572667.p.clickup-attachments.com/t10572667/2d8209d9-907d-42a2-a531-f65f3bdc69f7/image.png)

# 26. Optical Character Recognition (OCR)

The Optical Character Recognition File System Module allows RECON LAB to automatically identify and index pictures that have text in them. Detected pictures will be put into their own category for easy analysis.

## 26.1. Processing Optical Character Recognition (OCR)

Optical Character Recognition is processed as a file system module and is accessed by right-clicking a file or directory in the file system. The screenshot below shows the file system module processing options including Optical Character Recognition.

![Figure 26.1.f1: ](https://lh3.googleusercontent.com/hSNowlBOVsOJL-8CHrmdqiBkzoYGmF4RH9c1RsO1InOtTKzyq2ysh89gbySHuVhfYeEpQRMbphKwoictKcIqvLP36KfCK8eWtYbDjDW_B1ygjMfbHAKvBKc2VoiyymeWIsWCz_n9)

## 26.2. Optical Character Recognition (OCR) Analysis

Results from Optical Character Recognition are displayed in their own category in the left menu. After selecting Images all of the pictures with extracted text will be displayed in the main pane. Files can be displayed as either a list of files or a gallery view.![](https://t10572667.p.clickup-attachments.com/t10572667/982177b4-5356-4bd2-8d8f-4bda61b951ad/image.png)

A preview of the extracted text is shown in red under the OCR Text column.

Searching the extracted OCR text is done using the Search box at the top left corner of the Optical Character Recognition Pane. To search OCR indexed text click the Filter dropdown menu and check the OCR Text option.

![Figure 26.2.f2: ](https://t10572667.p.clickup-attachments.com/t10572667/d5841d28-cce7-47bc-815d-a1ab75530ed2/image.png)

The Show All button will remove the search filter and show all indexed files again.

After selecting the file the full OCR indexed will be displayed in the Detailed Information pane under OCR Text.

# 27. Examiner Space

RECON LAB’s examiner space is a feature that allows examiners to easily take notes about their case and add those notes to their final reports. The Examiner space has an Examiner comments note-taking area and a to-do list.

## 27.1. Examiner Comments

The Examiner comments tab acts as a general note-taking option where examiners can add notes about their current case. Examiners can edit their text using the options in the top left for **bold**, _italic_, underline, and font color.

The export button in the center of the window allows examiners to export their report in either a PDF or HTML format.

![Figure 27.1.f1: ](https://t10572667.p.clickup-attachments.com/t10572667/07113855-c4a0-42fb-9938-6f3c0cdddaf8/image.png)

The Add Timestamp button will inset a timestamp of the current machine time as either UTC (by checking the Use UTC box) or the current timezone offset of the examination machine.

## 27.2. Adding Examiner Notes to a Report

Examiner Notes can be added to a storyboard report as their own item. Once examiners create a storyboard report (see section 31.3 for how to generate a storyboard report) the same way any other bookmark is added.

Simply choose the Examiner Space option from the dropdown menu and add the record by right-clicking and selecting Add Record.

# 28. Terms and Conditions

**RECON LAB**

Copyright 2013-2023 – SUMURI LLC

[www.sumuri.com](http://www.sumuri.com/)

**IMPORTANT, PLEASE READ CAREFULLY. THIS IS A LICENSE AGREEMENT**

This RECON LAB is protected by copyright laws and international copyright treaties, as well as other intellectual property laws and treaties. This RECON LAB is licensed, not sold.

**End-User License Agreement**

This End User License Agreement (‘EULA’) is a legal agreement between you (either an individual or a single entity) and SUMURI LLC with regard to the copyrighted software (herein referred to as RECON LAB or ‘software’) provided with this EULA.   The RECON LAB includes computer software, the associated media, any printed materials, and any ‘online’ or electronic documentation. Use of any software and related documentation (‘software’) provided to you by RECON LAB in whatever form or media, will constitute your acceptance of these terms, unless separate terms are provided by the software supplier, in which case certain additional or different terms may apply. If you do not agree with the terms of this EULA, do not download, install, copy or use the software. By installing, copying or otherwise using RECON LAB, you agree to be bound by the terms of this EULA.  If you do not agree to the terms of this EULA, SUMURI LLC is unwilling to license RECON LAB to you.

Eligible License – This software is available for license solely to software owners, with no right of duplication or further distribution, licensing, or sub-licensing.

License Grant – SUMURI LLC grants to you a personal, non-transferable and non-exclusive right to use the copy of the software provided with this EULA. You agree you will not copy or duplicate the software. You agree that you may not copy the written materials accompanying the software. Modifying, translating, renting, copying, transferring or assigning all or part of the software, or any rights granted hereunder, to any other persons and removing any proprietary notices, labels or marks from the software is strictly prohibited.  Furthermore, you hereby agree not to create derivative works based on the software.  You may not transfer this software.

Copyright –  The software is licensed, not sold.  You acknowledge that no title to the intellectual property in the software is transferred to you. You further acknowledge that title and full ownership rights to the software will remain the exclusive property of SUMURI LLC and/or its suppliers, and you will not acquire any rights to the software, except as expressly set forth above. All copies of the software will contain the same proprietary notices as contained in or on the software. All title and copyrights in and to RECON LAB  (including but not limited to any images, photographs, animations, video, audio, music, text and ”applets,” incorporated into RECON LAB), the accompanying printed materials, and any copies of RECON LAB, are owned by SUMURI LLC.  RECON LAB is protected by copyright laws and international treaty provisions.  You may not copy the printed materials accompanying RECON LAB.

Reverse Engineering – You agree that you will not attempt, and if you are a corporation, you will use your best efforts to prevent your employees and contractors from attempting to reverse compile, modify, translate or disassemble the Software in whole or in part. Any failure to comply with the above or any other terms and conditions contained herein will result in the automatic termination of this license and the reversion of the rights granted hereunder to SUMURI LLC.

Disclaimer of Warranty – The software is provided ‘AS IS’ without warranty of any kind. SUMURI LLC and its suppliers disclaim and make no express or implied warranties and specifically disclaim the warranties of merchantability, fitness for a particular purpose, and non-infringement of third-party rights. The entire risk as to the quality and performance of the software is with you. Neither SUMURI LLC nor its suppliers warrant that the functions contained in the software will meet your requirements or that the operation of the software will be uninterrupted or error-free. SUMURI LLC is not obligated to provide any updates to the software for any user who does not have a software maintenance subscription.

Limitation of Liability – SUMURI LLC’s entire liability and your exclusive remedy under this EULA shall not exceed the price paid for the software, if any.  In no event shall SUMURI LLC or its suppliers be liable to you for any consequential, special, incidental or indirect damages of any kind arising out of the use or inability to use the software, even if SUMURI LLC or its supplier has been advised of the possibility of such damages, or any claim by a third party.

Rental – You may not loan, rent, or lease the software.

Transfer – You may not transfer the software to a third party, without written consent from SUMURI LLC and written acceptance of the terms of this Agreement by the transferee. Your license is automatically terminated if you transfer the software without the written consent of SUMURI LLC. You are to ensure that the software is not made available in any form to anyone not subject to this Agreement. A transfer fee of $150 USD will be charged to transfer the software (not applicable to transfers associated with orders from distributors, or resellers or intra-company transfers).

Upgrades – If the software is an upgrade from an earlier release or previously released version, you now may use that upgraded product only in accordance with this EULA.  If RECON LAB is an upgrade of a software program which you licensed as a single product, then RECON LAB may be used only as part of that single product package and may not be separated for use on more than one computer.

OEM Product Support – Product support for RECON LAB is provided by SUMURI LLC.  For product support, please call SUMURI LLC.  Should you have any questions concerning this, please refer to the address provided in the documentation.

No Liability for Consequential Damages – In no event shall SUMURI LLC or its suppliers be liable for any damages whatsoever (including, without limitation, incidental, direct, indirect special and consequential damages, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising out of the use or inability to use this ‘SUMURI LLC’ product, even if SUMURI LLC has been advised of the possibility of such damages.  Because some states/countries do not allow the exclusion or limitation of liability for consequential or incidental damages, the above limitation may not apply to you.

Indemnification By You – If you distribute the Software in violation of this Agreement, you agree to indemnify, hold harmless and defend SUMURI LLC and its suppliers from and against any claims or lawsuits, including attorney’s fees that arise or result from the use or distribution of the software in violation of this Agreement.

Jurisdiction – The parties consent to the exclusive jurisdiction and venue of the federal and state courts located in the State of Delaware, USA, in any action arising out of or relating to this Agreement. The parties waive any other venue to which either party might be entitled by domicile or otherwise.
