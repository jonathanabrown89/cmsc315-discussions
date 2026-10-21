
"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    """Represent a general smart-home device."""

    category = "Smart Home Device"

    def __init__(self, name: str, location: str):
        # Instance variables store information unique to each device.
        self.name = name
        self.location = location

    def display_info(self):
        """Return the device's identifying information."""
        return f"Device: {self.name}, Location: {self.location}"

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    """Represent a smart light with adjustable settings."""

    device_type = "Smart Light"

    def __init__(self, name: str, location: str, brightness: int):
        # Initialize inherited attributes using the parent constructor.
        super().__init__(name, location)

        # Each light receives its own brightness and settings dictionary.
        self.brightness = 0
        self.settings = {"schedule": ["07:00", "22:00"]}
        self.set_brightness(brightness)

    def set_brightness(self, brightness: int):
        """Update brightness only when the value is valid."""

        # Reject incorrect types, including booleans.
        if type(brightness) is not int:
            raise TypeError("Brightness must be an integer.")

        # Restrict brightness to the supported range.
        if not 0 <= brightness <= 100:
            raise ValueError("Brightness must be between 0 and 100.")

        self.brightness = brightness

    def night_mode(self):
        """Custom extension: reduce brightness for nighttime use."""
        self.set_brightness(10)

    def display_info(self):
        """Override the parent method to include light-specific details."""

        # Reuse the parent's information instead of duplicating it.
        parent_info = super().display_info()
        schedule = ", ".join(self.settings["schedule"])

        return (
            f"{parent_info}, "
            f"Type: {self.device_type}, "
            f"Brightness: {self.brightness}%, "
            f"Schedule: [{schedule}]"
        )


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    """Compare shared class attributes and individual object attributes."""

    print("\n=== Namespace Demonstration ===")

    light1 = ChildClass("Desk Light", "Office", 75)
    light2 = ChildClass("Bedroom Light", "Bedroom", 40)

    # Both expressions access the same class variable.
    print("Class access:", ChildClass.device_type)
    print("Object access:", light1.device_type)

    # The parent class variable is inherited by child objects.
    print("Inherited category:", light1.category)

    # Add a new attribute to only the first instance.
    light1.nickname = "Reading Lamp"

    # Instance namespaces contain attributes assigned to each object.
    print("\nLight 1 namespace:", light1.__dict__)
    print("Light 2 namespace:", light2.__dict__)

    # Class namespaces contain class variables and defined methods.
    print("\nParent class namespace:",
          sorted(ParentClass.__dict__.keys()))

    print("Child class namespace:",
          sorted(ChildClass.__dict__.keys()))

    # Verify that the objects maintain separate namespaces.
    assert hasattr(light1, "nickname")
    assert not hasattr(light2, "nickname")
    assert light1.device_type == ChildClass.device_type

    print("\nNamespace tests passed.")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    """Show how shallow and deep copies handle nested mutable data."""

    print("\n=== Copy Demonstration ===")

    original = ChildClass("Hall Light", "Hallway", 70)

    # Shallow copy: separate outer object, shared nested references.
    shallow = copy(original)

    # Deep copy: separate object with independent nested mutable data.
    deep = deepcopy(original)

    print("\nBefore modification:")
    print("Original:", original.display_info())
    print("Shallow:", shallow.display_info())
    print("Deep:", deep.display_info())

    # Mutate the nested schedule shared with the shallow copy.
    original.settings["schedule"].append("23:00")

    # Reassigning brightness changes only the original object's value.
    original.set_brightness(25)

    print("\nAfter modification:")
    print("Original:", original.display_info())
    print("Shallow:", shallow.display_info())
    print("Deep:", deep.display_info())

    # Confirm the shallow copy shares nested settings.
    assert shallow is not original
    assert shallow.settings is original.settings

    # Confirm the deep copy has independent nested settings.
    assert deep.settings is not original.settings

    assert shallow.settings["schedule"] == [
        "07:00", "22:00", "23:00"
    ]

    assert deep.settings["schedule"] == [
        "07:00", "22:00"
    ]

    assert shallow.brightness == 70
    assert deep.brightness == 70
    assert original.brightness == 25

    print("\nCopying tests passed.")


# Additional testing beyond the starter requirements.
def run_tests():
    """Test inheritance, independent data, and invalid inputs."""

    print("\n=== Additional Tests ===")

    light1 = ChildClass("Test Light 1", "Office", 0)
    light2 = ChildClass("Test Light 2", "Bedroom", 100)

    # Verify inheritance and valid brightness boundaries.
    assert isinstance(light1, ParentClass)
    assert light1.brightness == 0
    assert light2.brightness == 100

    print("Inheritance and boundary tests passed.")

    # Changes to one device's settings must not affect another.
    light1.settings["schedule"].append("12:00")

    assert light2.settings["schedule"] == [
        "07:00", "22:00"
    ]

    print("Independent settings test passed.")

    # Test numeric values outside the permitted range.
    for invalid in (-1, 101):
        try:
            light1.set_brightness(invalid)
        except ValueError:
            print(f"Rejected invalid brightness: {invalid}")
        else:
            raise AssertionError("Invalid brightness was accepted.")

    # Test incorrect data types.
    for invalid in ("50", 50.5, True):
        try:
            light1.set_brightness(invalid)
        except TypeError:
            print(f"Rejected invalid type: {invalid!r}")
        else:
            raise AssertionError("Invalid data type was accepted.")

    # Rejected inputs must leave the previous brightness unchanged.
    assert light1.brightness == 0

    # Verify the original night-mode extension.
    light1.night_mode()

    assert light1.brightness == 10
    assert light2.brightness == 100

    print("Night mode test passed.")
    print("\nAll additional tests passed.")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    """Execute the required demonstrations and additional tests."""

    print("=== Unit 1 OOP Assignment ===")

    # Demonstrate the parent class and its information method.
    print("\n=== Parent Object ===")

    parent = ParentClass("Home Hub", "Living Room")

    print(parent.display_info())
    print("Category:", ParentClass.category)

    # Demonstrate inheritance and overridden child behavior.
    print("\n=== Child Object ===")

    child = ChildClass("Reading Light", "Office", 80)

    print(child.display_info())

    # Demonstrate the student-created night-mode extension.
    child.night_mode()

    print("After night mode:", child.display_info())

    # Run the remaining required demonstrations.
    demonstrate_namespaces()
    demonstrate_copying()

    # Verify additional edge cases and independent object behavior.
    run_tests()

    print("\n=== Assignment Execution Complete ===")


# Run demonstrations only when this file is executed directly.
if __name__ == "__main__":
    main()
