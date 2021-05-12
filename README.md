# stackstorm-aruba-fc
# ARUBAFC Integration Pack
This pack allows you to integrate with
[Aruba Fabric Composer](https://www.arubanetworks.com/products/switches/core-and-data-center/fabric-composer/).

## Configuration
Copy the example configuration in [arubafc.yaml.example](./arubafc.yaml.example) to
`/opt/stackstorm/configs/arubafc.yaml` and edit as required.

It must contain:

```
ipaddress - Your AFC appliance IP address
username - AFC Username
password - AFC Password
```

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

Example configuration:

```yaml
---
  ipaddress: "10.10.10.10"
  username: "admin"
  password: "admin"
```
You can also run `st2 pack config arubafc` and answer the prompts

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`


## Actions

Actions are defined in two groups:

### Individual actions: GET, POST, PUT with under bar will precede each individual action
* ``get_alarms``
* ``get_switches``
* ``get_events``


### Orquestra Workflows: will not
* ``sendsnow``
* ``get-arubafc-events``
* ``getswitches``
