import pandas as pd
import os


def export_csv(records, filename):

    os.makedirs("outputs", exist_ok=True)

    df = pd.DataFrame(records)

    filepath = f"outputs/{filename}.csv"

    df.to_csv(filepath, index=False)

    print(f"Saved: {filepath}")