#https://chatgpt.com/share/69fb75a7-6da4-83a5-82aa-6b4af32624f1

#https://chatgpt.com/share/69fb8df1-c3bc-8321-9a7a-7c80cb117dcd

# Practical 1: DFS and BFS
# 1. Graph Basics

# A graph is a data structure made of:

# Vertices (Nodes) → points
# Edges → connections between nodes

# Example:

# A --- B
# |     |
# C --- D

# Here:

# Vertices = A, B, C, D
# Edges = A-B, A-C, B-D, C-D
# 2. What is Graph Traversal?

# Traversal means:

# Visiting all nodes of a graph systematically.

# Two major methods:

# DFS (Depth First Search)
# BFS (Breadth First Search)
# 3. Depth First Search (DFS)

# DFS explores:

# One branch completely before moving to another branch.

# It uses:

# Recursion OR
# Stack
# DFS Working

# Example:

#     A
#    / \
#   B   C
#  / \
# D   E

# DFS Traversal:

# A → B → D → E → C
# DFS Algorithm
# 1. Visit node
# 2. Mark node as visited
# 3. Recursively visit unvisited neighbors
# DFS Characteristics
# Feature	Value
# Data Structure	Stack
# Technique	Recursive
# Memory	Less
# Can get stuck deep	Yes
# Complete	No
# Optimal	No
# DFS Time Complexity

# For graph:

# O(V+E)

# Where:

# V = vertices
# E = edges
# DFS Applications
# Maze solving
# Cycle detection
# Topological sorting
# Path finding
# 4. Breadth First Search (BFS)

# BFS explores:

# Level by level.

# Uses:

# Queue
# BFS Working

# Example:

#     A
#    / \
#   B   C
#  / \
# D   E

# BFS Traversal:

# A → B → C → D → E
# BFS Algorithm
# 1. Insert start node into queue
# 2. Visit node
# 3. Add neighbors to queue
# 4. Repeat until queue empty
# BFS Characteristics
# Feature	Value
# Data Structure	Queue
# Complete	Yes
# Optimal	Yes (for equal cost)
# Memory	More
# Fast for shallow solution	Yes
# BFS Time Complexity
# O(V+E)
# BFS Applications
# Shortest path
# GPS navigation
# Social networks
# Web crawling
# DFS vs BFS
# Feature	DFS	BFS
# Data Structure	Stack	Queue
# Traversal	Depth-wise	Level-wise
# Memory	Less	More
# Optimal	No	Yes
# Complete	No	Yes
# Practical 2: A* Algorithm
# 1. What is A* Algorithm?

# A* is:

# An informed search algorithm used to find the shortest path.

# Used in:

# Games
# Robotics
# Maps
# AI navigation
# A* Formula

# f(n)=g(n)+h(n)

# Where:

# g(n) = actual cost from start
# h(n) = heuristic estimated cost to goal
# f(n) = total estimated cost
# Heuristic Function

# Heuristic means:

# Intelligent guess to reach goal faster.

# Example:

# Straight-line distance
# Manhattan distance
# A* Steps
# 1. Start from source node
# 2. Calculate f(n)
# 3. Choose node with smallest f(n)
# 4. Expand node
# 5. Repeat until goal found
# A* Characteristics
# Feature	Value
# Type	Informed Search
# Uses Heuristic	Yes
# Optimal	Yes
# Complete	Yes
# A* Applications
# Video games
# Robot navigation
# Google Maps
# Route optimization
# Complexity

# Worst case:

# O(b
# d
# )

# Where:

# b = branching factor
# d = depth
# Practical 3: Greedy Algorithms
# 1. What is Greedy Algorithm?

# Greedy algorithm:

# Chooses the best immediate solution at every step.

# Does NOT reconsider previous decisions.

# Greedy Characteristics
# Feature	Value
# Local optimum	Yes
# Fast	Yes
# Memory efficient	Yes
# Always globally optimal	No
# 2. Selection Sort
# Concept

# Repeatedly selects smallest element.

# Example:

# 64 25 12 22 11

# After sorting:

# 11 12 22 25 64
# Complexity

# O(n
# 2
# )

# 3. Minimum Spanning Tree (MST)

# MST:

# Connects all vertices with minimum total edge cost.

# Conditions:

# No cycles
# All nodes connected
# Applications
# Network design
# Road construction
# Cable layout
# 4. Prim’s Algorithm

# Prim’s:

# Expands tree one node at a time.

# Uses:

# Priority queue
# Prim’s Steps
# 1. Start from any node
# 2. Select minimum edge
# 3. Add new vertex
# 4. Repeat
# Complexity
# O(ElogV)
# 5. Kruskal’s Algorithm

