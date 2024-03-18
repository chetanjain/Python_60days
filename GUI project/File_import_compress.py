import PySimpleGUI as psg

label1 = psg.Text("Select files to compress:")
input1 = psg.Input()
choose_Button1 = psg.FilesBrowse("Choose")

label2 = psg.Text("Select Destination to store")
input2 = psg.Input()
choose_Button2 = psg.FolderBrowse("Destination path")

compress_button = psg.Button("Compress")

window = psg.Window(title="File to compress", layout=[[label1, input1, choose_Button1],
                                                      [label2, input2, choose_Button2],
                                                      [compress_button]])

window.read()
window.close()
