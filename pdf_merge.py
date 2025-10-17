from pypdf import PdfWriter
import os

folder_path = r"C:\Users\Nihal\Documents\nishant\Python-practice\pdf"
files = sorted([f for f in os.listdir(folder_path) if f.endswith('.pdf')])
merger = PdfWriter()

for pdf in files:
    merger.append(os.path.join(folder_path, pdf))

output_path = os.path.join(folder_path, "merged-pdf.pdf")
merger.write(output_path)

merger.close()
print("PDF files merged successfully into 'merged-pdf.pdf'")