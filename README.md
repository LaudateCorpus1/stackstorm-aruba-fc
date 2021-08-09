# stackstorm-arista-cvp
# ARISTA Integration Pack
This pack allows you to integrate with
[Arista EOSr](https://www.arista.com/en/products/eos).

## Configuration
Copy the example configuration in [arista-eos.yaml.example](./arista-eos.yaml.example) to
`/opt/stackstorm/configs/arista-eos.yaml` and edit as required.

It must contain:

```
ipaddress - Your Arista EOS appliance IP address
username - Arista EOS Username
password - Arista EOS Password
```

You can also use dynamic values from the datastore. See the
[docs](https://www.arista.com/en/cg-cv/cv-cloudvision-portal-cvp-overview) for more info.

Example configuration:

```yaml
---
  ipaddress: "10.10.10.10"
  username: "admin"
  password: "admin"
```
You can also run `st2 pack config arista-cvp` and answer the prompts

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`


## Actions

Actions are defined in two groups:

### Individual actions: GET, POST, PUT with under bar will precede each individual action
* ``get_alarms``
* ``get_interfaces``
* ``get_inventory``


### Orquestra Workflows: will not
* ``sendsnow``
* ``get-arista-eos-2-snow``
* ``set-vlans``

This application uses the mongo db installed by StackStorm. Since the DB is secured
you will need to log into the StackStorm mongo DB as a StackStorm admin and create a separate DB

# CVP to get mongengine to work with StackStorm mongo DB

log in to stackstorm database with admin first
-------------------------------------------------------------------------------------
mongo -u admin -p UkIbDILcNbMhkh3KtN6xfr9h admin  (passwd in /etc/st2/st2.config)

# Then create a new user
db.createUser({user: "appUser",pwd: "passwordForAppUser",roles: [ { role: "readWrite", db: "app_db" } ]})

If you want to look at the mongo collections via the mongo client do this:

```
mongo -u appUser -p passwordForAppUser admin
show dbs
use <db>
show collections
```
