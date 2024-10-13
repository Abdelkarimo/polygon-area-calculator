class Rectangle:
    def __init__(self, width, height):
        self.width = width  # Assign the width parameter to an instance variable
        self.height = height  # Assign the height parameter to an instance variable
    
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


    def set_width(self, w):
        self.width=w

    def set_height(self, h):
        self.height=h
    
    def get_area (self):
        return (self.height * self.width)
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50 :
            return 'Too big for picture.'
        ret=''
        for i in range(self.height):
            for j in range(self.width):
                ret += '*'
            ret += '\n'
        return (ret)
    
    def get_amount_inside(self, shap):
        return (self.height*self.width)//(shap.height*shap.width)


class Square (Rectangle):
    def __init__ (self, side):
        super().__init__(side , side)

    def set_width(self, side):
        super().set_width(side)
        self.height=side

    def set_height(self, side):
        super().set_height(side)
        self.width=side      

    def set_side(self, side):
        self.width = side
        self.height = side

        
    def __repr__(self):
        return f'Square(side={self.width})'

    
        