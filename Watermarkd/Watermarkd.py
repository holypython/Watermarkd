### Watermarkd Source Code
# -*- coding: utf-8 -*-
"""Created on Thu Sep 28 20:47:59 2020
   @author: Holypython.com"""



from PIL import Image, ImageDraw, ImageFont
import PySimpleGUI as sg
import random
import getpass
import os

sg.theme("DarkTeal2")
layout1 = [[sg.T("")], [sg.Text("Choose an Image:        ",pad=(0,10)), sg.Input(size=(45,2), key="-IN2-" ,change_submits=True), sg.FileBrowse(key="-IN-",pad=(0,10)), sg.T("   "),sg.Button("Preview")],
            [sg.T("")],
            [sg.T("Watermark Text:          "), sg.Multiline(key="-WMTEXT-", size=(30,4), default_text="Watermarkd")],
            [sg.T("")],
            [sg.T("Font Size:                     ", pad=(0,0)), sg.Radio('Normal', "RADIO0", default=True, key="-R100-"), sg.Radio('Small', "RADIO0", default=False, key="-R101-"), sg.Radio('Large', "RADIO0", default=False, key="-R102-"), sg.T("      Value: "), sg.Input(key="-INFONTSIZE-", size=(10,1))],
            [sg.T("Transparency (1-255):    ", pad=(0,20)), sg.Slider(range=(1, 255), orientation='h', size=(35, 20), default_value=85, key="-WMTRANS-")],
            [sg.T("Save As:                       ", pad=(0,10)), sg.Radio('.png', "RADIO1", default=True, key="-R1-"), 
            sg.Radio('.jpg', "RADIO1", default=False, key="-R2-"), sg.Radio('.gif', "RADIO1", default=False, key="-R3-"),
            sg.Radio('.bmp', "RADIO1", default=False, key="-R4-")],
            [sg.T('Save to:                        ', pad=(0,10)), sg.Radio('default (Desktop)', "RADIO2", default=True, key="-R10-"),
            sg.T(' or '), sg.FolderBrowse("Path", key="-IN3-", target=("-IN4-")) , sg.Input(key="-IN4-", size=(35,1))],
            [sg.T('Filename:                   '), sg.Radio('default (Watermarked)', "RADIO3", default=True, key="-R20-"),
            sg.T('  or    '), sg.Input(size=(20,1), key="-IN21-")],
            [sg.T("                                   ",pad=(10,100,100,100)), sg.Button("Submit"), sg.T("  "), sg.Button("Cancel")]]

window1 = sg.Window('Watermarkd', layout1, size=(750,600), margins=(60,25,20,10))


layout2 = [[sg.T("")], [sg.Text("Choose a Folder:        ",pad=(0,10)), sg.Input(size=(45,2), key="-IN2-" ,change_submits=True), sg.FolderBrowse(key="-IN-",pad=(0,10))],
            [sg.T("")],
            [sg.T("Watermark Text:          "), sg.Multiline(key="-WMTEXT-", size=(30,4), default_text="Watermarkd")],
            [sg.T("")],
            [sg.T("Font Size:                     ", pad=(0,0)), sg.Radio('Normal', "RADIO0", default=True, key="-R100-"), sg.Radio('Small', "RADIO0", default=False, key="-R101-"), sg.Radio('Large', "RADIO0", default=False, key="-R102-"), sg.T("      Value: "), sg.Input(key="-INFONTSIZE-", size=(10,1))],
            [sg.T("Transparency (1-255):    ", pad=(0,20)), sg.Slider(range=(1, 255), orientation='h', size=(35, 20), default_value=85, key="-WMTRANS-")],
            [sg.T("Save As:                       ", pad=(0,10)), sg.Radio('.png', "RADIO1", default=True, key="-R1-"), 
            sg.Radio('.jpg', "RADIO1", default=False, key="-R2-"), sg.Radio('.gif', "RADIO1", default=False, key="-R3-"),
            sg.Radio('.bmp', "RADIO1", default=False, key="-R4-")],
            [sg.T('Save to:                        ', pad=(0,10)), sg.Radio('default (Desktop)', "RADIO2", default=True, key="-R10-"),
            sg.T(' or '), sg.FolderBrowse("Path", key="-IN3-", target=("-IN4-")) , sg.Input(key="-IN4-", size=(35,1))],
            [sg.T('Filename:                   '), sg.Radio('default (Watermarked)', "RADIO3", default=True, key="-R20-"),
            sg.T('  or    '), sg.Input(size=(20,1), key="-IN21-")],
            [sg.T("                                   ",pad=(10,100,100,100)), sg.Button("Submit"), sg.T("  "), sg.Button("Cancel")]]

window2= sg.Window('Watermarkd', layout2, size=(750,600), margins=(60,25,20,10))



user_path=getpass.getuser()


