## Installation
You can run a demo of the app with Docker and Docker Compose:

```bash
docker-compose build
docker-compose run restaurant python3 manage.py migrate
docker-compose up
```
##### Create User
Post username and password for next url:
 ```bash 
http://localhost:8080/users/auth/users/
``` 
You can get an authorization token for an address(Need post your username and password)
 ```bash 
http://localhost:8080/users/auth/token/
```
You can retrieve, update or delete a user if you use the following URLs

 ```bash 
http://localhost:8080/users/retrieve/<int:pk>/
http://localhost:8080/users/update/<int:pk>/
http://localhost:8080/users/destroy/<int:pk>/
```
where < int:pk > - user id

### Restourant
To create a restaurant make a post request with the fields "name" and "address" to the following url:
 ```bash 
http://localhost:8081/api/create-restaurant/
``` 
Update:
 ```bash 
http://localhost:8081/api/update-restaurant/<int:pk>/
``` 
Get restaurants list:
 ```bash 
http://localhost:8081/api/restaurant-list/
``` 

### Menu

To create a restaurant make a post request with the fields "restaurant"(id), "name" and "details" to the following url:
```bash
http://localhost:8081/api/upload-menu/
```
All Menu list
```bash
http://localhost:8081/api/menu-list/
```
Today Menu list
```bash
http://localhost:8081/api/menu-today/
```
Update:
 ```bash 
http://localhost:8081/api/update-menu/<int:pk>/
``` 
### Vote
The following url works for voting, where < int:menu_id > is the menu id for which the employee wants to vote. Remember, you can vote for one menu once a day.

```bash
http://localhost:8081/api/vote/<int:menu_id>/
```

At the following address you can see the top three menus for today:
```bash
http://localhost:8081/api/results/<int:pk>/
```
< int:pk > - restaurant id

### Fronted 
In development (trying to learn Vue.js)


