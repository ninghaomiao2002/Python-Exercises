import PyPDF2
def extract_page(pdf_path, page_number, output_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Check if the specified page number is valid
        if 1 <= page_number <= len(pdf_reader.pages):
            # Create a new PDF writer object
            pdf_writer = PyPDF2.PdfWriter()

            # Add the specified page to the new PDF
            pdf_writer.add_page(pdf_reader.pages[page_number - 1])

            # Write the new PDF to the output file
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
            
            print(f"Page {page_number} extracted successfully to {output_path}")
        else:
            print(f"Invalid page number. The PDF has {len(pdf_reader.pages)} pages.")


pdf_path = 'G:\\IDs and Accounts'  
# Replace with the path to your PDF file
output_path = 'G:\\IDs and Accounts'  
# Replace with the desired output path
page_number = 3  
# Replace with the desired page number

extract_page(pdf_path, page_number, output_path)