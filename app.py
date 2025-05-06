import flet as ft

def main(page: ft.Page):
    page.title = "🧮 Bitwise Calculator"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 450
    page.window.height = 600
    page.window.min_height = 600
    page.window.max_height = 800  # Adjust as needed
    page.window.min_width = 450
    page.window.max_width = 450

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    num1 = ft.TextField(
        label="🔢 Number 1",
        keyboard_type="number",
        width=150,
        text_align=ft.TextAlign.CENTER
    )

    num2 = ft.TextField(
        label="🔢 Number 2 (if needed)",
        keyboard_type="number",
        width=150,
        text_align=ft.TextAlign.CENTER
    )

    operator_dropdown = ft.Dropdown(
        width=150,
        label="🧮 Select Operator",
        options=[
            ft.dropdown.Option("&"),
            ft.dropdown.Option("|"),
            ft.dropdown.Option("^"),
            ft.dropdown.Option("~"),
            ft.dropdown.Option("<<"),
            ft.dropdown.Option(">>"),
        ],
    )

    result = ft.Text(
        "Result will appear here...",
        size=16,
        color="blue",
        text_align=ft.TextAlign.CENTER
    )

    def bin8(n): return format(n & 0xFF, '08b')

    def calculate(e):
        try:
            n1 = int(num1.value)
            n2 = int(num2.value) if num2.value else 0
            op = operator_dropdown.value

            if op is None:
                result.value = "❌ Please select an operator!"
                page.update()
                return

            res = None

            if op == "&":
                res = n1 & n2
            elif op == "|":
                res = n1 | n2
            elif op == "^":
                res = n1 ^ n2
            elif op == "~":
                res = ~n1
            elif op == "<<":
                if n2 < 0 or n2 > 32:
                     result.value = "❌ Invalid shift amount."
                     page.update()
                     return
                res = n1 << n2
            elif op == ">>":
                 if n2 < 0 or n2 > 32:
                     result.value = "❌ Invalid shift amount."
                     page.update()
                     return
                 res = n1 >> n2
            else:
                result.value = "❌ Invalid operator!"
                page.update()
                return

            n1_bin = bin8(n1)

            if op == "~":
                res_bin_display = "".join('1' if bit == '0' else '0' for bit in n1_bin)
                result_text = (
                    f"  {n1_bin}  (Binary for {n1})\n"
                    f"{op}\n"
                    f"-----------\n"
                    f"  {res_bin_display}  (Result = {res})")
            elif op in ["<<", ">>"]:
                 res_bin = format(res, 'b') if res >= 0 else format(res & 0xFFFFFFFFFFFFFFFFFFFFFFFFFF, 'b')
                 result_text = (
                     f"  {n1_bin}  (Binary for {n1})\n"
                     f"{op} {n2}\n"
                     f"-----------\n"
                     f"  {res_bin}  (Result = {res})"
                 )
            else:
                 n1_bin_display = format(n1, 'b') if n1 >= 0 else format(n1 & 0xFFFFFFFFFFFFFFFF, 'b')
                 n2_bin_display = format(n2, 'b') if n2 >= 0 else format(n2 & 0xFFFFFFFFFFFFFFFF, 'b')
                 res_bin_display = format(res, 'b') if res >= 0 else format(res & 0xFFFFFFFFFFFFFFFF, 'b')
                 result_text = (
                     f"  {n1_bin_display}  (Binary for {n1})\n"
                     f"{op} {n2_bin_display}  (Binary for {n2})\n"
                     f"-----------\n"
                     f"  {res_bin_display}  (Result = {res})"
                 )

            result.value = result_text
            page.update()

        except ValueError:
            result.value = "❌ Please enter valid integers."
            page.update()
        except TypeError:
             result.value = "❌ Please select an operator."
             page.update()
        except Exception as e:
             result.value = f"An error occurred: {e}"
             page.update()


    calc_button = ft.ElevatedButton(
        text="✅ Calculate",
        on_click=calculate
    )

    page.add(
        ft.Column([
            ft.Container(
                content=ft.Text("🧠 Bitwise Calculator", size=22, weight="bold", text_align="center"),
                alignment=ft.alignment.center,
                expand=True
            ),
            ft.Row([num1], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([num2], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([operator_dropdown], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([calc_button], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([result], alignment=ft.MainAxisAlignment.CENTER)
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)