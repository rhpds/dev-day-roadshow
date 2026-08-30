# Dev Day Roadshow Automation Collection

Ansible collection for Dev Day Roadshow workshop automation.

## Namespace and Collection Name

- **Namespace**: `dev_day_roadshow`
- **Collection**: `automation`

## Installation

```bash
ansible-galaxy collection install dev_day_roadshow.automation
```

## Roles

This collection includes roles for automating the Dev Day Roadshow workshop environment.

## Usage

```yaml
---
- hosts: localhost
  collections:
    - dev_day_roadshow.automation
  roles:
    - role_name
```

## License

Apache-2.0
