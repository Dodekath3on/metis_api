README.md
# Dodekath3on / metis_api
Updating models

Test - Updating Models Branch

## Views
The following tables contain RESTful routes for the current models. 

### User
---
|  Route  |        URL        |  Verb  |    Desc     |
|---------|-------------------|--------|-------------|
| Index   | /users/           | GET    | All Users   |
| Show    | /users/:id        | GET    | One User    |
| Create  | /users/new        | POST   | New User    |
| Destroy | /users/delete/:id | DELETE | Delete User |
|         | /users/tasks/:d   | GET    | User Tasks   |





### Project


### Task


## Models

### User

|  field    | type  |
|-----------|-------|
|  name     | char  |
|  username | char  |
|  email    | email |

- access tasks with: 
`user.task_set.all()`

### Project

|  field    | type |
|-----------|------|
|  name     | char |

- access tasks with: 
`project.task_set.all()`

### Task

|  field    | type |
|-----------|------|
|  name     | char |
|  status   | char |
|  priority | int  |

- has_one User
- has_one Project

