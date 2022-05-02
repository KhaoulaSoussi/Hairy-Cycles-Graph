# Hairy-Cycle-Graph

## Description of the problem
This programming challenge was part of the Honors component of Analysis of Algorithms class with Dr. Naeem Nisar Sheikh.
The purpose is to check whether a graph is a hairy cycle. A hairy cycle is just a cycle, where each vertex may (but doesn't have to) have one or more paths of any length coming of it.
Here's an example of a hairy cycle:

<img width="251" alt="thumbnail_hairyCn" src="https://user-images.githubusercontent.com/85248282/166260259-0f0e19bb-3567-46f5-95ef-d904cbc732c0.png">

## Proposed solution
There are five input files that cover many possible input cases. The following figure shows the structure of the graphs represented by each input file.

![Input Files Graphs](https://user-images.githubusercontent.com/85248282/166260796-123ce76d-f2d9-4348-af16-7e70b7258143.jpg)

To run the program with each file, please change the name of the file at line 5 of the code.
I tried to provide descriptive comments in the code. If they are not clear enough, it might be helpful to print the adjacency list after line 26 and after line 50 to see the difference between the original adjacency list and the modified one.

Note that the program also covers bushy cycles (e.g. the fifth input graph)
A bushy cycle in this case is one where the paths coming out of a vertex of a hairy cycle have degree >= 2 vertices:

![bushy cycle](https://user-images.githubusercontent.com/85248282/166261691-56480f32-1604-43f4-b4f5-066afbae924f.png)

Done on May 30th, 2021
