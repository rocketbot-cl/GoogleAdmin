# Google Admin
  
This module connects to the google Api Directory. You can create, delete or restore the password of a User.  

## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  

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

6. Update User
Update the information of a user from Google Admin

--- 
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**google-api-python-client**](https://pypi.org/project/google-api-python-client/)
- [**google-auth-httplib2**](https://pypi.org/project/google-auth-httplib2/)
- [**google-auth-oauthlib**](https://pypi.org/project/google-auth-oauthlib/)
- 
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)
