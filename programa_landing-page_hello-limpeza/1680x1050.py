import flet as ft

def main(page: ft.Page):
    page.title = "Aplicação Responsiva"

    def load_layout():
        # Limpa os controles atuais
        page.controls.clear()

        # Verifica a largura da janela e importa o módulo correspondente
        if page.window_width < 800:
            import desktop  # Importa o módulo para desktop
            desktop.create_layout(page)  # Chama a função para criar o layout desktop
        

        page.update()  # Atualiza a página

    # Inicializa o layout
    load_layout()

    # Adiciona um evento para redimensionar a janela
    page.on_window_resize = lambda e: load_layout()

# Executa a aplicação
ft.app(target=main)
