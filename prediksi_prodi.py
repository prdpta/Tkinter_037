import tkinter as tk
from tkinter import ttk

BG = "#0f172a"        
CARD = "#1e293b"      
BORDER = "#334155"    
TEXT = "#e2e8f0"      
MUTED = "#94a3b8"     
ACCENT = "#3b82f6"    
ACCENT_HOVER = "#2563eb"
ACCENT_PRESSED = "#1d4ed8"
SUCCESS = "#34d399"   
FONT = "Helvetica Neue"


def hasil_prediksi(event=None):
    """Apapun input yang diberikan, hasilnya selalu Teknologi Informasi."""
    label_hasil.config(text="Teknologi Informasi", foreground=SUCCESS)


root = tk.Tk()
root.title("Prediksi Prodi Pilihan")
root.configure(bg=BG)
root.resizable(False, False)

lebar, tinggi = 580, 640
x = (root.winfo_screenwidth() - lebar) // 2
y = (root.winfo_screenheight() - tinggi) // 2
root.geometry(f"{lebar}x{tinggi}+{x}+{y}")

style = ttk.Style()
style.theme_use("clam")

style.configure("TFrame", background=BG)
style.configure("Card.TFrame", background=CARD)

style.configure("Title.TLabel", background=BG, foreground=TEXT,
                font=(FONT, 22, "bold"))
style.configure("Subtitle.TLabel", background=BG, foreground=MUTED,
                font=(FONT, 11))
style.configure("CardTitle.TLabel", background=CARD, foreground=TEXT,
                font=(FONT, 12, "bold"))
style.configure("Mapel.TLabel", background=CARD, foreground=TEXT,
                font=(FONT, 11))
style.configure("Muted.TLabel", background=CARD, foreground=MUTED,
                font=(FONT, 11))
style.configure("Result.TLabel", background=CARD, foreground=MUTED,
                font=(FONT, 22, "bold"))

style.configure("Field.TEntry",
                fieldbackground=BG, foreground=TEXT, insertcolor=TEXT,
                bordercolor=BORDER, lightcolor=BORDER, darkcolor=BORDER,
                padding=6)
style.map("Field.TEntry",
          bordercolor=[("focus", ACCENT)],
          lightcolor=[("focus", ACCENT)],
          darkcolor=[("focus", ACCENT)])

