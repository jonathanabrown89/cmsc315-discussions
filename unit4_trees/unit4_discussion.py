"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (JAB):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (JAB):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (JAB):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (JAB):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if node is None:
            return Node(value)

        # Smaller values belong on the left and larger values on the right.
        # Equal values leave the tree unchanged so each key appears once.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        return node

    def search(self, value, visited=None):
        """
        TODO (JAB):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        return self._search_recursive(self.root, value, visited)

    def _search_recursive(self, node, value, visited=None):
        """
        TODO (JAB):
        Implement recursive BST search.
        """
        if node is None:
            return False

        # Record each node checked when the caller asks to see the search path.
        if visited is not None:
            visited.append(node.value)
        if value == node.value:
            return True

        # Ordering rules let each comparison skip an entire subtree.
        if value < node.value:
            return self._search_recursive(node.left, value, visited)
        return self._search_recursive(node.right, value, visited)

    def inorder(self):
        """
        TODO (JAB):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (JAB):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return

        # Visiting smaller values first and larger values last sorts the result.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (JAB): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    tree = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        tree.insert(value)
    print(f"Insertion order: {values}")

    # ===============================
    # TODO (JAB): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print(f"Sorted values: {tree.inorder()}")

    # ===============================
    # TODO (JAB): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    # 20 and 60 are present on different sides of the root.
    # 35 and 90 lead to empty child references.
    for value in (20, 60, 35, 90):
        result = "found" if tree.search(value) else "not found"
        print(f"Search for {value}: {result}")

    # ===============================
    # TODO (JAB): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    empty_tree = BST()
    # The empty root triggers the base case for both operations.
    print(f"Empty tree traversal: {empty_tree.inorder()}")
    print(f"Empty tree search for 50: {empty_tree.search(50)}")

    # A duplicate key leaves the original node in place.
    tree.insert(50)
    print(f"After inserting duplicate 50: {tree.inorder()}")

    print("\n=== EMULATOR SAVE-STATE LOOKUP ===")
    # This example indexes save-state IDs for an emulator project.
    # The BST handles ID lookups while a dictionary holds save descriptions.
    save_states = {
        1050: "Mid-game checkpoint",
        1025: "First area cleared",
        1075: "Boss encounter",
        1001: "Starting position",
        1035: "Manual backup",
        1060: "Before final stage",
        1090: "Post-game checkpoint",
    }
    save_state_index = BST()
    # Inserting the middle ID first places smaller and larger IDs on both sides.
    for save_id in save_states:
        save_state_index.insert(save_id)
    print(f"Save-state IDs in order: {save_state_index.inorder()}")

    # Look up an existing save and an ID that was never added.
    for save_id in (1060, 1065):
        if save_state_index.search(save_id):
            print(f"Save state {save_id}: {save_states[save_id]}")
        else:
            print(f"Save state {save_id}: no matching save state")

    print("\n=== INSERTION ORDER COMPARISON ===")
    sequential_index = BST()
    ordered_ids = save_state_index.inorder()
    for save_id in ordered_ids:
        sequential_index.insert(save_id)

    print(f"Middle-first insertion: {list(save_states)}")
    print(f"Sequential insertion: {ordered_ids}")
    # Both trees hold the same save IDs, but ascending insertion forms a right chain.
    # Each BST search follows one branch, reducing work only when the tree is short.
    # Count nodes visited to show why insertion order affects performance.
    for label, index in (("Balanced", save_state_index), ("Sequential", sequential_index)):
        visited = []
        index.search(1090, visited)
        print(f"{label} search for 1090: {len(visited)} nodes visited {visited}")


if __name__ == "__main__":
    main()