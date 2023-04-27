import json

def save_json(dict, path):
    with open(path, 'w') as json_path:
        json.dump(dict, json_path)

def load_json(json_path):
    with open(json_path, 'r') as json_file:    
        json_data = json.load(json_file)
    return json_data

def labelme_to_egetra(labelme_dict):
    return {'latitude': labelme_dict['latitude'], 'longitude': labelme_dict['longitude'], 'data': labelme_dict['tempo'], 'shapes': labelme_dict['shapes']}    
