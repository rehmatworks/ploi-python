# Ploi Python Package
A Python package to interact with [Ploi API](https://developers.ploi.io/).

Ploi is an awesome server management tool that lets you manage an Ubuntu server to host PHP applications with great flexibility. If you want to programatically interact with Ploi using Python, then this package will let you consume their API the easy way.

## Installation
```shell
pip install ploi
```
### Usage
```python
from ploi.ploi import Ploi
ApiToken = '#############' # Your Ploi API Token
p = Ploi(ApiToken)
```

#### List Servers
```python
p.list_servers()
```

### Get a Server
```python
p.get_server(serverId)
```

### List Sites
```python
p.list_sites(serverId)
```

### Create a Site
```python
data = {
    'root_domain': 'example.com',
    'web_directory': '/example/', # Slashes are complusory
}
p.create_site(serverId, data=data)
```

### Get a Site
```python
p.show_site(serverId, siteId)
```

### Delete a Site
```python
p.delete_site(serverId, siteId)
```

### List Databases
```python
p.list_databases(serverId)
```

### Create a Database
```python
data = {
    'name': 'dbname',
    'user': 'dbuser',
    'password': 'dbpassword'
}
p.create_database(serverId, data=data)
```

### Get a Database
```python
p.show_database(serverId, databaseId)
```

### Delete a Database
```python
p.delete_database(serverId, databaseId)
```

More methods will be supported in future versions as this is just a starting point.
