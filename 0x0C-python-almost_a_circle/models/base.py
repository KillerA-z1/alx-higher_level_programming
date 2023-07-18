#!/usr/bin/python3
"""
Base class
"""

import json
import csv
import os
import turtle


class Base:
    """Base class for managing id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object.

        Args:
            id (int): The ID of the object. If not provided,
            the ID is automatically assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Create a new JSON representation"""
        if not list_dictionaries:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + '.json'
        obj_list = []

        if list_objs is not None:
            obj_list = [obj.to_dictionary() for obj in list_objs]

        with open(filename, 'w') as file:
            file.write(cls.to_json_string(obj_list))

    def from_json_string(json_string):
        """
        Load a list of objects from a JSON string.

        Args:
            json_string (str): JSON string representing a list of objects.

        Returns:
            list: List of objects loaded from the JSON string.
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of the class and update its attributes based on the
        provided dictionary.
        """
        if cls.__name__ == "Square":
            size = dictionary.get("size", 8)
            dummy = cls(size)
        elif cls.__name__ == "Rectangle":
            width = dictionary.get("width", 8)
            height = dictionary.get("height", 8)
            dummy = cls(width, height)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Returns:
            list: List of instances loaded from the file.
        """
        filename = cls.__name__ + ".json"

        if not os.path.exists(filename):
            return []
        else:
            with open(filename, 'r', encoding='utf-8') as file:
                json_data = file.read()
                object_list = cls.from_json_string(json_data)
                instance_list = [cls.create(**obj) for obj in object_list]
            return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list in CSV"""
        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y]
                    )

            if cls.__name__ == "Square":
                for obj in list_objs:
                    csv_writer.writerow(
                        [obj.id, obj.size, obj.x, obj.y]
                    )

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize a list in csv"""
        filename = cls.__name__ + ".csv"
        instance_list = []

        try:
            with open(filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)

                for row in csv_reader:
                    dictionary = {}

                    if cls.__name__ == "Rectangle":
                        dictionary = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }
                    elif cls.__name__ == "Square":
                        dictionary = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }

                    obj = cls.create(**dictionary)
                    instance_list.append(obj)
        except FileNotFoundError:
            pass

        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all the rectangles and squares"""
        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        screen.title("Shapes")

        pen = turtle.Turtle()
        pen.speed(2)
        pen.penup()

        for rectangle in list_rectangles:
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.color("blue")
            for _ in range(2):
                pen.forward(rectangle.width)
                pen.right(90)
                pen.forward(rectangle.height)
                pen.right(90)
            pen.penup()

        for square in list_squares:
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("red")
            for _ in range(4):
                pen.forward(square.size)
                pen.right(90)
            pen.penup()

        turtle.done()
