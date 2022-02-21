



# Google Admin
  
This module connects to the google Api Directory. You can create, delete or restore the password of a User.  

## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  


## How to use this module

Para utilizar este módulo necesitas habilitar la API de Google Admin para tu cuenta. Para ello,
 debes seguir los siguientes pasos ( [referencia](https://developers.google.com/admin-
sdk/directory/v1/quickstart/python) ):

- Crear un projecto en Google Cloud Console (Saltar si ya tienes un proyecto 
creado)
  - En el menú de la izquierda, dar click en Menu > IAM & Admin > Create a project

  - En el campo Project 
Name, agregar un nombre para el proyecto

  - Completar los siguientes campos según corresponda

- Habilitar la API:

    - Ir a [Google Cloud Console](https://console.cloud.google.com/)
    - En el menú arriba a la derecha, dar click en
 **Menu** > **APIs & Services** > **Library**
    - En el buscador, buscar **Admin SDK API**
    - Dar click en el 
resultado **Admin SDK API**
    -  Click en el botón **Habilitar**

- Crear credenciales de Google:
    - Ir a [Google 
Cloud Console](https://console.cloud.google.com/)
    - En el menú arriba a la derecha, dar click en **Menu** > **APIs &
 Services** > **Credentials**
    - Click en el botón **Create credentials**
    - Click en **OAuth client ID**
    - En
 el campo **Application type**, seleccionar **Desktop Application**
    - Escribir un nombre en el campo **Name**
    - Aparecerá una ventana con los datos de la credencial. Dar click en **Download JSON**
    - Utilizar este archivo como 
credenciales en el módulo

--- 
## Overview


1. Setup G-Suite credentials  
Configure credentials to connect with the Google Admin API.

2. Create a new user  
This command creates a new user in the Google Admin. The user will be created with the specified email and password.

3. Get users  
Get users from Google. You can add a filter to get only users with a specific email domain.

4. Delete User  
Delete a user from Google Admin

5. Get User  
Get the information of a user from Google Admin  

--- 
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**google-api-python-client**](https://pypi.org/project/google-api-python-client/)- [**google-auth-httplib2**](https://pypi.org/project/google-auth-httplib2/)- [**google-auth-oauthlib**](https://pypi.org/project/google-auth-oauthlib/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)