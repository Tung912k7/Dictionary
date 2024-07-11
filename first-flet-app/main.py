import flet as ft

def main(page: ft.Page):
    page.title = "Từ Điển"
    page.window.bgcolor = '#E6E6FA'
    page.bgcolor = '#E6E6FA'

    #Chức năng của nút
    def bacha1(e):
        print("Hello")
    
    
    img = ft.Image(src='anh/bacha.png', fit=ft.ImageFit.NONE)
    button = ft.ElevatedButton("Tìm hiểu thêm", on_click= bacha1)
    row = ft.Row(controls=[img, button], alignment=ft.MainAxisAlignment.CENTER)
    
    bacha = ft.Container(row, bgcolor= '#E6E6FA')

    img1 = ft.Image(src='anh/bachdongnu.png', fit=ft.ImageFit.NONE)
    button = ft.ElevatedButton("Tìm hiểu thêm", on_click= bacha1)
    row1 = ft.Row(controls=[img1, button], alignment=ft.MainAxisAlignment.CENTER)
    
    bachdongnu = ft.Container(row1, bgcolor= '#E6E6FA')
    
    tong = ft.Row(controls = [row, row1], scroll="always", alignment=ft.MainAxisAlignment.CENTER)
    tong1 = ft.Container(tong)
    


    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)

    lv.controls.append(ft.Image(src='anh/home1.png', fit= ft.ImageFit.FIT_WIDTH))

    lv.controls.append(tong1)
    
    
    page.update()
    
    page.add(lv,search)



if __name__ == "__main__":
    ft.app(target=main)



#Active .venv: .venv\Scripts\activate


