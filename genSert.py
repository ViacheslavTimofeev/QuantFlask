from docxtpl import DocxTemplate
from docx2pdf import convert
import codecs
from zipfile import ZipFile


def func(username, date1, date2):
    l = username.split("\r\n")
    print(l)
    for person in l:
        doc1 = DocxTemplate("test.docx")
        context1 = {'Name': username.rstrip(), 'Date1': date1, 'Date2': date2}
        doc1.render(context1)
        doc1.save("{}_olympiad.docx".format(username.rstrip()))
        #zipObj = ZipFile('sample.zip', 'w')
        #zipObj.write('{}_olympiad.pdf'.format(username.rstrip()))
       #zipObj.close()
# ФИО, дата начала, дата конца, название олимпиады
