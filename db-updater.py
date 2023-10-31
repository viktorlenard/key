import json

with open('/Users/viktor.lenard/Desktop/key/words_dictionary.json') as f:
    data = json.load(f)

updated_data = {}

for key in data:
   if len(key) > 4 and len(key) < 8:
        updated_data[key] = len(key) 

with open('/Users/viktor.lenard/Desktop/key/words.json', 'w') as output_file:
    json.dump(updated_data, output_file, indent=4)  # indent for pretty formatting

print(updated_data)