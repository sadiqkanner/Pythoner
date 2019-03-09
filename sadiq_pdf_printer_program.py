import shelve
shelfFile = shelve.open('C:\\Users\sadiq\Desktop\sadiq')  
records = shelfFile['MyRecords']
rec='2'
# k = len(records)
# for i in range(len(records)):
#     x = records[i].split()
#     Recipe_no = x[2]
#     if Recipe_no == rec:
#         print("des",x[7])
#         print("date ",x[5])
#         
#         
#         
# Item_no = x[4]
# date = x[5]
# time = x[6]
# des = x[7]
# rate = x[8]
# qty = x[10]
# total = x[11]
# amount =100

import fpdf as pyfpdf
from fpdf import FPDF, HTMLMixin

class MyFPDF(FPDF, HTMLMixin):
    pass

pdf=MyFPDF()
#First page
#pdf = pyfpdf.FPDF(format='letter')
pdf.add_page()
#set the font
pdf.set_font("Arial", size=10)


#define the html text
html = """<H3 align="center">Printing Records Pen and Paper </H3>"""
html += """<h4>Date : """+str(x[5])+"""</h4> <h4> Invoice No  """+str(i)+""" </h4></div>"""
html += """
<table border="1" align="center" width="100%">
<thead><tr><th width="8%">No</th><th width="15%">Date</th><th width="20%">Time</th><th width="30%">Description</th><th  width="10%">Rate</th><th width="7%">QTY</th><th width="10%">Amount</th></tr></thead>
<tbody>
"""    


for i in range(len(records)):
    x = records[i].split()
    Recipe_no = x[2]

    if Recipe_no == rec:
        html+='<tr><td align="center">' + str(x[4]) +'</td> <td align="center">'+str(x[5])+'</td><td align="center">'+str(x[6])+'</td><td align="center">'+str(x[7])+'</td> <td align="center">'+str(x[8])+'</td> <td align="center">'+str(x[10])+'</td> <td align="center">'+str(x[11])+' </td> </tr>'

html += """</tbody></table>"""

#write the html text to PDF
pdf.write_html(html)
pdf.output('C:\\Users\sadiq\Desktop\ '+str(i)+'.pdf','F')

# import os
# fd = os.startfile('E:\\'+str(i)+'.pdf', 'print')