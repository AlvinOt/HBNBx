#!/usr/bin/python3
"""Unittest for BaseModel class"""
from models.base_model import BaseModel

# Create a new instance of the BaseModel class
my_model = BaseModel()

# Add some attributes to the instance
my_model.name = "My First Model"
my_model.my_number = 89

# Print the string representation of the instance
print(my_model)

# Call the save method to update the instance's updated_at attribute
my_model.save()

# Print the string representation of the instance again to confirm that the updated_at attribute has changed
print(my_model)

# Call the to_dict method to obtain a dictionary representation of the instance
my_model_json = my_model.to_dict()

# Print the dictionary representation of the instance
print(my_model_json)

# Print the keys and values of the dictionary representation
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
