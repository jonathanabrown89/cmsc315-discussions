"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

# Author: JAB
# The original instructional prompts were retained; their implementations follow.


def linear_search(lst, target, stats=None):
    """
    TODO (JAB):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Optional statistics preserve the original index-or--1 return value.
    # Count elements examined, not individual equality/ordering operations.
    if stats is not None:
        stats["elements_checked"] = 0

    # A missing target requires checking all n elements: O(n) worst-case time.
    # An immediate match takes O(1). No sorting or extra list is needed.
    for index, value in enumerate(lst):
        if stats is not None:
            stats["elements_checked"] += 1
        if value == target:
            return index

    # This also handles an empty list because the loop never starts.
    return -1


def binary_search(lst, target, stats=None):
    """
    TODO (JAB):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    if stats is not None:
        stats["elements_checked"] = 0
    low = 0
    high = len(lst) - 1

    # Bounds are inclusive. With an empty list, high is -1 and no access occurs.
    while low <= high:
        mid = low + (high - low) // 2
        value = lst[mid]
        if stats is not None:
            stats["elements_checked"] += 1

        if value == target:
            # With duplicate keys, any matching index satisfies this contract.
            return mid
        if value < target:
            # Sorted order rules out the midpoint and everything to its left.
            low = mid + 1
        else:
            # Sorted order rules out the midpoint and everything to its right.
            high = mid - 1

    # Halving the remaining range gives O(log n) worst-case search time.
    # Index bounds and the optional scalar count use O(1) auxiliary space.
    return -1


def compare_searches(values, target):
    """Print actual element counts for both searches on the same sorted list."""
    linear_stats = {}
    binary_stats = {}
    linear_index = linear_search(values, target, linear_stats)
    binary_index = binary_search(values, target, binary_stats)
    print(
        f"Target {target!r}: linear index {linear_index}, "
        f"{linear_stats['elements_checked']:,} elements checked; "
        f"binary index {binary_index}, "
        f"{binary_stats['elements_checked']:,} elements checked."
    )
    return linear_index, binary_index


def lookup_save_id(save_ids, save_id, search_function):
    """Validate an application's ID before calling either reusable search."""
    # Reject text, booleans, None, and negative IDs without scanning the data.
    # The application supplies an already sorted list when choosing binary search.
    if type(save_id) is not int or save_id < 0:
        raise ValueError("A save-state ID must be a nonnegative integer.")
    return search_function(save_ids, save_id)


