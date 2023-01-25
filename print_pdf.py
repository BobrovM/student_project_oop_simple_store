from fpdf import FPDF


def print_pdf(id_number, name, price):
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    pdf.add_page()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Receipt for item nr.{id_number}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Article name: {name}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Price: {price}", ln=1)

    pdf.output("receipt.pdf")


if __name__ == "__main__":
    print_pdf(99, "Test", 99)
