# My notes of: SW101 - The Book (by Marko)

https://learn.withmarko.com/sw101

- Fundamentals: Strategy, Iterator, Visitor, Builder, Adapter, Facade, Proxy, Dependency Injection

- Performance: Laziness, Stream, Pool, Cache, Look Up Table

- Interaction & Stale: Observer, Delegate, Mediator, Command, CQRS, Chain of Responsibility, Reducer, Selector, Reactive Programming, ECS

- Programming Language: Interpretation, Compilation, JIT, Reference Types, Value Types, Static Types, Dynamic Types, Strong Types, Weak Types, Generics, Garbage Collection, Reference Counting, Error Handling

- The MVs: MVC, MVP, MVVM

- Functional Programming: Closures, Monads, Higher Order Functions, Partial Application, Currying, Immutability, Algebraic Data Types

- Scaling: Load Balancing, Producer / Consumer, Event Sourcing, Sharding, Dead Letter Queue, Edge Computing

- Data Processing: Serde, Marshaling, Hashing, Encryption

- Databases: SQL, NoSQL, Transactions, Views, Indexes, ORM, Query Builder, Migrations

- Concurrency & Parallelism: Concurrent Execution, Parallel Execution, Thread Pool, Lightweight Threads, Semaphore, Scheduler

- Web Services: REST, Middleware, Rate Limiting, Microservices, API Versioning, API Discovery, API Gateway, GraphQL

- Distributed Services: RPC, Message Broker, Eventual Consistency, ETL, Exponential Backoff, Circuit Breaker, Sidecar, Actor, Supervisor, Anti-Fragility

- Infrastructure & Deployment: VPS, Kubernetes, CDK, Serverless, Blue-Green Deployment

- Security: Auth, IAM, RBAC, Sandbox

- Unit Testing, Integration Testing, Functional Testing, Canary


----

## Fundamentals

### 1. Strategy Pattern

An interchangeable part of a more complex system. It allows you to define a family of algorithms, encapsulate each one, and make them interchangeable. It lets the algorithm vary independently from the clients that use it.


### 2. Iterator Pattern

Simplifies traversal of different data structures. It provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.


### 3. Visitor Pattern

The object or function that knows what to do with each element of some data structure, but it is not iterating over the data structure, that's the job of the iterator. The visitor is a separate object that is passed to the data structure and it is called for each element. In contrast to Strategy, the Visitor is not part of the object itself, but it is passed to the object it is visiting.


### 4. Builder Pattern

It serves two purposes, it makes the code more readable, and also helps with resource management at runtime. The Builder is an object whose sole purpose is to construct other objects. It is a separate class that is responsible for creating a complex object with configs, custom rules and validations. In contrast to the Factory Pattern, the Builder is used when the object is complex and requires a lot of configuration, the Factory is used when the object is simple and can be created with a single method call and simplifies the creation of predefined objects.


### 5. Adapter Pattern

Used to make two incompatible interfaces compatible. It is a structural pattern that allows objects with incompatible interfaces to collaborate. It is used when you have two classes that have incompatible interfaces, and you want to make them work together. The Adapter wraps an object and exposes a different interface to it. It is used when you have a class that you want to use, but it doesn't have the interface you need.


### 6. Facade Pattern

Provide uniform, consistent and simplified access to independent and potentially different and complex resources. It is like an adapter that translates from one to many but also simplifying and hidding the complexity of the system.


### 7. Proxy Pattern

Structural design used to create a representative object that controls access to another object, which may be remote (Remote Proxy), expensive to create (Virtual Proxy, Cache Proxy), or in need of scuring (Protection Proxy). It can also augment the behavior of the real subject by adding additional logic before/after forwarding requests to the real subject.

The proxy gateway is a proxy that controls access to the backend. It can be used to rate limit requests, cache responses, and add additional logic to the requests to the backend.

In Lazy Loading, the proxy is used to defer the creation of the real object until it is actually needed. 


### 8. Dependency Injection

Used to implement Inversion of Control (IoC) for resolving dependencies. It allows the creation of dependent objects outside of the object that needs them and provides those objects to a class through different ways. Helps to achieve loose coupling between classes and their dependencies, making the system more modular, testable and maintainable.

