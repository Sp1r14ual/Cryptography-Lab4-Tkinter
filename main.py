from tkinter import *
from tkinter import ttk

import hill2x2


def click_button():
    text_filename = text_entry.get()
    key_filename = key_entry.get()

    text_file = None
    key_file = None

    try:
        if not (".txt" in key_filename or ".txt" in text_filename):
            raise Exception("Incorrect filename")

        text_file = open(text_filename, "r")
        key_file = open(key_filename, "r")

    except Exception as E:
        print(E)
        return

    mode = cryptMode.get()

    key = list(map(int, key_file.read().split()))
    key = [[key[0], key[1]], [key[2], key[3]]]

    string = text_file.read()

    result = hill2x2.start(string, key, mode)

    output_file = open("output.txt", "w")
    output_file.write(result)
    output_file.close()

    return


root = Tk()
root.title("Hill 2x2")
root.geometry("400x400+200+150")

root.resizable(False, False)

text_label = ttk.Label(text="Файл с текстом", font=("Arial", 14))
text_label.pack(pady=10)

text_entry = ttk.Entry(justify=CENTER)
text_entry.pack()

key_label = ttk.Label(text="Ключ", font=("Arial", 14))
key_label.pack(padx=8, pady=10)

key_entry = ttk.Entry(justify=CENTER)
key_entry.pack()

cryptMode = StringVar(value="E")

encodeOption = ttk.Radiobutton(
    text="Закодировать", value="E", variable=cryptMode)
encodeOption.pack(ipady=5)

decodeOption = ttk.Radiobutton(
    text="Декодировать", value="D", variable=cryptMode)
decodeOption.pack()

btn = ttk.Button(text="Пуск", command=click_button)
btn.pack(pady=10)

root.mainloop()
