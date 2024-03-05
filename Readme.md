# PathFindingImage - Find the Shortest Path Between Two Pixels in an Image

## Description:
The program allows the user to find the shortest path between two pixels in an image. It provides a user-friendly interface for selecting pixels and visualizing the shortest path. The implementation is based on the Dijkstra algorithm. The program requires Python and the Tkinter library for the graphical user interface.

## Functionality:
The program allows the user to find the shortest path between two pixels in an image using the Dijkstra algorithm. To find the distance between two pixels, the Euclidean norm of the difference between the RGB values of the two pixels is calculated.

1. There is an `Image` folder where you can insert an image, or you can work on the default image provided.
2. The program prompts the user to select two points by clicking on the image.
3. A button labeled `Find Path` is displayed to the user.
4. Once the user clicks on the button, the Dijkstra algorithm executes and traces the shortest path, marking it in green.
5. The user can repeat this operation by clicking on the `Reset` button.

## Commands:
- You can execute it from any directory: `cd ~/ALGO/Projet && python3 main.py`
