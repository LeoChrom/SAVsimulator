import flet as ft

def main(page: ft.Page):
    page.title = "NavigationBar Example"
    
    # Creo contenitori per ogni sezione
    explore_view = ft.Container(
        content=ft.Column([
            ft.Text("Sezione Explore", size=30, weight="bold"),
            ft.Text("Qui puoi esplorare contenuti..."),
            ft.ElevatedButton("Cerca", icon=ft.icons.SEARCH)
        ]),
        padding=20
    )
    
    commute_view = ft.Container(
        content=ft.Column([
            ft.Text("Sezione Commute", size=30, weight="bold"),
            ft.Text("Pianifica il tuo viaggio..."),
            ft.Row([
                ft.TextField(label="Da"),
                ft.TextField(label="A")
            ]),
            ft.ElevatedButton("Trova percorso", icon=ft.icons.MAP)
        ]),
        padding=20
    )
    
    bookmarks_view = ft.Container(
        content=ft.Column([
            ft.Text("I tuoi Preferiti", size=30, weight="bold"),
            ft.Text("Contenuti salvati..."),
            ft.ListView(
                controls=[
                    ft.ListTile(title=ft.Text("Elemento salvato 1")),
                    ft.ListTile(title=ft.Text("Elemento salvato 2")),
                    ft.ListTile(title=ft.Text("Elemento salvato 3")),
                ],
                expand=True
            )
        ]),
        padding=20
    )
    
    # Contenitore principale che cambierà in base alla selezione
    content_container = ft.Container(content=explore_view)
    
    # Funzione che gestisce il cambio di sezione
    def change_page(e):
        index = e.control.selected_index
        # Cambia il contenuto in base alla selezione
        if index == 0:
            content_container.content = explore_view
        elif index == 1:
            content_container.content = commute_view
        elif index == 2:
            content_container.content = bookmarks_view
        
        # Aggiorna l'interfaccia
        content_container.update()
    
    # Navigation bar con gestore evento on_change
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Preferiti",
            ),
        ],
        selected_index=0,  # Sezione iniziale
        on_change=change_page
    )
    
    # Aggiungi il contenitore principale alla pagina
    page.add(content_container)

ft.app(main)