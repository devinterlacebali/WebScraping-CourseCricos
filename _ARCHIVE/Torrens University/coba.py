import pdfplumber
import re

pdf_path = "Torrens University/torrens_fee.pdf"
output_sql = []

# regex menangkap:
#  - CRICOS code: angka + huruf (contoh: 107271K)
#  - total fee: angka ribuan (contoh: 112,500 -> 112500)
cricos_regex = re.compile(r"\b(\d{6}[A-Z])\b")
fee_regex = re.compile(r"\$?([\d,]+)\s*$")


with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if not text:
            continue

        lines = text.split("\n")

        for line in lines:
            # cek apakah line punya CRICOS code
            cricos_match = cricos_regex.search(line)
            if cricos_match:
                cricos = cricos_match.group(1)

                # cari fee (kolom paling kanan biasanya)
                fee_match = fee_regex.search(line)
                if fee_match:
                    fee = fee_match.group(1).replace(",", "")

                    sql = (
                        f"UPDATE courses SET offshore_tuition_fee = '{fee}', "
                        f"updated_at = NOW() WHERE cricos_course_code = '{cricos}';"
                    )
                    output_sql.append(sql)

# simpan hasil SQL
with open("torrens_fee_update.sql", "w") as f:
    f.write("\n".join(output_sql))

print("Generated SQL:", len(output_sql))
