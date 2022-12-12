from tkinter import *
from utils import *
from math import *

class Object():
    # Create an instance of the Utils
    utils = Utils()
    
    # Define start and end colors
    START_COLOR = '#00005F'
    END_COLOR = '#0000FF'
    
    # Initialize the object by creating a canvas,
    # drawing the object, and binding mouse events
    def __init__(self, window, vertices, edges, faces, height, width) -> None:
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
        self.draw_object(edges, faces)

        # Bind mouse events to the canvas
        self.bind_mouse_buttons(edges, faces)
        pass
    
    # Initialize the vertices of the object
    def init_vertices(self, vertices):
        self.vertices = self.utils.transpose_matrix(vertices)

    # Create the Tkinter canvas
    def create_canvas(self, height, width):
        self.canvas = Canvas(self.window, width=width, height=height, background='white')
        self.canvas.pack()

    # Draw the object on the canvas
    def draw_object(self, edges, faces):
        # Get the width and height of the canvas
        w = self.canvas.winfo_width()/2
        h = self.canvas.winfo_height()/2

        # Clear the canvas
        self.canvas.delete(ALL)

        # Calculate the scale to use when drawing the object
        scale = h/2
                
        for i in range(len(faces)):
            # Get the x, y, and z coordinates of all three vertices of the current face.
            x1 = self.vertices[0][faces[i][0]]
            y1 = self.vertices[1][faces[i][0]]
            z1 = self.vertices[2][faces[i][0]]
            a = np.array([x1, y1, z1])

            x2 = self.vertices[0][faces[i][1]]
            y2 = self.vertices[1][faces[i][1]]
            z2 = self.vertices[2][faces[i][1]]
            b = np.array([x2, y2, z2])

            x3 = self.vertices[0][faces[i][2]]
            y3 = self.vertices[1][faces[i][2]]
            z3 = self.vertices[2][faces[i][2]]
            c = np.array([x3, y3, z3])

            # Create a unit vector representing the z-axis.
            z_unit = np.array([0, 0, 1])

            # Calculate the cross product of the vectors connecting the first and 
            # third vertices to the first and second vertices.
            vect = np.cross((a-c),(a-b))

            # Calculate the magnitude of the cross product.
            factor = 10

            # Calculate the angle between the triangle and the z-axis.
            val = np.linalg.norm(np.cross(vect/np.linalg.norm(vect),z_unit))*factor
            
            # Determine the color of the triangle based on its angle with the z-axis.
            color = self.utils.get_color(self.canvas, self.START_COLOR, self.END_COLOR, val, factor)

            # Draw the triangle face on the canvas with the determined color.
            self.canvas.create_polygon(self.utils.translate_point(scale*x1, scale*y1, w, h), 
            self.utils.translate_point(scale*x2, scale*y2, w, h), 
            self.utils.translate_point(scale*x3, scale*y3, w, h), fill=color)

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

    def bind_mouse_buttons(self, edges, faces):
        # bound the mouse_click and mouse_motion functions to the canvas
        self.canvas.bind("<Button-1>", self.mouse_click)
        self.canvas.bind("<B1-Motion>", lambda event, arg1=edges, arg2=faces: self.mouse_motion(event, arg1, arg2))

    def mouse_click(self, event):
        # Save the coordinates of the mouse click event.
        self.previous_x = event.x
        self.previous_y = event.y

    def mouse_motion(self, event, edges, faces):
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
        self.draw_object(edges, faces)

        # Save the current mouse coordinates as the previous coordinates
        # for the next mouse motion event.
        self.mouse_click(event)