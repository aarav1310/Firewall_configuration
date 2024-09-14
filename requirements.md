## Usage
Install the required dependencies:

pip install -r requirements.txt


Run the script:

python firewall_config.py

The script will apply the specified firewall rules to the system.

## Requirements

- Python 3.x
- `subprocess` module
- `iptables` command-line tool

## Configuration

The script uses a list of firewall rules defined in the `firewall_rules` variable. Each rule should be a string that follows the `iptables` command syntax.

```python
firewall_rules = [
 '-A INPUT -p tcp --dport 22 -j ACCEPT',
 '-A INPUT -p tcp --dport 80 -j ACCEPT',
 '-A INPUT -p tcp --dport 443 -j ACCEPT',
 '-A INPUT -j DROP'
]
