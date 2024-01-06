import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a pdf file that contains the data
    about the flatmates such as names, their due amount and
    period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # add icon
        pdf.image("files/house.png", w=30, h=20)

        #Add the title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)

        # insert period lable and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=0, h=40, txt='Period: '+bill.period, border=1, align='C', ln=1)
        # pdf.cell(w=350, h=40, txt='March 2021: ', border=1, ln=1)

        # insert name and due amount of flat mate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=0, h=40, txt=flatmate1.name + '\t' + str(flatmate1.pays(bill, flatmate2)), border=1, align='C', ln=1)
        pdf.cell(w=0, h=40, txt=flatmate2.name + '\t' + str(flatmate2.pays(bill, flatmate1)), border=1, align='C')

        pdf.output(self.filename)

        webbrowser.open(self.filename)
