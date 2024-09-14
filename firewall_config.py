import subprocess
def config_firewall(rules):
    for rule in rules:
        subprocess.run(['iptables']+ rule.split())

firewall_rules=[                                    #Enter firewall rules here 
    '-A INPUT -p tcp --dport -j ACCEPT',             # Sample ports rules 
    '-A INPUT -p tcp --dport 22 -j ACCEPT',
    '-A INPUT -p tcp --dport 80 -j ACCEPT',
    '-A INPUT -p tcp --dport 443 -j ACCEPT',
    '-A INPUT -j DROP'
    ]
config_firewall(firewall_rules)


