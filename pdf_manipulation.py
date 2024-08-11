import pymupdf
import time

while True:
    print()
    date_new = input("Zadaj novy datum vo formate den.mesiac.rok (napr. 01.01.2024): ")
    if len(date_new) == 10:
        break
    else:
        print()
        print("Zadal si nespravny format datumu!")
        print()
        time.sleep(3)
        continue

pdf_document = pymupdf.open("marken.pdf")

page = pdf_document[0]

blocks = page.get_text("blocks")

for block in blocks:
    for pattern in block:
        if "17.07." in str(pattern):
            x0, y0, x1, y1 = block[:4]
            rect = pymupdf.Rect(x0, y0, x1, y1)
            page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))
            page.insert_text((x0, y0), f"\n{date_new}", fontsize=9)
            pdf_document.save(f"result/marken_{date_new}.pdf")

print()
print("Hotovo! Datujem je zmeneny.")
print()
print(f"Novy nazov suboru je => marken_{date_new}.pdf.")
print()
