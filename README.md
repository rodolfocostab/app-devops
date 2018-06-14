# Projeto Teste DevOps

## Como usar:

### Requisitos

Ansible instalado, para Debian e distribuições utilizar comando abaixo:

```
sudo apt-get install ansible
```

### Instalação

Para começar a usar a API e rodar ela via Docker foi feito toda configuração com o Ansible. Basta rodar o comando:

```
ansible-playbook provision.yml
```

Ao finalizar a receita devera estar disponivel dois containers rodando um com API e o outro do banco.

### Testar a API

A API pode ser utilizada via navegador ou como exemplo via comando curl realizando post.

```
curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"component_name": "Componente2"}' http://localhost:8000/api/post/
```

Para receber a inclusão em JSON:

```
curl http://localhost:8000/api/post/1/?format=json
```

Levando em conta que o número apos a url /post/ é a ID da inclusão.

### Pagina Admin API

Foi utilizada a linguagem Python na criação da API em conjunto com framework Django.
Django fornece uma pagina Web com as inclusões da API e seus status.

```
localhost:8000\admin
```

Senha padrão de instalação customizavel da página Admin:

```
user: admin
passwd: testedevops
```
