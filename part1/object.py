from tkinter import *
from utils import *
from math import *

class Object():
    # Create an instance of the Utils
    utils = Utils()
    
    # Initialize the object by creating a canvas,
    # drawing the object, and binding mouse events
    def __init__(self, window, vertices, edges, height, width) -> None:
        # Previous x and y position of the mouse
        self.previous_x = 0
        self.previous_y = 0

        # Epsilon value used for calculating rotation angles
        self.epsilon = lambda d: d * 0.01

        # Tkinter window and canvas
        self.window = window
        self.canvas = None

        # Initialize the vertices of the object
        self.init_vertices(vertices)

        # Create the canvas and draw the object
        self.create_canvas(height, width)
        self.draw_object(edges)

        # Bind mouse events to the canvas
        self.bind_mouse_buttons(edges)

    # Initialize the vertices of the object
    def init_vertices(self, vertices):
        self.vertices = self.utils.transpose_matrix(vertices)

    # Create the Tkinter canvas
    def create_canvas(self, height, width):
        self.canvas = Canvas(self.window, width=width, height=height, background='white')
        self.canvas.pack()

    # Draw the object on the canvas
    def draw_object(self, edges):
        # Get the width and height of the canvas
        w = self.canvas.winfo_width()/2
        h = self.canvas.winfo_height()/2

        # Clear the canvas
        self.canvas.delete(ALL)
        # Calculate the scale to use when drawing the object
        scale = h/2

        for i in range(len(edges)):
            # Get the indices of the two points that make up the current edge
            point1 = edges[i][0]
            point2 = edges[i][1]
            
            # Get x & y coordinates of the points
            point1_x = self.vertices[0][point1]
            point1_y = self.vertices[1][point1]
            point2_x = self.vertices[0][point2]
            point2_y = self.vertices[1][point2]

            # Translate the coordinates to the centre of the canvas
            point1_x, point1_y = self.utils.translate_point(scale*point1_x, scale*point1_y, w, h)
            point2_x, point2_y = self.utils.translate_point(scale*point2_x, scale*point2_y, w, h)

            # Draw the points as circles on the canvas
            self.canvas.create_oval(self.utils.diametrically_opposite_points(point1_x, point1_y), fill = 'blue', outline = 'blue', width=5)
            self.canvas.create_oval(self.utils.diametrically_opposite_points(point2_x, point2_y), fill = 'blue', outline = 'blue', width=5)

            # Draw the edges as a line on the canvas
            self.canvas.create_line(point1_x, point1_y, point2_x, point2_y, fill = 'blue')

    def bind_mouse_buttons(self, edges):
        # bound the mouse_click and mouse_motion functions to the canvas
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.bind("<B1-Motion>", lambda event, arg = edges: self.mouse_motion(event, arg))

    def mouse_click(self, event):
        # Save the coordinates of the mouse click event.
        self.previous_x = event.x
        self.previous_y = event.y

    def mouse_motion(self, event, edges):
        # Calculate the difference in coordinates between the previous mouse click 
        # and the current mouse motion event.
        dx = self.previous_y - event.y 
        dy = self.previous_x - event.x 

        # Rotate the object along the x-axis by an amount determined 
        # by the difference in x coordinates.
        self.vertices = self.utils.rotate_along_x(self.epsilon(-dx), self.vertices)

        # Rotate the object along the y-axis by an amount determined 
        # by the difference in y coordinates.
        self.vertices = self.utils.rotate_along_y(self.epsilon(dy), self.vertices)

        # Redraw the object with the updated vertices.
        self.draw_object(edges)

        # Save the current mouse coordinates as the previous coordinates
        # for the next mouse motion event.
        self.mouse_click(event)