import requests
import json
from tkinter import *
import time


def get_user_data(user_name):
    url = f"https://api.github.com/users/{user_name}"

    return requests.get(url).json()


def save_result(value):
    file = open("gitParse.json", "w")
    file.writelines(json.dumps(value))


keys = [
    'company',
    'created_at',
    'email',
    'id',
    'name',
    'url'
]


def get_data():
    userData = get_user_data(txt.get())

    n: dict = {}

    n['timestamp'] = time.time()

    for i in range(len(keys)):
        n[keys[i]] = userData[keys[i]]

    save_result(n)


window = Tk()
window.title("Git Parser by Name")
window.geometry('400x250')
txt = Entry(window, width=20)
txt.grid(column=0, row=0)
btn = Button(window, text="Не нажимать!", command=get_data)
btn.grid(column=1, row=0)
window.mainloop()