We can solve Circular Dependencies by using Setter Injection, Constructor Injection, or Interface Injection. We can also use Interface Segregation to break down large interdependent interfaces into smaller ones that are more specific to the needs of the clients.


-----

## Performance

### 9. Laziness

Delaying a certain operation, until the result of it is needed.It is particularly useful in situations where the said operation is expensive and slow to run. Examples: JS Browser Reflow, Java Streams, Python Generators, etc.


### 10. Stream

A variant of laziness. Refers to processing data without loading it fully into memory. It is particularly useful when dealing with large datasets, where loading the entire dataset into memory would be impractical or impossible.


### 11. Pool

One of the most commonly used patterns when dealing with a number of objects of the same type. It's used in virutally every game and backend service out there. It is used to manage a collection of objects that are created in advance and reused when needed. It is used to reduce the overhead of creating and destroying objects, and to improve performance by reusing objects that are expensive to create.

Examples: video game bullets, vegetation, pedestrians, particle systems, etc.


### 12. Cache

Used to temporarilly save a result of an expensive or long operation. It can substantially improve the performance of the system, but only when we inted to read the result of this operation more frequently than perform the operation itself.


### 13. Look Up Table

Performance optimization technique that trades memory for speed. LUT is different from caching as LUTs are used when the input domain is finite and known in advance. It's also the opposite of laziness, as it precomputes all possible results in advance.



## Interaction & State

### 14. Observer Pattern

Behavioral design pattern that defines a one-to-many dependency between objects. When one object (subject) changes state, all its dependents (observers) are notified and updated automatically. It's fundamental to many event-driven systems and is widely used in user interface toolkits and other reactive programming scenarios. 

Examples: Event Handling in GUIs, Pub/Sub in Messaging Systems, Stock Market Updates, Weather Monitoring, Social Media posts and notifications, Subscriptions, etc.


### 15. Delegate Pattern

A behavioral design pattern that allows an object to delegate some of its responsibilities to another object. This pattern promotes loose coupling between objects and enables a more flexible and modular design. It's widely used in many programming languages and frameworks, particularly in user interface and event-driven programming.

The Delegate pattern is similar to the Observer pattern, but the observer is typically used for asynchronous notifications, while the delegate is used for synchrounous direct interactions.

It's also similar to the Strategy pattern, but the delegate implements multiple methods to handle different responsibilities, while the strategy is focused on implementing a single aspect of behavior.


### 16. Mediator Pattern

Behavioral design pattern that reduces coupling between components of a program by making them communicate indirectly, through a special mediator object. The Mediator serves as a central hub that coordinates actions between different parts of a system.

Examples: Air Traffic Control, Chat Room, GUI Frameworks, Event Bus, etc.

The Mediator pattern is often implemented using the Observer pattern, where the mediator acts as an observer of each component, and the components act as subjects, notifying the mediator of their changes.


### 17. Command Pattern

Behavioral design pattern that turns a request into a stand-alone object containing all information about the request. This transformation allows you to parametrize requests, delay or queue a request's execution, and support undoable operations.

Examples: Implement undo/redo functionality, Queue operations for later exection, Support remote exeucution of operations, Implement transaction-like behavior, etc.


### 18. CQRS (Command Query Responsilibity Segregation) Pattern

Architectural pattern that separates read and write operations for a data store. It suggests using different models to update information and read information. CQRS allows to optimize the performance, scalability, and security of your application by treating reads and writes as separate concerns.

CQRS proposes splitting the application's interface into two parts: Command (write ops: create, update, delete) and Query (read ops: retrieve data). 


### 19. Chain of Responsibility Pattern

Behavioral design pattern that allows passing requests along a chain of handlers. Each handler decides either to process the request or to pass it to the next handler in the chain. Each handler has a reference to the next handler in the chain. Upon receiving a request, it can either process it or pass it to the next handler in the chain.

Examples: Middleware in web frameworks, Event Propagation in GUIs, Exception Handling, Customer Suppoert Escalation, etc.


### 20. Reducer Pattern

Pattern commonly used in state management, particularly in functional programming and front-end frameworks like Redux. It's a pure function that takes the current state and an action as arguments, and returns a new state. Reducers provide a predictable way to manage state transitions in your application.