class Spread:

    #Event Loop 1
    def gui1():
        while True:
            event, values = window1.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Cancel":
                window1.close()
                break
                
            elif event=="Preview":
                try:
                    img_path=values["-IN2-"]
                    img = Image.open(img_path).convert("RGBA")
                    img.show()
                except Exception:
                    pass
    
            elif event == "Submit":
                img_path=values["-IN2-"]
                wm_text=values["-WMTEXT-"]
                # font_size=int(values["-INFONTSIZE-"])
                wm_trans = int(values["-WMTRANS-"])
                #Open Image & Create Text Layer
                img = Image.open(img_path).convert("RGBA")
                a, b = img.size
            
                #Font Size
                if (values["-INFONTSIZE-"])!="":
                    font_size=int(values["-INFONTSIZE-"])
                elif values["-R100-"]==True:
                    font_size=b//25
                elif values["-R101-"]==True:
                    font_size=b//30
                elif values["-R102-"]==True:
                    font_size=b//20
                else:
                    font_size=30
               #Path to Save
                if (values["-IN4-"])!="":
                    save_to_path=values["-IN4-"]+"/"
                    print(save_to_path)
                elif values["-IN4-"]=="":
                    save_to_path=r"c:/Users/"+user_path+"/Desktop/"
               
                #File Types
                if values["-R1-"] == True:
                    if values["-R10-"]==True:
                        save_to_suffix=".png"
                elif values["-R2-"] == True:
                    if values["-R10-"]==True:
                        save_to_suffix=".jpg"
                elif values["-R3-"] == True:
                    save_to_suffix=".gif"
                elif values["-R4-"] == True:
                    save_to_suffix=".bmp"
                    
                #File Name
                if values["-IN21-"]!="":
                    filename = values["-IN21-"]
                elif values["-R20-"] == True:
                    filename = "Watermarkd"


                output_filename=save_to_path+filename+save_to_suffix
                print(output_filename)
                window1.close()

        return img_path, wm_text, wm_trans, font_size, save_to_path, output_filename


    #Event Loop 2
    def gui2():
        while True:
            event, values = window2.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Cancel":
                window2.close()
                break
            elif event == "Submit":
                folder_path=values["-IN2-"]
                wm_text=values["-WMTEXT-"]
                wm_trans = int(values["-WMTRANS-"])
            
                #Font Size
                if (values["-INFONTSIZE-"])!="":
                    font_size=int(values["-INFONTSIZE-"])
                elif values["-R100-"]==True:
                    font_size=25
                elif values["-R101-"]==True:
                    font_size=30
                elif values["-R102-"]==True:
                    font_size=20
                else:
                    font_size=30
                    
               #Path to Save
                if (values["-IN4-"])!="":
                    save_to_path=values["-IN4-"]
                    print(save_to_path)
                elif values["-IN4-"]=="":
                    save_to_path=r"c:/Users/"+user_path+"/Desktop/Watermarkd_"
               
                #File Types
                if values["-R1-"] == True:
                    if values["-R10-"]==True:
                        save_to_suffix=".png"
                elif values["-R2-"] == True:
                    if values["-R10-"]==True:
                        save_to_suffix=".jpg"
                elif values["-R3-"] == True:
                    save_to_suffix=".gif"
                elif values["-R4-"] == True:
                    save_to_suffix=".bmp"
                    
                #File Name
                if values["-IN21-"]!="":
                    filename = values["-IN21-"]
                elif values["-R20-"] == True:
                    filename = "Watermarkd"


                output_filename=save_to_path+filename+save_to_suffix
                print(output_filename)
                window2.close()
                
        return folder_path, wm_text, wm_trans, font_size, save_to_path, filename, save_to_suffix




    def single(img_path="", gui=False, wm_text="Watermarkd", font_name="arial.ttf", font_size=55, wm_trans=85, a=2000, b=3000, output_filename=r"c:/Users/"+user_path+"/Desktop/watermarkd.png"):

        if gui==False:
            pass
        elif gui==True:
            try:
                img_path, wm_text, wm_trans, font_size, save_to_path, output_filename = Spread.gui1()
            except Exception:
                return None

        #Creating Image Layers
        img = Image.open(img_path).convert("RGBA")
        txt = Image.new('RGBA', img.size, (255,255,255,0))
        a, b = img.size

        #Creating Text
        text = wm_text
        font = ImageFont.truetype(font_name, font_size)
        d = ImageDraw.Draw(txt)

        #Create new path if necessary
        try:
            os.mkdir(save_to_path)
        except OSError:
            pass
        else:
            print ("Successfully created the directory %s " % save_to_path)


        #Positioning Algorithm
        x1=0
        for i in range(15):
            x1+=a*b/13.7

            x=x1%a
            y=x1//a
        
            print (x,y,x1)
            d.text((x, y*0.95), text, fill=(255,255,255, wm_trans), font=font)
    
        
        watermarked = Image.alpha_composite(img, txt)
        watermarked = watermarked.convert("RGB")
        watermarked.save(output_filename)


    def batch(gui=False, folder_path="", wm_text="Watermarkd", font_name="arial.ttf", font_size=55, wm_trans=85, a=2000, b=3000, filename="Watermarkd", save_to_path=r"c:/Users/"+user_path+"/Desktop/watermarkd_", save_to_suffix=".png"):
    
        if gui==False:
            pass
        elif gui==True:
            try:
                folder_path, wm_text, wm_trans, font_size, save_to_path, filename, save_to_suffix = Spread.gui2()   
            except:
                return None
            
        file=os.scandir(folder_path)
        
        try:
            os.mkdir(save_to_path)
        except OSError:
            pass
        else:
            print ("Successfully created the directory %s " % save_to_path)

        c=0
        for i in file:
            if os.path.isfile(i):
                img_path=folder_path+"/"+i.name
        
            img = Image.open(img_path).convert("RGBA")
            txt = Image.new('RGBA', img.size, (255,255,255,0))
            c+=1
            
            a, b = img.size
            
            #Creating Text
            text = wm_text
            font = ImageFont.truetype("arial.ttf", font_size)
        
            d = ImageDraw.Draw(txt)
        
            #Position
            x1=0
            for i in range(20):
                x1+=a*b/13.7
            
                x=x1%a
                y=x1//a
            
                d.text((x, y*0.95), text, fill=(255,255,255, wm_trans), font=font)
                print (x,y,x1,a,b)

        
            watermarked = Image.alpha_composite(img, txt)
            watermarked = watermarked.convert("RGB")
            watermarked.save(save_to_path+"/"+filename+str(c)+save_to_suffix)
