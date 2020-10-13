#!/usr/bin/python3
"""
Class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Define a class square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Init a square Constructor"""
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    @property
    def size(self):
        """ Getter of size """
        return self.width

    @size.setter
    def size(self, value):
        """Setter of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string of square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Method to assigns attributes"""
        if kwargs and len(args) == 0:
            for key, value in kwargs.items():
                if key in ['id', 'size', 'x', 'y']:
                    setattr(self, key, value)
        elif args is not None:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        """Dictionary representation of rectangle"""
        keys = ['id', 'size', 'x', 'y']
        vals = [self.id, self.size, self.x, self.y]
        return dict(zip(keys, vals))
