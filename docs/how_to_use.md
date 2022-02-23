# How to use this module

To use this module you need to configure the credentials to connect with the Google Admin API. To this, you need to follow the steps below:

- Create a new project in Google Cloud Console (Skip if you already have a project created)
    - At the top-left, click Menu menu > IAM & Admin > Create a Project.
    - In the Project Name field, enter a descriptive name for your project.
    - Complete the other steps with your information

- Enable API
    - Go to [Google Cloud Console](https://console.cloud.google.com/)
    - At the top-left, click **Menu** > **APIs & Services** > **Library**
    - In the browser field, enter **Admin SDK API**
    - Click in the result **Admin SDK API**
    - Click **Enable**

- Create Credentials
    - Go to [Google Cloud Console](https://console.cloud.google.com/)
    - At the top-left, click **Menu** > **APIs & Services** > **Credentials**
    - Click **Create credentials**
    - Click **OAuth client ID**
    - In the **Application type** field, select **Desktop Application**
    - In the **Name** field, enter a descriptive name for the credentials
    - Appears a window with the credentials data. Click **Download JSON**
    - Use this file as credentials in the module


--- 

## Como usar este módulo

Para utilizar este módulo necesitas habilitar la API de Google Admin para tu cuenta. Para ello, debes seguir los siguientes pasos ( [referencia](https://developers.google.com/admin-sdk/directory/v1/quickstart/python) ):

- Crear un projecto en Google Cloud Console (Saltar si ya tienes un proyecto creado)
  - En el menú de la izquierda, dar click en Menu > IAM & Admin > Create a project

  - En el campo Project Name, agregar un nombre para el proyecto

  - Completar los siguientes campos según corresponda

- Habilitar la API:
    - Ir a [Google Cloud Console](https://console.cloud.google.com/)
    - En el menú arriba a la derecha, dar click en **Menu** > **APIs & Services** > **Library**
    - En el buscador, buscar **Admin SDK API**
    - Dar click en el resultado **Admin SDK API**
    -  Click en el botón **Habilitar**

- Crear credenciales de Google:
    - Ir a [Google Cloud Console](https://console.cloud.google.com/)
    - En el menú arriba a la derecha, dar click en **Menu** > **APIs & Services** > **Credentials**
    - Click en el botón **Create credentials**
    - Click en **OAuth client ID**
    - En el campo **Application type**, seleccionar **Desktop Application**
    - Escribir un nombre en el campo **Name**
    - Aparecerá una ventana con los datos de la credencial. Dar click en **Download JSON**
    - Utilizar este archivo como credenciales en el módulo
