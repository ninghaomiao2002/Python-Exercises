import os
from PyPDF2 import PdfMerger

target_path = "C:\\Users\\ningh\\OneDrive\\Desktop\\4C5 Digital Signal Processing\\Lectures"
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

file_merger = PdfMerger()
for pdf in pdf_lst:
    file_merger.append(pdf)

file_merger.write("C:\\Users\\ningh\\OneDrive\\Desktop\\4C5 Digital Signal Processing\\Lectures\\merge.pdf")
file_merger.close()