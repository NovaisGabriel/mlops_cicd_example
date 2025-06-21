import pandas as pd
import requests
from io import BytesIO
from zipfile import ZipFile

# URL of the ZIP file containing the CSV
zip_url = "https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip"
csv_filename_in_zip = "day.csv"

try:
    # Download the ZIP file content
    response = requests.get(zip_url)
    response.raise_for_status() # Raise an exception for bad status codes

    # Read the ZIP file from memory
    with ZipFile(BytesIO(response.content)) as zf:
        # Check if the CSV file exists in the zip
        if csv_filename_in_zip in zf.namelist():
            # Open the CSV file from the zip and read into a Pandas DataFrame
            with zf.open(csv_filename_in_zip) as csv_file:
                df = pd.read_csv(csv_file)
                print("DataFrame loaded successfully:")
                print(df.head())
        else:
            print(f"Error: '{csv_filename_in_zip}' not found in the ZIP archive.")
            print(f"Files in ZIP: {zf.namelist()}")

except requests.exceptions.RequestException as e:
    print(f"Error downloading the ZIP file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

df.to_csv("./data/data.csv")
df.head()
