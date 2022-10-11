import yaml

augmentation = {
            'Rotation':12,
             'Contrast': {
                'brightness':100,'contrast':12
            },
            'Sharpening': {}
        }


with open("config.yaml", 'w') as yamlfile:
    data = yaml.dump(augmentation, yamlfile)
    print("Write successful")

with open("config.yaml", 'r') as stream:
        data_loaded = yaml.safe_load(stream)