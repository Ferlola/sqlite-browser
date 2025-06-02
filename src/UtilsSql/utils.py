from .input_file import OpenDialog


opendialog = OpenDialog()
if opendialog.open_file_dialog:
    filename = opendialog.open_file_dialog()
