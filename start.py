import os
import sys
import subprocess as sp



def mainmenu():
    print('1. Run on Windows')
    print('2. Run on Mac')
    print('3. Run on Linux')
    print('4. Quit')
    selection=int(input('Enter choice: '))
    
    #Get the users selection.
    if selection == 1:
        Windows()
    elif selection == 2:
        Mac()
    elif selection == 3:
        Linux()
    elif selection == 4:
        exit
    else:
        print('Invalid choice. Enter 1-4')

def Windows():
    path = os.getcwd()
    # print ("The current working directory is %s" % path)

    mypro = input("New Project Name:")
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


    #Open the editor, NixNote and Chrome
    #Send all files to GitHub



    os.system('code .')

def Linux():
    path = os.getcwd()
    print ("The current working directory is %s" % path)

    mypro = input("New Project Name:")
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


    #Open the editor, NixNote and Chrome
    #Send all files to GitHub



    os.system('code .')

def Mac():
        path = os.getcwd()
        print ("The current working directory is %s" % path)

        mypro = input("New Project Name:")
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


        #Open the editor, NixNote and Chrome
        #Send all files to GitHub



            os.system('code .')
          

# main menu
mainmenu()
    

