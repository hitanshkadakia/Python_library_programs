from fpdf import FPDF

# pip install fpdf

pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=20)
pdf.cell(200,10,txt="happy_coding01",ln=1,align='C')
pdf.cell(200,10,txt="Follow @happy_coding01 to learn python",ln=2,align='C')
pdf.output("happy_coding01.pdf")