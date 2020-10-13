#!/usr/bin/python3
"""
This module about Class Base
"""
import json
import csv


class Base:
    """
    Define our Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization general"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ that returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        _list = []
        if list_objs is not None:
            for i in list_objs:
                _list.append(i.to_dictionary())
        else:
            _list = []
        with open(filename, "w") as f:
            f.write(cls.to_json_string(_list))

    @staticmethod
    def from_json_string(json_string):
        """ loads file JSON """
        if json_string is not None or len(json_string) != 0:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        tmp_list = []
        try:
            with open(filename, 'r')as f:
                tmp_list = Base.from_json_string(f.read())
            for item, j in enumerate(tmp_list):
                tmp_list[item] = cls.create(**tmp_list[item])
        except:
            pass
        return tmp_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """that serializes and deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as csv_f:
            if cls.__name__ is "Rectangle":
                keys = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ is "Square":
                keys = ['id', 'size', 'x', 'y']
            writer_ = csv.DictWriter(csv_f, fieldnames = keys)
            for obj in list_objs:
                writer_.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """that serializes and deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "r") as csv_f:
            csv_reader = csv.DictReader(csv_f)
            list_ = {}
            list_2 = []
            for row in csv_reader:
                for l_key, l_value in dict(row).items():
                    list_[l_key] = l_value
                list_2.append(cls.create(**list_))
            return list_2