The Reducer pattern centralizes state management, makes state changes explicit through actions, and ensures that state transitions are pure functions.


### 21. Selector Pattern

Pattern used in state management to efficiently derive and memoize state data. It's commonly used in conjunction with the Reducer pattern and is a key concept in libraries like Redux. Selectors help optimize performance by computing derived state only when the relevant state has changed.


### 22. Reactive Programming

Programming paradigm oriented around data flows and the propagation of change. It allows you to express static or dynamic data flows with ease, and the underlying execution model will automatically propagate changes through the data flow. Reactive Programming makes it easier to create interactive applications that can react to user input, network responses, and other asynchronous events.

Examples: Spreadsheets where cells' changes are automatically propagated, GUI frameworks that react to user input, Web applications that update in real-time, etc.

In Reactive Programming, a key concept is the construction of an acyclic directed graph of dependencies. This graph allows the system to efficiently update only the necessary parts when changes occur.


### 23. ECS (Entity Component System) Pattern

Architectural pattern commonly used in game development and other complex, performance-critical systems. It's designed to allow for high performance in systems with many objects that have different behaviors. Its key concepts are Entities (simple IDs or containers that represent game objects), Components (pure data structures that hold properties but no game logic), Systems (contains the logic that operates on entities with specific components).

This layout allows for efficient memory access and cache utilization. Components of the same type are stored together, enabling fast iteration over all entities with a specific component. ECS significantly improves memory efficiency and cache locality. By organizing components of the same type contiguously in memory, and accessing one component often means that the next one is already in the CPU cache.


----

## Programming Languages

### 24. Interpretation

A method of executing computer programs where the source code is directly executed by an interpreter without prior compilation to machine code.

Examples: Python, Ruby, JavaScript, PHP, Lua, Perl, R


### 25. Compilation

The process of translating source code written in a high-level programming language into machine code or lower-level code that can be directly executed by a computer's processor.

Source Code -> Lexycal Analysis -> Syntax Analysis -> Semantic Analysis -> Intermediate Code -> Code Optimization -> Code Generation -> Linking -> Executable

The compiler produces native machine code for a specific platform.

Examples: C, C++, Rust, Go, Swift, C#, Java, Haskell


### 26. JIT

Technique that combines aspects of both interpretation and compilation. It compiles parts of thec ode to machine code just before they are executed, aiming to combine the flexibility of interpretation with the speed of compiled code. JIT compilation can provide significant performance improvements for long-running programs by optimizing frequently executed code paths.

Examples: JavaScript (V8 engine), C# (.NET CLR), PyPy (for Python), JRuby (for Ruby)


### 27. Reference Types

Data types that store a reference (or address) to their data, rather than the data itself. When you assign a reference type to a variable or pass it as an argument, you're working with a reference to the same data. Reference types allow for efficient handling of large data structures and enable sharing of data across different parts of a program.


### 28. Value Types

Data types that directly contain their data. When you assign a value type to a variable or pass it as an argument, you're working with a copy of the data. Value types are typically stored on the stack, which can lead to better performance for small, simple data structures.


### 29. Static Types

Type system where variable types are known at compile-time. In statically typed languages, you must declare the type of a variable before using it, and the type cannot change during runtime.

Example programming languages: Java, C#, Rust, TypeScript, Go, Scala.

Reflection is a powerful features in many statically types languages that allows programs to inspect and modify their own structure and behavior at runtime. This capability can be particularly useful for frameworks and libraries that rely on metadata to facilitate various functionalities, such as dependency injection.


### 30. Dynamic Types

Type system where variable types are determined at runtime rather than compile-time. In dynamically types languages, you don't need to declare the type of a variable before using it, and the type can change during runtime.

Examples: Python, JavaScript, Ruby, PHP, Lisp, Lua

Weak typing refers to how easily types can be converted implicitly, which is not the same as Dynamic typing which refers to when type checking occurs (runtime vs. compile-time)


### 31. Strong Types

Type system that enforces strict rules about how different data types can interact. In strongly types languages, operations between incompatible types are not allowed wihtout explicit conversion. Strong types helps catch type-related errors early in the development process, often at compile-time.

Examples: Java, C#, Rust, Haskell, TypeScript, Go


### 32. Weak Types

