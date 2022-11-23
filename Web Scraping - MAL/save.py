import os
import json

# checks if file exists
def does_file_exist(function):
    def check_file(filename):
        try:
            open(filename, 'r')
            return function(filename)
        except FileNotFoundError:
            with open(filename, 'w+') as file:
                json.dump({}, file, indent = 4)
            print(f'{filename.split("/")[-1]} does not exist. Created a file.')
            return function(filename)
    return check_file   

# creates backup data file to another folder
def create_backup(function):
    def backup_creation(filename, data):
        backup_name = filename.split('/')[-1]
        with open(f'./backup_folder/backup_{backup_name}', 'w+') as file:
            json.dump(data, file, indent = 4)
        function(filename, data)

    return backup_creation

# creates checkpoint for every file save
def create_checkpoint(function):
    def checkpoint(filename, data):
        idx = str(list(data.keys())[-1])

        with open('./checkpoint2/checkpoint.txt', 'w+') as file:
            file.write(idx)

        function(filename, data)

    return checkpoint

# loads checkpoint 
def load_checkpoint():
    with open('./checkpoint2/checkpoint.txt', 'r') as file:
        checkpoint = file.readline()
        return int(checkpoint)

# loads data to file
@does_file_exist
def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    return data

# save data to file
@create_checkpoint
@create_backup
def save_data(filename, data):
    with open(filename, 'w+') as file:
        json.dump(data, file, indent = 4)