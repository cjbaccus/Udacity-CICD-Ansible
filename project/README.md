## This is the instructions for executing this playbook, and where and why everything goes where it does
### will have to setup an aws EC2 instance and generate a private key named:
 ``` udacity.pem ```

### The folder structure is as follows:
```
/main-remote.yml
/roles
/roles/setup/
/rolese/setup/tasks/
/rolese/setup/tasks/main.yml
/roles/setup/files/
/roles/setup/files/index.js
```

### Ansible playbook command
ansible-playbook main-remote.yml -i inventory --private-key udacity.pem

