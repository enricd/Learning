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


### 6. Facade Pattern


### 7. Proxy Pattern


### 8. Dependency Injection



