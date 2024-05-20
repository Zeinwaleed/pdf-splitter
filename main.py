from pypdf import PdfReader, PdfWriter

# Define the input PDF file and the range of pages to extract
input_pdf = f"{str(input('zile name : '))}.pdf"
start_page = int(input("start at page : "))
end_page = int(input("end at page : "))
output_pdf = f"{str(input('name the file:'))}.pdf"

# Open the input PDF file
reader = PdfReader(input_pdf)

# Create a new PdfWriter object
output = PdfWriter()

# Iterate over the specified range of pages
for i in range(start_page, end_page):
    # Add each page to the writer object
    output.add_page(reader.pages[i])

# Write all the collected pages to a single output PDF file
with open(output_pdf, "wb") as file:
    output.write(file)

print(f"Created: {output_pdf}")
