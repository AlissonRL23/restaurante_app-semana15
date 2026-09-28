# ui/login_view.py
import tkinter as tk
from tkinter import ttk, messagebox

class LoginView(tk.Toplevel):
    def __init__(self, parent, on_login_success):
        super().__init__(parent)
        self.title("Inicio de Sesión")
        self.geometry("300x200")
        self.on_login_success = on_login_success
        
        ttk.Label(self, text="Usuario:").pack(pady=5)
        self.txt_usuario = ttk.Entry(self)
        self.txt_usuario.pack(pady=5)
        
        btn = ttk.Button(self, text="Ingresar", command=self._validar)
        btn.pack(pady=15)

    def _validar(self):
        if self.txt_usuario.get().strip():
            self.on_login_success()
            self.destroy()
        else:
            messagebox.showwarning("Atención", "Ingrese un nombre de usuario.")
