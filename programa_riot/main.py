import flet as ft

class Frontend():
    
    def main(self,page:ft.Page):
        page.window_width = 1300
        page.window_height = 840
        page.window_resizable = False
        page.padding = 0
        page.spacing = 0
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.window_frameless = True
    
        self.wallpaper = ft.Container(
            content=ft.Image(
                src="https://cdn.prod.website-files.com/64cbe27bc220e9bc233e1a66/64d585f7cae9039a86ccb141_F1WTiiUaEAAWl1s.jpg", width=page.window_width, height=page.window_height, fit=ft.ImageFit.COVER
            )
        )
        self.container = ft.Container(
            width=400,
            height=450,
            padding=ft.padding.only(top=70, right=50, left=50,bottom=50),
            bgcolor=ft.colors.WHITE,
            content=ft.Column(
                spacing=15,
                controls=[
                    ft.TextField(
                        border_color=ft.colors.TRANSPARENT,
                        height=45,
                        bgcolor=ft.colors.GREY_100,
                        cursor_color=ft.colors.BLACK,
                        color=ft.colors.BLACK,
                        focused_border_width=2,
                        focused_border_color=ft.colors.BLACK,
                    ),
                    ft.TextField(
                        border_color=ft.colors.TRANSPARENT,
                        height=45,
                        bgcolor=ft.colors.GREY_100,
                        cursor_color=ft.colors.BLACK,
                        color=ft.colors.BLACK,
                        focused_border_width=2,
                        focused_border_color=ft.colors.BLACK,
                        password=True
                    ),
                    ft.Container(
                        padding=ft.padding.only(top=10),
                        content=ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    on_click=True,
                                    url="https://www.facebook.com/",
                                    bgcolor=ft.colors.BLUE_600,
                                    width=93,
                                    height=35,
                                    style= ft.ButtonStyle(
                                        shape={
                                            ft.ControlState.DEFAULT:ft.RoundedRectangleBorder(4)
                                        }
                                    ),
                                    content=ft.Row(
                                        controls=[
                                            ft.Icon(name=ft.icons.FACEBOOK,color=ft.colors.WHITE,size=23)
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    )
                                ),
                                ft.ElevatedButton(
                                    on_click=True,
                                    url="https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue%26pli%3D1%26nlr%3D1&ec=GAlAwAE&hl=en&service=accountsettings&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S-1509082110%3A1727140498896223&ddm=0",
                                    bgcolor=ft.colors.WHITE,
                                    width=93,
                                    height=35,
                                    style= ft.ButtonStyle(
                                        shape={
                                            ft.ControlState.DEFAULT:ft.RoundedRectangleBorder(4)
                                        }
                                    ),
                                    content=ft.Row(
                                        controls=[
                                            ft.Image(src="https://static-00.iconduck.com/assets.00/google-icon-2048x2048-pks9lbdv.png",width=23,height=23)
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    )
                                ),
                                ft.ElevatedButton(
                                    on_click=True,
                                    url="https://account.apple.com/sign-in",
                                    bgcolor=ft.colors.BLACK,
                                    width=93,
                                    height=35,
                                    style= ft.ButtonStyle(
                                        shape={
                                            ft.ControlState.DEFAULT:ft.RoundedRectangleBorder(4)
                                        }
                                    ),
                                    content=ft.Row(
                                        controls=[
                                            ft.Icon(name=ft.icons.APPLE,color=ft.colors.WHITE,size=23)
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    )
                                ),
                            ]
                        )         
                    ),
                    ft.Container(
                        padding=ft.padding.only(left=117,top=70),
                        content=ft.FloatingActionButton(
                            bgcolor=ft.colors.RED_700,
                            width=65,
                            height=60,
                            hover_elevation=0,
                            elevation=0,
                            content=ft.Row(
                                controls=[
                                    ft.Icon(name=ft.icons.ARROW_FORWARD_ROUNDED,color=ft.colors.WHITE,size=31)
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            
                            )          
                        )
                    )
                ]
            )
        )               
        stack = ft.Stack(
            alignment=ft.alignment.center,
            controls=[self.wallpaper, self.container]
        )
        page.add(stack)

if __name__ == "__main__":

    app = Frontend()
    ft.app(target=app.main)