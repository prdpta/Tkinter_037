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

