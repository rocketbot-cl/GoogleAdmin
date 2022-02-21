# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

try:
    from queue import Queue, Empty
except ImportError:
    from Queue import Queue, Empty  # python 2.x


import os
import sys
import json

# Add the libs folder to the system path
base_path = tmp_global_obj["basepath"] #type:ignore
google_directory_path = os.path.join(base_path, "modules", "GoogleDirectory")
gd_libs_path = os.path.join(cur_path, "libs") #type:ignore

if gd_libs_path not in sys.path:
    sys.path.append(gd_libs_path)

# Import module libraries
from googleapiclient.errors import HttpError

"""
The code of each module works as a local scope. Each command that is executed resets the data.
To share information between commands, declare the variable as global. The sintax will be 'mod_modulename' or similar
"""
global mod_google_directory

"""
To connect to multiple databases, a dictionary is created and stores the instance of each connection.
The syntax is {"session name": {data}}
"""
SESSION_DEFAULT = "default"
try:
    if not mod_google_directory :
        mod_google_directory = {SESSION_DEFAULT:{}}
except NameError:
    mod_google_directory = {SESSION_DEFAULT:{}}

class GoogleDirectory:
    """
    Google Directory Class.

    Attributes:
        service (googleapiclient.discovery.Resource): Google Directory Service.
        creds (google.oauth2.credentials.Credentials): Credentials.
        SCOPES (list): Scopes.
        credential_path (str): Credential path.
        token_path (str): Token path where is stored the token.

    Methods:
        config_credentials(): Configure the credentials.
    """
    
    def __init__(self, credential_path, token_path="token.json"):
        """Initialize the class."""
        self.SCOPES = [
            "https://www.googleapis.com/auth/admin.directory.user.readonly",
            "https://www.googleapis.com/auth/admin.directory.user"
        ]
        self.creds = None
        self.credential_path = credential_path
        self.token_path = token_path
        self.service = None

    def config_credentials(self):
        """Configure the credentials."""
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from googleapiclient.discovery import build

        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(self.token_path):
            print("Loading credentials from token.json")
            self.creds = Credentials.from_authorized_user_file(self.token_path, self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credential_path, self.SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.token_path, 'w') as token:
                token.write(self.creds.to_json())

        self.service = build('admin', 'directory_v1', credentials=self.creds)



try:
    # Get data from robot
    module = GetParams("module") # Get command executed
    session = GetParams("session") # Get Session name
    other_params = GetParams("other_params") or {} # Get other params
    result = GetParams("result") # Get variable name where save results
    if not session:
        session = SESSION_DEFAULT # Set default session
    

    if isinstance(other_params, str):
        try:
            other_params = json.loads(other_params)
        except json.decoder.JSONDecodeError:
            other_params = eval(other_params)

    if module == "config":
        credentials_path = GetParams("credentials_path")

        google_directory = GoogleDirectory(
            credentials_path,
            os.path.join(google_directory_path, "token.json")
            )
        try:
            google_directory.config_credentials()
            mod_google_directory[session] = google_directory
            SetVar(result, True)
        except Exception as e:
            SetVar(result, False)
            PrintException()
            raise e
        

    if module == "get_users":
        domain = GetParams("domain")
        order_by = GetParams("order_by")
        sort_order = GetParams("sort_order")

        if domain:
            other_params["domain"] = domain
        if sort_order:
            other_params["sortOrder"] = sort_order
        if order_by:
            other_params["orderBy"] = order_by

        google_directory = mod_google_directory[session]
        users = google_directory.service.users().list(**other_params).execute()

        if result:
            SetVar(result, users)

    if module == "add_user":
        first_name = GetParams("first_name")
        last_name = GetParams("last_name")
        primary_email = GetParams("email")
        password = GetParams("password")

        body = {
            "name": {
                "familyName": last_name,
                "givenName": first_name
            },
            "password": password,
            "primaryEmail": primary_email,
            **other_params
            }

        google_directory = mod_google_directory[session]
        user = google_directory.service.users().insert(body=body).execute()
        if result:
            SetVar(result, user)

    if module == "delete":
        user_key = GetParams("user_key")
        google_directory = mod_google_directory[session]
        response = google_directory.service.users().delete(userKey=user_key).execute()
        if result:
            SetVar(result, response)

    if module == "get_user":
        user_key = GetParams("user_key")

        google_directory = mod_google_directory[session]
        user = google_directory.service.users().get(userKey=user_key, **other_params).execute()

        if result:
            SetVar(result, user)

    if module == "update":
        user_key = GetParams("user_key")
        body = GetParams("body")

        google_directory = mod_google_directory[session]
        user = google_directory.service.users().update(userKey=user_key, body=body).execute()

        if result:
            SetVar(result, user)
        


except Exception as e:
    PrintException()
    raise e
