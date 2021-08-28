import os 
from PyPDF2 import PdfFileMerger, PdfFileReader 


def merge(out_name):
	"""
	merge the pdfs located in a directory
	pdfs must be ordered order such as 
	1.pdf 2.pdf ...
	a.pdf b.pdf ...
	"""
	obj=PdfFileMerger()
	pdfList=[pdf for pdf in os.listdir() if pdf.endswith(".pdf")]
	for fil in pdfList:
		obj.append(PdfFileReader(fil, 'rb')) 
	obj.write(f"{out_name}.pdf") 
    

if __name__=="__main__":
	merge()




