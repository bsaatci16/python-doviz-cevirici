import tkinter as tk
from tkinter import ttk
import requests

# Your API key from ExchangeRate-API
API_KEY = 'your_api_key'
API_URL = 'https://v6.exchangerate-api.com/v6/{}/latest/{}'

# Function to get conversion rates
def get_conversion_rates(base_currency):
    url = API_URL.format(API_KEY, base_currency)
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data['conversion_rates']
    else:
        return None

# Function to perform conversion
def convert_currency():
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = float(amount_var.get())

    if from_currency == to_currency:
        converted_amount = amount
    else:
        conversion_rates = get_conversion_rates(from_currency)
        if conversion_rates:
            converted_amount = amount * conversion_rates[to_currency]
            result_var.set(f'{converted_amount:.2f} {to_currency}')
        else:
            result_var.set('Error fetching rates')

# Initialize main window
root = tk.Tk()
root.title("Currency Converter - Berkay")

# Dropdown for from_currency
from_currency_var = tk.StringVar(value='USD')
from_currency_label = ttk.Label(root, text="From:")
from_currency_label.grid(column=0, row=0, padx=10, pady=10)
from_currency_dropdown = ttk.Combobox(root, textvariable=from_currency_var, values=['USD', 'EUR', 'CAD', 'BAM', 'TRY'])
from_currency_dropdown.grid(column=1, row=0, padx=10, pady=10)

# Dropdown for to_currency
to_currency_var = tk.StringVar(value='EUR')
to_currency_label = ttk.Label(root, text="To:")
to_currency_label.grid(column=0, row=1, padx=10, pady=10)
to_currency_dropdown = ttk.Combobox(root, textvariable=to_currency_var, values=['USD', 'EUR', 'CAD', 'BAM', 'TRY'])
to_currency_dropdown.grid(column=1, row=1, padx=10, pady=10)

# Entry for amount
amount_var = tk.StringVar()
amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(column=0, row=2, padx=10, pady=10)
amount_entry = ttk.Entry(root, textvariable=amount_var)
amount_entry.grid(column=1, row=2, padx=10, pady=10)

# Label for result
result_var = tk.StringVar()
result_label = ttk.Label(root, text="Converted Amount:")
result_label.grid(column=0, row=3, padx=10, pady=10)
result_display = ttk.Label(root, textvariable=result_var)
result_display.grid(column=1, row=3, padx=10, pady=10)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(column=0, row=4, columnspan=2, pady=10)

root.mainloop()
