class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
    @property
    def size(self):
        """retrive the size of the square"""
        return(self.__size)
    @size.setter
    def size(self, value):
        """set the size """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
             raise ValueError('size must >= 0')
        self.__size = value
    def area(self):
        """Calculate the area of the sqaure"""
        """we should be getting the area now"""
        return(self.__size ** 2)
    
    
        


    
