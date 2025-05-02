import pandas as pd
import msoffcrypto
from io import BytesIO

# Sample DataFrame
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

# Save DataFrame to an in-memory buffer
buffer = BytesIO()
with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Sheet1", index=False)
buffer.seek(0)  # Reset buffer position

# Encrypt and save the file
password = "mypassword"
with open("yey.xlsx", "wb") as f_out:
    encryptor = msoffcrypto.OfficeFile(buffer)
    encryptor.encrypt( password, f_out)

print("✅ Excel file protected and saved as 'yey.xlsx'")
