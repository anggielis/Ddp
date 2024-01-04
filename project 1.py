import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

class KonversiMataUangAsia:
    def __init__(self, root):
        self.root= root
        self.root.title("Konversi Mata Uang Asia")
        
        #isntallasi objek style dari ttkbootstrap
        self.style = Style()
        
        #menentukan tema dan konfigurasi tambahan
        self.style.theme_use("darkly")
       
        # Variabel String buat entri
        self.nominal_var= tk.StringVar()
        
        # Label dan Entri buat Nominal
        ttk.Label(root, text="Nominal Duit:").grid(row=0, column=0, padx=10, pady=18)
        self.entry_nominal = ttk.Entry(root, textvariable=self.nominal_var)
        self.entry_nominal.grid(row=0, column=1, padx=10, pady=2)
        
        # Dropdown buat Opsi Mata Duit Sumber
        ttk.Label(root, text=" Mata Duit Dini:").grid(row=1, column=0, padx=10, pady=10)
        self.source_currency_var= tk.StringVar()
        self.source_currency_combobox = ttk.Combobox(root, textvariable=self.source_currency_var, values=["IDR", "THB", "MYR", "SGD", "LAK", "PHP", "KHR", "MMK", "BND", "USD(TMR LST)", "VND", "HKD", "JPY", "MNT", "KRW", "KPW", "CNY", "MOP", "TWD", "AFN", "BDT", "BTN", "INR", "MVR", "NPR", "PKR", "LKR", "SAR", "AMD", "AZN", "BHD", "GEL", "IRR", "IQD", "ILS", "KWD", "LBP", "OMR", "QAR", "EUR", "SYP", "TRY", "AED", "YER", "JOD", "KZT", "KGS", "TJS", "TMT", "UZS"])
        self.source_currency_combobox.grid(row=1, column=1, padx=10, pady=10)    
        self.source_currency_combobox.set("IDR")
        
        # Nilai default
        # Dropdown buat Opsi Mata Duit Tujuan
        ttk.Label(root, text="Mata Duit Tujuan:").grid(row=2, column=0, padx=10, pady=10)
        self.target_currency_var = tk.StringVar()
        self.target_currency_combobox = ttk.Combobox(root, textvariable=self.target_currency_var, values=["IDR", "THB", "MYR", "SGD", "LAK", "PHP", "KHR", "MMK", "BND", "USD(TMR LST)", "VND", "HKD", "JPY", "MNT", "KRW", "KPW", "CNY", "MOP", "TWD", "AFN", "BDT", "BTN", "INR", "MVR", "NPR", "PKR", "LKR", "SAR", "AMD", "AZN", "BHD", "GEL", "IRR", "IQD", "ILS", "KWD", "LBP", "OMR", "QAR", "EUR", "SYP", "TRY", "AED", "YER", "JOD", "KZT", "KGS", "TJS", "TMT", "UZS"])
        self.target_currency_combobox.grid( row=2, column=1, padx=10, pady=10)
        self.target_currency_combobox.set("IDR")
        
        # Nilai default
        # Tombol Konversi
        ttk.Button(root, text="Konversi", command=self.konversi).grid(row=3, column=0, columnspan=2, pady=15)
        
        # Label buat Hasil Konversi
        self.result_label= ttk.Label(root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=9)
        
    def konversi(self):
        try:
            nominal= float(self.nominal_var.get())
            mata_uang_sumber= self.source_currency_var.get()
            mata_uang_tujuan= self.target_currency_var.get()
            
            # Kurs Mata Uang( Kalian dapat mengganti nilai- nilai ini cocok kebutuhan)
            
            kurs = {"IDR": 15399,"THB": 34.38, "MYR": 4.595, "SGD": 1.3196, "LAK": 20594.8, "PHP": 55.398, "KHR": 4096.7, "MMK": 2105.9, "BND": 1.3231, "USD(TMR LST)": 1, "VND": 24270, "HKD": 7.8201, "JPY": 141.04, "MNT": 3441, "KRW": 1294.5, "KPW": 900, "CNY": 7.0999, "MOP": 8.0692, "TWD": 30.684, "AFN": 70.64, "BDT": 110.05, "BTN": 83.42, "INR": 83.226, "MVR": 15.4, "NPR": 133.47, "PKR": 278.98, "LKR": 324.8, "SAR": 3.75, "AMD": 404.79, "AZN": 1.7, "BHD": 0.3779, "GEL": 2.6823, "IRR": 42105, "IQD": 1312.7, "ILS": 3.6231, "KWD": 0.3073, "LBP": 15072.2, "OMR": 0.385, "QAR": 3.641, "EUR": 0.9, "SYP": 2511.5, "TRY": 29.477, "AED": 3.6728, "YER": 250.25, "JOD": 0.70960, "KZT": 455.36, "KGS": 89.085, "TJS": 10.9757, "TMT": 3.51, "UZS": 12373.4}
            
            if mata_uang_sumber in kurs and mata_uang_tujuan in kurs:
                hasil_konversi = (nominal * kurs[mata_uang_tujuan])/ kurs[mata_uang_sumber]
                self.result_label.config(text=f"Hasil konversi Mata Duit: {hasil_konversi:.2f} {mata_uang_tujuan}")
            else:
                self.result_label.config(text="Mata duit sumber ataupun tujuan tidak valid.")
            
        except ValueError:
            self.result_label.config(text=" Masukkan nominal yang valid.")

if __name__=="__main__":
    root= tk.Tk()
    app= KonversiMataUangAsia(root)
    root. mainloop()

