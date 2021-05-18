# PDF Converter

'''
- Get all images from current folder
    * Get all the files from current folder
    * Filter out only the images you have given as the extension

- Convert those images into a single PDF
'''

import os
import img2pdf

files = []
extensions = input("Enter the file extension with '.' : ")

# os.listdir() returns a list of names of all files and folders inside the current directory
for path in os.listdir():
    if os.path.isfile(path) and path.endswith(extensions):
        files.append(path)

files.sort(key=os.path.getmtime)

with open("document.pdf", "wb") as f:
    pdf = img2pdf.convert(files)
    f.write(pdf)

print("Compiled to document.pdf!")