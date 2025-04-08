import flet as ft
import os

def done():
    os.remove("Files")        
def main(page: ft.Page):
    #This is just a comment
    page.add(ft.Text("Hola"), ft.ElevatedButton("Press Here", on_click=done))
    

ft.app(main)
