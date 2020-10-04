from random import randint as r
from fpdf import FPDF
for year in range(7,14):
    for dynasty in ["H","M","Q","S","T","Y"]:
        pdf = FPDF()
        nums = [4,4,5]
        for c,i in enumerate(range(3)):
            pdf.add_page(("960px","540px"))
            print()
            pdf.image("questionPics/" + str(i) + "/" + str(r(0,nums[c]-1))+ ".jpg", x=0, y=0, w=300)
        pdf.output(str(year) + dynasty + ".pdf")