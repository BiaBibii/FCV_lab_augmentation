import yaml

augmentation = [
    {
        'Algorithm' : 'Rotation',
        'Parameters': '15'
    }
]

with open("config.yaml", 'w') as yamlfile:
    data = yaml.dump(augmentation, yamlfile)
    print("Write successful")