/*-----------------------------------------

Summary: Testing Django ModelViewSet built-in routes.

|  NAME   |  VERB  |   PATH    |
|---------|--------|-----------|
| INDEX   | GET    | /user     |
| SHOW    | GET    | /user/:id |
| CREATE  | POST   | /user     |
| EDIT    | PATCH  | /user/:id |
| UPDATE  | PUT    | /user/:id |
| DESTROY | DELETE | /user/:id |

-----------------------------------------*/

let URL = 'http://127.0.0.1:8000/user/'

/*-----------
Get all Users
-----------*/
async function getUsers() {
  const response = await fetch(URL)
  const users = await response.json()
  return users
}
// getItems().then(data=>console.log(data))

/*-----------
Get one User
-----------*/
async function getUser() {
  const response = await fetch(URL + '1/')
  const users = await response.json()
  return users
}
// getUser().then(data=>console.log(data))

/*-----------
Create a User
-----------*/
async function createUser() {
  const response = await fetch(URL, {
    method: 'POST',
    mode:'no-cors',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      'name': 'Joseph Smith',
      'username': 'jsmith',
      'email': 'jsmith@jsmithy.com'
    })
  })
  const user = await response.json()
  return user
}
// createUser().then(data=>console.log(data))

/*-------------------
Update User Attribute
-------------------*/
async function updateUserAttr() {
  const response = await fetch(URL + '6/', {
    method:'PATCH',
    // mode: 'no-cors', // > TypeError: 'PATCH is unsupported in no-cors mode.
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      'name': 'Joe Smith'
    })
  })
  const user = await response.json()
  return user
}
// updateUserAttr().then(data=>console.log(data))

/*-------------------
Update Whole User
-------------------*/
async function updateUser() {
  const response = await fetch(URL + '6/', {
    method:'PUT',
    // mode: 'no-cors', // > TypeError: 'PATCH is unsupported in no-cors mode.
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      'name': 'Willy Wonka',
      'username': 'wwonka',
      'email': 'wwonka@email.email'
    })
  })
  const user = await response.json()
  return user
}
updateUser().then(data=>console.log(data))

/*-----------
Delete User
-----------*/
async function deleteUser() {
  const response = await fetch(URL + '6/', {method: 'DELETE'})
}
// deleteUser().then(data=>console.log(data))