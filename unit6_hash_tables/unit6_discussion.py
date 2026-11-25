"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


# Author: JAB
def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (JAB): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    # The dictionary hashes each ID so it can look up values without sorting.
    save_states = {}
    for save_id, description in (
        (1001, "Opening checkpoint"),
        (1015, "Forest entrance"),
        (1032, "Castle courtyard"),
        (1060, "Before final stage"),
        (1084, "Final stage complete"),
    ):
        save_states[save_id] = description
    print(f"Inserted {len(save_states)} saves: {save_states}")

    # ===============================
    # TODO (JAB): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    # get() returns the description for a key without scanning an ID list.
    for save_id in (1001, 1060):
        print(f"{save_id}: {save_states.get(save_id)}")

    # ===============================
    # TODO (JAB): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    # Assigning to an existing key replaces its value without adding a slot.
    print(f"Before update: {save_states}")
    save_states[1060] = "Final stage checkpoint"
    print(f"After update ({len(save_states)} saves): {save_states}")

    # ===============================
    # TODO (JAB): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    # pop() removed the entry and returned the description that was stored.
    print(f"Before deletion: {save_states}")
    removed = save_states.pop(1032)
    print(f"Removed 1032: {removed}")
    print(f"After deletion ({len(save_states)} saves): {save_states}")

    # ===============================
    # TODO (JAB): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    # Save descriptions are strings, so None can signal that an ID is absent.
    missing_id = 1065
    print(f"Lookup {missing_id}: {save_states.get(missing_id, 'Save not found')}")
    print(f"Delete {missing_id}: {save_states.pop(missing_id, 'Nothing to delete')}")
    print(f"Save count after missing delete: {len(save_states)}")

    empty_saves = {}
    print(f"Empty index lookup: {empty_saves.get(1001, 'Save not found')}")

    # This toy bucket calculation illustrates a collision, not dict internals.
    print("\n=== COLLISION EXAMPLE ===")
    first, second = 12, 20
    print(f"IDs {first} and {second} both map to bucket {first % 8} with ID % 8.")
    print("Both IDs still represent separate saves.")



if __name__ == "__main__":
    main()