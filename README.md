# Watermarkd
Friendly Watermarking Software with GUI option.


[![Watermarkd_logo](https://github.com/holypython/holypython2/blob/master/default.png)](https://holypython.com)


# Watermarkd User's Manual


# Jump-Start


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

### Single File Example

#### With GUI Enabled

```python
import Watermarkd as wmd

#Enable GUI & Enjoy
wmd.Spread.single(gui=True)

```
#### Working Without GUI

```python
import Watermarkd as wmd

#Or work without GUI
wmd.Spread.single(img_path=r"c://Users/ABC/Desktop/Anniversary.jpg")

```

### Batch Example

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