(Also known as loose typing) refers to a type system that allows operations between different types with implicit type conversions. In weakly typed languages, the interpreter or runtime automatically coerces values to the appropriate type when needed. Weak typing can lead to more flexible and concise code, but it may also introduce subtle bugs that are hard to detect.


### 33. Generics

Feature in programming languages that allow the creation of reusable code components that can work with different data types while maintaining type safety. They provide a way to write flexible, reusable code without sacrificing type safety or performance. Generics enable developers to create algorithms and data structures that can operate on various types, promoting code reuse and reducing duplication.


### 34. Garbage Collection

An automatic memory management mechanism that frees the programmer from mamually deallocating memory. It identifies and removes objects that are no longer needed by the program, reclaiming the memory they occupy. Garbage collection helps prevent memory leaks and dangling pointer errors, but it can introduce performance overhead and unpredictable pauses.

Primarily manages objects allocated on the heap, where most dynamic allocations occur.

Examples: Java (JVM), C# (.NET), Python, JS (V8), Go, Ruby, Kotlin, Clojure. 


### 35. Reference Counting

Memory management technique where each object keeps a count of the number of references to it. When the count reaches zero, the object is no longer in use and can be safely deallocated. This approach is used in various programming languages and frameworks to automate memory management. Reference counting provides deterministic cleanup of resources but can struggle with circular references.

Examples: Objective-C, Swift, PHP, Python (CPython), Rust


### 36. Error Handling

A programming language feature that deals with the occurrence of exceptional or unexpected events during program execution. Proper error handling is crucial for creating robust and realiable software. 

Key approaches: 
- Exception-based (try-catch): Java, C#, Python, JS
- Error as values: Go
- Result types: Rust
- Monadic error handling: Haskell


----

## The MVs

### 37. MVC (Model-View-Controller) Pattern

Architectural pattern that separates an application into three main logical components: the Model, the View, and the Controller. Each of these components is built to handle specific development aspects of an application.

- Model: Manages the data, logic, and rules of the application.
- View: Handles the display of data to the user in a passive way.
- Controller: Acts as an intermediary between the Model and the View, processing all the business logic and incoming requests.


### 38. MVP (Model-View-Presenter) Pattern

Architectural pattern derived from MVC, but with key differences that enhance testability and separation of concerns. It separates the presentation logic from the business logic, allowing for more independent development and easier unit testing.

The Presenter in MVP handles presentation logic, while the Controller in MVC primarily coordinates between Model and View. In MVP, the View is more passive and knows nothing about the Model, unlike MVC where the View can sometimes directly interactwith the Model.


### 39. MVVM (Model-View-ViewModel) Pattern

Architectural pattern that facilitates the separation of concerns between the GUI and the business logic or backend logic of an application. MVVM leverages data binding features in UI frameworks to minimize boilerplate code, distinguishing it from MVC and MVP patterns.

The ViewModel acts as an intermediary between the Model and the View, handling the View's display logic and state. Unlike the Presenter in MVP, the ViewModel has no direct reference to the View.

- The View declaratively binds to properties and commands on the ViewModel.
- When the user interacts with the View, it automatically updates the ViewModel through data binding.
- The ViewModel communicates with the Model to retrieve or update data.
- The ViewModel processes data from the Model and exposes it to the View.
- The View automatically updates due to data binding when the ViewModel changes, without explicit calls from the ViewModel (unlike in MVP).


----

## Functional Programming

### 40. Closures

A function that has access to variables in its outer (enclosing) lexical scope, even after the outer function has returned. It "closes over" the variables from its outer scope. Closures allow for data privacy, the creation of function factories, and the implementation of callbacks and higher-order functions.

Some examples are to generate unique ids counting over with a function, memoization functions.

Examples: JS, Swift, Python, Ruby, C#, Java


### 41. Monads

Design Pattern used in functional programming to represent computations with a specific structre. It's a way of wrapping a value (or absense of one) in a context, along with a set of rules for manipulating the context.


### 42. Higher Order Functions

Functions that can take other functions as arguments or return functions as their results. They are a fundamental concept in functional programming and enable powerful abstractions and code reuse. Higher Order Functions allow for more flexible and modular code by treating functions as first-class citizens.


### 43. Partial Application

