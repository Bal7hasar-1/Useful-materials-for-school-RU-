import tkinter as tk
from tkinter import messagebox

def calculate():
    
    result_text.delete("1.0", tk.END)
    
    try:
        
        country = entry_country.get().strip()
        if not country:
            raise ValueError("Введите название страны")
            
        N = int(entry_N.get().replace(" ", ""))
        M = int(entry_M.get().replace(" ", ""))
        D = int(entry_D.get().replace(" ", ""))
        S = int(entry_S.get().replace(" ", ""))
        O = int(entry_O.get().replace(" ", ""))
        
        if N < 0 or M < 0 or D < 0 or S < 0 or O < 0:
            raise ValueError("Числа не могут быть отрицательными")
            
        
        P = D + S + O
        if P == 0:
            raise ValueError("Население не может быть равно нулю")
            
        
        birth_rate = (N / P) * 1000
        death_rate = (M / P) * 1000
        natural_increase = ((N - M) / P) * 1000
        
        child_share = (D / P) * 100
        adult_share = (S / P) * 100
        elderly_share = (O / P) * 100
        
        
        report = (
            f"ОТЧЕТ ДЛЯ СТРАНЫ: {country.upper()}\n"
            f"{'-'*40}\n"
            f"Всего населения (P): {P:,} чел.\n"
            f"Коэффициент рождаемости: {birth_rate:.2f} ‰\n"
            f"Коэффициент смертности: {death_rate:.2f} ‰\n"
            f"Естественный прирост: {natural_increase:.2f} ‰\n"
            f"{'-'*40}\n"
            f"Доля детей (0-14 лет): {child_share:.2f} %\n"
            f"Доля населения (15-64 лет): {adult_share:.2f} %\n"
            f"Доля пожилых (65+ лет): {elderly_share:.2f} %\n"
        )
        
        
        result_text.insert(tk.END, report)
        
    except ValueError as e:
        
        messagebox.showerror("Ошибка ввода", f"Пожалуйста, проверьте данные.\nДетали: {e}")


root = tk.Tk()
root.title("Демографический калькулятор")
root.geometry("450x600")



labels_text = [
    ("Страна:", "entry_country"),
    ("Число родившихся (N):", "entry_N"),
    ("Число умерших за год (M):", "entry_M"),
    ("Дети (0-14 лет):", "entry_D"),
    ("Трудоспособные (15-64 лет):", "entry_S"),
    ("Пожилые (65+ лет):", "entry_O")
]

entries = {}


for label_text, entry_name in labels_text:
    frame = tk.Frame(root)
    frame.pack(fill="x", padx=15, pady=5)
    
    lbl = tk.Label(frame, text=label_text, width=25, anchor="w")
    lbl.pack(side="left")
    
    entry = tk.Entry(frame)
    entry.pack(side="right", expand=True, fill="x")
    entries[entry_name] = entry


entry_country = entries["entry_country"]
entry_N = entries["entry_N"]
entry_M = entries["entry_M"]
entry_D = entries["entry_D"]
entry_S = entries["entry_S"]
entry_O = entries["entry_O"]


btn_calc = tk.Button(root, text="Рассчитать показатели", command=calculate, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_calc.pack(pady=15, padx=15, fill="x")


result_text = tk.Text(root, height=12, font=("Courier", 10))
result_text.pack(pady=5, padx=15, fill="both", expand=True)


root.mainloop()
