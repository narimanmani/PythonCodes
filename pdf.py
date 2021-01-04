import PyPDF2

# PDF files manipulation using PyPDF2
# make sure on terminal you run :
#  - > py -3 -m pip install --upgrade pip
#  - > pip3 install PyPDF2

# Rotate PDF
with open("first.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("rotated.pdf", "wb") as output:
        writer.write(output)
        output.close()

# Merge PDF
merger = PyPDF2.PdfFileMerger()
file_names = ["first.pdf", "rotated.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("combined.pdf")