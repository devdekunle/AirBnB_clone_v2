#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""

        if cls is None:
            return FileStorage.__objects
        else:

            new_dict = {}
            all_objects = FileStorage.__objects
            for key, value in all_objects.items():
                if value.__class__.__name__ == "{}".format(cls.__name__):
                    new_dict[key] = value
            return new_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        class_id = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[class_id] = obj

    def delete(self, obj=None):
        """ Deletes an object from the list of objects"""
        if obj is not None:
            all_objects = self.all()
            obj_keys = all_objects.keys()
            obj_del_key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if obj_del_key in obj_keys:
                del all_objects[obj_del_key]
            self.save()

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name = val['__class__']
                    del val['__class__']
                    self.all()[key] = classes[class_name](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """ call reload method for deserializing the json file to objects
        """
        self.reload()
