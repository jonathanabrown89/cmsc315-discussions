# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Implementation and results

I built a binary search tree that stored smaller keys in the left subtree and larger keys in the right subtree. Recursive insertion created a node at the first empty position and returned the subtree root so the caller could update its child reference. Recursive search followed one branch at a time and returned `False` when it reached an empty child. In-order traversal visited the left subtree, the node, and the right subtree to collect the keys in ascending order.

I inserted `[50, 30, 70, 20, 40, 60, 80]` and got `[20, 30, 40, 50, 60, 70, 80]` from traversal. Searches found `20` and `60` and returned `False` for `35` and `90`. The empty tree returned an empty traversal and a failed search. Inserting a second `50` left the traversal unchanged because the tree stored each key once.

For the real-world example, I modeled a save-state index inspired by an emulator project I have been developing. The BST stored numerical save-state IDs, while a separate dictionary held the description for each save. Searching for ID `1060` located the save named `Before final stage`, and searching for `1065` showed that no matching save state existed. The example demonstrated an index; it did not create or load actual emulator save files.

I built two trees using the same seven save-state IDs. I inserted the middle ID first in one tree and inserted IDs in ascending order in the other. Searching for `1090` visited three nodes in the balanced tree and all seven nodes in the sequential tree. Both searches returned the same result, but insertion order changed the work required.

Search and insertion took time proportional to the tree height: O(log n) when the BST was balanced, but O(n) in the worst case when sorted save-state IDs formed a chain. A regular BST did not rebalance itself. This was relevant to an emulator because save-state IDs could be created sequentially. In-order traversal took O(n) because it visited every node. Deeply skewed trees could also reach Python's recursion limit; this implementation intentionally kept recursive operations because the assignment required them.

## Run and sample output

I ran the program from the `unit4_trees` folder with Python 3.13 and no third-party packages.

```text
python unit4_discussion.py
```

The program produced this output.

```text
=== UNIT 4: BINARY SEARCH TREES ===

=== TREE CONSTRUCTION ===
Insertion order: [50, 30, 70, 20, 40, 60, 80]

=== IN-ORDER TRAVERSAL ===
Sorted values: [20, 30, 40, 50, 60, 70, 80]

=== SEARCH TESTS ===
Search for 20: found
Search for 60: found
Search for 35: not found
Search for 90: not found

=== EDGE CASES ===
Empty tree traversal: []
Empty tree search for 50: False
After inserting duplicate 50: [20, 30, 40, 50, 60, 70, 80]

=== EMULATOR SAVE-STATE LOOKUP ===
Save-state IDs in order: [1001, 1025, 1035, 1050, 1060, 1075, 1090]
Save state 1060: Before final stage
Save state 1065: no matching save state

=== INSERTION ORDER COMPARISON ===
Middle-first insertion: [1050, 1025, 1075, 1001, 1035, 1060, 1090]
Sequential insertion: [1001, 1025, 1035, 1050, 1060, 1075, 1090]
Balanced search for 1090: 3 nodes visited [1050, 1075, 1090]
Sequential search for 1090: 7 nodes visited [1001, 1025, 1035, 1050, 1060, 1075, 1090]
```

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

For Unit 4, I built a binary search tree in Python using recursive insertion, searching, and in-order traversal. Smaller values went left, larger values went right, and in-order traversal returned values in ascending order. I tested empty trees, missing keys, and duplicates to verify the implementation.

For the real-world application, I modeled save-state indexing for an emulator project I've been developing. The BST organized numerical save-state IDs, while a dictionary stored the associated information.

One challenge I explored was how insertion order affected the tree's structure and efficiency. Both trees held the same seven IDs and found the same save state, but their search paths differed. I compared middle-first insertion against sequential insertion and counted the nodes visited when searching for 1090. The balanced tree checked three nodes; the sequential tree checked seven.

This demonstrated why a balanced BST can search in O(log n) time rather than the O(n) time needed for a linear search through an unsorted list. Sequential insertion can create a chain, increasing BST search time to O(n). Since save-state IDs may be generated sequentially, I would consider a self-balancing tree for a larger indexing system.
