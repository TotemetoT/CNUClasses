import csv

# Specify the input CSV file path and the output TSV (tab-separated values) file path
input_csv_file_path = 'data/books_new.csv'
output_tsv_file_path = 'data/big_list.txt'

# Open the input CSV file and the output TSV file
with open(input_csv_file_path, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_tsv_file_path, mode='w', newline='', encoding='utf-8') as outfile:
    # Create a CSV reader that handles the input format (with commas and optional quotes)
    reader = csv.reader(infile)
    # Create a CSV writer that will write tab-delimited lines to the output file
    writer = csv.writer(outfile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Read each row from the input file and write it to the output file with tabs
    count = 0
    for row in reader:
        if count != 1:
            count += 1
        else:
            print(row)
        writer.writerow(row)

print(f"Conversion complete. The tab-delimited file has been saved as '{output_tsv_file_path}'.")
