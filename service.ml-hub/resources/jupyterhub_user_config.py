import os

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = "mltooling/ml-workspace:0.8.6"
c.DockerSpawner.workspace_images = [c.Spawner.image, "mltooling/ml-workspace-gpu:0.8.6", "mltooling/ml-workspace-r:0.8.6"]
c.DockerSpawner.notebook_dir = '/workspace'

# c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.DockerSpawner.use_internal_ip = True
#c.JupyterHub.hub_ip = os.environ['HUB_IP']

# used to read the json gitlab oauth config file
import json

from oauthenticator.gitlab import LocalGitLabOAuthenticator

c.JupyterHub.authenticator_class = LocalGitLabOAuthenticator

with open('/resources/gitlab_oauth_credentials.json') as f:
    gitlab_oauth = json.load(f)

c.LocalGitLabOAuthenticator.client_id = gitlab_oauth['web']['application_id']
c.LocalGitLabOAuthenticator.client_secret = gitlab_oauth['web']['secret']

c.LocalGitLabOAuthenticator.oauth_callback_url = gitlab_oauth['web']['redirect_uris'] # replace with your domain
c.LocalGitLabOAuthenticator.create_system_users = True
#c.LocalGitLabOAuthenticator.hosted_domain = 'ma.tum.de'   # replace with your domain
#c.LocalGitLabOAuthenticator.login_service = 'Technische Universität München'  # replace with your 'College Name'

# Users
#c.Authenticator.whitelist = {'ritter','viviana'}
c.Authenticator.admin_users = {'admin','ge49gar'}
c.Authenticator.add_user_cmd = ['adduser', '-q', '--gecos', '""', '--disabled-password', '--force-badname']

#c.DummyAuthenticator.password = "some_password"

# The username is "jovyan" and the password is "jupyter"
# As documented here https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-jupyterhub-user-access.html

# the default admin is named "jovyan" and the password is "jupyter" :)

