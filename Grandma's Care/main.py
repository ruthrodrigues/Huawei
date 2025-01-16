import flet as ft #importando e nomeando

def main(page: ft.Page): #função página principal
    page.title = "Grandma's Care"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Configurações da tela
    page.window_width = 375
    page.window_height = 667
    page.window_resizable = False  #impede o redimensionamento

    # Navegação entre as telas
    def navigate_to_idoso(e):
        page.clean() #Limpa a página
        page.add(tela_idoso()) #Adiciona a página
        page.update() #Faz o update

    def navigate_to_responsavel(e):
        page.clean()
        page.add(tela_responsavel())
        page.update()

    def navigate_to_login(e):
        page.clean()
        page.add(tela_login())
        page.update()

    # Tela de Login
    def tela_login(): 
        return ft.Column(
            controls=[ #Controle de página com os stacks de texto, tamanho e etc
                ft.Text(
                    "Como você vai usar o Grandma's Care?",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.ElevatedButton( #Botão
                    text="Idoso",
                    on_click=navigate_to_idoso,
                    bgcolor=ft.Colors.PINK_300,
                    color=ft.Colors.WHITE,
                    width=250,
                    height=50,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12))
                ),
                ft.ElevatedButton(
                    text="Responsável",
                    on_click=navigate_to_responsavel,
                    bgcolor=ft.Colors.PINK_300,
                    color=ft.Colors.WHITE,
                    width=250,
                    height=50,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12))
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )

    # tela do idoso que o GPT fez e fez mal feita (Só pra não ficar sem nada)
    def tela_idoso():
        return ft.Column(
            controls=[
                ft.IconButton(ft.Icons.ARROW_BACK, on_click=navigate_to_login, icon_color=ft.Colors.GREY),
                ft.Text("19 de Dezembro", size=16, weight=ft.FontWeight.NORMAL, color=ft.Colors.GREY),
                ft.Text("Bom dia, Maria!", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_400),
                ft.GridView(
                    max_extent=180, 
                    spacing=10,
                    run_spacing=10,
                    padding=10,

                    controls=[
                        ft.Container(
                            content=ft.Column([
                                ft.Icon(ft.Icons.WARNING, size=32, color=ft.Colors.WHITE),
                                ft.Text("EMERGÊNCIA", size=18, color=ft.Colors.WHITE)
                            ], alignment=ft.MainAxisAlignment.CENTER),
                            bgcolor=ft.Colors.RED_300,
                            alignment=ft.alignment.center,
                            border_radius=12,
                            height=100
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Icon(ft.Icons.CHAT, size=32, color=ft.Colors.WHITE),
                                ft.Text("CONVERSAS", size=18, color=ft.Colors.WHITE)
                            ], alignment=ft.MainAxisAlignment.CENTER),
                            bgcolor=ft.Colors.BLUE_200,
                            alignment=ft.alignment.center,
                            border_radius=12,
                            height=100
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Icon(ft.Icons.NOTE, size=32, color=ft.Colors.WHITE),
                                ft.Text("NOTAS", size=18, color=ft.Colors.WHITE)
                            ], alignment=ft.MainAxisAlignment.CENTER),
                            bgcolor=ft.Colors.ORANGE_200,
                            alignment=ft.alignment.center,
                            border_radius=12,
                            height=100
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Icon(ft.Icons.ALARM, size=32, color=ft.Colors.WHITE),
                                ft.Text("LEMBRETES", size=18, color=ft.Colors.WHITE)
                            ], alignment=ft.MainAxisAlignment.CENTER),
                            bgcolor=ft.Colors.YELLOW_200,
                            alignment=ft.alignment.center,
                            border_radius=12,
                            height=100
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Icon(ft.Icons.FITNESS_CENTER, size=32, color=ft.Colors.WHITE),
                                ft.Text("ATIVIDADES", size=18, color=ft.Colors.WHITE)
                            ], alignment=ft.MainAxisAlignment.CENTER),
                            bgcolor=ft.Colors.GREEN_200,
                            alignment=ft.alignment.center,
                            border_radius=12,
                            height=100
                        ),
                    ],
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
        )

    # Tela do Responsável
    def tela_responsavel():
        return ft.Column(
            expand=True, #Permitir que o widget expanda
            controls=[
                ft.IconButton(ft.Icons.ARROW_BACK, on_click=navigate_to_login, icon_color=ft.Colors.GREY), #botão de voltar
                ft.Container(
                    bgcolor=ft.Colors.PINK_300,
                    width=page.window_width,
                    padding=10,
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.WB_SUNNY_OUTLINED, color=ft.Colors.WHITE),
                            ft.Text("19 de Dezembro", size=14, color=ft.Colors.WHITE),
                            ft.Icon(ft.Icons.CALENDAR_MONTH, color=ft.Colors.WHITE)
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ),
                ft.Container(
                    content=ft.Text(
                        "Bom dia, Maria!",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.WHITE,
                    ),
                    padding=20,
                    bgcolor=ft.Colors.PINK_300,
                    width=page.window_width,
                ),
                ft.Column(
                    controls=[
                        criar_cartao("Como reagir em casos de emergência?", "Consulte o guia abaixo.", ft.Colors.RED_200, ft.Icons.HELP),
                        criar_cartao("Vovó", "Oi querida, tá tudo bem sim", ft.Colors.ORANGE_200, ft.Icons.PERSON_3),
                        ft.Container(
                            content=ft.Text(
                                "Lembretes",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.YELLOW_600
                            ),
                            padding=10
                        ),
                        criar_checklist([
                            "Dar remédio",
                            "Consulta amanhã às 11h",
                            "Fazer mingau de aveia",
                            "Fazer crochê",
                            "Assistir à novela",
                            "Fazer tricô"
                        ])
                    ],
                    spacing=10
                )
            ],
        )

    # funções auxiliares
    def criar_cartao(titulo, subtitulo, cor, icone):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(icone, size=28, color=ft.Colors.RED_700),
                    ft.Column(
                        controls=[
                            ft.Text(titulo, size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_700),
                            ft.Text(subtitulo, size=12, color=ft.Colors.BLACK54),
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            bgcolor=cor,
            padding=10,
            border_radius=12
        )

    def criar_checklist(itens):
        return ft.Column(
            controls=[
                ft.Checkbox(label=item, value=False) for item in itens
            ],
            spacing=5
        )

    page.add(tela_login())

# Inicializar a aplicação
ft.app(target=main)