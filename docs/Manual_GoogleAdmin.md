# Google Admin
  
This module connects to the google Api Directory. You can create, delete or restore the password of a User.
  
![banner](imgs/Banner_GoogleAdmin.jpg)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  

# How to use this module

To use this module you need to configure the credentials to connect with the Google Admin API. To this, you need to follow the steps below ( [reference](https://developers.google.com/admin-sdk/directory/v1/quickstart/python) )::

- Create a new project in Google Cloud Console (Skip if you already have a project created)
    - At the top-left, click **Menu** > **IAM & Admin** > **Create a Project**.
    - In the **Project Name** field, enter a descriptive name for your project.
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


## Description of the commands

### Setup G-Suite credentials
  
Configure credentials to connect with the Google Admin API.
|Parameters|Description|example|
| --- | --- | --- |
|Credentials file path|JSON file with the credentials to access the Google Admin API. See the documentation for more information.|C:\User\Desktop\credentials.json|
|Assign result to variable|Name of the variable where the result of the execution of the command will be assigned.|result|

### Create a new user
  
This command creates a new user in the Google Admin. The user will be created with the specified email and password.
|Parameters|Description|example|
| --- | --- | --- |
|First name|First name of the user to be created|Joe|
|Last name|Last name of the user to be created|Bloggs|
|Assign result to variable|Variable name where to store the result of the command|response|
|Email|Email of the user to be created|joe.bloggs@mail.com|
|Password|Password of the user to be created. If not specified, a random password will be generated|123456789|
|Aditional data|Additional data to be added to the user. More info here https//developers.google.com/admin-sdk/directory/reference/rest/v1/users/insert|{"isAdmin": True, "recoveryEmail": "r2d2@gmail.com"}|

### Get users
  
Get users from Google. You can add a filter to get only users with a specific email domain.
|Parameters|Description|example|
| --- | --- | --- |
|Domain (optional)|Filter users by email domain.|@rocketbot.com|
|Variable name where to store the result of the command|Variable name where to store the result of the command|response|
|Order by (optional)|Order users by this field. If not selected, the users will be ordered by email.|email|
|Acending or Descending|Sort users in ascending or descending order.|ASCENDING|
|Aditional data|Additional data to be added to the user. More info here https//developers.google.com/admin-sdk/directory/reference/rest/v1/users/list|{"maxResults": 10, "viewType": "domain_public", ...}|

### Delete User
  
Delete a user from Google Admin
|Parameters|Description|example|
| --- | --- | --- |
|User Key|User Key or Email Address of the user to be deleted|111575529871886135722 or joe.bloggs@mail.com|
|Variable name where to store the result|Variable name where to store the result of the command|response|
|Aditional data|Aditional data to be sent to the API. More info https//developers.google.com/admin-sdk/directory/reference/rest/v1/users/delete|{"viewType": "domain_public", ...}|

### Get User
  
Get the information of a user from Google Admin
|Parameters|Description|example|
| --- | --- | --- |
|User Key|The user key can be the user's primary email address or the user's unique ID. List the users to know their user key|111575529871886135722 or joe.bloggs@mail.com|
|Variable name where to store the result|Variable name where to store the result of the command|response|
|Aditional data|Additional data to be sent along with the request. More info https//developers.google.com/admin-sdk/directory/reference/rest/v1/users/get|{"viewType": "domain_public", ...}|

### Update User
  
Update the information of a user from Google Admin
|Parameters|Description|example|
| --- | --- | --- |
|User Key|The user key can be the user's primary email address or the user's unique ID. List the users to know their user key|111575529871886135722 or joe.bloggs@mail.com|
|Variable name where to store the result|Variable name where to store the result of the command|response|
|Email|Email of the user to be created|joe.bloggs@mail.com|
|Password|Password of the user to be created. If not specified, a random password will be generated|123456789|
|Aditional data|Additional data to be sent along with the request. More info https//developers.google.com/admin-sdk/directory/reference/rest/v1/users/patch|{"viewType": "domain_public", ...}|
