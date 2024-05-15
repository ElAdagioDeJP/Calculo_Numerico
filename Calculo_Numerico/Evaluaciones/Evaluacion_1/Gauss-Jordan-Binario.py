
import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors

import flet as ft

def main(page: Page):
    page.title = "Matematiqueitor NumericoGauseal"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 600
    page.window_height = 500
    
    def route_change(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text(f"Bienvenidos al Matematiqueitor NumericoGauseal "), bgcolor=colors.SURFACE_VARIANT),
                    ft.Column([
                        ft.Row([
                            ft.Image('c:\\Users\\ElAdagioDeJP\\Pictures\\Trabajos\\Stonks.webp',width=250),
                        ],alignment='center'),
                        ft.Row([
                            ElevatedButton("Traductor Numerico", on_click=lambda _: page.go("/Traductor")),
                            ElevatedButton("Gauss-Jordan", on_click=lambda _: page.go("/Gauss-Jordan"))
                        ],alignment='center')
                    ],alignment='center',height=page.width/3)
                   
                    
                ],horizontal_alignment= ft.alignment.bottom_center
            )
        )
        def valid(e):
            if(txt.value != ''):
                if not(txt.value[-1] in ['0','1','2','3','4','5','6','7','8','9']):
                    txt.value = txt.value[0:-2]
                    txt.update()
                
        txt = ft.TextField(hint_text='Ingrese un Numero',on_change=valid)
        
        desde = ft.Dropdown(options=[
                        ft.dropdown.Option('Hexadecimal')
                        #Agregar mas opciones
                        ],width=150)
        hacia = ft.Dropdown(options=[
                        ft.dropdown.Option('Dec')
                        #Agregar mas opciones
                        ],width=150)
        
        if page.route == "/Traductor":
            page.views.append(
                View(
                    "/Traductor",
                    [
                        AppBar(title=Text("Traductor Numerico"), bgcolor=colors.SURFACE_VARIANT),
                        ft.Column([
                            ft.Row([
                                txt,
                                ElevatedButton("Ejecutar", on_click=lambda _: page.go("/Traductor"))
                            ],alignment='center'),
                            ft.Row([
                                desde,hacia

                            ])
                            
                    ],alignment='center',height=page.width/3)
                        
                    ],
                )
            )
        page.update()
        
        if page.route == "/Gauss-Jordan":
            page.views.append(
                View(
                    "/Gauss-Jordan",
                    [
                        AppBar(title=Text("Gauss-Jordan"), bgcolor=colors.SURFACE_VARIANT),
                        
                    ],
                )
            )
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


flet.app(main)