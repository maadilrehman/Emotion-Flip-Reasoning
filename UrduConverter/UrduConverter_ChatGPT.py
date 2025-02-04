import json
import csv
import sys
import openai

def translate_text(text, target_language="ur"):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a translator. Translate the following text to Urdu."},
            {"role": "user", "content": text}
        ]
    )
    return response["choices"][0]["message"]["content"].strip()

def json_to_csv_urdu(json_filename, csv_filename):
    with open(json_filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    # Define CSV headers
    headers = ["episode", "speakers", "emotions", "utterances", "triggers"]
    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)  # Write header row
        i=0
        # Iterate through JSON records and write to CSV
        for record in data:
            episode = record.get("episode", "")
            speakers = ", ".join(record.get("speakers", []))
            emotions = ", ".join(record.get("emotions", []))
            utterances = ", ".join(record.get("utterances", []))
            triggers = ", ".join(map(str, record.get("triggers", [])))
            
            # Translate text to Urdu using ChatGPT API
            episode_urdu = translate_text(episode)
            speakers_urdu = translate_text(speakers)
            emotions_urdu = translate_text(emotions)
            utterances_urdu = translate_text(utterances)
            triggers_urdu = translate_text(triggers)
            
            writer.writerow([episode_urdu, speakers_urdu, emotions_urdu, utterances_urdu, triggers_urdu])
            print(f"Written '{i}' -> '{episode}' \n")
            i = i + 1
    
    print(f"CSV file '{csv_filename}' has been created successfully with Urdu translations.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.json output.csv")
        sys.exit(1)
    # first run the following command on linux
    #export OPENAI_API_KEY=<your key>

    
    json_filename = sys.argv[1]
    csv_filename = sys.argv[2]
    json_to_csv_urdu(json_filename, csv_filename)
