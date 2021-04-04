import datetime,tts
import winsound  # exclusively for windows only,
# if you are on any other system you can use 'playsound' or 'simpleaudio' module.
import PySimpleGUI as sg


def set(hour,minute,ampm):
    #alarm_hour = int(input("Set hour: "))
    #alarm_minutes = int(input("Set minutes: "))
    #am_pm = input("am or pm? ")

    alarm_hour = int(hour)
    alarm_minutes = int(minute)
    am_pm = ampm

    x = "Waiting for time"
    tts.say(x)

    # time conversion
    # because datetime module returns time in military form i.e. 24 hrs format
    if am_pm == 'pm':  # to convert pm to military time
        alarm_hour += 12

    elif alarm_hour == 12 and am_pm == 'am':  # to convert 12am to military time
        alarm_hour -= 12

    else:
        pass

    while True:  # infinite loop starts to make the program running until time matches alarm time

        # ringing alarm + execution condition for alarm
        if alarm_hour == datetime.datetime.now().hour and alarm_minutes == datetime.datetime.now().minute:

            print("\nIt's the time!")
            winsound.Beep(1000, 1000)
            break

sg.theme('Dark Amber')

layout = [[sg.Text("Set your Alarm!")],
             [sg.Text("Set Hour"), sg.InputText()],
             [sg.Text("Set Minutes"), sg.InputText()],
             [sg.Text("Is it AM or PM"), sg.InputText()],
             [sg.Button("Set Alarm")],
             [sg.Multiline(" ",key='-alarmn-')]]

window = sg.Window("Alarm Program",layout,resizable=True)

events, values = window.read()

if(events == "Set Alarm"):
    set(values[0],values[1],values[2])
if(events == sg.WIN_CLOSED):
    exit()

