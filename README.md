# Watermarkd
Friendly Watermarking Software with GUI option.


[![Watermarkd_logo](https://raw.githubusercontent.com/holypython/Watermarkd/master/HP_logo_h.png)](https://holypython.com)


# Watermarkd User Manual

You can find a couple of simple examples below. You are also welcome to visit this tutorial on holypython.com: [How to Use Watermarkd: A Batch Watermarking Library with GUI](https://holypython.com/watermarkd/)

# Installation

Watermarkd can be installed using this command:

```
pip install watermarkd
```
or
```
pip3 install watermarkd
```

# Dependencies

Watermarkd is built on two Python libraries in addition to several default Python libraries. These are:

1) PIL
2) PySimpleGui

Please make sure these libraries are installed before using Watermarkd. You can also refer to our requirements.txt.

The Python Imaging Library (PIL) is

    Copyright © 1997-2011 by Secret Labs AB
    Copyright © 1995-2011 by Fredrik Lundh

Pillow is the friendly PIL fork. It is

    Copyright © 2010-2020 by Alex Clark and contributors

# Examples

## Single File Example

### With GUI Enabled

```python
import Watermarkd as wmd

#Enable GUI & Enjoy
wmd.Spread.single(gui=True)
```

![Watermarkd_Single_GUI](https://raw.githubusercontent.com/holypython/Watermarkd/master/Watermarkd_Single_GUI.webp)

### Working Without GUI

```python
import Watermarkd as wmd

#Or work without GUI
wmd.Spread.single(img_path=r"c://Users/ABC/Desktop/Anniversary.jpg")
```

* File will be saved to Desktop under name Watermarkd.png by default.

## Batch Example

```python
import Watermarkd as wmd

#Or work without GUI
wmd.Spread.batch(folder_path=r"c://Users/ABC/Desktop/New_Photos")
```

![Watermarkd_Single_GUI](https://raw.githubusercontent.com/holypython/Watermarkd/master/Watermarkd_Batch_GUI.webp)

* Files will be saved to Desktop/watermarkd_/ folder by default.

## Functions

There are currently two functions in Watermarkd module and they both belong to Spread class. They both aim to do a good job spreading out watermark texts nicely on image file(s).

### Spread.single()

single is one of the two current functions, the other being batch. It can be used to watermark a single image file.

It shares most of the same parameters with batch function with the exception of:

-img_path

which is replaced with:

-folder_path

in the batch case.

Default output file name and path are as following:
r"c:/Users/"+user_path+"/Desktop/watermarkd.png"

### Spread.batch()

batch the other function can be used to watermark a folder of images at once. This option can be useful for people who has to deal with watermarking images in large amounts and in high frequency.

Currently batch function is missing the GUI component which should be ready soon.

Default output file name and path are as following:

Output Path: r"c:/Users/"+user_path+"/Desktop/watermarkd_/"

Output File: 1.png, 2.png, 3.png, 4.png and so on.

## Parameters

- gui, (default=False) : Opens graphical user interface when True
- img_path: Image's Path and Name for Watermarking
- folder_path : For Batch Operation, Folder's Path for Watermarking
- wm_text, (default= Watermarkd) : Watermark Text 
- wm_trans, (default= 85) : Watermark Transparency
- font_size, (default= 55) : Watermark Font Size
- font_name, (default= "arial.ttf") : Font Type
- filename, (default="Watermarkd") : Saving File Name
- save_to_path, (default="Desktop/watermarkd_"): Saving Folder Path
- save_to_suffix, (default=".png") : Saving File Type
- output_filename, (default= r"c:/Users/"+user_path+"/Desktop/watermarkd.png") : Watermarked File Name When Saving Single File

# Use Cases

Although watermarking technology existed long before digital technologies (on money, stamps and special documents), its use cases reached astronomical levels with the revolution of digital imaging brought about in the last couple of decades.

Watermarkd aims to help users do watermarking in the most practical sense, without having to open resource heavy Photo Editors. You can probably be done with Watermarking all together via Watermarkd in the time that it takes for a traditional Image Editing Software to load up in most computers.

Through photos, watermarking can be used to:

- Communicate contact information
- Advertise
- Share artist info
- Share owner info
- Imply Confidentiality
- Imply Sensitivity
- Post instructions
- Notify of copyright
etc.

It's expected to be dominantly used by:

- Professional photographers
- Illustrators
- Visual Artists
- Newspapers and Magazines
- Bloggers
- Media agencies
- Businesses in general
- Educational institutions
- Non-profit organizations
- Military & Law Enforcement
- Entrepreneurs

## Known Issues

- Sometimes, current algorithm doesn't spread out the watermark as nicely. This happens in approximately 10-20% of different size and shapes of photos. It can be fixed by improving the algorithm.

- In batch function font size is not calculated dynamically. When a folder has images with very different image resolutions this can cause a problem of very different watermark font sizes.

## Versions
|Version | Description |
|--|--|
| 0.7.0.1 | September 27, 2020 - Initial Release |
| 0.7.0.2 | September 28, 2020 - New Version |
| 0.7.0.3 | September 28, 2020 - New Version: __init__.py fixed |
| 0.7.1.0 | September 29, 2020 - New Version w/ batch GUI: __init__.py fixed, bugs fixed |
| 0.7.1.1 | September 29, 2020 - New Version: code typo fixed |
| 0.7.1.2 | September 29, 2020 - New Version: logo fixed, source code correct description added |
| 0.7.2.0 | October 5, 2020 - New Version: GUI Exit behavior improved |
| 0.7.2.1 | October 5, 2020 - New Version: Correct Version Name |

## Release Notes

0.7.0.1 - Initial release is out.

0.7.0.2 - Added functionality to add folder for batch operations when saving folder doesn't already exist.

0.7.0.3 - Fixed __init__.py files for correct installation.

0.7.1.0 - Added Batch GUI, fixed Cancel button, fixed path conflicts

0.7.2.0 - When GUI is closed without picking any image or folder, instead of giving an error, function is terminated by returning None. This should allow repeat operations in a single session and make usage more convenient and smooth for users.

0.7.2.1 - Version name fixed


### Upcoming Work

~Batch Graphic User Interface (done)~

Add color options for watermarking white color dominant images (soon)

Add Dynamic font_size calculation to batch function. (soon)

Improved algorithm For spreading out watermark text (soon)

A sibling class to the only current class: Spread, potentially named Place that can be used to places a single watermark text on the image. (maybe soon)


# Author & Owner

Written and owned by Holypython.com a Python lessons, tutorials and exercises site. (https://holypython.com)

This documentation as well as all other Watermarkd documentation and code is Copyright 2020, 2021, 2022 by Holypython.com

Send correspondence to watermarkd@holypython.com

## License

Apache-2.0

## Acknowledgments

PySimpleGui and PIL libraries for faciliating and inspiring.

UMICH Professors Dr. Charles Severance & Dr. Paul Resnick, for doing an amazing job teaching Python and their inspirational Computer Science works.

Stack Overflow Co-Founder Jeff Atwood for creating such an amazing platform to learn and share and also for sharing inspiring knowledge on his blog and other platforms.
