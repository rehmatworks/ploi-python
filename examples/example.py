from ploi.ploi import Ploi
ApiToken = '#############################'

p = Ploi(ApiToken)

# List Servers
p.list_servers()

# Get Server
p.get_server(serverId)

# List Sites
p.list_sites(serverId)

# Create a Site
data = {
    'root_domain': 'example.com',
    'web_directory': '/example/', # Slashes are complusory
}
p.create_site(serverId, data=data)

# Get a Site
p.show_site(serverId, siteId)

# Delete a Site
p.delete_site(serverId, siteId)
