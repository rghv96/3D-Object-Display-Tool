# 3D Object Display Tool

The program uses the Tkinter module to create a GUI window and display an object based on input provided as an argument. The input is parsed using the InputParser module, and the object is created using the Object class. If any exceptions occur while creating the object, they are handled and printed to the console. The program starts by calling the main function, which sets up the Tkinter window and creates the object. The mainloop method is then called to start the main event loop and keep the window open.

## Algorithm

### Object Rotation
To rotate the object when the mouse is moved, the concept of transformation matrices is used. The new coordinates of the vertices of the object are calculated by multiplying the initial coordinates matrix by a rotation matrix. The rotation matrix depends on the axis of rotation.

### Points Translation
The initial coordinates of the object are defined relative to the object itself. However, the origin of the Tkinter canvas is in the top left corner, so the coordinates must be translated to be drawn in the center of the canvas. This is done using the translate_point method in the Utils class.

### Object Face Color
To determine the color of a face on an object with 3 edges, the cross product of any two edges is calculated. This cross product, which we'll call vector C, is normal to the face. If vector C is parallel to the Z-axis, then the face is colored dark blue. If vector C is perpendicular to the Z-axis, then the face is colored light blue. The color of the face will change depending on the value of the cross product.

## Input Format
- The first line contains two integers. The first integer is the number of vertices that define the 3D
object, and the second number is the number of faces that define the 3D object.
-  Starting at the second line each line will define one vertex of the 3D object and will consist of an
integer followed by three real numbers. The integer is the ID of the vertex and the three real
numbers define the (x,y,z) coordinates of the vertex. The number of lines in this section will be
equal to the first integer in the file.
- Following the vertex section will be a section defining the faces of the 3D object. The number of
lines in this section will be equal to the second integer on the first line of the file. Each line in
this section will consist of three integers that define a triangle that is a face of the object. The
three integers each refer to the ID of a vertex from the second section of the file.

## Code

Each directory has the following code structure:

### main.py
The program that uses the Tkinter module to create a GUI window and display an object based on input provided as an argument. The input is parsed using the InputParser module, and the object is created using the Object class. If any exceptions occur while creating the object, they are handled and printed to the console. The program starts by calling the main function, which sets up the Tkinter window and creates the object. The mainloop method is then called to start the main event loop and keep the window open.

### input_parser.py
The file parses the input data for a three-dimensional object. The parse_input() method loads the input data from the specified file, splits it into its individual parts, and then processes each part to extract the relevant information. The method returns three arrays: one containing the coordinates of the vertices, one containing the pairs of vertices that make up the edges of the object, and one containing the sets of vertices that make up each face of the object.

### object.py
The code initializes a 3D object by creating a canvas. The user can rotate the object by clicking and dragging the mouse. It has methods to draw the object, and bind mouse events. The object is shifted to the centre of the canvas and its edges and points are built using canvas lines and oval respectively.

### utils.py
The code contains a collection of utility functions for working with matrices, points, and angles. It contains functions for transposing a matrix, translating a point, rotating a matrix along different axes, and finding the diametrically opposite points of a given point. These functions can be used to perform various transformations on matrices and points, making it easier to work with them in a program.


## Steps to Run the program

- The program requires python to be installed. After installing python, install the requirements by running the command on terminal `pip install -r requirements.txt`

- Move into either part1/part2 directory by running the command on terminal. Eg: `cd part1`

- Place the input file along the other files. Provide it as an argument to run the program. Eg: `python main.py object.txt`

- When the program runs, a window appears with the object on the top left corner. Click and drag the mouse on the window to bring the object to the center of the window.

Feel free to contact me for any doubts