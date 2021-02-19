import json

result = []

with open('smoothie_data_cleaned.json', 'r') as f:
    data1 = json.load(f)

for item in data1:
    result.append(item)

with open('smoothie_data_cleaned_2.json', 'r') as f:
    data2 = json.load(f)

for item in data2:
    result.append(item)

with open('smoothie_data_cleaned_3.json', 'r') as f:
    data3 = json.load(f)

for item in data3:
    result.append(item)

with open(str(len(result)) + '_recipes.json', 'w') as f:
    json.dump(result, f, indent=2)

