import os, json


def load_existing_save(savepath):
    with open(savepath, 'r+') as file:
        save = json.load(file)
    return save

def write_save(savepath, data):
    with open(savepath, 'w') as file:
        json.dump(data, file, indent=4)

def load_save(savepath, save_dict):
    try:
        save = load_existing_save(savepath)
    except:
        save = save_dict
        write_save(savepath, save)
    return save

