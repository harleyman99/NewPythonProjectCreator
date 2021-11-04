import PySimpleGUI as sg
import os
import sys
import subprocess as sp
font = ("Arial", 16)
newfont = ("Arial", 14)
layout = [[sg.Text('New Project Name: '),sg.Input(font=font, enable_events=True, key='combo')],
          [sg.Button('Mac', font=font), sg.Button('Windows', font=font), sg.Button('Linux', font=font), sg.Exit(font=font)]
          ]

window = sg.Window('New Application Creator', layout, margins=(40, 20))

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

elif event == 'Linux':
         linproject = values['combo']
         path = os.getcwd()
                    
                #print ("The current working directory is %s" % path)

         mypro = linproject
         path = "/home/okorn/Programming/"
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
            window.Close()

            os.chdir(os.path.join(path, mypro))

            f= open(file,"w+")
            window.Close()
else:window.Close()