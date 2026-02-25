import tkinter as tk

number = ""

def fakefind():
    global number
    pochta = input('Введи почту ')
    txt = 'Почта по номеру', number, '-', pochta
    label1 = tk.Label(root, text='Поиск в базе данных Google')
    label2 = tk.Label(root, text='ERROR not finded password code 3')
    label3 = tk.Label(root, text='Подбор паролей. Примерное время ожидания 24 часа')
    label4 = tk.Label(root, text='Пароль найден. Подбор занял 34 часа')
    label5 = tk.Label(root, text='Поиск почты в базе данных')
    label6 = tk.Label(root, text='Готово')
    label7 = tk.Label(root, text=txt)

    label1.pack(pady=20)
    label2.pack(pady=20)
    label3.pack(pady=20)
    label4.pack(pady=20)
    label5.pack(pady=20)
    label6.pack(pady=20)
    label7.pack(pady=20)



def on_submit():
    global number
    number = entry.get()
    print(number)
    fakefind()


root = tk.Tk()
root.title("FakeHack")
root.geometry("520x340")

label = tk.Label(root, text="Введите номер:")
label.pack(pady=(12, 4))

entry = tk.Entry(root, width=24)
entry.pack(pady=4)
entry.focus_set()

button = tk.Button(root, text="Найти", command=on_submit)
button.pack(pady=6)




root.mainloop()
