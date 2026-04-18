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
different angles and distances
