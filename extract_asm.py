import pymupdf
import os, sys

folder = r'c:\Users\asdf\Downloads\MSc_BDA_AL-\asm'
outdir = r'c:\Users\asdf\Downloads\MSc_BDA_AL-\asm_text'
os.makedirs(outdir, exist_ok=True)

for f in sorted(os.listdir(folder)):
    if not f.endswith('.pdf'):
        continue
    path = os.path.join(folder, f)
    outpath = os.path.join(outdir, f.replace('.pdf', '.txt'))
    try:
        doc = pymupdf.open(path)
        text = ""
        for i, page in enumerate(doc):
            t = page.get_text()
            if t.strip():
                text += f"=== PAGE {i+1} ===\n{t}\n"
        doc.close()
        with open(outpath, 'w', encoding='utf-8') as out:
            out.write(text)
        lines = len(text.splitlines())
        print(f"OK  {f} -> {lines} lines extracted")
    except Exception as e:
        print(f"ERR {f} -> {e}")
