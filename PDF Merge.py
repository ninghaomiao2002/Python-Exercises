import os
from PyPDF2 import PdfMerger

# Use raw string to avoid issues with backslashes
target_path = r"C:\Users\ningh\Documents\2022"

pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

file_merger = PdfMerger()
for pdf in pdf_lst:
    file_merger.append(pdf)

# Provide a valid file path for the merged output
output_path = r"C:\Users\ningh\Documents\2022\merged_file.pdf"
file_merger.write(output_path)
file_merger.close()

print(f"PDFs merged and saved to {output_path}")
