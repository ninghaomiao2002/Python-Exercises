# Python code to demonstrate PDF compression using PyPDF2 library.
# This code assumes that PyPDF2 is installed and the user provides the input and output file paths.

import PyPDF2

def compress_pdf(input_path, output_path):
    try:
        # Open the existing PDF
        with open(input_path, "rb") as original_file:
            reader = PyPDF2.PdfFileReader(original_file)

            # Create a new PDF writer object
            writer = PyPDF2.PdfFileWriter()

            # Copy content from original to new, this doesn't apply actual compression
            for i in range(reader.getNumPages()):
                writer.addPage(reader.getPage(i))

            # Write the content to a new file
            with open(output_path, "wb") as output_file:
                writer.write(output_file)

        return "PDF compression completed. Output file saved at: " + output_path
    except Exception as e:
        return "An error occurred: " + str(e)

# Example usage:
# compress_pdf("path/to/your/input.pdf", "path/to/your/output.pdf")

# Note: This code does not perform actual compression in terms of reducing file size.
# It simply copies the content to a new file. For real compression, you would need a tool that can modify image quality,
# remove unnecessary metadata, or apply other file size reduction techniques.
input_path = 'G:\\IDs and Accounts\\Ninghao\\Psssport2023.pdf'
output_path= 'G:\\IDs and Accounts\\Ninghao\\CompressedPages'