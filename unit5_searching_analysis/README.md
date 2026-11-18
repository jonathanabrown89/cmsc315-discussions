# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Implementation and results

I kept the original two-argument calls working. Both searches returned a matching index or `-1` when the target was missing. Linear search checked the list from the beginning and returned the first matching index. Binary search used inclusive `low` and `high` bounds, checked the midpoint, and excluded the midpoint when narrowing the remaining range. For duplicate values, binary search returned a matching index without promising the first occurrence. Neither algorithm sorted or modified its input.

I added an optional `stats` dictionary to count elements examined while preserving the index return value. Each iteration increased one scalar counter. I counted visited elements rather than individual `==` and `<` operations, and I kept printing outside the two search functions. I did not store a complete search trace or use elapsed timings.

The small sorted dataset contained seven save-state IDs. The large dataset contained 100,000 IDs from `100001` through `200000`. These were actual results from running the implementation.

| Dataset | Target | Linear index | Binary index | Linear elements checked | Binary elements checked |
| --- | ---: | ---: | ---: | ---: | ---: |
| Seven sorted IDs | 1060 | 4 | 4 | 5 | 3 |
| Seven sorted IDs | 1065, missing | -1 | -1 | 7 | 3 |
| 100,000 sorted IDs | 200000, last ID | 99999 | 99999 | 100,000 | 17 |
| 100,000 sorted IDs | 200001, missing | -1 | -1 | 100,000 | 17 |

The first-position edge case also showed why binary search was not always faster. Linear search found ID `1001` after examining one element, while binary search examined three. A target at the initial midpoint gave binary search its own one-element best case.

## Emulator save-state application

I continued the emulator example from Unit 4 with the same modeled save IDs and descriptions. I used linear search on the original arrival-order ID list and prepared a separate sorted ID list once for binary search. Searching for ID `1060` returned arrival index `5` and sorted index `4`. Both indices identified the same save, `Before final stage`. ID `1065` returned `-1` from both searches.

I checked for `-1` before indexing because Python otherwise interpreted that index as the last element. I also checked that sorting a copy left the arrival-order list unchanged. The dictionary supplied a description only after the search located the ID; it did not replace either search algorithm. The example modeled an index and did not create or load emulator save files.

At the application boundary, `lookup_save_id()` rejected text, `None`, booleans, and negative IDs with a `ValueError`. This constant-time target validation remained separate from the generic algorithms. The search functions expected an indexable collection; binary search additionally required ascending order and consistent comparisons between the stored keys and target. I kept that sorted-input precondition explicit instead of adding an O(n) validation scan to every binary search.

## Performance and preparation tradeoffs

For the bounded numeric IDs in the demonstration, linear search had O(n) worst-case lookup time and binary search had O(log n) worst-case lookup time. Both had O(1) best-case lookup time and O(1) auxiliary search space, including the optional counter. Binary search gained its advantage by discarding approximately half of the remaining candidates at every unsuccessful midpoint check.

The visit counts excluded dataset creation and sorting. In the emulator example, preparing the sorted copy added up to O(n log n) comparison-sort work and O(n) storage for the copy. Repeated searches could justify that preparation, but a one-time lookup in an unsorted batch of imported saves could favor linear search. Constant changes to the collection could also add maintenance costs to the sorted view.

Binary search could not reliably eliminate half the candidates when the data was unsorted, was sorted by a different key, or lacked a consistent ordering rule. A list ordered by save ID did not support binary search by description without a separate appropriately ordered view. A stream required buffering for this indexed implementation, and a linked list lacked the constant-time midpoint access that supported the same O(log n) time bound. These access limitations reduced suitability; they did not make every form of binary search on linked structures conceptually impossible.

## Verification

I ran the completed program with Python 3.12.14 and no third-party packages. I used explicit assertion checks that raised `AssertionError` for an unexpected result, so the checks also remained active with Python optimization enabled.

All twelve paired edge-case demonstrations passed. I verified empty lists, a singleton hit, singleton misses below and above the value, first/middle/last positions, missing values within and outside the range, duplicate IDs, and sorted text keys. I checked that linear search returned the first occurrence, that binary search returned a valid matching occurrence, and that neither search changed its input.

I also verified all four invalid-ID cases through the application wrapper. The real-world demonstration exercised linear search on unsorted IDs, binary search on a sorted copy, a successful lookup, and a missing lookup. No case indexed a list using the not-found sentinel.

## Run and sample output

I ran the following command from the repository root.

```text
python3 unit5_searching_analysis/unit5_discussion.py
```

From inside the Unit 5 folder, I used `python3 unit5_discussion.py`. The file required no external packages. These excerpts came from the completed run.

```text
=== LARGE DATASET TEST ===
TODO: Create a larger dataset and compare results.
Sorted ID count: 100,000; range: 100001 through 200000
Target 200000: linear index 99999, 100,000 elements checked; binary index 99999, 17 elements checked.
Target 200001: linear index -1, 100,000 elements checked; binary index -1, 17 elements checked.

All 12 paired search cases passed; inputs stayed unchanged.
PASS: Rejected invalid save ID '1060': A save-state ID must be a nonnegative integer.
PASS: Rejected invalid save ID None: A save-state ID must be a nonnegative integer.
PASS: Rejected invalid save ID True: A save-state ID must be a nonnegative integer.
PASS: Rejected invalid save ID -1: A save-state ID must be a nonnegative integer.

=== EMULATOR SAVE-STATE LOOKUP ===
Arrival-order IDs: [1050, 1025, 1075, 1001, 1035, 1060, 1090]
Sorted lookup IDs: [1001, 1025, 1035, 1050, 1060, 1075, 1090]
Save 1060: linear arrival index 5; binary sorted index 4.
Located save: Before final stage
Save 1065: linear arrival index -1; binary sorted index -1.
No matching save state.
The sorted index did not change the original arrival order.
```

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

I continued my emulator save-state example by searching numerical save IDs. Linear search checked IDs in arrival order, while binary search used a sorted copy. Both returned a matching index or -1, and the original order stayed unchanged.

On 100,000 IDs, finding the last ID or confirming an ID above the maximum was missing took 100,000 element checks with linear search and 17 with binary search. Binary search eliminated about half the remaining candidates each time, giving it O(log n) worst-case lookup time compared with O(n) for linear search.

The implementation challenge I addressed was keeping the binary search boundaries correct and checking for -1 before indexing, since Python treats -1 as the last position. I verified empty lists, single items, endpoints, missing values, duplicates, and invalid save IDs.

This showed me why organizing data could reduce search work, but preparation still mattered. Sorting a separate copy took time and extra memory. For a one-time lookup in an unsorted batch of imported saves, linear search remained practical. Binary search would not reliably work on unsorted data, data ordered by a different key, or values without a consistent comparison rule.
