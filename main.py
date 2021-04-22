import PySimpleGUI as sg

from random import choice


def randomize(text, *texts):
    returned = []
    #print(texts)
    if not texts:
        texts = ""
    else:
        texts = "".join([el for el in texts])
    all_text = (text + texts).split(" ")
    while len(all_text) != 0:
        word = choice(all_text)
        returned.append(word)
        all_text.remove(word)
    return " ".join(returned)



sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout =   [[sg.Text('first text'),sg.Multiline(key="input-1",size=(50,5), tooltip="Mettre le premier texte à cut up ici")],
            [sg.Text('second text'), sg.Multiline(key="input-2", size=(50, 5), tooltip="(optionnel) Mettre le second texte à cut up ici")],
            [sg.Text("resultat: "),sg.Multiline(size=(50,5), key="--RES--")],
            [sg.Button('Cut up'), sg.Button('Cancel')], [sg.Text("by Alexandre W")]]

# Create the Window
window = sg.Window('Window Title',layout, size=(600,600), resizable = True )


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event == "Cut up":
        print(values["input-1"])
        print(values["input-2"])
        print(randomize(values["input-1"],values["input-2"]))
        t = randomize(values["input-1"],values["input-2"])
        window["--RES--"].update(t)


window.close()