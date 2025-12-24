import flet as ft


def main(page: ft.Page):
    page.title = "Flet-Droid Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    text_label = ft.Text(value="Press plus or minus!", size=18)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        text_label,
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


if __name__ == "__main__":
    ft.app(main, view=ft.WEB_BROWSER)
