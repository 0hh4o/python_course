class Block:
    def __init__(self,data):
        self.height = data[2]
        self.width = data[0]
        self.length = data[1]
    def get_width(self):
        return self.width
    def get_length(self):
        return self.length
    def get_height(self):
        return self.height
    def get_volume(self):
        return (self.height*self.length*self.width)
    def get_surface_area(self):
        return ((self.height*self.width*2)+(self.height*self.length*2)+(self.length*self.width*2))
b = Block([2,4,6])
print(b.get_surface_area())