import json
import csv
import sys

def json_to_csv(json_filename, csv_filename):
    with open(json_filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    # Define CSV headers
    headers = ["episode", "speakers", "emotions", "utterances", "triggers"]
    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)  # Write header row
        
        # Iterate through JSON records and write to CSV
        for record in data:
            episode = record.get("episode", "")
            speakers = ", ".join(record.get("speakers", []))
            emotions = ", ".join(record.get("emotions", []))
            utterances = ", ".join(record.get("utterances", []))
            triggers = ", ".join(map(str, record.get("triggers", [])))
            
            writer.writerow([episode, speakers, emotions, utterances, triggers])
    
    print(f"CSV file '{csv_filename}' has been created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.json output.csv")
        sys.exit(1)
    
    json_filename = sys.argv[1]
    csv_filename = sys.argv[2]
    json_to_csv(json_filename, csv_filename)

