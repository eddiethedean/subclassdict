"""Shared test fixtures and configuration."""

import pytest


@pytest.fixture
def animal_hierarchy():
    """Create a simple class hierarchy for testing."""

    class Animal:
        pass

    class Mammal(Animal):
        pass

    class Dog(Mammal):
        pass

    class Cat(Mammal):
        pass

    class Puppy(Dog):
        pass

    class Bird(Animal):
        pass

    return {
        "Animal": Animal,
        "Mammal": Mammal,
        "Dog": Dog,
        "Cat": Cat,
        "Puppy": Puppy,
        "Bird": Bird,
    }


@pytest.fixture
def multiple_inheritance_hierarchy():
    """Create a multiple inheritance hierarchy for testing."""

    class A:
        pass

    class B:
        pass

    class C(A, B):
        pass

    class D(C):
        pass

    return {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
    }
