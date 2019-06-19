# Djamazon

## Deployed Link
https://djamazon.herokuapp.com/

## Description
Djamazon is an 'Amazon' like store API allowing customer, supervisor, and manager interaction with the Djamzon database

## Motivation
This project sets up an easy to use RESTful API backend ready for a user interface implementation 

## Result
Djamazon implements a RESTful API built using Django and Django REST Framework (DRF), both Python web frameworks. Users can belong to one or many of the following groups: Customer, Supervisor, Manager, each of which can interact with the API differently. For example, Customer users can purchase item stock, but cannot add new stock, or create or update products. Users can log in directly to the browsable web api that is automagically generated by DRF. JSON web tokens as an authentication and authorization strategy are also implemented, allowing an external front end framework to interact with the API.

## Try out Djamazon browsable API
### Customer login
```
username: customer
password: I3,#9Jfn
```

## Superuser login
```
username: superuser
password: I3,#9Jfn
```

## Manager login
```
username: customer
password: I3,#9Jfn
```

## Token Authentication Routes
### Obtain JSON token with the correct credentials
```
POST https://djamazon.herokuapp.com/api/token/
body: {
  username: <username>,
  password: <password>
}

Sample response:
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU2MTA2MzgxNCwianRpIjoiMmYwNWM4Nzg5YzM2NDVlMGE5OWE5ODFlYWRhYjNjODIiLCJ1c2VyX2lkIjoyfQ.nt_BQBT6Q4fe6hJScAHnllXRGdtxWCt_5wfWhXK9NsQ",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYwOTgzNDE0LCJqdGkiOiJiNTQ4NGE4YzRkZjI0MmY5YTcwMTU2MTE5OGMxNTY5MiIsInVzZXJfaWQiOjJ9.1DEPJGIcNEXdDVWWYC3jWk4Ms7_0NuXUAQGx_kEZy2w"
}
```

### Refresh token
```
POST https://djamazon.herokuapp.com/api/token/refresh/
body: {
  refresh: <refresh token>
}

Sample valid response:
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYwOTgzODE1LCJqdGkiOiI0NTExNWE1MWRmNDc0NmMxYjIyMWM2ZTA5NmNiZWFmOCIsInVzZXJfaWQiOjJ9.ChUX_tvQbytmKDnLs_I1ApWUDg5l-JkjeSsSAvTUUjk"
}

Sample invalid response:
{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}
```

### Verify token
```
POST https://djamazon.herokuapp.com/api/token/verify/
body: {
  token: <access token>
}

Valid token response:
{}

Invalid token response:
{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}
```
