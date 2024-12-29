# My notes of: SW101 - The Book (by Marko)

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


### 20. Reducer Pattern


### 21. Selector Pattern


### 22. Reactive Programming


### 23. ECS Pattern

