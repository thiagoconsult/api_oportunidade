# MICROSERVIÇO OPORTUNIDADE

Esta API foi desenvolvida para entrega do MVP da Sprint 3 da PUC-RIO. Ela foi desenvolvida em Flask para servir uma aplicação
desenvolvida em React.

### Esta API trás os seguintes métodos:

| Método                 | Funcionalidade                              |
| ---------------------- | ------------------------------------------- |
| oportunidade_create    | Inclusão de uma nova oportunidade           |
| oportunidade_update    | Atualização de uma oportunidade existente   |
| oportunidade_delete    | Exclusão de uma oportunidade existente      |
| oportunidade_get_by_id | Consulta uma oportunidade pelo ID           |
| oportunidade_get_all   | Consulta lista de oportunidades cadastradas |
| ---------------------- | ------------------------------------------- |

# Como executar

Você precisa ter todas as libs utilizadas no projeto e que estão listadas no arquivo requirements.txt.

Para executar este projeto você poderá criar um ambiente virtual primeiramente e ativá-lo.

### Para instalar e ativar a virtual env no Linux:

Na raiz do projeto, exexute:

```
python3 -m venv env
```

Para ativar a env, execute:

```
source env/bin/activate
```

### Instalando o projeto:

Quando a virtual env estiver ativa, irá aparecer antes do caminho do projeto no cmd o nome (env). Agora, é necessário instalar as libs:

```
pip install -r requirements.txt
```

### EXECUTANDO

Execute o comando:

```
python3 run.py
```

```
http://127.0.0.1:5003/
```

Esta página permitirá explorar a documentação do Microserviço
