import flet as ft

def main (page:ft.Page):
    #Alinha conteúdo da minha page horizontalmente
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #Alinha conteúdo da minha page verticalmente
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #Define a largura mínima do meu programa
    page.window_min_width = 500
    #Define a altura mínima do meu programa
    page.window_min_height = 600
    #Define a cor de fundo do meu programa
    page.bgcolor = ft.colors.BLACK

    image = ft.Container(
        expand=2,
        border_radius=ft.border_radius.vertical(top=20),
        clip_behavior=ft.ClipBehavior.NONE,
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_right,
            end=ft.alignment.top_left,
            colors=[ft.colors.BROWN, ft.colors.SURFACE]

        ),
        content=ft.Image(
            src = "https://static.wikia.nocookie.net/clashofclans/images/9/9b/Barbarian-xx.png/revision/latest/scale-to-width-down/250?cb=20170703143506",
            scale=ft.Scale(scale=2.4),

        )
    )
    info = ft.Container(
        expand=2,
        padding=ft.padding.all(30),
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    
            controls=[
                ft.Text(value="LEVEL 5", color=ft.colors.ORANGE),
                ft.Text(value="Bárbaro",weight=ft.FontWeight.BOLD,size=40, color=ft.colors.BLACK),
                ft.Text(value="Bárbaros são uma excelente opção para as tropas do castelo do clã, pois têm relativamente saúde alta e os danos para o espaço de tropas para habitação individual. Eles são capazes de absorver uma quantidade significativa de dano.", color=ft.colors.GREY, text_align=ft.TextAlign.CENTER)
            ]
        )
    )
    skills = ft.Container(
        expand=1,
        padding=ft.padding.symmetric(horizontal=20),
        bgcolor=ft.colors.ORANGE,
        border_radius=ft.border_radius.vertical(bottom=20),
        content=ft.Row(
            controls=[
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(value="20", color=ft.colors.WHITE, weight=ft.FontWeight.BOLD, size=40),
                        ft.Text(value="Defesa",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD)

                    ]       
                ),
                ft.VerticalDivider(opacity=0.5),
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(value="16", color=ft.colors.WHITE, weight=ft.FontWeight.BOLD, size=40),
                        ft.Text(value="Velocide",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD)
                    ]       
                ),
                ft.VerticalDivider(opacity=0.5),
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(value="150", color=ft.colors.WHITE, weight=ft.FontWeight.BOLD, size=40),
                        ft.Text(value="Dano",color=ft.colors.WHITE,weight=ft.FontWeight.BOLD)

                    ]       
                ),
            ]
        )
    )
    layout = ft.Container(
            width=380,
            height=650,
            clip_behavior=ft.ClipBehavior.NONE,
            shadow=ft.BoxShadow(blur_radius=100,color=ft.colors.BROWN),
            bgcolor=ft.colors.WHITE,
            border_radius=30,
            content=ft.Column(
                spacing=0,
                controls=[
                    image,
                    info,
                    skills

                ]
            )
    )    

    page.add(layout) 

if __name__ == "__main__":
    ft.app(target=main)