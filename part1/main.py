# Import necessary modules
from tkinter import *  
import sys
import traceback

from input_parser import *
from object import *

def main():
    # Check if input was provided
    if len(sys.argv) < 2:
        print('Input not provided!')
        return

    # Create a Tkinter object
    root = Tk()

    # Get the screen height and width
    height = root.winfo_screenheight()
    width = root.winfo_screenwidth()

    try:
        # Parse the input provided as an argument
        vertices, edges, _ = InputParser.parse_input(sys.argv[1])

        # Create a new object using the parsed input
        Object(root, vertices, edges, height, width)
    except:
        # Handle any exceptions that occur
        print("An exception occurred while creating object")
        traceback.print_exc()
        return

    # Set the title of the Tkinter window
    root.title("Neocis Software Assessment: Part 1")

    # Start the main event loop
    root.mainloop()

if __name__ == '__main__':
    main()