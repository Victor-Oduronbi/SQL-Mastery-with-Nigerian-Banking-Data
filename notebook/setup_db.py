import pandas as pd
import sqlite3
from datasets import load_dataset

print("Fetching a small sample of the data... (this will be much faster)")

# 1. Use 'streaming=True' to avoid downloading the whole 423MB file at once
dataset_stream = load_dataset("electricsheepafrica/nigerian-banking-retail-transactions", split='train', streaming=True)

# 2. Take only the first 50,000 rows (plenty for complex SQL queries)
small_set = dataset_stream.take(50000)

# 3. Convert to DataFrame
df = pd.DataFrame(list(small_set))

# 4. Save to SQL
conn = sqlite3.connect('nigerian_bank.db')
df.to_sql('transactions', conn, if_exists='replace', index=False)

print(f"✅ Done! Created a database with {len(df)} rows.")
conn.close()
