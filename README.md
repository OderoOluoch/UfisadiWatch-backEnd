# UfisadiWatch

## Introduction

Ufisadi Watch is a web application idea that has been pitched to participate in the __Coding4Integrity__ *the African Youth Anti-Corruption Hackathon* that is organised by the United Nations Office on Drugs and Crime (UNDOC)\
>The objectives of the hackathon are to promote the use of information and communications technologies (ICT) to prevent and combat corruption in Africa and to give young developers the chance to come up with their own ideas on how to counter corruption through technologies.
>The challenge will also promote the implementation of the United Nations Convention Against Corruption (UNCAC) by enhancing public-private partnerships in the development of sustainable ICT-based anti-corruption solutions; youth engagement and employment; innovation and technology.

### About the API
This is a REST API developed using the `django-rest` framework. The goal is to provide an interface that will be consumed by any `frontend` framework or a mobile application if the **The Code Walkers** manages to develop one. 
## Running the application
The UfisadiAPI is a fully dockerized application. You need to worry not about the enviroment you're running it on. Ensure you have `docker` and `docker-compose` installed and working on your local environment.

### Steps
Step1: Cloning the repo:
    `git clone https://github.com/OderoOluoch/UfisadiWatch-backEnd.git`
Step2: Build the Image
    Docker only option
    `docker build --tag ufisadi`
    `docker run ufisadi`

    Docker Compose
`docker compose build`
`docker compose run --rm 'service-name' sh -c "django-admin startproject appname ."` -> run this command when you want to create a django app. 
**Note:** _all django apps are created inside the `/apps` folder_
`docker compose up/down` start or stop the container

### Creating a django app using docker compose
```docker
docker compose run --rm ufisadi sh -c "python manage.py app_name apps/app_name "
or 
 docker compose run ufisadi python manage.py startapp product apps/product
```
## view app on browser
When you run the container, navigate to your browser and type the following entry endpoint
 `127.0.01:8000/api/tender-list/` to list all tenders. This is the format for accessing all the `http` verbs on this API.

## Usage

All responses will have the form:
_(envelope)_
```json
{
    "data":"Mixed type holding the content of the response",
    "message":"Description of what happened"
}
```

Subsequent  response definition willl only detail the expected value of the `data field`

### List all tenders

`GET /tenders`
**Response**
- `200 OK` on success

```json
{
    "id":"1",
    "tender_no":"KU/EOI/024/SPP/2021-2022",
    "description":"EXPRESION OF INTEREST FOR THE PROPOSED CONSTRUCTION OF A 2MW SOLAR PV POWER PLANT",
    "entity_name":"Kenyatta University (KU)",
    "procurement_method":"Expression of Interest",
    "procurement_category":"Consultancy Services",
    "created_at":"2021-10-14",
    "closing_date": "2021-11-25",
    "is_active":"true"
},
{
    "id":"3",
    "tender_no":"NCIC/OT/HR/002/2021-2022",
    "description":"PROVISION OF MEDICAL, LIFE & GPA INSURANCE COVER FOR COMMISSIONERS AND STAFF",
    "entity_name":"National Cohesion and Integration Commission",
    "procurement_method":"Open Tender",
    "procurement_category":"Non Consultancy Services",
    "created_at":"2021-10-14",
    "closing_date": "2021-11-25",
    "is_active":"false"
}
```

**Definitions**
`POST /tenders`
**Arguements**
-  `"id":int` globally unique id for the tender.
- `"Tender No":string` a number associated with the tender and organization
- `"Entity Name:string` a name for the procuring entity
- `"description":string` tender detailed description
- `"procurement method":string` tender procurement mentod
- `"category":string` tender category
- `"created at":date` date which the tender was posted
- `"closing date":date` date which the tender validity ends
- `"is active":Boolean` defines whether the tender is active or archived

**Responses**
- `201 Created` on success
```json
{
    "id":"1",
    "tender_no":"KU/EOI/024/SPP/2021-2022",
    "description":"EXPRESION OF INTEREST FOR THE PROPOSED CONSTRUCTION OF A 2MW SOLAR PV POWER PLANT",
    "entity_name":"Kenyatta University (KU)",
    "procurement_method":"Expression of Interest",
    "procurement_category":"Consultancy Services",
    "created_at":"2021-10-14",
    "closing_date": "2021-11-25",
    "is_active":"true"
}
```
## Lookup Tender details

`GET /tender/<int:str>`
**Response**
- `404 Not Found` if the tender does not exist
- `200 OK` on success

```json
{
    "id":"1",
    "tender_no":"KU/EOI/024/SPP/2021-2022",
    "description":"EXPRESION OF INTEREST FOR THE PROPOSED CONSTRUCTION OF A 2MW SOLAR PV POWER PLANT",
    "entity_name":"Kenyatta University (KU)",
    "procurement_method":"Expression of Interest",
    "procurement_category":"Consultancy Services",
    "created_at":"2021-10-14",
    "closing_date": "2021-11-25",
    "is_active":"true"
}
```

## Delete a tender

`DELETE /tender/<int:id>/`

**Response**
- `404 Not Found` if the tender does not exist
- `204 No content` on success



