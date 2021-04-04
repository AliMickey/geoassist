import PySimpleGUI as ui  
from languageDetection import langDetection

#Layouts
langLayout = [[ui.Text("Language Detection")],
        #image drop location
        [ui.Listbox(["Slavic", "Nordic/Baltic", "South Asian"], key="-langRegion-", select_mode="multiple", bind_return_key=True, size=(13,3)), ui.Text(size=(200,1), key="-LANGOUTPUT-")],
        [ui.Button("Submit")]
]

objLayout = [[ui.Text("Object Detection")],
        #image drop location
        [ui.Text(size=(200,1), key="-OBJOUTPUT-")],
]

aboutLayout = [[ui.Text("About")],
        [ui.Text("This tool uses various python libraries to analyse the input photo.\nSource available at: github.com/AliMickey/geoguessr-ml", size=(200,1))],
]

mainLayout = [[ui.Button("Language"), ui.Button("Object"), ui.Button("About")], [ui.Column(langLayout, key="-COLLAN-"), ui.Column(objLayout, visible=False, key="-COLOBJ-"), ui.Column(aboutLayout, visible=False, key="-COLABT-")]]

window = ui.Window("Language", mainLayout, size=(1280,720))
currentLayout = "-COLLAN-"

while True:
    event, values = window.read()
    if event == ui.WINDOW_CLOSED or event == "Quit":
        break  
    if event == "Language" and currentLayout != "-COLLAN-":
        window[f"{currentLayout}"].update(visible=False)
        window["-COLLAN-"].update(visible=True)
        currentLayout = "-COLLAN-"
        
    if event == "Object" and currentLayout != "-COLOBJ-":
        window[f"{currentLayout}"].update(visible=False)
        window["-COLOBJ-"].update(visible=True) 
        currentLayout = "-COLOBJ-"

    if event == "About" and currentLayout != "-COLABT-":
        window[f"{currentLayout}"].update(visible=False)
        window["-COLABT-"].update(visible=True) 
        currentLayout = "-COLABT-"

    if event == "Submit":
        matchedCountries = langDetection(window["-langRegion-"].get())
        matchedCountriesString = ' '.join(matchedCountries)
        window["-LANGOUTPUT-"].update("Matched Countries: " + matchedCountriesString)

window.close()