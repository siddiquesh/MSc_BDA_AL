import os
folder = r'c:\Users\asdf\Downloads\MSc_BDA_AL-\asm'
for f in sorted(os.listdir(folder)):
    if f.endswith('.pdf'):
        path = os.path.join(folder, f)
        with open(path, 'rb') as fh:
            data = fh.read()
            idx = data.find(b'%PDF')
            nulls = 0
            for b in data:
                if b == 0:
                    nulls += 1
                else:
                    break
            if nulls < len(data):
                first_real = data[nulls:nulls+30]
            else:
                first_real = b'ALL_NULL'
            status = "OK" if idx >= 0 else ("ALL NULL" if nulls == len(data) else "NO PDF HEADER")
            print(f"[{status}] {f}: size={len(data)}, nulls={nulls}, PDF_at={idx}")
