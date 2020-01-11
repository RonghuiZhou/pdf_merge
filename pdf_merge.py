import glob

# Scan current directory for a list of all PDF files
pdf_files=glob.glob("*.pdf")

# print the list of PDF files
print(pdf_files)

# merge pdf

from PyPDF2 import PdfFileReader, PdfFileMerger

result_pdf=PdfFileMerger()

for pdf in pdf_files:
	with open(pdf,'rb') as fp:
		pdf_reader=PdfFileReader(fp)
		if pdf_reader.isEncrypted:
			print(f'neglect encrypted file: {pdf}')
			continue
		result_pdf.append(pdf_reader, import_bookmarks=True)
		
# save file
result_pdf.write('combined.pdf')
result_pdf.close()