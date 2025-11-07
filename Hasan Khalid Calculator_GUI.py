import tkinter as tk

# ===== نافذة البرنامج الأساسية =====
root = tk.Tk()
root.title("آلة حاسبة - Hasan Khalid")
root.geometry("350x500")          # حجم أكبر شوية
root.resizable(False, False)      # قفل تغيير الحجم
root.configure(bg="#f0f0f0")      # لون خلفية قريب من ويندوز

# ===== عنوان أعلى النافذة (زي Standard) =====
title_label = tk.Label(
    root,
    text="Standard",
    font=("Segoe UI", 16, "bold"),
    bg="#f0f0f0",
    anchor="w"
)
title_label.pack(fill="x", padx=15, pady=(10, 0))

# ===== فريم الشاشة =====
display_frame = tk.Frame(root, bg="#f0f0f0")
display_frame.pack(fill="x", padx=10, pady=(5, 10))

# شاشة العرض (زي شاشة الكالكليتور)
entry = tk.Entry(
    display_frame,
    font=("Segoe UI", 26),
    borderwidth=0,
    relief="flat",
    justify="right"
)
entry.pack(fill="x", ipady=15)   # ipady لتكبير ارتفاع الشاشة

# بوردر خفيف حوالين الشاشة
border = tk.Frame(display_frame, bg="#d0d0d0", height=2)
border.pack(fill="x", pady=(3, 0))


# ===== دوال الأزرار =====
def button_click(symbol):
    entry.insert(tk.END, symbol)


def button_equal():
    try:
        # نشيل أي فواصل قبل الحساب
        expression = entry.get().replace(",", "")
        result = eval(expression)

        entry.delete(0, tk.END)

        # كتابة النتيجة بالفواصل
        formatted_result = f"{result:,}"
        entry.insert(tk.END, formatted_result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "خطأ")


def button_clear():
    entry.delete(0, tk.END)


def button_backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])


# ===== التعامل مع الكيبورد =====
def on_key(event):
    k = event.keysym

    # أرقام 0–9
    if k in [str(i) for i in range(10)]:
        button_click(k)

    # النقطة
    elif k in ("period", "KP_Decimal"):
        button_click(".")

    # العمليات
    elif k in ("plus", "KP_Add"):
        button_click("+")
    elif k in ("minus", "KP_Subtract"):
        button_click("-")
    elif k in ("asterisk", "KP_Multiply"):
        button_click("*")
    elif k in ("slash", "KP_Divide"):
        button_click("/")

    # Enter = يساوي
    elif k in ("Return", "KP_Enter"):
        button_equal()

    # Backspace
    elif k == "BackSpace":
        button_backspace()

    # مسح كل الشاشة
    elif k in ("Escape", "c", "C", "Delete"):
        button_clear()


# ===== فريم الأزرار =====
buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.pack(padx=10, pady=10, fill="both")

# نستخدم grid جوه الفريم ده
for i in range(4):
    buttons_frame.columnconfigure(i, weight=1)
for i in range(5):
    buttons_frame.rowconfigure(i, weight=1)

# دالة مساعدة لإنشاء زر بشكل موحّد
def create_button(text, row, col, bg="#ffffff", fg="#000000", command=None):
    btn = tk.Button(
                buttons_frame,
                text=text,
                font=("Segoe UI", 16),
                bg=bg,
                fg=fg,
                activebackground="#dddddd",
                bd=0,
                relief="flat",
                command=command
          )
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5, ipadx=5, ipady=5)
    return btn

# ===== إنشاء الأزرار (أقرب لترتيب ويندوز) =====
create_button("7", 1, 0, command=lambda: button_click("7"))
create_button("8", 1, 1, command=lambda: button_click("8"))
create_button("9", 1, 2, command=lambda: button_click("9"))
create_button("/", 1, 3, bg="#f4f4f4", command=lambda: button_click("/"))

create_button("4", 2, 0, command=lambda: button_click("4"))
create_button("5", 2, 1, command=lambda: button_click("5"))
create_button("6", 2, 2, command=lambda: button_click("6"))
create_button("*", 2, 3, bg="#f4f4f4", command=lambda: button_click("*"))

create_button("1", 3, 0, command=lambda: button_click("1"))
create_button("2", 3, 1, command=lambda: button_click("2"))
create_button("3", 3, 2, command=lambda: button_click("3"))
create_button("-", 3, 3, bg="#f4f4f4", command=lambda: button_click("-"))

create_button("0", 4, 0, command=lambda: button_click("0"))
create_button(".", 4, 1, command=lambda: button_click("."))
create_button("=", 4, 2, bg="#2e8bff", fg="white", command=button_equal)
create_button("+", 4, 3, bg="#f4f4f4", command=lambda: button_click("+"))

# صف زرار C و Backspace زي CE
create_button("C", 0, 0, bg="#ff9999", command=button_clear)
create_button("⌫", 0, 1, bg="#f4f4f4", command=button_backspace)
# خانات فاضية عشان الشكل
create_button("", 0, 2, bg="#f0f0f0", command=None)
create_button("", 0, 3, bg="#f0f0f0", command=None)

# ربط الكيبورد
root.bind("<Key>", on_key)

# تشغيل التطبيق
root.mainloop()
