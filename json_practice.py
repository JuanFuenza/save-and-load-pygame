import json

# data = {
#     'Germany': 'Berlin',
#     'Uk': 'London',
#     'China': 'Beijing',
#     'Kitten': 123
# }

# dumps the data in a json file
# with open('test_data.txt', 'w') as test_file:
#     json.dump(data, test_file)

# loads and read the data
with open('test_data.txt') as test_file:
    data = json.load(test_file)
    for entry in data.items():
        print(entry)