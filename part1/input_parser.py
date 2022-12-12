import numpy as np

class InputParser:
    # Method for parsing the input data for a 3D object.
    def parse_input(file_name):
        # Load the input data from the specified file.
        input = np.loadtxt(file_name, dtype=str)

        # Parse the first line to extract the number of vertices and faces.
        num_vertices, num_faces = input[0].split(',')

        # Create empty lists for storing the edges and faces.
        edges = []
        faces = []

        # Create an array for storing the coordinates of the vertices.
        vertices = np.empty([int(num_vertices), 3])

        # Parse the input data for the vertices.
        vertices_input = input[1:int(num_vertices)+1]
        for i in range(int(num_vertices)):
            _, x, y, z = vertices_input[i].split(',')
            vertices[i] = (float(x), float(y), float(z))

        # Parse the input data for the faces.
        faces_input = input[-int(num_faces):]
        for i in range(int(num_faces)):
            # Extract the indices of the vertices that make up the face.
            v1, v2, v3 = faces_input[i].split(',')

            # Add the face to the list of faces.
            faces.append([int(v1)-1, int(v2)-1, int(v3)-1])

            # Check if each pair of vertices that make up the face is already
            # in the list of edges. If not, add it to the list.
            if (int(v1)-1, int(v2)-1) not in edges:
                edges.append((int(v1)-1, int(v2)-1))
            if (int(v1)-1, int(v3)-1) not in edges:
                edges.append((int(v1)-1, int(v3)-1))
            if (int(v2)-1, int(v3)-1) not in edges:
                edges.append((int(v2)-1, int(v3)-1))

        # Return the arrays containing the vertices, edges, and faces.
        return vertices, edges, faces