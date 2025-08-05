import ttkbootstrap
from tkinter import StringVar, Text, END
from translator import DualTranslator

translator = DualTranslator()

def translate():
    src = input_text.get("1.0", END).strip()
    if not src:
        output_var.set("Please enter some text.")
        return

    if mode_var.get() == "EN → FR":
        output = translator.en_to_fr(src)
    else:
        output = translator.fr_to_en(src)

    output_var.set(output)
    
# Initialize window
app = ttkbootstrap.Window(themename="superhero")
app.title("NLPTranslator")
app.geometry("600x400")

# Input
ttkbootstrap.Label(app, text="Input Text:", font=("Segoe UI", 12)).pack(pady=5)
input_text = Text(app, height=5, wrap="word")
input_text.pack(padx=10, fill="x")

# Mode toggle
mode_var = StringVar(value="EN → FR")
ttkbootstrap.Frame(app).pack(pady=5)
ttkbootstrap.Radiobutton(app, text="English → French", variable=mode_var, value="EN → FR").pack()
ttkbootstrap.Radiobutton(app, text="French → English", variable=mode_var, value="FR → EN").pack()

# Translate button
ttkbootstrap.Button(app, text="Translate", command=translate, bootstyle="success").pack(pady=10)

# Output
ttkbootstrap.Label(app, text="Translation:", font=("Segoe UI", 12)).pack()
output_var = StringVar()
ttkbootstrap.Label(app, textvariable=output_var, wraplength=550, font=("Segoe UI", 10)).pack(pady=5)

app.mainloop()
