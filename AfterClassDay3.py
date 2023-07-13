#Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.
from itertools import chain

def flatten_and_sort(arr):
    flattened = list(chain.from_iterable(arr))  # Flatten the array
    sorted_arr = sorted(flattened)  # Sort the flattened array
    return sorted_arr

array = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
result = flatten_and_sort(array)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# How does this solution ensure data immutability?
# The solution avoids mutating the original data and instead creates new data structures or iterators.

# Is this solution a pure function? Why or why not?
# The provided solution is not a pure function. A pure function is a function that, given the same inputs, always produces the same output and has no side effects.

# Is this solution a higher order function? Why or why not?
# No, the provided solution is not a higher-order function. A higher-order function is a function that either takes one or more functions as arguments or returns a function as its result.

# Would it have been easier to solve this problem using a different programming style?
# In the case of flattening and sorting an array, the provided solution already employs functional programming constructs like list comprehension, the sorted() function, and the chain.from_iterable() function. These constructs are well-suited for solving this problem in a functional programming style.

# Why in particular is functional programming a helpful paradigm when solving this problem?
# Functional programming is particularly helpful when solving the problem of flattening and sorting an array due to its key characteristics and concepts like: Immutability, and list comprehension.


# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
  
  def boost(self):
    self.max_speed *= 2

# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)

  def flame_jet(self,other):
    other.condition = "trashed"

# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
#       Encapsulation: Demonstrated by the classes used (Podracer, AnakinsPod, and SebulbasPod) and the attributes that get 'Encapsulated' in the classes.
#       Abstraction: This is not  really shown in the code.
#       Inheritance: This is demonstrated with AnakinsPod and SebulbasPod as they inherit the attributes and methods defined in the Podracer class.
#       Polymorphism: This is demonstrated with AnakinsPod and SebulbasPod as they are treated like the Podracer class which is the base class. This also means a Podracer object variable can be 'AnakinsPod' or 'SebulbasPod'.
# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    # I think this question is very subjective. Me personally I am more comfortable with OOP as it provides structure and code reusability.

# How in particular did Object Oriented Programming assist in the solving of this problem?
    # Object-oriented programming assisted in the solving of this problem by allowing me to structure my code in a way to allow modularity. It also lets me reuse code in other classes using inheritance which avoids duplicating code.