import flet as ft

def main(page: ft.Page):
    page.title = "SAV simulator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    
    """___Gestione eventi___"""

    # Funzione click inizializza vendite
    def inizializza(e):
        tbPin.value = ""
        page.open(pinDialog)
        page.update()

    def navigaMenu(e):
        index = e.control.selected_index
        if index==0:
            pass
        elif index==1:
            inizializza(e)
        elif index==2:
            pass

        page.update()



    def caricaProdotti(filename,dictProdotti):
        dati=open(filename,"r")
        
        for r in dati:
            r=r.strip()
            p=r.split("|")
            dictProdotti[p[0]]=[p[1],p[2]]

    def venditaProdotti(e):
        # contenitore principale prodotti vuoto
        prodottiContainer = ft.Column(spacing=10)
        
        vendita = ft.Column(
            [
                ft.Container(
                    content=ft.Text("Seleziona prodotto", weight="bold", size=40),
                    alignment=ft.Alignment(0,1),
                    margin=0,
                    padding=0,
                    width=page.width
                ),
                ft.Container(height=20),  # spazio
                prodottiContainer  # contenitore prodotti
            ],
            spacing=0,
        )

        #cambio schermata
        mainContainer.content.clean()
        mainContainer.content=vendita
        page.update()
        
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
                on_click=lambda e, prod=p, prezzo=info[0]: selProdotto(e, prod, prezzo)
            ))
        
        # Aggiungi la riga al contenitore centrato
        prodottiContainer.controls.append(ft.Container(
            content=row,
            alignment=ft.alignment.center,
            expand=True
        ))
        page.update()

    def selProdotto(e, prodotto, prezzo):
        # un prodotto viene selezionato
        snackBar = ft.SnackBar(content=ft.Text(f"Selezionato: {prodotto} - €{prezzo}"))
        page.open(snackBar)
        page.update()
    
    def pinAccessoVendite(e):
        """Funzione per verificare il PIN"""
        if tbPin.value == PIN_VENDITE:
            page.close(pinDialog)
            venditaProdotti(e)
            page.update()
        else:
            tbPin.error_text = "PIN non valido."
            tbPin.value = ""
            page.update()
    
    def loginOperatore(e):
        pass

    """--- Controlli e variabili ---"""

    tbPin = ft.TextField(
        label="Inserisci PIN", 
        password=True, 
        width=300,
        on_submit=pinAccessoVendite,  # tasto invio
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
            ft.ElevatedButton("Conferma", on_click=pinAccessoVendite)
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )
    
    PIN_VENDITE = "0000"
    credito=0.0

    # Start screen
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

    navbar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon="HOME_OUTLINED", selected_icon="HOME_FILLED", label="Start"),
            ft.NavigationBarDestination(icon="SELL", label="Vendite"),
            ft.NavigationBarDestination(icon="BOOKMARK_BORDER", selected_icon="BOOKMARK", label="Explore",),
        ],
        on_change=navigaMenu
    )

    mainContainer= ft.Container(
        content=start
    )

    mainScroll=ft.ListView(
            [mainContainer],
            expand=True
        )



    page.navigation_bar = navbar
    page.add(mainScroll)
    
    # posiziona navbar
    

ft.app(main)