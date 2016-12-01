from fabric.api import env, task, sudo, run
from cs43202api import Client

env.use_ssh_config = True

# Create a CS43202api client object and automatically get all container ips!
client = Client()
env.hosts = client.get_container_ips()

@task
def example():
    run('whoami')

@task
def yumupgrade():
    sudo('yum -y -q upgrade')
