import shelve
shelfFile = shelve.open('C:\\Users\sadiq\Desktop\sadiq')  
records = shelfFile['MyRecords']
rec= input("Enter Recipe No# for search ")


import fpdf as pyfpdf
from fpdf import FPDF, HTMLMixin

pdf=MyFPDF()
#First page
#pdf = pyfpdf.FPDF(format='letter')
pdf.add_page()
#set the font
pdf.set_font("Arial", size=10)

    #define the html text


for i in range(len(records)):
    x = records[i].split()
    Recipe_no = x[2]
    if Recipe_no == rec:
        html = """<H1 align="center">Printing Records Pen and Paper </H1>
        <h3>Date:"""+str(x[5])+"""</h3>
        <h3> Invoice No: """+str(x[2])+"""</h3>"""
        html += """
        <table border="1" align="center" width="100%">
        <thead><tr><th width="8%">No</th><th width="15%">Date</th><th width="20%">Time</th><th width="30%">Description</th><th  width="10%">Rate</th><th width="7%">QTY</th><th width="10%">Amount</th></tr></thead>
        <tbody>
        """

grand=[]

for i in range(len(records)):
    x = records[i].split()
    Recipe_no = x[2]

    if Recipe_no == rec:
        m = x[11]
        print(m ,"\n ******************")
        tt = int(m)
        grand = grand + [tt]
        html+='<tr><td align="center">' + str(x[4]) +'</td> <td align="center">'+str(x[5])+'</td><td align="center">'+str(x[6])+'</td><td align="center">'+str(x[7])+'</td> <td align="center">'+str(x[8])+'</td> <td align="center">'+str(x[10])+'</td> <td align="center">'+str(x[11])+' </td> </tr>'

html +='<hr/> <tr> <td align="right" colspan="5"> GRAND TOTAL</td>  <td align="center" colspan="2">'+str(sum(grand))+'</td>  </tr>'

html += """</tbody></table>"""

    #write the html text to PDF
pdf.write_html(html)


pdf.output('C:\\Users\sadiq\Desktop\ '+str(rec)+'.pdf','F')

import os

fd = os.startfile('C:\\Users\sadiq\Desktop\ '+str(rec)+'.pdf', 'print')
os.close(fd)
