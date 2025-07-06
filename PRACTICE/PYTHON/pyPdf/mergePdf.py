from pypdf import PdfReader , PdfWriter

print("merging start..")

writer = PdfWriter()

pdfs = ["p.pdf" , "p1.pdf" , "p.pdf" , "p1.pdf"]


for file in pdfs:
    reader = PdfReader(file)
    for page in reader.pages:
        writer.add_page(page)
    
with open ("merged.pdf" , "wb") as f:
    writer.write(f)

print("pdf merged successful!")
