README.md
# Dodekath3on / metis_api
Updating models

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

