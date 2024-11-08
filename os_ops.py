import os
import subprocess as sp
paths={
    'notepad':r"C:\Windows\System32\notepad.exe",
    'calculator':r"C:\Windows\System32\calc.exe"

}

def open_camera():
    sp.run('start microsoft.windows.camera:',shell=True)

def open_notepad():
    os.startfile(paths['notepad'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])
