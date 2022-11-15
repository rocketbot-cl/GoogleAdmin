



# Google Admin
  
Este módulo de conecta a la Api Directory de google. Puedes Crear, eliminar o restaurar la contraseña de un Usuario  

## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  

## Como usar este módulo

Para usar este módulo, você precisa configurar as credenciais para se conectar à Google Admin API. Para fazer isso, você precisa seguir os passos abaixo ( [referência](https://developers.google.com/admin-sdk/directory/v1/quickstart/python) ):

- Crie um novo projeto no Google Cloud Console (pule se você já tiver um projeto criado)
    - No canto superior esquerdo, clique no menu **Menu** > **IAM & Admin** > **Create a project**.
    - No campo **Project Name**, insira um nome descritivo para seu projeto.
    - Complete as outras etapas com suas informações

-Ativar API
    -Acesse o [Console do Google Cloud](https://console.cloud.google.com/)
    - No canto superior esquerdo, clique em **Menu** > **APIs & Services** > **Credentials**
    - No campo do navegador, digite **Admin SDK API**
    - Clique no resultado **Admin SDK API**
    - Clique em **Enable**

- Criar credenciais
    -Acesse o [Console do Google Cloud](https://console.cloud.google.com/)
    - No canto superior esquerdo, clique em **Menu** > **APIs e serviços** > **Credenciais**
    - Clique em **Create credentials**
    - Clique em **OAuth client ID**
    - No campo **Application type**, selecione **Desktop Application**
    - No campo **Name**, insira um nome descritivo para as credenciais
    - Aparece uma janela com os dados das credenciais. Clique em **Download JSON**
    - Use este arquivo como credenciais no módulo

## Overview


1. Configurar as credenciais para conectar com o Google Admin API  
Configure google credenciais

2. Criar um novo usuario  
Este comando cria um novo usuario no diretorio do google. O usuario sera criado com o email e senha especificados.

3. Obter usuários  
Obter usuários de Google. Você pode adicionar um filtro para obter apenas usuários com um domínio de e-mail específico.

4. Deletar usuário  
Deletar um usuário do Google Admin

5. Obter usuário  
Obter a informação de um usuário de Google Admin

6. Atualizar usuário  
Atualiza a informação de um usuário de Google Admin  

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