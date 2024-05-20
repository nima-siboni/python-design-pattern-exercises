Here is a short description of the strategy patter, (common) situation where it is needed, and
finally to which object orientated programming principles this design pattern is related.

# Concept

The strategy pattern is a behavioral design pattern that allows you to define a family of algorithms
(strategies) and encapsulate them in separate classes. These strategies are interchangeable,
enabling clients to select different algorithms at runtime without modifying their code.

# Structure

* Strategy Interface: This abstract class defines the common interface for all concrete strategies.
It specifies the method(s) that clients will call to invoke the algorithm behavior.
* Concrete Strategies: These classes implement the specific algorithms and provide the actual logic
for the operations defined in the interface.
* Context Class:
Holds a reference to a concrete strategy object. Delegates the execution of the algorithm to the linked strategy object.
May allow clients to replace the currently used strategy with a different one at runtime.

# Identification

Here are some indicators suggesting the use of the strategy pattern:

* Your code contains a set of conditional statements (e.g., if-else) that determine which algorithm to use based on different conditions.
* You need to extend the functionality of a class by adding new algorithms, but inheritance becomes cumbersome or inflexible.
* You want to decouple the algorithm selection from the code that uses it, promoting loose coupling and testability.

# Object Oriented Programming Principles

The strategy pattern adheres to several key principles of object-oriented programming:

* Open/Closed Principle: The context class can be extended with new strategies without modifying its existing code.
* Single Responsibility Principle: Concrete strategies encapsulate specific algorithms, promoting modularity and reusability.
* Liskov Substitution Principle: Subclasses (concrete strategies) can be used wherever their base class (strategy interface) is expected, ensuring type safety.
