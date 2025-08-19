""" Firewalls have four basic fundamental principle which includes:

Have a rule list where IPs are defined as Allowed or Blocked.
Have a way to generate multiple random IP addresses that can be tested against against the rules set for specific IPs (where known).
The process of Evaluation takes place to check if the generated IP matches any IP in the rule list to know if to Allow or Block.
Result is output to the console """


import random

def generate_random_ip():
    """Generate a random IP address between 0 to 254, which is between 192.168.1.0 to 192.168.1.254"""
    return f"192.168.1.{random.randint(0, 255)}"

def check_firewall_rules(ip, rules):
    """Check if the IP address matches any firewall rule and return the action."""
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"  # Default action if no rule matches

def main():
    """All these IP addresses are used for an Implicit Trust Implementation, meaning Block only these list and allow the rest, changing these
    Block values to Allow creates a Zero Trust Implementation where you are Allowing only these and Blocking everyone else."""
    # Define the firewall rules (key: IP address, value: action)
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block"
    }

      # Simulate network traffic
    for _ in range(12):
     ip_address = generate_random_ip()
     action = check_firewall_rules(ip_address, firewall_rules)
     random_number = random.randint(0, 9999)
     print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

if __name__ == "__main__":
    main()
