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


### Single File Example

```python
import Watermarkd as wmd

#Enable GUI & Enjoy
wmd.Spread.single(gui=True)

#Or work without GUI
wmd.Spread.single(img_path=r"c://Users/ABC/Desktop/Anniversary.jpg")

```


### Batch Example

```python
import Watermarkd as wmd

#Enable GUI & Enjoy
wmd.Spread.batch(gui=False)

#Or work without GUI
wmd.Spread.batch(img_folder=r"c://Users/ABC/Desktop/New_Photos")

```


##Parameters


- img_path: Image's Path and Name for Watermarking
- folder_path: For Batch Operation, Folder's Path for Watermarking
- wm_text: Watermark Text 
- wm_trans: Watermark Transparency
- font_size: Watermark Font Size
- output_filename: Watermarked File Name While Saving

