import PyPDF2
import os

def extract_all_pages(pdf_path, output_folder, output_template):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Iterate through all pages in the PDF
        for page_number in range(1, len(pdf_reader.pages) + 1):
            # Create a new PDF writer object for each page
            pdf_writer = PyPDF2.PdfWriter()

            # Add the current page to the new PDF
            pdf_writer.add_page(pdf_reader.pages[page_number - 1])

            # Construct the output path for the current page based on the template
            output_path = os.path.join(output_folder, output_template.format(page_number=page_number))

            # Write the new PDF to the output file
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)

            print(f"Page {page_number} extracted successfully to {output_path}")

# Example usage
pdf_path = 'G:\\IDs and Accounts'  # Replace with the path to your PDF file
output_folder = 'G:\\IDs and Accounts'  # Replace with the desired output folder
output_template = 'Page_{page_number}.pdf'  # Define the output path template

extract_all_pages(pdf_path, output_folder, output_template)
