import netifaces
import subprocess

CONFIG_PATH = "/etc/ppp/peers/"
PAP_PATH = "/etc/ppp/pap-secrets"
CHAP_PATH = "/etc/ppp/chap-secrets"

DEFAULT_CONFIG = """plugin rp-pppoe.so
# rp_pppoe_ac 'имя концентратора доступа'
# rp_pppoe_service 'имя службы PPPoE'

# netw iface
{0}
# login
name "{1}"
usepeerdns
persist
# раскомментируйте, если вам нужен автодозвон "по требованию"
#demand
#idle 180
defaultroute
hide-password
noauth
"""#.format(netifaces.interfaces()[1], "username")

def WritePPPConfig(username : str, password : str):
    config_file = open(CONFIG_PATH + "batya_pppoe", "w")
    config_file.write(DEFAULT_CONFIG.format(netifaces.interfaces()[1], username))
    config_file.close()

    pap_config = open(PAP_PATH, "a")
    pap_config.write(username + " * " + password)
    pap_config.close()

    chap_config = open(CHAP_PATH, "a")
    chap_config.write(username + " * " + password)
    chap_config.close()

    subprocess.call(["pon", "batya_pppoe"])
    # CHECK! --> journalctl -b --no-pager | grep pppd
