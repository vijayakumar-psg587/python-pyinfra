from pyinfra.api import deploy
from pyinfra.operations import apt, ssh
from pyinfra.facts.server import LinuxName, Crontab, Date, Sysctl, User, Users
from pyinfra.facts.pkg import PkgPackages
@deploy('JInstall curl wget',  data_defaults=None)
def deploy_into_docker(state, host):
    print('!!!!!!!OOO',host.get_fact(LinuxName))
    print('!!SSS',host.get_fact(Sysctl))
    print('!!SSS',host.get_fact(Users))

    print('!!UUU',host.get_fact(PkgPackages))
    if host.get_fact(LinuxName) == 'Ubuntu':
        filename='pgconf_backup.sh'
        ssh.upload(
            filename, remote_filename='/root', port=22, user='root', use_remote_sudo=False,
            ssh_keyscan=False, ssh_user=None,state=state, host=host
        )
    #    After uploading the file - execute this crontab command
        server.crontab(
            name='Backup /etc weekly',
            command='/bin/tar cf /tmp/etc_bup.tar /etc',
            day_of_week=0,
            hour=1,
            minute=0,
            state=state, host=host
        )