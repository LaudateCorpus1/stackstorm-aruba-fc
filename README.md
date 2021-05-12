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

This application uses the mongo db installed by StackStorm. Since the DB is secured
you will need to log into the StackStorm mongo DB as a StackStorm admin and create a separate DB

# Companion mongengine to work with StackStorm mongo DB

log in with admin first
-------------------------------------------------------------------------------------
mongo -u admin -p UkIbDILcNbMhkh3KtN6xfr9h admin  (passwd in /etc/st2/st2.config)

# Then create a new user
db.createUser({user: "appUser",pwd: "passwordForAppUser",roles: [ { role: "readWrite", db: "app_db" } ]})

If you want to look at the mongo collections via the mongo client do this:


```
mongo -u appUser -p passwordForAppUser admin
```
