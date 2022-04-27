import json

# functions
# loads data to file
def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    return data

# save data to file
def save_data(filename, data):
    with open(filename, 'w+') as file:
        last_item = list(data.keys())[-1].split(' ')[0]
        create_checkpoint(last_item)

        json.dump(data, file, indent = 4)
    create_backup(data)

def create_backup(data):
    with open('./data/backup.json', 'w') as file:
        json.dump(data, file, indent = 4)

# creates checkpoint
def create_checkpoint(idx):
    with open('./checkpoint/checkpoint.cp', 'w') as file:
        file.write(f'Checkpoint: {idx}') 

# loads checkpoint
def load_checkpoint():
    with open('./checkpoint/checkpoint.cp', 'r') as file:
        checkpoint = file.readlines()

        return int(checkpoint[0].split(' ')[1])