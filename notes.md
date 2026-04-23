# Dijkstra's Algorithm

## Intro
The goal of this program is to demonstrate Dijkstra's algorithm for finding the shortest path on a weighted graph.  
When complete the program will present the user with a randomly generated graph where the user can click any 2 points and the program will
run Dijkstra's Algorithm on the graph until the cheapest path is generated. While the algorithm is running the user will be shown information about
the state of the algorithm such as the contents of the priority queue and the cost of the paths it finds.  

Things I will need to implement:
- Visualization stuff
- Random graph generation
- User interaction
- Priority queue
- Dijkstra's Algorithm

## Visualization Stuff
I will be using pygame for this because I have experience with it and I used it for my last algorithm project. Because I used it last time I can just reuse a few parts to get my window setup.  
Now what I want to do is to draw a simple graph of 2 points and a weighted edge.  

Ok so far what I've done is draw 2 points and a line between them with their distance as the weight drawn in the middle of the line. I set one of the points to follow the cursor to test it at
different angles and distances.  

Now I need to be able to draw more complex graphs which means I also need to come up with a way to represent graphs. I think an adjacency list will be the easiest to adapt to what I need
and it should run better because the graphs in the finished program are likely to be sparse.  
Each entry in the adjacency list will have a coordinate pair and a list of the indexes of the other nodes it neighbors and the weight of their edge.  

## Random Graph Generation
Now that I have an internal representation of weighted graphs and I can draw them to the screen I need to create an algorithm to randomly generate graphs.  
I could just randomly generate N points, connected each of them to random neighbors, and give them random weights, but my concern is that would look ugly.
Ideally my graph would be a nice completely connected planar graph. I don't even think I'm going to try making it planar because that sounds like a massive
headache, but I could avoid it looking too bad by setting a max distance that the edges can be from each other. For connectedness I could say that each node
has to at least connect to either its closest neighbor or closest 2 neighbors.  
I tested out connecting the 2 closest neighbors of random points on a white board and it seems like this could be a good way to do this.  
I implemented it and I was wrong the graphs are very bad.  

I'm thinking about using a library called networkx to help me display the graphs. If I use this then I can just randomly generate edges and weights between nodes and it will figure out
where to put them while drawing it.  
It turns out networkx can do the random edge generation which would have been the easy part anyway. There are a lot of different random graph generating algorithms and I'm honestly not
sure which one to use. Then once randomly generated my program will need to go through and add weights to all of the edges which should also be easy. The hardest part will be re-writing
the code to draw the graphs to work with the new library.  
As an aside networkx does have an implementation of Dijkstra's Algorithm but I'm not going to use that because it would defeat the point of this project and because I wouldn't be able to show it running.  

The graph generation is a lot better but not perfect, I have to re roll a few times in order to get a nice looking graph. So I'm going to play with the settings a little bit to try and make it nicer.

## User Interaction
The goal of the user interaction is to have the user be able to selected a start and end node with their mouse.  
There are a few parts to this:
- Selecting the node on click
- Showing that a node is being hovered over
- a UI element telling the user that they are supposed to select a node and tell the user if they are selecting the start or end node.

And being that I already have to have UI and mouse support I can easily add a few buttons to either regenerate the graph or pick new points to path find to.

I'm going to start by changing some of the rendering code to be easier to add more elements to.  
I've done that and added a basic UI for telling the user which point to select. Now I have to add mouse interaction.  
I can get the mouse coordinates easily because of pygame then I just have to check all the nodes to see if the mouse is within a certain radius of them. I shouldn't have to worry about nodes being
too close together because the placement algorithm should keep them far enough apart.  
For the UI buttons I can just make them a rectangle and then user pygame functions to check if the mouse is within the rectangle.  
I've finished user interaction with the nodes and the UI. The main file is starting to get quite large and I haven't even started work on the algorithm so I might have to split it up soon.  
