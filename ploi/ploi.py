import requests, json

class Ploi:

    def __init__(self, ApiToken):
        self.BaseUrl = 'https://ploi.io/api'
        self.ApiToken = ApiToken
        self.Headers = {
            'Authorization': 'Bearer {}'.format(self.ApiToken),
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.endpoints = {
            'servers': 'servers',
            'sites': 'servers/{serverId}/sites',
            'databases': 'servers/{serverId}/mysql'
        }

    def send_response(self, res, json=True):
        if res.status_code in [200, 201]:
            if json:
                return res.json()
            else:
                return True
        else:
            raise Exception('{} Error: {}'.format(res.status_code, res.reason))

    def make_request(self, endpoint, requestType='GET', data=None):
        expectJson = True
        if requestType == 'GET':
            res = requests.get('{}/{}'.format(self.BaseUrl, endpoint), headers=self.Headers)
        elif requestType == 'POST':
            res = requests.post('{}/{}'.format(self.BaseUrl, endpoint), data=json.dumps(data), headers=self.Headers)
        elif requestType == 'DELETE':
            expectJson = False
            res = requests.delete('{}/{}'.format(self.BaseUrl, endpoint), headers=self.Headers)
        return self.send_response(res, json=expectJson)

    def list_servers(self):
        return self.make_request('{}'.format(self.endpoints.get('servers')))

    def get_server(self, serverId):
        return self.make_request('{}/{}'.format(self.endpoints.get('servers'), serverId))

    def list_sites(self, serverId):
        return self.make_request('{}'.format(self.endpoints.get('sites')).format(serverId=serverId))

    def create_site(self, serverId, data):
        # Data should be a dictionary: {'root_domain': 'abc.com', 'web_directory': '/abc/', 'project_root': '/abc/'}
        if not 'web_directory' in data:
            data['web_directory'] = '/public/'

        params = ['root_domain']
        for item in params:
            if not item in data:
                raise Exception('{} is a required parameter.'.format(item))
        return self.make_request('{}'.format(self.endpoints.get('sites')).format(serverId=serverId), requestType='POST', data=data)

    def show_site(self, serverId, siteId):
        return self.make_request('{}/{}'.format(self.endpoints.get('sites'), siteId).format(serverId=serverId))

    def delete_site(self, serverId, siteId):
        return self.make_request('{}/{}'.format(self.endpoints.get('sites'), siteId).format(serverId=serverId), requestType='DELETE')

    def list_databases(self, serverId):
        return self.make_request('{}'.format(self.endpoints.get('databases')).format(serverId=serverId))

    def create_database(self, serverId, data):
        # Data should be a dictionary: {'name': 'mydb', 'user': 'dbuser', 'password': 'dbpass'}
        params = ['name', 'user', 'password']
        for item in params:
            if not item in data:
                raise Exception('{} is a required parameter.'.format(item))
        return self.make_request('{}'.format(self.endpoints.get('databases')).format(serverId=serverId), requestType='POST', data=data)

    def show_database(self, serverId, databaseId):
        return self.make_request('{}/{}'.format(self.endpoints.get('databases'), databaseId).format(serverId=serverId))

    def delete_database(self, serverId, databaseId):
        return self.make_request('{}/{}'.format(self.endpoints.get('databases'), databaseId).format(serverId=serverId), requestType='DELETE')
