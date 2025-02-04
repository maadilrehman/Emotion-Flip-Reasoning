import json
import csv
import sys
from deep_translator import GoogleTranslator

def json_to_csv_urdu(json_filename, csv_filename):
    translator = GoogleTranslator(source='auto', target='ur')
    
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
            
            # Translate text to Urdu
            episode_urdu = translator.translate(episode)
            speakers_urdu = translator.translate(speakers)
            emotions_urdu = translator.translate(emotions)
            utterances_urdu = translator.translate(utterances)
            triggers_urdu = translator.translate(triggers)
            
            writer.writerow([episode_urdu, speakers_urdu, emotions_urdu, utterances_urdu, triggers_urdu])
    
    print(f"CSV file '{csv_filename}' has been created successfully with Urdu translations.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.json output.csv")
        sys.exit(1)
    
    json_filename = sys.argv[1]
    csv_filename = sys.argv[2]
    json_to_csv_urdu(json_filename, csv_filename)
