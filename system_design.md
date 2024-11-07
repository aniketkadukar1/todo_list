# System Vision Document
## Problem Description
Students often struggle to stay organized with assignments, projects, and deadlines, resulting in stress and missed tasks.

## System Capabilities
    - Use case diagram
    - Functional and non-functional requirements
    - Features

## Business Benefits
Students can easily organize assignments, projects, and deadlines, leading to better time utilization and reduced last-minute rushes.
---

## Use Case Diagram
The use case diagram presents the actors and the actions they can take when interacting with the system. CRUD operations are a good starting point to come up with use cases.

### UML Use Case Diagram

```plaintext
+---------------------+
|      Student        |
+---------------------+
        |
        v
+---------------------+
|  Create a Task      |
+---------------------+
        |
        v
+---------------------+
|  List Tasks         |
+---------------------+
        |
        v
+---------------------+
|  Mark Task Complete |
+---------------------+
        |
        v
+---------------------+
|  Edit Task          |
+---------------------+
        |
        v
+---------------------+
|  Delete Task        |
+---------------------+

```
## Functional Requirements
The functional requirements denote the behavior of the system. You must define the minimum requirements for a system to operate. Let’s define the requirements for our to-do app:

The system should provide students with the ability to create a task. A task comprises of:

    - Title
    - Description (Optional)
    - Deadline
    - is_completed

The system should provide students the ability to list all available tasks they created:

Tasks are ordered by the deadline in chronological order.

Completed tasks will have a strikethrough text title.

Deleted tasks must not be shown.

The system should provide students the ability to mark a task as complete.

The system should provide students the ability to edit the title, description, and deadline of a task.

The system should provide students the ability to delete tasks.

## Non-Functional Requirements
The non-functional requirements denote the system constraints. The architecture terms are known as the “-ilities”, for example, maintainability, scalability, and usability.

The application must be responsive to all screen sizes up to large laptop screens (usability).

The application must provide an onboarding guide (usability).

The application must display the list of tasks within a predefined time (performance).

The application must enforce a design system (maintainability/usability).

## UML Class Diagram
The UML class diagram represents the entities and the relationship between entities in a system. We model the class diagram according to our use case diagram and the functional requirements.

### To-Do List Class Diagram
```plaintext
+---------------------+
|       Task          |
+---------------------+
| - title: String     |
| - description: String|
| - deadline: Date    |
| - isCompleted: Boolean|
+---------------------+
        |
        v
+---------------------+
|      Student        |
+---------------------+
| - name: String      |
| - email: String     |
+---------------------+

```