def check(condition, description):
    """Fail a demonstration check even if Python optimization is enabled."""
    if not condition:
        raise AssertionError(description)


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (JAB): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")
    small_ids = [1001, 1025, 1035, 1050, 1060, 1075, 1090]
    print(f"Sorted save-state IDs: {small_ids}")
    # ID 1060 is at index 4. ID 1065 falls in a gap and must return -1.
    check(compare_searches(small_ids, 1060) == (4, 4), "Small dataset hit")
    check(compare_searches(small_ids, 1065) == (-1, -1), "Small dataset miss")

    # ===============================
    # TODO (JAB): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")
    # Prepare the data before measuring the search work; range is already ordered.
    large_ids = list(range(100001, 200001))
    print(f"Sorted ID count: {len(large_ids):,}; range: 100001 through 200000")
    # The last ID and an absent ID both require a full linear scan.
    # Binary search keeps halving the candidates instead of advancing one by one.
    check(compare_searches(large_ids, 200000) == (99999, 99999), "Large dataset hit")
    check(compare_searches(large_ids, 200001) == (-1, -1), "Large dataset miss")

    # ===============================
    # TODO (JAB): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")
    # Each expected linear index describes the first occurrence, or a missing key.
    # Binary search may return another correct index when keys are duplicated.
    cases = [
        ("Empty list", [], 1060, -1),
        ("Singleton hit", [1060], 1060, 0),
        ("Singleton miss below", [1060], 1059, -1),
        ("Singleton miss above", [1060], 1061, -1),
        ("First position", small_ids, 1001, 0),
        ("Middle position", small_ids, 1050, 3),
        ("Last position", small_ids, 1090, 6),
        ("Missing between IDs", small_ids, 1065, -1),
        ("Missing below minimum", small_ids, 999, -1),
        ("Missing above maximum", small_ids, 1100, -1),
        ("Duplicate IDs", [1001, 1060, 1060, 1060, 1090], 1060, 1),
        ("Sorted text keys", ["auto", "backup", "manual"], "backup", 1),
    ]
    for label, values, target, expected in cases:
        original = values.copy()
        linear_index, binary_index = compare_searches(values, target)
        check(linear_index == expected, f"{label}: incorrect linear result")
        if expected == -1:
            check(binary_index == -1, f"{label}: incorrect binary miss")
        else:
            check(0 <= binary_index < len(values), f"{label}: invalid binary index")
            check(values[binary_index] == target, f"{label}: wrong binary match")
        check(values == original, f"{label}: a search changed its input")
        print(f"PASS: {label}")
    print(f"All {len(cases)} paired search cases passed; inputs stayed unchanged.")

    # Application validation is separate from the generic search algorithms.
    for invalid_id in ("1060", None, True, -1):
        try:
            lookup_save_id(small_ids, invalid_id, binary_search)
        except ValueError as error:
            print(f"PASS: Rejected invalid save ID {invalid_id!r}: {error}")
        else:
            raise AssertionError(f"Accepted invalid save ID {invalid_id!r}")

    print("\n=== EMULATOR SAVE-STATE LOOKUP ===")
    # Continue the Unit 4 example using the same modeled IDs and descriptions.
    # These records illustrate searches; they do not load actual emulator files.
    save_states = {
        1050: "Mid-game checkpoint",
        1025: "First area cleared",
        1075: "Boss encounter",
        1001: "Starting position",
        1035: "Manual backup",
        1060: "Before final stage",
        1090: "Post-game checkpoint",
    }
    arrival_ids = list(save_states)
    original_arrival_ids = arrival_ids.copy()
    # Sort once for repeated ID searches. Preserve the original arrival order.
    sorted_ids = sorted(arrival_ids)
    print(f"Arrival-order IDs: {arrival_ids}")
    print(f"Sorted lookup IDs: {sorted_ids}")
    for target in (1060, 1065):
        linear_index = lookup_save_id(arrival_ids, target, linear_search)
        binary_index = lookup_save_id(sorted_ids, target, binary_search)
        print(
            f"Save {target}: linear arrival index {linear_index}; "
            f"binary sorted index {binary_index}."
        )
        # Check -1 before indexing; Python would otherwise select the last item.
        if linear_index == -1:
            check(binary_index == -1, "The missing save ID had a binary match")
            print("No matching save state.")
        else:
            check(0 <= binary_index < len(sorted_ids), "Invalid sorted save index")
            check(
                arrival_ids[linear_index] == sorted_ids[binary_index] == target,
                "Searches located different save IDs",
            )
            print(f"Located save: {save_states[target]}")
    check(arrival_ids == original_arrival_ids, "Arrival order changed")
    print("The sorted index did not change the original arrival order.")

    print("\n=== SEARCH ANALYSIS ===")
    print("Linear search: O(n) worst-case lookup; no sorted input required.")
    print("Binary search: O(log n) worst-case lookup on a sorted Python list.")
    print("Both searches: O(1) auxiliary space, including the scalar visit counter.")
    print("Counts measured examined elements, not elapsed time or sorting work.")
    print("Sorting added preparation work; the sorted copy also used O(n) space.")
    print("One unsorted lookup may favor linear search; repeated lookups may justify sorting.")
    print("Binary search required ordering by the same key used for comparisons.")
    print("A stream or linked list did not provide this list's direct midpoint access.")


if __name__ == "__main__":
    main()
