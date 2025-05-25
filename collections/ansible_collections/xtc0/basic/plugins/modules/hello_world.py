

DOCUMENTATION = '''
---
module: hello_world
short_description: Prints Hello + user_name
description:
  - This module prints "Hello" followed by a user-provided name or "World" if no name is given.
options:
  user_name:
    description:
      - Name of the user to greet.
    required: false
    type: str
author:
  - xtc0
'''

EXAMPLES = '''
- name: Say hello to Sally
  xtc0.basic.hello_world:
    user_name: Sally
'''

RETURN = '''
greeting:
  description: The greeting message
  type: str
'''


# module: hello_world
# short description of module: prints "Hello" + user_name
# type of user_name variable: string

# example of how to use module in playbook:

# - name: Greet someone
# yk.basic.hello_world:
#   user_name: Alice


from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        user_name=dict(type='str', required=False, default="World")
    )

    module = AnsibleModule(argument_spec=module_args)

    user_name = module.params['user_name']
    message = f"Hello {user_name}!"

    module.exit_json(changed=False, msg=message)

def main():
    run_module()

if __name__ == '__main__':
    main()

