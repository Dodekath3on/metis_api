README.md
# Dodekath3on / metis_api

## Views
The following tables contain RESTful routes to interact with the backend api. Relational routes are currently being worked on. 

### User
---
|  NAME   |  VERB  |      PATH       |
|---------|--------|-----------------|
| INDEX   | GET    | /user           |
| SHOW    | GET    | /user/:id       |
| CREATE  | POST   | /user           |
| EDIT    | PATCH  | /user/:id       |
| UPDATE  | PUT    | /user/:id       |
| DESTROY | DELETE | /user/:id       |

### Project
---
|  NAME   |  VERB  |    PATH       |
|---------|--------|---------------|
| INDEX   | GET    | /project      |
| SHOW    | GET    | /project/:id  |
| CREATE  | POST   | /project      |
| EDIT    | PATCH  | /project/:id  |
| UPDATE  | PUT    | /project/:id  |
| DESTROY | DELETE | /project/:id  |
<!-- |         | GET    | /project/tasks| -->

### Task
---
|  NAME   |  VERB  |   PATH         |
|---------|--------|----------------|
| INDEX   | GET    | /task          |
| SHOW    | GET    | /task/:id      |
| CREATE  | POST   | /task          |
| EDIT    | PATCH  | /task/:id      |
| UPDATE  | PUT    | /task/:id      |
| DESTROY | DELETE | /task/:id      |
|         | GET    | /task/user/:id |
<!-- |         | GET    | /task/project | -->

## Models

### User

|  field       | type    |
|--------------|---------|
|  name        | char    |
|  username    | char    |
|  email       | email   |
|  project_set | list    |
|  teams       | list    |
|  bill_rate   | decimal |

### Project

|  field    | type    |
|-----------|---------|
|  name     | char    |
|  teams    | list    |
|  budget   | decimal |

### Task

|  field    | type |
|-----------|------|
|  name     | char |
|  status   | char |
|  priority | int  |
