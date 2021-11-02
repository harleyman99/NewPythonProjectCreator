import PySimpleGUI as sg
import os
import sys
import subprocess as sp
font = ("Arial", 16)
newfont = ("Arial", 14)
layout = [[sg.Input(font=font, enable_events=True, key='combo')],
          [sg.Button('Mac', font=font), sg.Button('Windows', font=font), sg.Button('Linux', font=font), sg.Exit(font=font)]
          ]

window = sg.Window('New Application Creator', layout, margins=(60, 40))

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break

if event == 'Mac':
        macproject = values['combo']  # use the combo key
        path = os.getcwd()
        print ("The current working directory is %s" % path)

        mypro = macproject   #input("New Project Name:")
        path = "/users/jack/python_projects/"
        file = "README.md"

        check_folder = os.path.isdir(path)

        #if not check_folder:

        try:
            os.mkdir(os.path.join(path, mypro))
        # os.makedirs(os.path.join(path, mypro))
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)

            os.chdir(os.path.join(path, mypro))

            f= open(file,"w+")

elif event == 'Windows':
        winproject = values['combo']
        path = os.getcwd()
        # print ("The current working directory is %s" % path)

        mypro = winproject
        path = "/Programming/"
        file = "README.md"

        check_folder = os.path.isdir(path)

    #if not check_folder:

        try:
            os.makedirs(os.path.join(path, mypro))
        # os.makedirs(os.path.join(path, mypro))
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)

            os.chdir(os.path.join(path, mypro))

            f= open(file,"w+")

"""         else event == 'Linux'
        linuxproject = values['combo']
        path = os.getcwd()
            
        print ("The current working directory is %s" % path)

        mypro = linuxproject
        path = "/home/jack/Programming/"
        file = "README.md"

        check_folder = os.path.isdir(path)

                #if not check_folder:

        try:
                os.makedirs(os.path.join(path, mypro))
        # os.makedirs(os.path.join(path, mypro))
        except OSError:
                print ("Creation of the directory %s failed" % path)
        else:
                print ("Successfully created the directory %s " % path)

                os.chdir(os.path.join(path, mypro))

                f= open(file,"w+")
 """
window.Close()