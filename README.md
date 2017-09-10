

# Consul watch handler for slack

Consul watch handler that sends alerts to slack channel.

To use this script with Consul use configuration like the following:

    {
        "type": "checks",
        "state" "critical" #optional
        "handler": "consul-watch-handler"
    }

