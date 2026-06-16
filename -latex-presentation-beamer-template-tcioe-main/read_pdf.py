import sys

libraries = ['pypdf', 'pdfplumber', 'fitz', 'pdfminer.high_level']
installed = []
for lib in libraries:
    try:
        __import__(lib)
        installed.append(lib)
    except ImportError:
        pass

print("Installed libraries:", installed)

# Try extraction with the first available library
if 'pypdf' in installed:
    import pypdf
    reader = pypdf.PdfReader("proposal.pdf")
    text = ""
    for i, page in enumerate(reader.pages):
        text += f"\n--- Page {i+1} ---\n"
        text += page.extract_text() or ""
    with open("proposal_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Extracted text using pypdf")
elif 'pdfplumber' in installed:
    import pdfplumber
    with pdfplumber.open("proposal.pdf") as pdf:
        text = ""
        for i, page in enumerate(pdf.pages):
            text += f"\n--- Page {i+1} ---\n"
            text += page.extract_text() or ""
        with open("proposal_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
    print("Extracted text using pdfplumber")
elif 'fitz' in installed:
    import fitz
    doc = fitz.open("proposal.pdf")
    text = ""
    for i, page in enumerate(doc):
        text += f"\n--- Page {i+1} ---\n"
        text += page.get_text()
    with open("proposal_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Extracted text using fitz")
else:
    print("No pdf extraction library found!")
