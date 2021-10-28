from pyinfra.operations import server
from pyinfra.api import deploy
from deploy_operation import deploy_into_docker

server.service(
    'docker',
    running=True)
deploy_into_docker()
