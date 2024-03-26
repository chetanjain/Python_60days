import PySimpleGUI as psg

feet_label = psg.Text("Enter feet")
feet_text = psg.InputText(key='feet')
inches_label = psg.Text("Enter inches")
inches_text = psg.InputText(key='inches')
convert = psg.Button("Convert", key='convert')
results_label = psg.Text(key = "meters_text")
window = psg.Window(title="Convertor", layout=[[feet_label, feet_text],
                                               [inches_label, inches_text],
                                              [convert, results_label]])
while True:

    event, values = window.read()
    print(event, values)
    meters_result = float(values['feet'])*0.3048 + float(values['inches'])*0.0254
    meters_result = str(meters_result) +'m'
    window['meters_text'].update(value=meters_result)
window.close()
