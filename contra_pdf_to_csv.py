# convert pdf to csv

import tabula
df = tabula.read_pdf("databooklet.pdf", encoding='utf-8', pages='17-24', guess=False)

tabula.convert_into("databooklet.pdf", "contra1.csv", output_format="csv", pages='17-24')
