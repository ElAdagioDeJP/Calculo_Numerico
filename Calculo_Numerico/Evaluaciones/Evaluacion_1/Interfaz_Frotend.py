import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors

import flet as ft

from SistemasNumericos import SistemasNumericos


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
                            ft.Image('..\\Imagenes\\notstonk.jpg',width=250),
                        ],alignment='center'),
                        ft.Row([
                            ElevatedButton("Traductor Numerico", on_click=lambda _: page.go("/Traductor")),
                            ElevatedButton("Gauss-Jordan", on_click=lambda _: page.go("/Gauss-Jordan"))
                        ],alignment='center')
                    ],alignment='center',height=page.width/3)
                   
                    
                ],horizontal_alignment= ft.alignment.bottom_center
            )
        )
        
        
        def Click(e):
            sn = SistemasNumericos(entrada.value, desde.value, hacia.value)
            salida.value = sn.Resolver()
            page.update()
            
        def Limpiar(e):
            entrada.value = ''
            salida.value = ''
            desde.value = ''
            hacia.value = ''
            tamano_Matriz.value = ''
            num_matriz.value = ''
            page.update()
        
        entrada = ft.TextField(label='Ingrese un Numero')
        salida = ft.TextField(label='Salida',disabled=True)

        desde = ft.Dropdown(options=[
                        ft.dropdown.Option('Hexadecimal'),
                        ft.dropdown.Option('Decimal'),
                        ft.dropdown.Option('Octal'),
                        ft.dropdown.Option('Cuaternario'),
                        ft.dropdown.Option('Terceario'),
                        ft.dropdown.Option('Binario')
                        #Agregar mas opciones
                        ],width=200,hint_text='Hexadecimal',label='De')
        hacia = ft.Dropdown(options=[
                        ft.dropdown.Option('Hexadecimal'),
                        ft.dropdown.Option('Decimal'),
                        ft.dropdown.Option('Octal'),
                        ft.dropdown.Option('Cuaternario'),
                        ft.dropdown.Option('Terceario'),
                        ft.dropdown.Option('Binario')
                        ],width=200,hint_text='Hexadecimal',label='A')
        
        if page.route == "/Traductor":
            page.views.append(
                View(
                    "/Traductor",
                    [
                        AppBar(title=Text("Traductor Numerico"), bgcolor=colors.SURFACE_VARIANT),
                        ft.Column([
                            ft.Row([
                                desde,hacia
                            ],alignment='center'),
                            ft.Row([
                                entrada,salida,
                                ],alignment='center'),
                            ft.Row([
                                ElevatedButton("Ramdon", on_click=lambda _: page.go("/Traductor")),
                                ElevatedButton("Limpiar", on_click=Limpiar),
                                ElevatedButton("Ejecutar", on_click=Click)
                            ],alignment='center'),
                    ],alignment='center',height=page.width/3)
                        
                    ],
                )
            )
        page.update()
        
        tamano_Matriz = ft.Dropdown(options=[
                        ft.dropdown.Option('1x1'),
                        ft.dropdown.Option('2x2'),
                        ft.dropdown.Option('3x3'),
                        ft.dropdown.Option('4x4'),
                        ft.dropdown.Option('5x5'),
                        ft.dropdown.Option('6x6'),
                        ft.dropdown.Option('7x7'),
                        ft.dropdown.Option('8x8'),
                        ft.dropdown.Option('9x9'),
                        ft.dropdown.Option('10x10')
                        #Agregar mas opciones
                        ],width=200,hint_text='2x2',label='Tamaño de la Matriz')
        
        
        num_matriz = ft.TextField(label='',height = 30, width= 30, text_size=10)
        
        
        if page.route == "/Gauss-Jordan":
            page.views.append(
                View(
                    "/Gauss-Jordan",
                    [
                        AppBar(title=Text("Gauss-Jordan"), bgcolor=colors.SURFACE_VARIANT),
                        ft.Column([
                            ft.Row([
                                tamano_Matriz
                            ],alignment='center'),
                            ft.Row([
                                num_matriz
                                ],alignment='center'),
                            ft.Row([
                                ElevatedButton("Ramdon", on_click=lambda _: page.go("/Traductor")),
                                ElevatedButton("Limpiar", on_click=Limpiar),
                                ElevatedButton("Ejecutar", on_click=lambda _: page.go("/Traductor"))
                            ],alignment='center'),
                            
                    ],alignment='center',height=page.width/3)
                        
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