# Watermarkd
Simple Watermark Program with GUI



# Watermarkd
Simple Watermark Program with GUI


![Watermarkd_logo](https://holypython.com/wp-content/uploads/2019/11/default.png)

[![tkinter](http://pepy.tech/badge/pysimplegui)](http://pepy.tech/project/pysimplegui) tkinter
[![tkinter27](https://pepy.tech/badge/pysimplegui27)](https://pepy.tech/project/pysimplegui27) tk 2.7
[![Downloads](https://pepy.tech/badge/pysimpleguiqt)](https://pepy.tech/project/pysimpleguiqt) Qt
[![Downloads](https://pepy.tech/badge/pysimpleguiwx)](https://pepy.tech/project/pysimpleguiWx) WxPython
[![Downloads](https://pepy.tech/badge/pysimpleguiweb)](https://pepy.tech/project/pysimpleguiWeb) Web (Remi)

![Documentation Status](https://readthedocs.org/projects/pysimplegui/badge/?version=latest)
![Python Version](https://img.shields.io/badge/Python-2.7_3.4+-yellow.svg)

[![PyPI Version](https://img.shields.io/pypi/v/pysimplegui.svg?style=for-the-badge)](https://pypi.org/project/pysimplegui/) tkinter
[![PyPI Version](https://img.shields.io/pypi/v/pysimpleguiqt.svg?style=for-the-badge)](https://pypi.org/project/pysimpleguiqt/) Qt
[![PyPI Version](https://img.shields.io/pypi/v/pysimpleguiweb.svg?style=for-the-badge)](https://pypi.org/project/pysimpleguiweb/) Web
[![PyPI Version](https://img.shields.io/pypi/v/pysimpleguiwx.svg?style=for-the-badge)](https://pypi.org/project/pysimpleguiwx/) Wx
![GitHub issues](https://img.shields.io/github/issues-raw/PySimpleGUI/PySimpleGUI?color=blue)  ![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/PySimpleGUI/PySimpleGUI?color=blue)
[![Commit activity](https://img.shields.io/github/commit-activity/m/PySimpleGUI/PySimpleGUI.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/PySimpleGUI/PySimpleGUI.svg?style=for-the-badge)](../../commits/master)

# PySimpleGUI User's Manual

## <span>The Call Reference Section Moved to <a href="https://pysimplegui.readthedocs.io/en/latest/call%20reference/">here</a></span>

### This manual is crammed full of answers so start your search for answers here. Read/Search this prior to opening an Issue on GitHub.  Press Control F and type.
---

# Jump-Start

## Install

```
pip install Watermarkd
or
pip3 install Watermarkd
```

### This Code

```python
import PySimpleGUI as sg

sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
```



# About The PySimpleGUI Documentation System

This User's Manual (also the project's readme) is one ***vital*** part of the PySimpleGUI programming environment.  The best place to read it is at http://www.PySimpleGUI.org

If you are a professional or skilled in how to develop software, then you understand the role of documentation in the world of technology development. Use it, please.

***It WILL be required, at times, for you to read or search this document in order to be successful.***

Using Stack Overflow and other sites to post your questions has resulted in advice given by a lot of users that have never looked at the package and are sometimes just flat bad advice.  When possible, post an Issue on this GitHub. Definitely go through the Issue checklist.  Take a look through the docs, again.

There are 5 resources that work together to provide to you the fastest path to success.  They are:

1. This User's Manual
2. The Cookbook
3. The 170+ Demo Programs
4. Docstrings enable you to access help directly from Python or your IDE
5. Searching the GitHub Issues as a last resort (search both open and closed issues)

Pace yourself.  The initial progress is exciting and FAST PACED.  However, GUIs take time and thought to build.  Take a deep breath and use the provided materials and you'll do fine.  Don't skip the design phase of your GUI after you run some demos and get the hang of things.  If you've tried other GUI frameworks before, successful or not, then you know you're already way ahead of the game using PySimpleGUI versus the underlying GUI frameworks.  It may feel like the 3 days you've been working on your code has been forever, but by comparison of 3 days learning Qt, PySimpleGUI will look trivial to learn.

It is not by accident that this section, about documentation, is at the TOP of this document.

This documentation is not HUGE in length for a package this size. In fact it's still one document and it's the readme for the GitHub.  It's not written in complex English.  It is understandable by complete beginners.  And pressing `Control+F` is all you need to do to search this document.  USUALLY you'll find less than 6 matches.

## Documentation and Demos Get Out of Date

Sometimes the documentation doesn't match exactly the version of the code you're running.  Sometimes demo programs haven't been updated to match a change made to the SDK.  Things don't happen simultaneously generally speaking.  So, it may very well be that you find an error or inconsistency or something no longer works with the latest version of an external library.

If you've found one of these problems, and you've searched to make sure it's not a simple mistake on your part, then by ALL means log an Issue on the GitHub.  Don't be afraid to report problems if you've taken the simple steps of checking out the docs first.

# Platforms

## Hardware and OS Support

PySimpleGUI runs on Windows, Linux and Mac, just like tkinter, Qt, WxPython and Remi do.  If you can get the underlying GUI Framework installed / running on your machine then PySimpleGUI will also run there.

### Hardware

* PC's, Desktop, Laptops
* Macs of all types
* Raspberry Pi
* Android devices like phones and tablets
* Virtual machine online (no hardware) - repl.it

### OS

* Windows 7, 8, 10
* Linux on PC - Tested on several distributions
* Linux on Raspberry Pi
* Linux on Android - Can use either Termux or PyDroid3
* Mac OS

#### Python versions

As of 9/25/2018 **both Python 3 and Python 2.7 are supported** when using **tkinter version** of PySimpleGUI! The Python 3 version is named `PySimpleGUI`. The Python 2.7 version is `PySimpleGUI27`.  They are installed separately and the imports are different. See instructions in Installation section for more info.  **None** of the other ports can use Python 2.

###### Python 2.7 Code will be deleted from this GitHub on Dec 31, 2019

Note that the 2.7 port will *cease to exist on this GitHub* on Jan 1, 2020.  If you would like to know how much time you have to move over to the Python 3 version of PySimpleGUI, then go here: https://pythonclock.org/.  The only thing that will be available is an unsupported PyPI release of PySimpleGUI27.

By "will cease to exist on this GitHub" I mean, it will be deleted entirely.  No source code, no supporting programs.  Nothing.  If you're stuck using 2.7 in December, it would behoove you to fork the 2.7 code on Dec 31, 2019.  Legacy Python doesn't have a permanent home here.  It sounds cruel, but experts in security particularly says 2.7 is a huge risk. Furthering it use only hurts the computing world.

#### Warning - tkinter + Python 3.7.3 and later, including 3.8 has problems

The version of tkinter that is being supplied with the 3.7.3 and later versions of Python is known to have a problem with table colors.  Basically, they don't work.  As a result, if you want to use the plain PySimpleGUI running on tkinter, you should be using 3.7.2 or less.  3.6 is the version PySimpleGUI has chosen as the recommended version for most users.

## Output Devices

In addition to running as a desktop GUI, you can also run your GUI in a web browser by running PySimpleGUIWeb. 

This is ideal for "headless" setups like a Raspberry Pi that is at the core of a robot or other design that does not have a normal display screen.  For these devices, run a PySimpleGUIWeb program that never exits.  

Then connect to your application by going to the Pi's IP address (and port #) using a browser and you'll be in communication with your application.  You can use it to make configuration changes or even control a robot or other piece of hardware using buttons in your GUI





# Elements

You will find information on Elements and all other classes and functions are located near the end of this manual.  They are in 1 large section of the readme, in alphabetical order for easy lookups.  This section's discussion of Elements is meant to teach you how they work.  The other section has detailed call signatures and parameter definitions.

"Elements" are the building blocks used to create windows.  Some GUI APIs use the term "Widget" to describe these graphic elements.

- Text
- Single Line Input
- Buttons including these types:
	- File Browse
	- Folder Browse
	- Calendar picker
	- Date Chooser
	- Read window
	- Close window ("Button" & all shortcut buttons)
	- Realtime
- Checkboxes
- Radio Buttons
- Listbox
- Slider
- Multi-line Text Input/Output
- Multi-line Text Output (not on tkinter version)
- Scroll-able Output
- Vertical Separator
- Progress Bar
- Option Menu
- Menu
- ButtonMenu
- Frame
- Column
- Graph
- Image
- Table
- Tree
- Tab, TabGroup
- StatusBar
- Pane
- Stretch (Qt only)
- Sizer (plain PySimpleGUI only)

Previously this program was implemented using a sleep in the loop to control the clock tick.  This version uses the new timeout parameter.  The result is a window that reacts quicker then the one with the sleep and the accuracy is just as good.

## Instead of a Non-blocking Read --- Use `enable_events = True` or `return_keyboard_events = True`

Any time you are thinking "I want an X Element to cause a Y Element to do something", then you want to use the `enable_events` option.

***Instead of polling, try options that cause the window to return to you.***  By using non-blocking windows, you are *polling*.  You can indeed create your application by polling.  It will work.  But you're going to be maxing out your processor and may even take longer to react to an event than if you used another technique.

**Examples**

One example is you have an input field that changes as you press buttons on an on-screen keypad.

![keypad 3](https://user-images.githubusercontent.com/13696193/45260275-a2198e80-b3b0-11e8-85fe-a4ce6484510f.jpg)

# Updating Elements (changing element's values in an active window)

If you want to change an Element's settings in your window after the window has been created, then you will call the Element's Update method.

**NOTE** a window **must be Read or Finalized** before any Update calls can be made.  Also, not all settings available to you when you created the Element are available to you via its `update` method.

# "Demo Programs" Applications

There are too many to list!!

There are over 170 sample programs to give you a jump start.

These programs are an integral part of the overall PySimpleGUI documentation and learning system.  They will give you a headstart in a way you can learn from and understand.  They also show you integration techiques to other packages that have been figured out for you.

You will find Demo Programs located in a subfolder named "Demo Programs" under the top level and each of the PySimpleGUI ports on GitHub.

Demo programs for plain PySimpleGUI (tkinter)
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms

Demo programs for PySimpleGUIQt:
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIQt/Demo%20Programs

Demo programs for PySimpleGUIWx:
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWx/Demo%20Programs

Demo programs for PySimpleGUIWeb:
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWeb/Demo%20Programs

There are not many programs under each of the port's folders because the main Demo Programs should run on all of the other platforms with minimal changes (often only the import statement changes).

You will also find a lot of demos running on Trinket
http://Trinket.PySimpleGUI.org

# Creating a Windows .EXE File

It's possible to create a single .EXE file that can be distributed to Windows users. There is no requirement to install the Python interpreter on the PC you wish to run it on. Everything it needs is in the one EXE file, assuming you're running a somewhat up to date version of Windows.

Installation of the packages, you'll need to install PySimpleGUI and PyInstaller (you need to install only once)

```bash
pip install PySimpleGUI
pip install PyInstaller

```

To create your EXE file from your program that uses PySimpleGUI,  `my_program.py`, enter this command in your Windows command prompt:

```bash
pyinstaller -wF my_program.py

```

You will be left with a single file,  `my_program.exe`, located in a folder named  `dist`  under the folder where you executed the  `pyinstaller`  command.

That's all... Run your  `my_program.exe`  file on the Windows machine of your choosing.

> "It's just that easy."

(famous last words that screw up just about anything being referenced)

Your EXE file should run without creating a "shell window". Only the GUI window should show up on your taskbar.

If you get a crash with something like:
```python
ValueError: script '.......\src\tkinter' not found
```

Then try adding **`--hidden-import tkinter`** to your command

# Creating a Mac App File

There are reports that PyInstaller can be used to create App files.  It's not been officially tested.

Run this command on your Mac

> pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' your_program.py

Another also mentioned it may be helpful to add the "windowed" option so that a console is not opened.  That should make the command:

> pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --windowed --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' your_program.py

This info was located on Reddit with the source traced back to:
https://github.com/pyinstaller/pyinstaller/issues/1350



# Look and Feel

You can change defaults and colors of a large number of things in PySimpleGUI quite easily.

##  `ChangleLookAndFeel`

Want a quick way of making your windows look a LOT better?  Try calling `ChangeLookAndFeel`.  It will, in a single call, set various color values to widgets, background, text, etc.

Or dial in the look and feel (and a whole lot more) that you like with the `SetOptions` function.  You can change all of the defaults in one function call.  One line of code to customize the entire GUI.

```python
    sg.ChangeLookAndFeel('GreenTan')


```



---
# Known Issues

Well, there are a few quirks, and problems of course.  Check the [GitHub Issues database](https://github.com/PySimpleGUI/PySimpleGUI/issues) for a list of them.

As previously mentioned **this is where you should post all problems and enhancements.**

Random crashes have been rare.  The code is stable and hasn't been "quirky" nor have there been many "emergency" releases.

## MACS & tkinter

Macs and PySimpleGUI did not play well together up until Nov 2019 and the release of ttk buttons.  Prior to that buttons had to be white.  Now the Mac can use any color for buttons and they work great.  Images on buttons work as well.

The problems were the normal tk.Button was not working correctly on the Mac.  You couldn't set the button color.  If you tried it appeared as if the text was missing.

Users have recently reported the ability to install Python 3.7 from the Python.org website and not use the Homebrew version.  This resolved all of the button color problems. 

Regardless of where you get your Python / tkinter, Macs can now enjoy using all of the look and feel color themes that Windows and Linux users are able to achieve.

Many PySimpleGUI users have switched from PySimpleGUI to PySimpleGUIQt due to the button problems.  IF you're one of them, ***you should consider switching back***.  One reason to return to PySimpleGUI is that features tend to get implemented on PySimpleGUI (tkinter version) and then later on the  other ports.  There are a number of other reasons to give tkinter another try.

## Multiple threads

Consider this is a ***stern warning***

### **Do not attempt** to call `PySimpleGUI` from multiple threads! At least the `tkinter` based port because tkinter is not threadsafe and has known issues with multiple threads

Tkinter also wants to be the MAIN thread in your code.  So, if you have to run multiple threads, make sure the GUI is the main thread.

Other than that, feel free to use threads with PySimpleGUI on all of the ports.  You'll find a good example for how to run "long running tasks" in your event loop by looking at the demo program: `Demo_Multithreaded_Long_Tasks.py`.  There are several examples of using threads with PySimpleGUI.

Be sure and **delete** your windows after you close them if you are running with multiple threads.  There is a chance another thread's garbage collect will attempt to delete the window when not in the mainthread which will cause tkinter to crash.

### The dreaded "Tcl_AsyncDelete: async handler deleted by the wrong thread" error

This crash has plagued and mystified tkinter users for some time now.  It happens when the user is running multiple threads in their application.  Even if the user doesn't make any calls that are into tkinter, this problem can still cause your program to crash.

I'm thrilled to say there's a solution and it's easy to implement.  If you're getting this error, then here is what is causing it.

When you close a window and delete the layout, the tkinter widgets that were in use in the window are no longer needed.  Python marks them to be handled by the "Garbage Collector".  They're deleted but not quite gone from memory.  Then, later, while your thread is running, the Python Garbage Collect algorithm decides it's time to run garbage collect.  When it tells tkinter to free up the memory, the tkinter code looks to see what context it is running under.  It sees that it's a thread, not the main thread, and generates this exception.  

The way around this is actually quite easy.

When you are finished with a window, be sure to:

* Close the Window
* Set the `layout` variable to None
* Set the `window` variable to None
* Trigger Python's Garbage Collect to run immediately

The sequence looks like this in code:

```python
    import gc

    # Do all your windows stuff... make a layout... show your window... then when time to exit
    window.close()
    layout = None
    window = None
    gc.collect()
```

This will ensure that the tkinter widgets are all deleted in the context of the main-thread and another thread won't accidently run the Garbage Collect

# Contributing to PySimpleGUI

### Open Source License, but Private Development

PySimpleGUI is different than most projects on GitHub.  It is licensed using the "Open Source License" LGPL3.  However, the coding and development of the project is not "open source".

This project does not accept user submitted code.

#### Write Applications, Use PySimpleGUI, Write Tutorials, Teach Others

These are a few of the ways you can directly contribute to PySimpleGUI.  Using the package to make cool stuff and helping others learn how to use it to make cool stuff and a big help to PySimpleGUI.   **Everyone** learns from seeing other people's implementations.  It's through user's creating applications that new problems and needs are discovered.  These have had a profound and positive impact on the project in the past.

#### Pull Requests

Pull requests are *not being accepted* for the project.  This includes sending code changes via other means than "pull requests".  Plainly put, core code you send will not be used.

#### Bug Fixes

If you file an Issue for a bug, have located the bug, and found a fix in 10 lines of code or less.... and you wish to share your fix with the community, then feel free to include it with the filed Issue.  If it's longer than 10 lines and wish to discuss it, then send an email to help@PySimpleGUI.org.

## Thank You

The support from the user community has been amazing.  Your passion for creating PySimpleGUI applications is infectious.  Every "thank you" is noticed and appreciated!  Your passion for wanting to see PySimpleGUI improve is neither ignored nor unappreciated.

It's understood that this way of development of a Python package is unorthodox.  You may find it frustrating and slow, but hope you can respect the decision for it to operate in this manner and be supportive.

## GitHub Repos

If you've created a GitHub for your project that uses PySimpleGUI then please post screenshots in in the "User's Screenshots" Issue on the PySimpleGUI GitHub.  Say a little something about it and I'll also add it to the announcements. People *love* success stories and showing your GUI's screen visually communicates your success. 

## Versions
|Version | Description |
|--|--|
| 1.0.9   | July 10, 2018 - Initial Release |
| 1.0.21 | July 13, 2018 - Readme updates  |
| 2.0.0 | July 16, 2018 - ALL optional parameters renamed from CamelCase to all_lower_case
| 2.1.1 | July 18, 2018 - Global settings exposed, fixes
| 2.2.0| July 20, 2018 - Image Elements, Print output
| 2.3.0 | July 23, 2018 - Changed form.Read return codes, Slider Elements, Listbox element. Renamed some methods but left legacy calls in place for now.
| 2.4.0 | July 24, 2018 - Button images. Fixes so can run on Raspberry Pi
| 2.5.0 | July 26, 2018 - Colors. Listbox scrollbar. tkinter Progress Bar instead of homegrown.
| 2.6.0 | July 27, 2018 - auto_size_button setting.  License changed to LGPL 3+
| 2.7.0 | July 30, 2018 - realtime buttons, window_location default setting
| 2.8.0 | Aug 9, 2018 - New None default option for Checkbox element, text color option for all elements, return values as a dictionary, setting focus, binding return key
| 2.9.0 | Aug 16,2018 - Screen flash fix, `do_not_clear` input field option, `autosize_text` defaults to `True` now, return values as ordered dict, removed text target from progress bar, rework of return values and initial return values, removed legacy Form.Refresh() method (replaced by Form.ReadNonBlockingForm()), COLUMN elements!!, colored text defaults
| 2.10.0 | Aug 25, 2018 - Keyboard & Mouse features (Return individual keys as if buttons, return mouse scroll-wheel as button, bind return-key to button, control over keyboard focus), SaveAs Button, Update & Get methods for InputText, Update for Listbox, Update & Get for Checkbox, Get for Multiline, Color options for Text Element Update, Progess bar Update can change max value, Update for Button to change text & colors, Update for Image Element, Update for Slider, Form level text justification, Turn off default focus, scroll bar for Listboxes, Images can be from filename or from in-RAM, Update for Image).  Fixes - text wrapping in buttons, msg box, removed slider borders entirely and others
| 2.11.0 | Aug 29, 2018 - Lots of little changes that are needed for the demo programs to work. Buttons have their own default element size, fix for Mac default button color, padding support for all elements, option to immediately return if list box gets selected, FilesBrowse button, Canvas Element, Frame Element, Slider resolution option, Form.Refresh method, better text wrapping, 'SystemDefault' look and feel settin
| 2.20.0 | Sept 4, 2018 - Some sizable features this time around of interest to advanced users.  Renaming of the MsgBox functions to Popup. Renaming GetFile, etc, to PopupGetFile. High-level windowing capabilities start with Popup, PopupNoWait/PopupNonblocking, PopupNoButtons, default icon, change_submits option for Listbox/Combobox/Slider/Spin/, New OptionMenu element, updating elements after shown, system defaul color option for progress bars, new button type (Dummy Button) that only closes a window, SCROLLABLE Columns!! (yea, playing in the Big League now), LayoutAndShow function removed, form.Fill - bulk updates to forms, FindElement - find element based on key value (ALL elements have keys now), no longer use grid packing for row elements (a potentially huge change), scrolled text box sizing changed, new look and feel themes (Dark, Dark2, Black, Tan, TanBlue, DarkTanBlue, DarkAmber, DarkBlue, Reds, Green)
| 2.30.0 | Sept 6, 2018 - Calendar Chooser (button), borderless windows, load/save form to disk
| 3.0.0 | Sept 7, 2018 - The "fix for poor choice of 2.x numbers" release. Color Chooser (button), "grab anywhere" windows are on by default, disable combo boxes, Input Element text justification (last part needed for 'tables'), Image Element changes to support OpenCV?, PopupGetFile and PopupGetFolder have better no_window option
| 3.01.01 | Sept 10, 2018 - Menus! (sort of a big deal)
| 3.01.02 | Step 11, 2018 - All Element.Update functions have a `disabled` parameter so they can be disabled.  Renamed some parameters in Update function (sorry if I broke your code), fix for bug in Image.Update. Wasn't setting size correctly, changed grab_anywhere logic again,added grab anywhere option to PupupGetText (assumes disabled)
| 3.02.00 | Sept 14, 2018 - New Table Element (Beta release), MsgBox removed entirely, font setting for InputText Element, **packing change** risky change that allows some Elements to be resized,removed command parameter from Menu Element, new function names for ReadNonBlocking (Finalize, PreRead), change to text element autosizing and wrapping (yet again), lots of parameter additions to Popup functions (colors, etc).
| 3.03.00 | New feature - One Line Progress Meters, new display_row_numbers for Table Element, fixed bug in EasyProgresssMeters (function will soon go away), OneLine and Easy progress meters set to grab anywhere but can be turned off.
| 03,04.00 | Sept 18, 2018 - New features - Graph Element, Frame Element, more settings exposed to Popup calls.  See notes below for more.
| 03.04.01 | Sept 18, 2018 - See release notes
| 03.05.00 | Sept 20, 2018 - See release notes
| 03.05.01 | Sept 22, 2018 - See release notes
| 03.05.02 | Sept 23, 2018 - See release notes
| 03.06.00 | Sept 23, 2018 - Goodbye FlexForm, hello Window
| 03.08.00 | Sept 25, 2018 - Tab and TabGroup Elements\
| 01.00.00 for 2.7 | Sept 25, 2018 - First release for 2.7
| 03.08.04 | Sept 30, 2018 - See release notes
| 03.09.00 | Oct 1, 2018 |
| 2.7 01.01.00 | Oct 1, 2018
| 2.7 01.01.02 | Oct 8, 2018
| 03.09.01 | Oct 8, 2018
| 3.9.3 & 1.1.3 | Oct 11, 2018
| 3.9.4 & 1.1.4 | Oct 16, 2018
| 3.10.1 & 1.2.1 | Oct 20, 2018
| 3.10.3 & 1.2.3 | Oct 23, 2018
| 3.11.0 & 1.11.0 | Oct 28, 2018
| 3.12.0 & 1.12.0 | Oct 28, 2018
| 3.13.0 & 1.13.0 | Oct 29, 2018
| 3.14.0 & 1.14.0 | Nov 2, 2018
| 3.15.0 & 1.15.0 | Nov 20, 2018
| 3.16.0 & 1.16.0 | Nov 26, 2018
| 3.17.0 & 1.17.0 | Dec 1, 2018

## Release Notes
2.3 - Sliders, Listbox's and Image elements (oh my!)

If using Progress Meters, avoid cancelling them when you have another window open.  It could lead to future windows being blank. It's being worked on.

New debug printing capability.  `sg.Print`

2.5 Discovered issue with scroll bar on `Output` elements.  The bar will match size of ROW not the size of the element.  Normally you never notice this due to where on a form the `Output` element goes.

Listboxes are still without scrollwheels. The mouse can drag to see more items.  The mouse scrollwheel will also scroll the list and will `page up` and `page down` keys.

2.7 Is the "feature complete" release. Pretty much all features are done and in the code

2.8 More text color controls.  The caller has more control over things like the focus and what buttons should be clicked when enter key is pressed. Return values as a dictionary! (NICE addition)

2.9 COLUMNS!  This is the biggest feature and had the biggest impact on the code base.  It was a difficult feature to add, but it was worth it.  Can now make even more layouts. Almost any layout is possible with this addition.

.................. insert releases 2.9 to 2.30 .................

3.0 We've come a long way baby!  Time for a major revision bump.  One reason is that the numbers started to confuse people  the latest release was 2.30, but some people read it as 2.3 and thought it went backwards.  I kinda messed up the 2.x series of numbers, so why not start with a clean slate.  A lot has happened anyway so it's well earned.

One change that will set PySimpleGUI apart is the parlor trick of being able to move the window by clicking on it anywhere.  This is turned on by default.  It's not a common way to interact with windows.  Normally you have to move using the titlebar.  Not so with PySimpleGUI.  Now you can drag using any part of the window.  You will want to turn off for windows with sliders.  This feature is enabled in the Window call.

Related to the Grab Anywhere feature is the no_titlebar option, again found in the call to Window.  Your window will be a spiffy, borderless window.  It's a really interesting effect.  Slight problem is that you do not have an icon on the taskbar with these types of windows, so if you don't supply a button to close the window, there's no way to close it other than task manager.

3.0.2 Still making changes to Update methods with many more ahead in the future.  Continue to mess with grab anywhere option.  Needed to disable in more places such as the PopupGetText function.  Any time these is text input on a form, you generally want to turn off the grab anywhere feature.



## 4.28.0 PySimpleGUI 3-Aug-2020



## 4.29.0 PySimpleGUI 25-Aug-2020

Custom titlebar capabilities (several new features required)
Better Alignment
Calendar button works again

* Window.visiblity_changed now refreshes the window 
* Added Column.contents_changed which will update the scrollbar so corrently match the contents
* Separators expand only in 1 direction now
* Added 8 SYMBOLS:
	SYMBOL_SQUARE = '█'
	SYMBOL_CIRCLE = '⚫'
	SYMBOL_CIRCLE_OUTLINE = '◯'
	SYMBOL_UP =    '▲'
	SYMBOL_RIGHT = '►'
	SYMBOL_LEFT =  '◄'
	SYMBOL_DOWN =  '▼'
	SYMBOL_X = '❎'
* New dark themes - dark grey 8, dark grey 9, dark green 9, dark purple 7
* When closing window no longer deletes the tkroot variable and rows but instead set to None


### Upcoming

There will always be overlapping work as the ports will never actually be "complete" as there's always something new that can be built.  However there's a definition for the base functionality for PySimpleGUI.  This is what is being strived for with the current ports that are underway.

The current road ahead is to complete these ports - Qt (very close), Web (pretty close), Wx (not all that close).

PySimpleGUIDroid is in the works....

In addition to the ports there is ongoing work with educators that want to bring PySimpleGUI into their classrooms.  Some projects have already started with teachers.  One effort is to examine a number of books that teach Python to kids and convert the exercises to use PySimpleGUI instead of tkinter or command line.  Another educational effort is in integrating with Circuit Python.  It's unclear exactly how PySimpleGUI will fit into the picture.  A board from Adafruit is arriving soon which should help solidify what's possible.

## Code Condition

    Make it run
    Make it right
    Make it fast

It's a recipe for success if done right.  PySimpleGUI has completed the "Make it run" phase.  It's far from "right" in many ways.  These are being worked on.  The module has historically been particularly poor for PEP8 compliance.  It was a learning exercise that turned into a somewhat complete GUI solution for lightweight problems.

While the internals to PySimpleGUI are a tad sketchy, the public interfaces into the SDK are more strictly defined and comply with PEP8 naming conventions.  A set of "PEP8 Bindings" was released in summar 2019 to ensure the externally facing interfaces all adhere to PEP8 names.

Please log bugs and suggestions **only on the PySimpleGUI GitHub**!  It will only make the code stronger and better in the end, a good thing for us all, right?  Logging them elsewhere doesn't enable the core developer and other PySimpleGUI users to help.  To make matters worse, you may get bad advice from other sites because there are simply not many PySimpleGUI experts, yet.

## Design

A moment about the design-spirit of `PySimpleGUI`.  From the beginning, this package was meant to take advantage of Python's capabilities with the goal of programming ease.

**Single File**
While not the best programming practice, the implementation resulted in a single file solution.  Only one file is needed, PySimpleGUI.py.  You can post this file, email it, and easily import it using one statement.

**Functions as objects**
In Python, functions behave just like object. When you're placing a Text Element into your form, you may be sometimes calling a function and other times declaring an object.  If you use the word Text, then you're getting an object.  If you're using `Txt`, then you're calling a function that returns a `Text` object.

**Lists**
It seemed quite natural to use Python's powerful list constructs when possible.  The form is specified as a series of lists.  Each "row" of the GUI is represented as a list of Elements. 

**Dictionaries**
Want to view your form's results as a dictionary instead of a list... no problem, just use the `key` keyword on your elements.  For complex forms with a lot of values that need to be changed frequently, this is by far the best way of consuming the results.

You can also look up elements using their keys.  This is an excellent way to update elements in reaction to another element.  Call `form.FindElement(key)` to get the Element.

**Named / Optional Parameters**
This is a language feature that is featured **heavily**  in all of the API calls, both functions and classes.  Elements are configured, in-place, by setting one or more optional parameters.  For example, a Text element's color is chosen by setting the optional `text_color` parameter.

**tkinter**
tkinter is the "official" GUI that Python supports.  It runs on Windows, Linux, and Mac.  It was chosen as the first target GUI framework due to its ***ubiquity***.  Nearly all Python installations, with the exception of Ubuntu Linux, come pre-loaded with tkinter.   It is the "simplest" of the GUI frameworks to get up an running (among Qt, WxPython, Kivy, etc).

From the start of the PSG project, tkinter was not meant to be the only underlying GUI framework for PySimpleGUI.  It is merely a starting point.  All journeys begin with one step forward and choosing tkinter was the first of many steps for PySimpleGUI.  Now there are 4 ports up and running - tkinter, WxPython, Qt and Remi (web support)

# Author & Owner

Written and owned by Holypython.com a Python lessons, tutorials and exercises site.
 
This documentation as well as all Watermarkd documentation and code is Copyright 2020, 2021, 2022 by Holypython.com

Send correspondence to watermarkd@holypython.com

## License

GNU Lesser General Public License (LGPL 3) +

## Acknowledgments

There are a number of people that have been key contributors to this project both directly and indirectly.  Paid professional help has been deployed a number of critical times in the project's history.  This happens in the life of software development from time to time.

If you've helped, I sure hope that you feel like you've been properly thanked.  That you have been recognized.  If not, then say something.... drop an email to comments@PySimpleGUI.org. 

## Support

In response to a number of email contacts from individuals and corporations that are using PySimpleGUI that wanted to financially support the project a "Support" Button was added to the GitHub site.  This support button is connected with a PayPal account.  If you wish to help support this currently freely supplied software and free technical support, then follow this link: www.paypal.me/psgui . 

To be clear, this is not a solicitation for your money.  No one is being directly asked to support / contribute.  The project is self-funded and there are ongoing costs just to offer the software (URLs, ReadTheDocs, etc). If you're a corporate user and find that PySimpleGUI is helping you financially, that's awesome.  If you want to help ensure PySimpleGUI has a future, you now have that option to help.  It's likely that at some point the costs will become too high for the project to continue to be free, but until then we'll all enjoy the successes we're having.
