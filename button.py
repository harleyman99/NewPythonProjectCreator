import PySimpleGUI as sg


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
     print('You pushed button Mac')

    elif event == 'Windows':
     print('You pushed the Windows button')

    elif event == 'Linux':
     print('You pushed the Linux button')

    window.Close()