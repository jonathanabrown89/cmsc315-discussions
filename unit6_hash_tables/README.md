# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

## Implementation and results

I modeled an emulator save-state index with a Python dictionary. I started with an empty dictionary and inserted five save IDs as keys, with a short description for each value. This example tracked save descriptions only; it did not create, load, or change emulator save files.

I looked up IDs 1001 and 1060 with `get()`. I updated 1060 from “Before final stage” to “Final stage checkpoint” without changing the entry count. I then removed 1032 with `pop()` and confirmed the count dropped from five to four.

## Edge cases and performance

I tested a lookup and deletion for missing ID 1065, and a lookup in an empty index. Each operation produced a clear message. The missing deletion left the dictionary unchanged.

I used a separate eight-bucket example to explain collisions: different IDs 12 and 20 both mapped to bucket 4 with remainder-based indexing. They still represented separate saves. In a chained implementation they could share a bucket; in open addressing the second key would probe for another position. That calculation illustrated the concept, not Python’s dictionary internals. With a good key distribution and a controlled load factor, dictionary lookups generally took O(1) on average. Many collisions could force additional checks, with O(n) lookup in the worst case. No timings or internal probe counts were measured.

## Run and verification

I ran `python unit6_hash_tables/unit6_discussion.py` from the repository root using Python 3.11. The script used no third-party packages. I checked the five insertions, both successful lookups, the update and deletion counts, the missing and empty cases, and the toy collision output. I also verified that all five TODO prompts and original source comments were preserved.

Expected output included:

```text
1060: Before final stage
Removed 1032: Castle courtyard
Lookup 1065: Save not found
Delete 1065: Nothing to delete
Save count after missing delete: 4
Empty index lookup: Save not found
IDs 12 and 20 both map to bucket 4 with ID % 8.
```
