# Watermarkd
Friendly Watermarking Software with GUI option.


[![Watermarkd_logo](https://github.com/holypython/holypython2/blob/master/default.png)](https://holypython.com)


# Watermarkd User's Manual


# Installation

Watermarkd can be installed using this command:

```
pip install Watermarkd
or
pip3 install Watermarkd
```

# Dependencies

Watermarkd is built on two Python libraries in addition to several default Python libraries. These are:

1) PIL
2) PySimpleGui

Please make sure these libraries are installed before using Watermarkd. You can also refer to our requirements.txt.

# Examples

## Single File Example

### With GUI Enabled

```python
import Watermarkd as wmd

#Enable GUI & Enjoy
wmd.Spread.single(gui=True)

```
### Working Without GUI

```python
import Watermarkd as wmd

#Or work without GUI
wmd.Spread.single(img_path=r"c://Users/ABC/Desktop/Anniversary.jpg")

```

## Batch Example

```python
import Watermarkd as wmd

#Or work without GUI
wmd.Spread.batch(img_folder=r"c://Users/ABC/Desktop/New_Photos")

```

Note: GUI for Batch Function is in the works.

## Functions

There are currently two useful functions in Watermarkd module and they both belong to Spread class. They both aim to do a good job spreading out watermark texts nicely on image file(s).

### Spread.single()

single is one of the two current functions, the other being batch. It can be used to watermark a single image file.

It shares most of the same parameters with batch function with the exception of:

-img_path

which is replaced with:

-folder_path

in the batch case.

### Spread.batch()

batch the other function can be used to watermark a folder of images at once. This option can be useful for people who has to deal with watermarking images in large amounts and in high frequency.

Currently batch function is missing the GUI component which should be ready soon.

## Parameters

- gui, (default=False) : Opens graphical user interface when True
- img_path: Image's Path and Name for Watermarking
- folder_path : For Batch Operation, Folder's Path for Watermarking
- wm_text, (default= Watermarkd) : Watermark Text 
- wm_trans, (default= 85) : Watermark Transparency
- font_size, (default= 55) : Watermark Font Size
- output_filename, (default= r"c:/Users/"+user_path+"/Desktop/watermarkd.png") : Watermarked File Name While Saving


# Use Cases
Although watermarking technology existed long before digital technologies, it's use cases reached astronomical levels with the revolution of digital imaging brought about in the last couple of decades.

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




## GitHub Repos

If you've created a GitHub for your project that uses PySimpleGUI then please post screenshots in in the "User's Screenshots" Issue on the PySimpleGUI GitHub.  Say a little something about it and I'll also add it to the announcements. People *love* success stories and showing your GUI's screen visually communicates your success. 

## Versions
|Version | Description |
|--|--|
| 0.7.0.1 | September 30, 2020 - Initial Release |


## Release Notes

0.7.0.1 - Initial release is out.


### Upcoming


Graphic User Interface for batch function (soon)

Improved algorithm For spreading out watermark text (maybe soon)

A sibgling class to the only current class: Spread, potentially named Place that can be used to places a single watermark text on the image. (not so soon)


# Author & Owner

Written and owned by Holypython.com a Python lessons, tutorials and exercises site.

This documentation as well as all other Watermarkd documentation and code is Copyright 2020, 2021, 2022 by Holypython.com

Send correspondence to watermarkd@holypython.com

## License

Apache-2.0

## Acknowledgments

PySimpleGui and PIL libraries for faciliating and inspiring.

UMICH Professor Dr. Charles Severance, for his invaluable contribution both as a professor and a CS influencer.


## Support

In response to a number of email contacts from individuals and corporations that are using PySimpleGUI that wanted to financially support the project a "Support" Button was added to the GitHub site.  This support button is connected with a PayPal account.  If you wish to help support this currently freely supplied software and free technical support, then follow this link: www.paypal.me/psgui .
