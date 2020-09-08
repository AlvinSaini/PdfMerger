import os 
from PyPDF2 import PdfFileMerger, PdfFileReader 

class PlayWithPdf:	
	@staticmethod
	def merge():
		obj=PdfFileMerger()
		pdfList=[pdf for pdf in os.listdir() if pdf.endswith(".pdf")]
		for fil in pdfList:
			obj.append(PdfFileReader(fil, 'rb')) 
		obj.write("Merged.pdf") 
    

if __name__=="__main__":
	a="/storage/emulated/0/Pdf/"
	os.chdir(input("Enter path of folder where you have pdfs : "))
	PlayWithPdf.merge()




