import pandas as pd

def write_to_excel(data, filename="output.xlsx"):
    if not data:
        print("No data to write.")
        return

    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"✅ Data written to {filename}")
