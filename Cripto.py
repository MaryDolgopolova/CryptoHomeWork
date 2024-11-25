from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

# Создаем функцию для криптовалют.
def update_b_label(event):
    code = base_combobox.get()
    name = currencies.get(code, "Неизвестная криптовалюта")
    b_label.config(text=name)

# Создаем функцию для валюты.
def update_t_label(event):

    code = target_combobox.get()
    name = currencies2.get (code, "Неизвестная валюта")
    t_label.config(text=name)

# Создаем функцию для получения данных. Формируем URL для API CoinGecko. Обрабатываем наш запрос для конвертации курсов.
def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()

    if target_code and base_code:
        try:
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={base_code}&vs_currencies={target_code.lower()}")
            response.raise_for_status()
            data = response.json()

            if target_code.lower()  in data.get (base_code, {}):
                exchange_rate = data[base_code][target_code.lower()]
                base = currencies [base_code]
                target = currencies2 [target_code]
                mb.showinfo("Курс обмена", f"Курс {exchange_rate:.1f} {target} за 1 {base}")
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите необходимую валюту")



# Валюты
currencies2 = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    }
# Крипта
currencies = {
    "bitcoin": "Биткоин",
    "ethereum": "Эзереум",
    "tether": "Тизер",
    "solana": "Солана",
    "litecoin": "Литкоин",
    }

# Создание графического интерфейса
window = Tk()
window.title("Обмен крипты")
window.geometry("300x250")
window.iconbitmap (default="btc-crypto-cryptocurrency-cryptocurrencies-cash-money-bank-payment_95386.ico")

# Создание элементов управления для выбора криптовалюты.
Label(text="Криптовалюта:", font=("Comic Sans MS", 10)).pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=5, pady=5)

# Создание элементов управления для выбора валюты.
Label(text="Валюта:", font=("Comic Sans MS", 10)).pack(padx=10, pady=5)
target_combobox = ttk.Combobox(values=list(currencies2.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=5, pady=5)

# Создание кнопки конвертации курса.
Button(text="Вывести курс", command=exchange).pack(padx=10, pady=10)

window.mainloop()
