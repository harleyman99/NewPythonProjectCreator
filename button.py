import PySimpleGUI as sg
import os
# Tested Jan 10, 2022 this is the file that is working correctly for this project. 

font = ("Arial", 16)
newfont = ("Arial", 14)
""" layout = [[sg.Text('New Project Name: '),sg.Input(font=font, enable_events=True, key='combo')],
          [sg.Button('Mac', font=font), sg.Button('Windows', font=font), sg.Button('Linux', font=font), sg.Exit(font=font)]
          ] """

#window = sg.Window('New Application Creator', layout, margins=(40, 20))

from sys import platform
if platform == "linux" or platform == "linux2":
    layout = [[sg.Text('New Project Name: '),sg.Input(font=font, enable_events=True, key='combo')],
          [sg.Button('Mac', font=font, visible=False), sg.Button('Windows', font=font, visible=False), sg.Button('Linux', font=font), sg.Exit(font=font)]
          ]
    window = sg.Window('New Application Creator', layout, margins=(40, 20))
elif platform == "darwin":
    layout = [[sg.Text('New Project Name: '),sg.Input(font=font, enable_events=True, key='combo')],
          [sg.Button('Mac', font=font), sg.Button('Windows', font=font, visible=False), sg.Button('Linux', font=font, visible=False), sg.Exit(font=font)]
          ]
    window = sg.Window('New Application Creator', layout, margins=(40, 20))
elif platform == "win32":
    layout = [[sg.Text('New Project Name: '),sg.Input(font=font, enable_events=True, key='combo')],
          [sg.Button('Mac', font=font, visible=False), sg.Button('Windows', font=font), sg.Button('Linux', font=font, visible=False), sg.Exit(font=font)]
          ]
#I need to write the Windows line to only show the Windows button.





while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break

    if event == 'Mac':
     macproject = values['combo']
     Mac()

    elif event == 'Windows':
     winproject = values['combo']
     print('You pushed the Windows button', winproject)
     window.Close()

    elif event == 'Linux':
     linproject = values['combo']
     Linux()
     #print('You pushed the Linux button')


    def Linux():
        path = os.getcwd()
        print ("The current working directory is %s" % path)

        mypro = linproject
        path = "/home/jack/Programming/"
        file = "README.md"
        file2 = 'required.txt'
        file3 = 'dev.txt'

        check_folder = os.path.isdir(path)

        #if not check_folder:

        try:
                os.makedirs(os.path.join(path, mypro))
                os.makedirs(os.path.join(path, mypro, 'required'))
        # os.makedirs(os.path.join(path, mypro))
        except OSError:
                print ("Creation of the directory %s failed" % path)
        else:
                print ("Successfully created the directory %s " % path)

                os.chdir(os.path.join(path, mypro))
                f= open(file,"w+")
                #Now will add the required foles for the project.
                os.chdir(os.path.join(path, mypro, 'required'))
                f = open(file2, "w+")
                f = open(file3, "w+")
        window.Close()

    def Mac():
        path = os.getcwd()
        print ("The current working directory is %s" % path)

        mypro = macproject   #input("New Project Name:")
        path = "/users/jackokorn/python_projects/"
        file = "README.md"
        file2 = 'required.txt'
        file3 = 'dev.txt'

        check_folder = os.path.isdir(path)

        #if not check_folder:

        try:
            os.mkdir(os.path.join(path, mypro))
            os.makedirs(os.path.join(path, mypro, 'required'))
        # os.makedirs(os.path.join(path, mypro))
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)

            os.chdir(os.path.join(path, mypro))

            f= open(file,"w+")

            os.chdir(os.path.join(path, mypro, 'required'))
            f = open(file2, "w+")
            f = open(file3, "w+")
        window.Close()

    def Windows():
        path = os.getcwd()
        # print ("The current working directory is %s" % path)

        mypro = winproject #input("New Project Name:")
        path = "/Programming/"
        file = "README.md"
        file2 = 'required.txt'
        file3 = 'dev.txt'

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
            f = open(file2, "w+")
            f = open(file3, "w+")
        window.Close()