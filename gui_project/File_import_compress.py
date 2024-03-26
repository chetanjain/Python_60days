import PySimpleGUI as psg
import zip_creator

label1 = psg.Text("Select files to compress:")
input1 = psg.Input()
choose_Button1 = psg.FilesBrowse("Choose", key="files")

label2 = psg.Text("Select Destination to store")
input2 = psg.Input()
choose_Button2 = psg.FolderBrowse("Destination path", key="folder")

compress_button = psg.Button("Compress")
output = psg.Text(key="success", text_color="green")

window = psg.Window(title="File to compress", layout=[[label1, input1, choose_Button1],
                                                      [label2, input2, choose_Button2],
                                                      [compress_button, output]])
while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values['files'].split(";")
    folder_path = values['folder']
    zip_creator.make_archive(filepaths, folder_path)
    window["success"].update("Compression Successfully")
window.close()
