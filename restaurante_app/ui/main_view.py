# ui/main_view.py
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from servicios.restaurante_servicio import RestauranteServicio

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurante App - Sistema de Gestión")
        self.geometry("950x650")
        self.servicio = RestauranteServicio()

        self.cargar_recursos()
        self.construir_interfaz()

    def cargar_recursos(self):
        self.logo_img = None
        logo_path = os.path.join("assets", "logo.png")
        if os.path.exists(logo_path):
            try:
                img = Image.open(logo_path).resize((120, 40))
                self.logo_img = ImageTk.PhotoImage(img)
            except Exception:
                self.logo_img = None

    def construir_interfaz(self):
        header_frame = ttk.Frame(self, padding=10)
        header_frame.pack(fill="x")

        if self.logo_img:
            lbl_logo = ttk.Label(header_frame, image=self.logo_img)
            lbl_logo.pack(side="left", padx=5)

        lbl_titulo = ttk.Label(header_frame, text="Módulo de Gestión de Ventas", font=("Helvetica", 16, "bold"))
        lbl_titulo.pack(side="left", padx=10)

        main_container = ttk.Frame(self, padding=15)
        main_container.pack(fill="both", expand=True)

        form_frame = ttk.LabelFrame(main_container, text=" Registrar Nueva Venta ", padding=10)
        form_frame.pack(fill="x", pady=10)

        ttk.Label(form_frame, text="Cliente / Usuario:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.combo_usuarios = ttk.Combobox(form_frame, state="readonly", width=30)
        self.combo_usuarios.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Producto:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.combo_productos = ttk.Combobox(form_frame, state="readonly", width=30)
        self.combo_productos.grid(row=0, column=3, padx=5, pady=5)

        # Evento vinculado con command=
        btn_registrar = ttk.Button(
            form_frame, 
            text="Registrar Venta", 
            command=self._on_registrar_venta_click
        )
        btn_registrar.grid(row=0, column=4, padx=10, pady=5)

        table_frame = ttk.LabelFrame(main_container, text=" Historial de Ventas Registradas ", padding=10)
        table_frame.pack(fill="both", expand=True, pady=10)

        columnas = ("id_venta", "usuario", "producto", "precio", "fecha")
        self.tree_ventas = ttk.Treeview(table_frame, columns=columnas, show="headings")
        
        self.tree_ventas.heading("id_venta", text="ID Venta")
        self.tree_ventas.heading("usuario", text="Usuario / Cliente")
        self.tree_ventas.heading("producto", text="Producto")
        self.tree_ventas.heading("precio", text="Precio ($)")
        self.tree_ventas.heading("fecha", text="Fecha / Hora")

        self.tree_ventas.column("id_venta", width=120, anchor="center")
        self.tree_ventas.column("usuario", width=220, anchor="w")
        self.tree_ventas.column("producto", width=220, anchor="w")
        self.tree_ventas.column("precio", width=100, anchor="e")
        self.tree_ventas.column("fecha", width=160, anchor="center")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree_ventas.yview)
        self.tree_ventas.configure(yscroll=scrollbar.set)
        
        self.tree_ventas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.actualizar_combos()
        self.actualizar_tabla_ventas()

    def actualizar_combos(self):
        self.usuarios_dict = {f"{u['nombre']} ({u['id']})": u['id'] for u in self.servicio.obtener_usuarios()}
        self.productos_dict = {f"{p['nombre']} - ${p['precio']} ({p['id']})": p['id'] for p in self.servicio.obtener_productos()}

        self.combo_usuarios['values'] = list(self.usuarios_dict.keys())
        self.combo_productos['values'] = list(self.productos_dict.keys())

    def actualizar_tabla_ventas(self):
        for row in self.tree_ventas.get_children():
            self.tree_ventas.delete(row)

        ventas = self.servicio.obtener_ventas()
        for v in ventas:
            self.tree_ventas.insert("", "end", values=(
                v.id_venta,
                v.nombre_usuario,
                v.nombre_producto,
                f"${v.precio:.2f}",
                v.fecha
            ))

    def _on_registrar_venta_click(self):
        usr_sel = self.combo_usuarios.get()
        prod_sel = self.combo_productos.get()

        if not usr_sel or not prod_sel:
            messagebox.showwarning("Atención", "Debe seleccionar un usuario y un producto de las listas.")
            return

        id_usuario = self.usuarios_dict.get(usr_sel)
        id_producto = self.productos_dict.get(prod_sel)

        exito, mensaje = self.servicio.registrar_venta(id_usuario, id_producto)

        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.actualizar_tabla_ventas()
            self.combo_usuarios.set('')
            self.combo_productos.set('')
        else:
            messagebox.showerror("Error", mensaje)
