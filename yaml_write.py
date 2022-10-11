import yaml

augmentation = {
        'Algorithm': [
            'Rotation',
            'Color'
        ],
        'Parameters': [
            15,
            'red'
        ]
}


with open("config.yaml", 'w') as yamlfile:
    data = yaml.dump(augmentation, yamlfile)
    print("Write successful")

with open("config.yaml", 'r') as stream:
        data_loaded = yaml.safe_load(stream)
