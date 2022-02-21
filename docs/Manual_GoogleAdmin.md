# Google Admin
  
Este módulo se conecta a la Api Directory de google. Puedes Crear, eliminar o restaurar la contraseña de un Usuario  
  
![banner](imgs/Banner_GoogleDirectory.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.  

## How to use this module

To use this module you need to configure the credentials to connect with the Google Admin 
API. To this, you need to follow the steps below:

- Create a new project in Google Cloud Console (Skip if you already 
have a project created)
    - At the top-left, click Menu menu > IAM & Admin > Create a Project.
    - In the Project 
Name field, enter a descriptive name for your project.
    - Complete the other steps with your information

- Enable 
API
    - Go to [Google Cloud Console](https://console.cloud.google.com/)
    - At the top-left, click **Menu** > **APIs
 & Services** > **Library**
    - In the browser field, enter **Admin SDK API**
    - Click in the result **Admin SDK 
API**
    - Click **Enable**

- Create Credentials
    - Go to [Google Cloud Console](https://console.cloud.google.com/)

    - At the top-left, click **Menu** > **APIs & Services** > **Credentials**
    - Click **Create credentials**
    - Click **OAuth client ID**
    - In the **Application type** field, select **Desktop Application**
    - In the **Name** 
field, enter a descriptive name for the credentials
    - Appears a window with the credentials data. Click **Download 
JSON**
    - Use this file as credentials in the module



## Descripción de los comandos

### Configurar credenciales G-Suite
  
Configura credenciales para conectar con el API de Google Admin.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta archivo de credenciales|Archivo json con las credenciales de acceso a la API de Google Admin. Revisar la documentación para obtener más información.|C:\Usuario\Desktop\credenciales.json|

### Crear un nuevo usuario
  
Este comando crea un nuevo usuario en el directorio de google. El usuario será creado con el email y contraseña 
especificados.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre|Nombre del usuario a crear|Juan|
|Apellido|Apellido del usuario a crear|Perez|
|Nombre de la variable donde almacenar el resultado del comando|Nombre de la variable donde almacenar el resultado del comando|resultado|
|Correo|Correo del usuario a crear|juan.perez@mail.com|
|Contraseña|Contraseña del usuario a crear. Si no se especifica, se generará una contraseña aleatoria|123456789|
|Datos adicionales|Datos adicionales a ser agregados al usuario. Mas información [aquí](https//developers.google.com/admin-sdk/directory/reference/rest/v1/users/insert)|{"isAdmin": True, "recoveryEmail": "r2d2@gmail.com"}|

### Obtener usuarios
  
Obtener usuarios de Google. Puedes añadir un filtro para obtener solo usuarios con un dominio de correo electrónico 
específico.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dominio (opcional)|Filtrar usuarios por dominio de correo electrónico.|@rocketbot.com|
|Nombre de la variable donde almacenar el resultado del comando|Nombre de la variable donde almacenar el resultado del comando|resultado|
|Ordenar por (opcional)|Ordenar usuarios por este campo. Si no seleccionas ningún campo, los usuarios se ordenarán por email.|email|
|Ascendente o Descendente|Ordenar usuarios de forma ascendente o descendente.|ASCENDING|
|Datos adicionales|Datos adicionales a ser agregados al usuario. Mas información [aquí](https//developers.google.com/admin-sdk/directory/reference/rest/v1/users/get) |{"maxResults": 10, "viewType": "domain_public", ...}|

### Borrar usuario
  
Borrar un usuario de Google Admin
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Key de Usuario|Key de Usuario o Email Address del usuario a ser borrado|111575529871886135722 o juan.perez@mail.com|
|Nombre de la variable donde almacenar el resultado|Nombre de la variable donde almacenar el resultado del comando|resultado|
|Datos adicionales|Datos adicionales a ser enviados a la API. Mas info [aquí](https//developers.google.com/admin-sdk/directory/v1/reference/users/delete)|{"viewType": "domain_public", ...}|

### Obtener usuario
  
Obtener la información de un usuario de Google Admin
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Key de Usuario|El key de usuario puede ser el correo electrónico primario del usuario o su ID único. Listar los usuarios para conocer su key de usuario|111575529871886135722 o juan.perez@mail.com|
|Nombre de la variable donde almacenar el resultado|Nombre de la variable donde almacenar el resultado del comando|resultado|
|Datos adicionales|Datos adicionales a ser enviados junto con la solicitud. Más información [aquí](https//developers.google.com/admin-sdk/directory/v1/reference/users/get) |{"viewType": "domain_public", ...}|
