import flet as ft

class Frontend():

    def main(self,page:ft.Page):
        page.title = "E-commerce"
        page.bgcolor = ft.colors.BLACK
        page.window_width = 1250
        page.window_height = 800
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.scroll = ft.ScrollMode.AUTO

        def change_main_image(e):
            for elem in options.controls:
                if elem == e.control:
                    elem.opacity = 1
                    main_image.src = elem.image_src
                else:
                    elem.opacity = 0.5
            
            main_image.update()
            options.update()
                    
        self.product_images = ft.Container(
            col={"xs":12,"md":6},
            width=400,
            height=640,
            padding=ft.padding.all(40),
            bgcolor=ft.colors.WHITE,
            content=(
                ft.Column(
                    spacing=190, 
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        main_image := ft.Image(
                            src="https://http2.mlstatic.com/D_NQ_NP_2X_854323-MLU71482693117_092023-F.webp",width=300,
                            height=300
                        ),
                        options := ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Container(
                                    width=80,
                                    height=80,
                                    opacity=1,
                                    on_click=change_main_image,
                                    image_src="https://http2.mlstatic.com/D_NQ_NP_2X_854323-MLU71482693117_092023-F.webp"
                                ),
                                ft.Container(
                                    width=80,
                                    height=80,
                                    opacity=0.5,
                                    on_click=change_main_image,
                                    image_src="https://http2.mlstatic.com/D_NQ_NP_2X_942879-MLU71482713005_092023-F.webp"
                                ),
                                ft.Container(
                                    width=80,
                                    height=80,
                                    opacity=0.5,
                                    on_click=change_main_image,
                                    image_src="https://http2.mlstatic.com/D_NQ_NP_2X_766427-MLU71437119022_092023-F.webp"
                                )
                            ]
                        )
                    ]
                )
            )
        )
        self.product_details = ft.Container(
            col={"xs":12,"md":6},
            padding=ft.padding.all(25),
            width=400,
            height=640,
            bgcolor=ft.colors.BLACK87,
            content=(
                ft.Column(
                    controls=[
                        ft.Text(
                            value="CADEIRAS",
                            color=ft.colors.AMBER,
                            size=11,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Text(
                            value="Poltrona Amarela\nModerna",
                            size=30,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Text(
                            value="Sala de estar",
                            color=ft.colors.GREY,
                            size=10,
                            italic=True
                        ),
                        ft.ResponsiveRow(
                            columns=13,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    col={"xs":12, "sm":7},
                                    value="R$ 399",
                                    color=ft.colors.WHITE,
                                    size=24,
                                    weight="bold"
                                ),
                                ft.Row(
                                    col={"xs":12, "sm":6},
                                    wrap=False,
                                    spacing=5,
                                    controls=[
                                        ft.Icon(
                                            size=26,
                                            name=ft.icons.STAR_ROUNDED,
                                            color=ft.colors.AMBER if _ <4 else ft.colors.WHITE
                                        ) for _ in range(5)
                                    ]
                                )
                            ]
                        ),
                        ft.Tabs(
                            selected_index=0,
                            height=150,
                            indicator_color=ft.colors.AMBER,
                            label_color=ft.colors.AMBER,
                            unselected_label_color=ft.colors.GREY,
                            
                            tabs=[
                                ft.Tab(
                                    text="Descrição",
                                    content=ft.Container(
                                        padding=ft.padding.all(10),
                                        content=ft.Text(
                                            value="A poltrona Decorativa Cadeira Reforçada Opala Bege Cor Amarelo Desenho Do Tecido Suede é perfeita para criar um ambiente moderno e aconchegante na sua casa. Com seu design retrô e cor amarela vibrante.",size=13,
                                            color=ft.colors.GREY,
                                        )
                                    )
                                ),
                                ft.Tab(
                                    text="Detalhes",
                                    content=ft.Container(
                                        padding=ft.padding.all(10),
                                        content=(
                                            ft.Text(value="Dimensões: 0.8m de largura, 0.9m de altura e 0.76m de profundidade.\n\nMaterial dos pés: Eucalipto.",size=13,
                                            color=ft.colors.GREY,)
                                        )
                                    )
                                )
                            ]
                        ),
                        ft.ResponsiveRow(
                            columns=12,
                            controls=[
                                ft.Dropdown(
                                    
                                    col=6,
                                    label="Cor",
                                    label_style=ft.TextStyle(color=ft.colors.WHITE,size=16),
                                    border_color=ft.colors.GREY,
                                    border_width=0.5,
                                    options=[
                                        ft.dropdown.Option(text="Amarelo"),
                                        ft.dropdown.Option(text="Vermelho"),
                                        ft.dropdown.Option(text="Azul")
                                    ]
                                ),
                                ft.Dropdown(
                                    col=6,
                                    label="Quantidade",
                                    label_style=ft.TextStyle(color=ft.colors.WHITE,size=16),
                                    border_color=ft.colors.GREY,
                                    border_width=0.5,
                                    options=[
                                        ft.dropdown.Option(text=f"{num} unid.") for num in range(1,9)
                                    ]
                                )
                            ]
                        ),

                        ft.Container(expand=True),

                        ft.ElevatedButton(
                            width=500,
                            text="Adicionar na lista de desejos",
                            style=ft.ButtonStyle(
                                padding=ft.padding.all(20),
                                bgcolor={
                                    ft.MaterialState.DEFAULT:ft.colors.BLACK87,
                                    ft.MaterialState.HOVERED:ft.colors.BLACK12
                                },
                                color={
                                    ft.MaterialState.DEFAULT:ft.colors.WHITE
                                },
                                side={
                                    ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE)
                                }
                            )
                        ),
                        ft.ElevatedButton(
                            width=500,
                            text="Adicionar ao carrinho",
                            style=ft.ButtonStyle(
                                padding=ft.padding.all(20),
                                bgcolor={
                                    ft.MaterialState.DEFAULT:ft.colors.AMBER,
                                    ft.MaterialState.HOVERED:ft.colors.AMBER_600
                                }, color=ft.colors.BLACK87,
                            )
                        )   
                    ]
                )  
            )
        )

        self.layout = ft.Container(
            margin=ft.margin.all(30),
            width=900,
            shadow=ft.BoxShadow(blur_radius=300,color=ft.colors.AMBER_700),
            content=(
                ft.ResponsiveRow(
                    columns=12,
                    spacing=0,
                    run_spacing=0,
                    controls=[
                        self.product_images,
                        self.product_details
                    ]
                )
            )
        )
        page.add(self.layout)


if __name__ == "__main__":
    app = Frontend()
    ft.app(target=app.main)
