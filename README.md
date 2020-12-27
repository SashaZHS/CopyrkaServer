# CopyrkaServer
1. Post
Login with token
http://167.99.8.160:8080/api/v1/auth_token/token/login
send Body:
{
    "password": "123123asdA",
    "email": "test@gmail.com"
}
return:
{
    "auth_token": "82db8c90091dbbaed8793800dfb555cd731f4c57"
}
2.  Get
Info about me
http://167.99.8.160:8080/api/v1/auth/users/me
send Headers:
key: 
Authorization  
value: 
Token 82db8c90091dbbaed8793800dfb555cd731f4c57
return:
{
    "name": "Murka",
    "surname": "MurMur",
    "gender": 1,
    "date_of_birth": "2222-02-22",
    "id": 2,
    "email": "test@gmail.com"
}
3.  Put
update info
http://167.99.8.160:8080/api/v1/auth/users/{id}/
send Headers:
key: 
Authorization  
value: 
Token 82db8c90091dbbaed8793800dfb555cd731f4c57
Body:
{
    "name": "new name",
    ...other parameters
}
return:
{
    "name": "new name",
    "surname": "MurMur",
    "gender": 1,
    "date_of_birth": "2222-02-22",
    "id": 2,
    "email": "test@gmail.com"
}
4. Post
Set new email
http://167.99.8.160:8080/api/v1/auth/users/set_email/
send Headers:
key: 
Authorization  
value: 
Token 82db8c90091dbbaed8793800dfb555cd731f4c57
send Body:
{
	"new_email":"test2@gmail.com"
}


5. Post
Set new password
http://167.99.8.160:8080/api/v1/auth/users/set_password/
send Headers:
key: 
Authorization  
value: 
Token 82db8c90091dbbaed8793800dfb555cd731f4c57
send Body:
{
    "new_password": "",
    "current_password": ""
}

6. Post
Logout and drop token 
http://167.99.8.160:8080/api/v1/auth_token/token/logout
send Headers:
key: 
Authorization  
value: 
Token 82db8c90091dbbaed8793800dfb555cd731f4c57

7. Post
Create new user
http://167.99.8.160:8080/api/v1/auth/users/
send Body:
{
    "name": "name",
    "surname": "surname<",
    "gender": 2,
    "date_of_birth": "2020-06-03",
    "email": "test4@gmail.com",
    "password": "123123asdA"
}
return:
{
    "name": "name",
    "surname": "surname<",
    "gender": 2,
    "date_of_birth": "2020-06-03",
    "email": "test4@gmail.com",
    "id": 4
}


8. Post
Create new photo
http://167.99.8.160:8080/api/v1/photos



9. Get
Get all photos
http://167.99.8.160:8080/api/v1/photos


10. Get
Get photo by id
http://167.99.8.160:8080/api/v1/photo/{id}


10. Post
Find user by photo
http://167.99.8.160:8080/api/v1/facebook/find
