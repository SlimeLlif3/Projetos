import flet as ft
import desktop

def main (page:ft.Page):
    page.window_width = 1920

    def check_window():
        if page.window_width == 1800:
            app = desktop.Frontend()
            ft.app(target=app.main)
        page.update()

    check_window()
ft.app(target=main)