Refers to the process of fixing a number of arguments to a function, producing another function of smaller arity (number of arguments). It's a technique used in functional programming to create more specialized functions from more general ones. Partial application allows you to create new functions by pre-filling some of the arguments to a function, increasing code reuse and flexibility.

Examples: custom loggers, custom URL builders, ...

```python
# Python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(4))  # 16
print(cube(4))    # 64
``` 


### 44. Currying

Functional programming technique that transforms a function taking multiple args into a series of single-argument functions, returning a new function for each argument until all are provided. This process enhances code reusability and enables powerful function composition techniques.


### 45. Immutability

Core concept in functional programming where data, once created, cannot be changed. Instead of modifying existing data structures, operaions on immutable data create new data structures with the desire changes.


### 46. Algebraic Data Types (ADTs)

Composite types formed by combining other types. They are a fundamental feature in many functional programming languages and provide a powerful way to model complex data structures and domain-specific concepts. ADTs allow for precise modeling of data, enabling compile-time checks and pattern matching, which leads to more robust and expressive code.


----

## Scaling

### 47. Load Balancing

Technique used to distrubute incoming network traffic or computational workloads across multiple servers or resources. It aims to optimize resource utilization, maximize throughput, minimize response time, and avoid overload of any single resource. Load Balancing is crucial for building scalable and highly available systems, ensuring that no single server becomes a bottleneck.


### 48. Producer / Consumer Pattern

Classic design pattern used in concurrent programming. It describes a scenario where one or more producer threads generate data and add it to a shared queue, while one or more consumer threads remove data from queue and process it. This pattern helps decouple data production from its consumption, allowing these processes to operate at different speeds.


### 49. Event Sourcing Pattern

The state of a system is determined by a sequence of events rather than just the current state. Instead of storing the current state of an entity, event sourcing stores a sequence of state-changing events. Event Sourcing provides a complete audit trail and enables powerful features like event replay, temporal queries, and alternative state derivation.


### 50. Sharding Pattern

A Database architecture pattern related to horizontal partitioning - the practice of separating one table's rows into multiple different tables, known as partitions. Each partition has the same schema and columns, but entirely different rows. Likewise, the data held in each shard is unique and independent of other shards. You can think of sharding as loading balancing for your database, distributing the load across multiple servers, which are independent of each other.

Key concepts: Shard Key (the attribute by which data is distributed across shards), Partition Strategy, Shard Balancing, Cross-Shard Operations.

Examples: MongoDB, Apache Cassandra, MySQL Cluster (NDB Storage Engine), PostgreSQL (Citus), Redis Cluster


### 51. Dead Letter Queue (DLQ)

A service implementation to store messages that meet one or more of the following criteria:
- Message that fails to be processed.
- Message that gets processed but fails to be deleted from the source queue.
- Messages that exceed the retention period in the source queue.

DLQ act as a "safety net" for your application, allowing to handle problematic messages without losing them or disrupting the processing of other messages.


### 52. Edge Computing

A distributed computing paradigm that brings computation and data storage closer to the location where it is needed, improving response times and saving bandwidth. By processing data at the edge of the network, edge computing reduces latency and enhances the performance of applications.


----

## Data Processing

### 53. Serialization and Deserialization (Serde)

- Serialization is the process of converting complex data structures or objects into a format that can be easily stored or transmitted.

- Desearialization is the reverse process, reconstructing the data structure or object from the serialized format.

Serde is crucial for data persistance, inter-process communication, and network transmission of complex data structures.



### 54. Marshaling

The process of tranforming the memory representation of an object to a data format suitable for storage or transmission. It's closely related to serialization but often implies a lower-level, language-specific process. Marshaling is crucial for inter-process communication, remote procedure calls (RPC), and object persistence.


### 55. Hashing

Process of converting input data of arbitrary size into a fixed-size output, typically a string of characters or a number. The output, called a hash value or hash code, is unique to the input data.


### 56. Encryption

The process of encoding information in such a way that only authorized parties can access it. It converts data into a form that appears random to anyone without the decryption key.


----

## Databases

### 57. SQL (Structured Query Language)


### 58. NoSQL


### 59. Transactions


### 60. Views


### 61. Indexes


### 62. ORM (Object-Relational Mapping)


### 63. Query Builder


### 64. Migrations



----






