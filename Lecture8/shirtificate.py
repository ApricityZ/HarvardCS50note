from fpdf import FPDF
from PIL import Image
class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def header(self):
        self.set_font("helvetica", "B", 20)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        self.ln(20)

    def add_image(self):
        # 获取图像大小
        img = Image.open("shirtificate.png")
        img_size = img.size
        img_width = img_size[0]
        img_height = img_size[1]

        # 计算页面宽度和高度
        page_width = self.w - 2 * self.l_margin
        page_height = self.h - 2 * self.t_margin

        # 计算调整后的图像大小
        if img_width > page_width or img_height > page_height:
            ratio = min(page_width / img_width, page_height / img_height)
            new_width = img_width * ratio
            new_height = img_height * ratio
        else:
            new_width = img_width
            new_height = img_height


        self.set_xy(10, 50)
        # self.set_x(1)
        self.image("shirtificate.png", w=new_width, h=new_height)
        self.set_auto_page_break(False)


    def add_name(self):
        # 计算页面宽度和高度
        page_width = self.w - 2 * self.l_margin
        page_height = self.h - 2 * self.t_margin

        self.set_xy(30,100)
        self.set_font("helvetica")
        self.set_text_color(255,255,255)
        text = f"{self._name} took CS50"
        # weight = self.get_string_width(self.title)
        # self.set_x((210-weight))
        self.cell(0,10, text, 0, align="C")

def main():
    name = input("Input your name: ")
    pdf = PDF(name)
    pdf.add_page()
    pdf.add_image()
    pdf.add_name()
    pdf.output("shirtificate.pdf")


if __name__ == '__main__':
    main()