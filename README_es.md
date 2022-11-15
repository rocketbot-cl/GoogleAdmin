



# Google Admin
  
Este módulo de conecta a la Api Directory de google. Puedes Crear, eliminar o restaurar la contraseña de un Usuario.

## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  

## Como usar este modulo

Para utilizar este módulo necesitas habilitar la API de Google Admin para tu cuenta. Para ello, debes seguir los siguientes pasos ( [referencia](https://developers.google.com/admin-sdk/directory/v1/quickstart/python) ):

- Crear un projecto en Google Cloud Console (Saltar si ya tienes un proyecto creado)
  - En el menú de la izquierda, dar click en **Menu** > **IAM & Admin** > **Create a project**.
  - En el campo **Project Name**, agregar un nombre para el proyecto
  - Completar los siguientes campos según corresponda

- Habilitar la API:
    - Ir a [Google Cloud Console](https://console.cloud.google.com/)
    - En el menú arriba a la derecha, dar click en **Menu** > **APIs & Services** > **Library**
    - En el buscador, buscar **Admin SDK API**
    - Dar click en el resultado **Admin SDK API**
    -  Click en el botón **Enable**

- Crear credenciales de Google:
    - Ir a [Google Cloud Console](https://console.cloud.google.com/)
    - En el menú arriba a la derecha, dar click en **Menu** > **APIs & Services** > **Credentials**
    - Click en el botón **Create credentials**
    - Click en **OAuth client ID**
    - En el campo **Application type**, seleccionar **Desktop Application**
    - Escribir un nombre en el campo **Name**
    - Aparecerá una ventana con los datos de la credencial. Dar click en **Download JSON**
    - Utilizar este archivo como credenciales en el módulo

## Overview


1. Configurar credenciales G-Suite  
Configura credenciales para conectar con el API de Google Admin.

2. Crear un nuevo usuario  
Este comando crea un nuevo usuario en el directorio de google. El usuario será creado con el email y contraseña especificados.

3. Obtener usuarios  
Obtener usuarios de Google. Puedes añadir un filtro para obtener solo usuarios con un dominio de correo electrónico específico.

4. Borrar usuario  
Borrar un usuario de Google Admin

5. Obtener usuario  
Obtener la información de un usuario de Google Admin

6. Actualizar usuario  
Actualizar la información de un usuario de Google Admin  

----
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