import PySimpleGUI as sg
import requests, time, json, os, re


def loadSymbols():
    symbols = json.load(open("symbols.json"))["symbols"]
    return symbols


symbolIndex = 0
symbols = loadSymbols()
url = f"https://api1.binance.com/api/v3/ticker/price?symbol="
data = f"##########: ##########"
textBox = [
    sg.Text(
        data,
        key="-OUTPUT-",
    )
]

layout = [textBox]

# Create the window
window = sg.Window(
    "Ticker",
    layout,
    keep_on_top=True,
    no_titlebar=True,
    grab_anywhere=True,
    return_keyboard_events=True,
    location=(1768, 972),
)


# Create an event loop
counter = 0
symbolCounter = 0

while True:

    # data = f"ADA: {json.loads(requests.get(url).text)['price'].replace('0000','')}"
    if symbolCounter >= 20000:
        symbols = loadSymbols()
        symbolCounter = 0
    else:
        symbolCounter += 1

    event, values = window.read(timeout=0.1)
    if counter >= 1000:
        data = re.sub(
            "0+$",
            "",
            f"{symbols[symbolIndex]}: {json.loads(requests.get(url + symbols[symbolIndex]).text)['price']}",
        )
        counter = 0
    # print(window.CurrentLocation())
    window["-OUTPUT-"](data)
    counter += 1
    if event == "f":
        if symbolIndex >= len(symbols) - 1:
            symbolIndex = 0
            counter = 1000
        else:
            symbolIndex += 1
            counter = 1000

    if event == sg.WIN_CLOSED or event == "q":
        break

window.close()
