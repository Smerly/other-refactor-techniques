# by Kami Bigdely
# Extract superclass.
class Shape:
    def __init__(self, x, y, width, height, r, visible=True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = visible
        self.r = r

    def display_circle(self):
        if self.visible:
            print('drew the rectable.')

    def display_rectangle(self):
        if self.visible:
            print('drew the rectable.')

    def get_center_rect(self):
        return self.x + self.width/2, \
            self.y + self.height/2

    def set_visible_rect(self, is_visible):
        self.visible = is_visible

    def set_visible_circle(self, is_visible):
        self.visible = is_visible
