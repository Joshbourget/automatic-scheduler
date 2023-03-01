import PySimpleGUI as sg

d = {}

for i in range(12):
    if i == 0:
        i += 12
    d["{0}AM".format(i)] = input("What are you doing at " + str(i) + "AM? ")

morningLayout = [[sg.Text("12AM: " + d["12AM"] + "\n"), sg.Text("1AM: " + d["1AM"] + "\n"),
sg.Text("2AM: " + d["2AM"] + "\n"), sg.Text("3AM: " + d["3AM"] + "\n"), sg.Text("4AM: " + d["4AM"] + "\n"),
sg.Text("5AM: " + d["5AM"] + "\n"), sg.Text("6AM: " + d["6AM"] + "\n"), sg.Text("7AM: " + d["7AM"] + "\n"),
sg.Text("8AM: " + d["8AM"] + "\n"), sg.Text("9AM: " + d["9AM"] + "\n"), sg.Text("10AM: " + d["10AM"] + "\n"),
sg.Text("11AM: " + d["11AM"] + "\n")]]

morningWindow = sg.Window(title="My Morning Schedule", layout=morningLayout, margins=(100,50)).read()