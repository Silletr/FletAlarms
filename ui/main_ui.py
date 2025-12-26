import flet as ft


def main(page: ft.Page):
    page.title = "Flet-Droid Calculator"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.appbar = ft.AppBar(
        title=ft.Text("Flet-Droid Calculator", size=20),
        center_title=True,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
    )

    text_label = ft.Text(value="Your Alarms will be here!", size=18)
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.add(text_label)


if __name__ == "__main__":
    ft.app(main, view=ft.AppView.WEB_BROWSER)
