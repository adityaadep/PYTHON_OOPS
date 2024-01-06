from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("ENter the bill amount: \n"))
period = input("what is the Bill period ? : e.g December 2023 \n")

name1 = input("what is your name ? \n")
days_in_house1= int(input(f"How many days did {name1} stay in the house \n"))

name2 = input("what is the name of other flatmate ? \n")
days_in_house2= int(input(f"How many days did {name2} stay in the house \n"))

the_bill = Bill(amount, "December 2023")
Aditya = Flatmate(name1, days_in_house1)
Ahalya = Flatmate(name2, days_in_house2)

print(f"{name1} Pays", Ahalya.pays(the_bill, Aditya))
print(f"{name2} Pays", Aditya.pays(the_bill, Ahalya))
print("Total : ", Ahalya.pays(the_bill, Aditya)+Aditya.pays(the_bill, Ahalya))

pdf_report = PdfReport("December.pdf")
pdf_report.generate(Aditya, Ahalya, the_bill)