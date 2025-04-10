import flet as ft

def main(page: ft.Page):
    page.title = "SAV simulator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # VAR
    PIN_VENDITE = "0000"
    credito=0.0
    
    # Funzione per verificare il PIN
    def pinAccesso(e):
        if tbPin.value == PIN_VENDITE:
            page.close(pinDialog)
            page.controls.clear()
            venditaProdotti(e)
            page.update()
        else:
            tbPin.error_text = "PIN non valido."
            tbPin.value = ""
            page.update()
    
    def venditaProdotti(e):
        # contenitore principale vuoto
        prodottiContainer = ft.Column(spacing=10)
        
        vendita = ft.Column(
            [
                ft.Container(
                    content=ft.Text("Seleziona prodotto", weight="bold", size=40),
                    alignment=ft.alignment.center,
                    margin=0,
                    padding=0,
                    width=page.width
                ),
                ft.Container(height=20),  # spazio
                prodottiContainer  # contenitore
            ],
            spacing=0,
            alignment=ft.MainAxisAlignment.CENTER,
        )
        
        page.controls.clear()
        page.add(vendita)
        
        # dizionario prodotti
        prodotti=dict()
        caricaProdotti("prodotti.txt",prodotti)

        """
        prodotti = {
            "Acqua naturale": [1.50, 5],
            "Acqua frizzante": [1.60, 3],
            "Cola": [2.00, 10]
        }
        """
        
        # Crea una riga di prodotti con wrap e allineamento centrale
        row = ft.Row(
            wrap=True, 
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        # Aggiungi i prodotti alla riga
        for p, info in prodotti.items():
            row.controls.append(ft.Container(
                content=ft.Column([
                    ft.Text(value=p, size=16, weight="bold"),
                    ft.Text(f"€{info[0]}", size=14),
                    ft.Text(f"Disponibili: {info[1]}", size=12)
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                height=200,
                width=200,
                bgcolor="indigo100",
                border_radius=10,
                margin=10,
                alignment=ft.alignment.center,
                on_click=lambda e, prod=p, prezzo=info[0]: seleziona_prodotto(e, prod, prezzo)
            ))
        
        # Aggiungi la riga al contenitore centrato
        prodottiContainer.controls.append(ft.Container(
            content=row,
            alignment=ft.alignment.center,
            expand=True
        ))
        page.update()

    def caricaProdotti(filename,dictProdotti):
        dati=open(filename,"r")
        
        for r in dati:
            r=r.strip()
            p=r.split("|")
            dictProdotti[p[0]]=[p[1],p[2]]


    def seleziona_prodotto(e, prodotto, prezzo):
        # Funzione chiamata quando un prodotto viene selezionato
        snackBar = ft.SnackBar(content=ft.Text(f"Selezionato: {prodotto} - €{prezzo}"))
        page.open(snackBar)
        page.update()

    # Funzione click inizializza
    def inizializza(e):
        tbPin.value = ""
        page.open(pinDialog)
        page.update()
    
    # Dialog per l'inserimento del PIN
    tbPin = ft.TextField(
        label="Inserisci PIN", 
        password=True, 
        width=300,
        on_submit=pinAccesso,  # tasto invio
    )
    
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
                        color="WHITE",
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