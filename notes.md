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
