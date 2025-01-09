import csv

def save_to_csv(data, filename):
  
    # Ensure data is a list (handle single dictionary case)
    if isinstance(data, dict):
        data = [data]

    # Open the CSV file for writing
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            # Create a CSV DictWriter using the keys from the first dictionary as headers
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()  # Write the headers
            writer.writerows(data)  # Write all rows of data
        print(f"Data successfully saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving to {filename}: {e}")
