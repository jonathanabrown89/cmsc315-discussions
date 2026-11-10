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

I used employee IDs as keys in a separate example. The BST stored the IDs, and a dictionary held the names for those IDs. I found the record for `1060` and reported a missing record for `1065`.

I built two trees from the same seven employee IDs. I inserted the middle ID first in one tree and inserted the IDs in ascending order in the other. When I searched for `1090`, the balanced tree checked three nodes and the sequential tree checked seven.

Search and insertion took time proportional to the tree height. They took O(log n) in a balanced tree and on average with a randomly ordered set of distinct keys. They could take O(n) in the worst case because sequential insertion formed a chain. In-order traversal took O(n) because it visited every node.

## Run and sample output

I ran the program from the `unit4_trees` folder with Python 3.11 and no third-party packages.

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

=== EMPLOYEE RECORD LOOKUP ===
Employee IDs in order: [1001, 1025, 1035, 1050, 1060, 1075, 1090]
Employee 1060: Sam
Employee 1065: no matching record

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