# Kruskal’s:

# Selects smallest edge globally.

# Uses:

# Sorting
# Union-Find
# Kruskal’s Steps
# 1. Sort edges
# 2. Pick smallest edge
# 3. Avoid cycle
# 4. Repeat
# Complexity
# O(ElogE)
# 6. Dijkstra Algorithm

# Dijkstra:

# Finds shortest path from source node.

# Conditions:

# No negative weights
# Working
# 1. Set source distance = 0
# 2. Select minimum distance node
# 3. Update neighbors
# 4. Repeat
# Complexity
# O((V+E)logV)
# 7. Job Scheduling

# Goal:

# Maximize profit with deadlines.

# Strategy:

# Select highest profit jobs first.

# Applications:

# CPU scheduling
# Task management
# Practical 4: CSP using Backtracking & Branch and Bound
# 1. Constraint Satisfaction Problem (CSP)

# CSP:

# Problem where variables must satisfy constraints.

# Components:

# Variables
# Domain
# Constraints
# Examples
# N-Queens
# Sudoku
# Graph coloring
# 2. N-Queens Problem

# Goal:

# Place N queens so that no queen attacks another.

# Rules:

# No same row
# No same column
# No same diagonal
# 3. Backtracking

# Backtracking:

# Try solution → if fails → go back.

# Backtracking Steps
# 1. Place queen
# 2. Check safety
# 3. Recur
# 4. If unsafe → backtrack
# Characteristics
# Feature	Value
# Recursive	Yes
# Efficient than brute force	Yes
# Uses DFS idea	Yes
# Complexity

# Worst case:

# O(N!)
# 4. Branch and Bound

# Branch and Bound:

# Optimization technique using bounds to prune search.

# Idea:

# Ignore impossible branches early.
# Difference
# Feature	Backtracking	Branch & Bound
# Goal	Feasibility	Optimization
# Pruning	Constraint violation	Cost bound
# 5. Graph Coloring

# Goal:

# Color graph using minimum colors such that adjacent nodes differ.

# Applications:

# Compiler design
# Timetable scheduling
# Register allocation
# Practical 5: Elementary Chatbot
# 1. What is Chatbot?

# Chatbot:

# Software that communicates with users automatically.

# Types of Chatbots
# Type	Description
# Rule-based	Uses predefined rules
# AI-based	Uses ML/NLP
# Elementary Chatbot

# Your practical usually uses:

# Rule-based chatbot
# Components
# Component	Work
# Input	User message
# Processing	Match keywords
# Response	Return answer
# Example

# User:

# Hello

# Bot:

# Hi! How can I help you?
# Working
# 1. User enters query
# 2. Program checks condition
# 3. Matching response displayed
# Applications
# Customer support
# Banking
# E-commerce
# Hospital systems
# Advantages
# 24/7 support
# Fast responses
# Reduces human work
# Limitations
# Cannot think like humans
# Limited understanding
# Depends on predefined rules
# Important Viva Questions
# DFS/BFS
# Difference between DFS and BFS?
# Which data structure is used in BFS?
# Which algorithm gives shortest path?
# Time complexity of DFS?
# A*
# What is heuristic function?
# Difference between informed and uninformed search?
# Explain A* formula.
# Where is A* used?
# Greedy
# What is greedy method?
# Difference between Prim and Kruskal?
# Why Dijkstra fails for negative edges?
# Define MST.
# CSP
# What is backtracking?
# Define CSP.
# Explain N-Queens.
# Difference between Branch and Bound and Backtracking?
# Chatbot
# What is chatbot?
# Difference between AI chatbot and rule-based chatbot?
# Applications of chatbot?
# What is NLP?
# Most Important Exam Definitions
# Artificial Intelligence

# AI is the simulation of human intelligence in machines.

# Heuristic

# A heuristic is an intelligent estimate used to solve problems faster.

# CSP

# CSP is a problem where variables satisfy constraints.

# Greedy Algorithm

# Greedy algorithm chooses locally optimal solution at every step.

# Backtracking

# Backtracking is a recursive problem-solving technique that removes invalid solutions.

# 1. What is DFS?
# Answer

# DFS (Depth First Search) is a graph traversal algorithm that explores one branch completely before moving to another branch.

# It uses:

# Stack
# Recursion
# Follow-Up Questions
# Q1. Which data structure is used in DFS?
# Answer

# Stack data structure is used in DFS.

# Q2. Why is recursion used in DFS?
# Answer

