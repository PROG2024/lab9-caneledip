"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""


class SingletonCounterMeta(type):
    """Singleton metaclass for the Counter class."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Counter(metaclass=SingletonCounterMeta):
    """A Counter class."""

    def __init__(self):
        """Initiate counter."""
        self.__count = 0

    def __str__(self):
        """Counter string value."""
        return f"{self.__count}"

    def count(self):
        """Return count value."""
        return self.__count

    def increment(self):
        """Increase counter count."""
        self.__count += 1
        return self.__count
