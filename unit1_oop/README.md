# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

A Python smart-home lighting example for CMSC 315. The program demonstrates inheritance, class and instance namespaces, shallow and deep copying, and input validation through a general device class and a specialized smart light.

The Unit 1 source is included below. The submission checklist remains local and is not published in this repository.

## Files

- `unit1_discussion.py` - device classes, demonstrations, and assertion-based tests.
- `README.md` - project overview, run instructions, and verification notes.
- `submission_checklist.md` (local project root only) - checklist for the weekly discussion submission.

## Requirements

- Python 3; verified with Python 3.11.
- Standard-library `copy` module. No third-party packages are required.

## Run

From the `unit1_oop` directory, run:

```powershell
python unit1_discussion.py
```

The program displays the parent and child objects, runs the namespace and copying demonstrations, and executes the additional tests. The `__main__` guard keeps these demonstrations from running on import.

## What it demonstrates

- **Parent class:** `ParentClass` defines the shared `category` class variable, the `name` and `location` instance variables, a constructor, and `display_info()`.
- **Inheritance:** `ChildClass` calls `super().__init__()`, adds `device_type`, `brightness`, and `settings`, and overrides `display_info()` while reusing the parent method.
- **Namespaces:** two lights access `device_type` through the class and an object. Only one receives a dynamic `nickname` attribute. Instance and class `__dict__` output shows where attributes and methods are stored.
- **Copying:** the original light's nested schedule is shared with its shallow copy. Appending `23:00` affects both; the deep copy retains its independent schedule. Reassigning the original brightness from 70 to 25 leaves both copies at 70.
- **Extension:** `night_mode()` sets brightness to 10 through the existing validation method.
- **Validation:** `set_brightness()` accepts integers from 0 through 100. Out-of-range values raise `ValueError`; incorrect types, including booleans, raise `TypeError`. Attributes remain directly accessible, so validation applies through this method rather than strict access restriction.

This device model illustrates reusing common behavior across specialized connected devices. Separately constructed lights have independent settings. Shallow copies reuse nested references; deep copies allocate independent nested structures and require additional memory. The demonstration compares references and output, without measuring memory usage.

## Verification

The program was executed with Python 3.11 and exited with code `0`. All included assertions passed:

- Namespace isolation and class-variable access.
- Shared shallow-copy settings and independent deep-copy settings.
- Inheritance and brightness boundaries of `0` and `100`.
- Independent settings for separately constructed lights.
- Rejection of `-1`, `101`, `"50"`, `50.5`, and `True` without changing the previous brightness.
- Night mode setting one light to `10` without changing another light.

Successful output includes:

```text
Namespace tests passed.
Copying tests passed.
All additional tests passed.
=== Assignment Execution Complete ===
```

These checks cover the included demonstrations and test cases; they do not establish correctness for every possible input.

## Discussion submission

The assignment also requires a 150-200-word initial reflection in LEO covering concepts learned, challenges and solutions, OOP versus procedural programming, and maintainability and reusability in relation to overhead, practical development, and future use. Follow the local project's `submission_checklist.md` for the remaining submission steps.
