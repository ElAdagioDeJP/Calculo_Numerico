import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors
import random
import flet as ft

from SistemasNumericos import SistemasNumericos

from Gauss_Jordan import Gauss_Jordan


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
                AppBar(title=Text(f"Bienvenidos al Matematiqueitor NumericoGauseal ", size=24), bgcolor=colors.BLUE_200),
                ft.Column([
                ft.Row([
                    ft.Image('..\\Imagenes\\Stonks.webp',width=250),
                ],alignment='center'),
                ft.Row([
                    ElevatedButton("Traductor Numerico", on_click=lambda _: page.go("/Traductor")),
                    ElevatedButton("Gauss-Jordan", on_click=lambda _: page.go("/Gauss-Jordan"))
                ],alignment='center')
                ],alignment='center',height=page.width/3)
               
                
            ],horizontal_alignment= ft.alignment.bottom_center
            )
        )
        
        def Ramdon_sis(e):
            sn = SistemasNumericos(entrada.value, desde.value, hacia.value)
            entrada.value = sn.Ramdom()
            page.update()
            
        def Click(e):
            sn = SistemasNumericos(entrada.value, desde.value, hacia.value)
            salida.value = sn.Resolver()
            page.update()
            
        def Limpiar_sis(e):
            entrada.value = ''
            salida.value = ''
            page.update()
        
        def Limpiar(e):
            tamano_Matriz.value = ''
            for control in Separador:
                if isinstance(control, ft.Row):
                    for txt in control.controls:
                        if isinstance(txt, ft.TextField):
                            txt.value =""
            Matricular.update()
            Separador.clear()
            Matricular.controls = []
            fila_res.controls = []
            page.update()
        
        def Matriz_Random(e):
            for control in Separador:
                if isinstance(control, ft.Row):
                    for txt in control.controls:
                        if isinstance(txt, ft.TextField):
                            txt.value = str(random.randint(1, 9))
            Matricular.update()
            page.update()
        Separador = []
        Matricular = ft.Column([])
        
        def generar_matriz(e):
            Separador.clear()
            Matricular.controls = []
            v = tamano_Matriz.value[:-2]
            v = int(v)
            value = v
            if not value or int(value) <= 0:
                v.value = ""
                return
            n = int(value)
            
            for i in range(n):
                contenedores_filas = []
                for j in range(n+1):
                    txt = ft.TextField(width=50, 
                                color=ft.colors.BLACK,
                                text_align=ft.TextAlign.CENTER,
                                on_change=Validar_Matriz)
                    contenedores_filas.append(txt)
                Separador.append(
                ft.Row(controls=contenedores_filas))
            page.update()
            Matricular.controls = Separador
            page.update()
        
        def Validar_Matriz(e):
            if not(e.control.value == ''):
                if not(e.control.value[-1] in ['0','1','2','3','4','5','6','7','8','9']):
                    e.control.value = e.control.value[0:len(e.control.value) - 1]
                    e.control.update()
        
        def Enviar_Matriz(e):
            datos = []
            for control in Separador:
                if isinstance(control, ft.Row):
                    fila = []
                    for txt in control.controls:
                        if isinstance(txt, ft.TextField):
                            fila.append(float(txt.value))
                    datos.append(fila)
            gj = Gauss_Jordan()
            gj.set_Matriz(datos)
            solucion = gj.gaussJordan()
            for i, value in enumerate(solucion, start=1):
                respuesta_matriz = ft.Text(f"X{i} = {round(value,2)}  ", size=16, color="black",)
                fila_res.controls.append(respuesta_matriz)
            page.update()
            
        
        
        entrada = ft.TextField(label='Ingrese un Numero')
        salida = ft.TextField(label='Salida', disabled=True, color=ft.colors.BLACK)
        
        

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
                        AppBar(title=Text("Traductor Numerico",size=24), bgcolor=colors.BLUE_200),
                        ft.Column([
                            ft.Row([
                                desde,hacia
                            ],alignment='center'),
                            ft.Row([
                                entrada,salida,
                                ],alignment='center'),
                            ft.Row([
                                ElevatedButton("Ramdon", on_click=Ramdon_sis),
                                ElevatedButton("Limpiar", on_click=Limpiar_sis),
                                ElevatedButton("Ejecutar", on_click=Click)
                            ],alignment='center'),
                    ],alignment='center',height=page.width/3)
                        
                    ]
                )
            )
        page.update()
        
        tamano_Matriz = ft.Dropdown(options=[
                        ft.dropdown.Option('2x2'),
                        ft.dropdown.Option('3x3'),
                        ft.dropdown.Option('4x4'),
                        ft.dropdown.Option('5x5'),
                        ft.dropdown.Option('6x6'),
                        ft.dropdown.Option('7x7')
                        #Agregar mas opciones
                        ],width=200,label='Tamaño de la Matriz', on_change=generar_matriz)
        
        
        fila_res = ft.Row(spacing=10, alignment=ft.MainAxisAlignment.CENTER)
        
        if page.route == "/Gauss-Jordan":
            page.views.append(
                View(
                    "/Gauss-Jordan",
                    [
                        AppBar(title=Text("Gauss-Jordan",size=24), bgcolor=colors.BLUE_200),
                        ft.Column([
                            ft.Row([
                                tamano_Matriz
                            ],alignment='center'),
                            ft.Row([
                                Matricular,
                                ],alignment='center'),
                            fila_res,
                            ft.Row([
                                ElevatedButton("Ramdon", on_click=Matriz_Random),
                                ElevatedButton("Limpiar", on_click = Limpiar),
                                ElevatedButton("Ejecutar", on_click=Enviar_Matriz)
                            ],alignment='center'),
                            
                    ],alignment='center')
                        
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