# Because recursion internally uses stack memory and helps traverse deep nodes easily.

# Q3. What is the time complexity of DFS?
# Answer

# O(V+E)

# Where:

# V = Vertices
# E = Edges
# Q4. What are applications of DFS?
# Answer
# Maze solving
# Cycle detection
# Topological sorting
# Path finding
# 2. What is BFS?
# Answer

# BFS (Breadth First Search) is a graph traversal algorithm that explores nodes level by level.

# It uses:

# Queue
# Follow-Up Questions
# Q1. Which data structure is used in BFS?
# Answer

# Queue data structure.

# Q2. Why BFS gives shortest path?
# Answer

# Because BFS explores nodes level-wise and reaches the nearest solution first.

# Q3. What is the complexity of BFS?

# O(V+E)

# Q4. Applications of BFS?
# Answer
# Shortest path finding
# GPS navigation
# Social networks
# Web crawling
# 3. Difference Between DFS and BFS
# Feature	DFS	BFS
# Data Structure	Stack	Queue
# Traversal	Depth-wise	Level-wise
# Memory	Less	More
# Optimal	No	Yes
# Complete	No	Yes
# Follow-Up Viva
# Q. Which algorithm consumes more memory?
# Answer

# BFS consumes more memory because it stores all neighboring nodes.

# Q. Which is faster?
# Answer

# Depends on problem:

# DFS is better for deep solutions
# BFS is better for shallow solutions
# Practical 2: A* Algorithm
# 1. What is A* Algorithm?
# Answer

# A* is an informed search algorithm used to find the shortest path using heuristics.

# 2. Explain A* Formula

# f(n)=g(n)+h(n)

# Answer

# Where:

# g(n) = actual path cost
# h(n) = estimated heuristic cost
# f(n) = total estimated cost
# Follow-Up Questions
# Q1. What is heuristic function?
# Answer

# A heuristic function is an intelligent estimate of distance from current node to goal.

# Q2. Give examples of heuristics.
# Answer
# Manhattan distance
# Euclidean distance
# Straight-line distance
# Q3. Why is A* called informed search?
# Answer

# Because it uses heuristic information to guide search.

# Q4. What is uninformed search?
# Answer

# Search without heuristic knowledge.

# Examples:

# DFS
# BFS
# Q5. Applications of A*?
# Answer
# Video games
# Robot navigation
# Maps
# Route optimization
# Q6. Is A* optimal?
# Answer

# Yes, if heuristic is admissible.

# Q7. What is admissible heuristic?
# Answer

# A heuristic that never overestimates actual cost.

# Practical 3: Greedy Algorithms
# 1. What is Greedy Algorithm?
# Answer

# Greedy algorithm selects the best immediate solution at each step without reconsidering previous choices.

# Follow-Up Questions
# Q1. Does greedy always give optimal solution?
# Answer

# No, greedy may fail for some problems.

# Q2. Advantages of greedy algorithms?
# Answer
# Fast
# Simple
# Memory efficient
# Q3. Disadvantages?
# Answer

# May not produce globally optimal solution.

# 2. What is Minimum Spanning Tree (MST)?
# Answer

# MST is a tree connecting all vertices with minimum total edge weight and no cycles.

# Follow-Up Questions
# Q1. Applications of MST?
# Answer
# Network design
# Cable connections
# Road construction
# Q2. Properties of MST?
# Answer
# No cycles
# Minimum cost
# Connects all vertices
# 3. Explain Prim’s Algorithm
# Answer

# Prim’s algorithm builds MST by selecting minimum edge connected to existing tree.

# Follow-Up Questions
# Q1. Which data structure is used in Prim’s?
# Answer

# Priority Queue / Min Heap.

# Q2. Time complexity of Prim’s?

# O(ElogV)

# Q3. Is Prim’s greedy?
# Answer

# Yes, because it selects minimum edge locally.

# 4. Explain Kruskal’s Algorithm
# Answer

# Kruskal’s algorithm creates MST by selecting globally smallest edges without forming cycles.

# Follow-Up Questions
# Q1. Which algorithm detects cycles in Kruskal’s?
# Answer

# Union-Find algorithm.

# Q2. Time complexity of Kruskal’s?

# O(ElogE)

# Q3. Difference between Prim’s and Kruskal’s?
# Prim’s	Kruskal’s
# Vertex based	Edge based
# Starts from node	Sorts edges
# Better for dense graph	Better for sparse graph
# 5. Explain Dijkstra Algorithm
# Answer

# Dijkstra algorithm finds shortest path from source to all vertices.

