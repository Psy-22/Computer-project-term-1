import PySimpleGUI as psg

psg.theme("Default1")

options = [
"------------------------------------------------------------------",
"Select Here" ,
"Hydrochloric Acid",
"Sulfuric Acid", 
"Nitric Acid", 
"Acetic Acid", 
"Phosphoric Acid", 
"Alanine(amino acid)", 
"Valine(amino acid)",
"glycine(amino acid)", 
"Methane", 
"Ethane",
"Propane", 
"Water", 
"Methanol",
"Copper Sulfate",
"------------------------------------------------------------------"
]

layout = [
    [psg.Text("Please select the compound to show the structure of")],
    [psg.OptionMenu(options, default_value="Select Here", key = "option-selected", size = (38,1))],
    [psg.Button("Select", key = "but", size=(37,1))],
    [psg.Image(source = "imagesofcode\Screenshot 2022-08-11 124328.png")]
]

window = psg.Window("Structure of compounds", layout = layout)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break
    if event == "but":
        if values["option-selected"] == "Hydrochloric Acid":
            x =r"imagesofcode\structurehcl.png"
        elif values["option-selected"] == "Nitric Acid":
            x =r"imagesofcode\structurehno3.png"      
        elif values["option-selected"] == "Sulfuric Acid":
            x =r"imagesofcode\structureh2so4.png"   
        elif values["option-selected"] == "Acetic Acid":
            x =r"imagesofcode\aceticacid.png"   
        elif values["option-selected"] == "Phosphoric Acid":
            x =r"imagesofcode\h3p04structure.png"   
        elif values["option-selected"] == "Alanine(amino acid)":
            x =r"imagesofcode\alanine.png"   
        elif values["option-selected"] == "Valine(amino acid)":
            x =r"imagesofcode\valine.png"   
        elif values["option-selected"] == "glycine(amino acid)":
            x =r"imagesofcode\glycine.png"  
        elif values["option-selected"] == "Methane":
            x =r"imagesofcode\Methane-CH4.png"   
        elif values["option-selected"] == "Ethane":
            x =r"imagesofcode\Ethane-2D-flat.png"   
        elif values["option-selected"] == "Propane":
            x =r"imagesofcode\Propane-2D-flat.png"   
        elif values["option-selected"] == "Water":
            x =r"imagesofcode\wtaer.png"  
        elif values["option-selected"] == "Methanol":
            x =r"imagesofcode\methanol.png"  
        elif values["option-selected"] == "Copper Sulfate":
            x =r"imagesofcode\copper sulfate.png"   
        else:
            x ="error"
    if x != "error":
        psg.popup(title="Structure", image=x)
    else:
        psg.popup("Please select the name of the compound",title = "ERROR SCREEN")


window.close()