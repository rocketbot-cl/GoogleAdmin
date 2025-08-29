



# Google Admin
  
Este módulo se conecta ao diretório de APIs do Google. Você pode criar, excluir ou restaurar a senha de um usuário.

![banner](imgs/Banner_GoogleAdmin.jpg)
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

## Descrição do comando

### Configurar as credenciais para conectar com o Google Admin API
  
Configure google credenciais
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho de credenciais|Arquivo json com as credenciais de acesso ao API do Google Admin. Veja a documentação para obter mais informações.|C:\Usuario\Desktop\credentials.json|
|Atribuir resultado a variável|Nome da variável onde será atribuído o resultado da execução do comando.|result|

### Criar um novo usuario
  
Este comando cria um novo usuario no diretorio do google. O usuario sera criado com o email e senha especificados.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome|Nome do usuario a ser criado|Thiago|
|Sobrenome|Sobrenome do usuario a ser criado|Silva|
|Atribuir resultado a variável|Nome da variavel onde armazenar o resultado do comando|resultado|
|E-mail|E-mail do usuario a ser criado|thiago.silva@mail.com|
|Senha|Senha do usuario a ser criado. Se nao especificado, uma senha aleatoria sera gerada|123456789|
|Dados adicionais|Dados adicionais a ser adicionados ao usuario. Mais informacao aqui https//developers.google.com/admin-sdk/directory/reference/rest/v1/users/insert|{"isAdmin": True, "recoveryEmail": "r2d2@gmail.com"}|

### Obter usuários
  
Obter usuários de Google. Você pode adicionar um filtro para obter apenas usuários com um domínio de e-mail específico.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Domínio (opcional)|Filtrar usuários por domínio de e-mail.|@rocketbot.com|
|Nome da variavel onde armazenar o resultado do comando|Nome da variavel onde armazenar o resultado do comando|resultado|
|Ordenar por (opcional)|Ordenar usuários por este campo. Se não selecionar nenhum campo, os usuários serão ordenados por email.|email|
|Ascendente ou Descendente|Ordenar usuários de forma ascendente ou descendente.|ASCENDING|
|Dados adicionais|Dados adicionais a ser adicionados ao usuario. Mais informacao aqui https//developers.google.com/admin-sdk/directory/reference/rest/v1/users/list|{"maxResults": 10, "viewType": "domain_public", ...}|

### Deletar usuário
  
Deletar um usuário do Google Admin
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Chave de Usuário|Chave de Usuário ou Email Address do usuário a ser deletado|111575529871886135722 ou thiago.silva@mail.com|
|Nome da variavel onde armazenar o resultado|Nome da variavel onde armazenar o resultado do comando|resultado|
|Dados adicionais|Dados adicionais a ser enviados a API. Mais info https//developers.google.com/admin-sdk/directory/reference/rest/v1/users/delete|{"viewType": "domain_public", ...}|

### Obter usuário
  
Obter a informação de um usuário de Google Admin
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Chave de Usuário|A chave de usuário pode ser o endereço de e-mail primário do usuário ou o ID único do usuário. Listar os usuários para conhecer sua chave de usuário|111575529871886135722 ou thiago.silva@mail.com|
|Nome da variavel onde armazenar o resultado|Nome da variavel onde armazenar o resultado do comando|resultado|
|Dados adicionais|Dados adicionais a ser enviados junto com a solicitação. Mais informação https//developers.google.com/admin-sdk/directory/reference/rest/v1/users/get|{"viewType": "domain_public", ...}|

### Atualizar usuário
  
Atualiza a informação de um usuário de Google Admin
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Chave de Usuário|A chave de usuário pode ser o endereço de e-mail primário do usuário ou o ID único do usuário. Listar os usuários para conhecer sua chave de usuário|111575529871886135722 ou thiago.silva@mail.com|
|Nome da variavel onde armazenar o resultado|Nome da variavel onde armazenar o resultado do comando|resultado|
|E-mail|E-mail do usuario a ser criado|thiago.silva@mail.com|
|Senha|Senha do usuario a ser criado. Se nao especificado, uma senha aleatoria sera gerada|123456789|
|Dados adicionais|Dados adicionais a ser enviados junto com a solicitação. Mais informação https//developers.google.com/admin-sdk/directory/reference/rest/v1/users/patch|{"viewType": "domain_public", ...}|