# Follow-Up Questions
# Q1. Why Dijkstra fails for negative edges?
# Answer

# Because negative weights can reduce already finalized shortest paths.

# Q2. Time complexity?

# O((V+E)logV)

# Q3. Applications?
# Answer
# GPS navigation
# Network routing
# Maps
# 6. Explain Job Scheduling Problem
# Answer

# Job Scheduling selects jobs to maximize profit within deadlines.

# Follow-Up Questions
# Q1. Why is it greedy?
# Answer

# Because highest profit jobs are selected first.

# Q2. Real-world applications?
# Answer
# CPU scheduling
# Task management
# Resource allocation
# Practical 4: CSP using Backtracking and Branch & Bound
# 1. What is CSP?
# Answer

# Constraint Satisfaction Problem is a problem where variables must satisfy given constraints.

# Follow-Up Questions
# Q1. Components of CSP?
# Answer
# Variables
# Domain
# Constraints
# Q2. Examples of CSP?
# Answer
# Sudoku
# N-Queens
# Graph coloring
# 2. Explain Backtracking
# Answer

# Backtracking tries possible solutions recursively and removes invalid solutions.

# Follow-Up Questions
# Q1. Why is backtracking efficient?
# Answer

# Because it avoids exploring invalid branches completely.

# Q2. What is pruning?
# Answer

# Removing impossible branches from search space.

# Q3. Complexity of N-Queens?

# O(N!)

# 3. Explain N-Queens Problem
# Answer

# Place N queens on chessboard so that no two queens attack each other.

# Follow-Up Questions
# Q1. When do queens attack?
# Answer
# Same row
# Same column
# Same diagonal
# Q2. Which technique is commonly used?
# Answer

# Backtracking.

# 4. Explain Branch and Bound
# Answer

# Branch and Bound is an optimization technique that removes branches using bounds.

# Follow-Up Questions
# Q1. Difference between Backtracking and Branch & Bound?
# Backtracking	Branch & Bound
# Finds feasible solution	Finds optimal solution
# Uses constraints	Uses bounds/cost
# Q2. What is bound?
# Answer

# A limit used to reject non-promising solutions.

# 5. Explain Graph Coloring
# Answer

# Assign colors to graph vertices such that adjacent vertices have different colors.

# Follow-Up Questions
# Q1. Applications of graph coloring?
# Answer
# Timetable scheduling
# Register allocation
# Compiler design
# Q2. What is chromatic number?
# Answer

# Minimum number of colors needed.

# Practical 5: Chatbot
# 1. What is Chatbot?
# Answer

# A chatbot is software that communicates automatically with users.

# Follow-Up Questions
# Q1. Types of chatbots?
# Answer
# Rule-based chatbot
# AI-based chatbot
# Q2. Difference between rule-based and AI chatbot?
# Rule-Based	AI-Based
# Fixed rules	Learns automatically
# Limited responses	Intelligent responses
# Simple	Advanced
# 2. What is NLP?
# Answer

# NLP (Natural Language Processing) enables computers to understand human language.

# Follow-Up Questions
# Q1. Applications of NLP?
# Answer
# Chatbots
# Translation
# Voice assistants
# Sentiment analysis
# 3. Explain Working of Elementary Chatbot
# Answer
# 1. User enters message
# 2. Program checks keywords
# 3. Matching response displayed
# Follow-Up Questions
# Q1. Which programming concepts are used?
# Answer
# if-else
# loops
# string matching
# Q2. Limitations of chatbot?
# Answer
# Cannot think like humans
# Limited understanding
# Depends on predefined rules
# Most Asked External Viva Questions
# 1. What is Artificial Intelligence?
# Answer

# Artificial Intelligence is the simulation of human intelligence by machines.

# 2. Difference between AI and Machine Learning?
# AI	ML
# Broad field	Subset of AI
# Simulates intelligence	Learns from data
# 3. What is Search Space?
# Answer

# Search space is the set of all possible solutions.

# 4. What is Heuristic?
# Answer

# A heuristic is an intelligent estimate used to solve problems faster.

# 5. Define Agent in AI.
# Answer

# An agent is an entity that perceives environment and takes actions.

# 6. What is Rational Agent?
# Answer

# A rational agent takes actions that maximize performance.

# 7. What is State Space?
# Answer

# Collection of all possible states of a problem.

# 8. What is Optimization?
# Answer

# Finding best possible solution among many solutions.

# 9. Difference between Complete and Optimal Algorithm?
# Complete	Optimal
# Finds solution if exists	Finds best solution
# 10. What is Local Search?
# Answer

# Search technique that improves current solution iteratively.