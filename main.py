import flet as ft

def main(page: ft.Page):
    page.title = "SAV simulator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # PIN per l'inizializzazione vendite
    PIN_VENDITE = "1789"
    
    # Funzione per verificare il PIN
    def pinAccesso(e):
        if tbPin.value == PIN_VENDITE:
            page.close(pinDialog)
            page.update()
        else:
            tbPin.error_text = "PIN non valido."
            tbPin.value = ""
            page.update()
    
    # Funzione per aprire il dialog del PIN
    def inizializza(e):
        tbPin.value = ""
        page.open(pinDialog)
        page.update()
    
    # Dialog per l'inserimento del PIN
    tbPin = ft.TextField(label="Inserisci PIN", password=True, width=300)
    
    pinDialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Verifica PIN"),
        content=ft.Column([
            ft.Text("Inserisci il PIN per continuare:"),
            tbPin,
        ], tight=True, spacing=20, width=300),
        actions=[
            ft.ElevatedButton("Annulla", on_click=lambda e: page.close(pinDialog)),
            ft.ElevatedButton("Conferma", on_click=pinAccesso)
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )
    
    def loginOperatore(e):
        pass

    start = ft.Column(
        [
            ft.Row(
                [ft.Text("Schermata di avvio", weight="bold", size=40)],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.START
            ),
            ft.Container(height=250),  # space
            ft.Row(
                [ft.ElevatedButton(
                    width=500,
                    height=100,
                    on_click=inizializza,
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.BLUE_700,
                        elevation=10,
                    ),
                    content=ft.Text("Inizializza vendite", size=24, weight="bold")
                )],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Container(height=50),
            ft.Row(
                [ft.ElevatedButton(
                    width=500,
                    height=100,
                    on_click=loginOperatore,
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.RED_700,
                        elevation=10,
                        
                    ),
                    content=ft.Text("Login operatore", size=24, weight="bold")
                )],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        spacing=0
    )

    page.add(start)

ft.app(main)