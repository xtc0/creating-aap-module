#!/usr/bin/python
# coding: utf-8 -*-


# (c) 2020, John Westcott IV <john.westcott.iv@redhat.com>
# (c) 2021, Sean Sullivan <@sean-m-sullivan>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: aap_token
author: "John Westcott IV (@john-westcott-iv), Sean Sullivan (@sean-m-sullivan)"
short_description: create, update, or destroy automation platform gateway tokens.
description:
    - Create or destroy automation platform gateway tokens.
    - In addition, the module sets an Ansible fact which can be passed into other
      aap modules as the parameter aap_token. See examples for usage.
    - Because of the sensitive nature of tokens, the created token value is only available once
      through the Ansible fact. (See RETURN for details)
    - Due to the nature of tokens in automation platform gateway this module is not idempotent. A second will
      with the same parameters will create a new token.
    - If you are creating a temporary token for use with modules you should delete the token
      when you are done with it. See the example for how to do it.
options:
    application:
      description:
        - The application name, ID, or named URL tied to this token.
      required: False
      type: str
    description:
      description:
        - Optional description of this access token.
      required: False
      type: str
    existing_token:
      description: The data structure produced from token in create mode to be used with state absent.
      type: dict
    existing_token_id:
      description: A token ID (number) which can be used to delete an arbitrary token with state absent.
      type: str
    scope:
      description:
        - Allowed scopes, further restricts user's permissions. Must be a simple space-separated string with allowed scopes ['read', 'write'].
      required: False
      type: str
      choices: ["read", "write"]
    state:
      description:
        - Desired state of the resource.
      choices: ["present", "absent"]
      default: "present"
      type: str

extends_documentation_fragment: ansible.gateway_configuration.auth
"""

EXAMPLES = """
- block:
    - name: Create a new token using an existing token
      ansible.gateway_configuration.aap_token:
        description: '{{ token_description }}'
        scope: "write"
        state: present
        aap_token: "{{ my_existing_token }}"

    - name: Delete this token
      ansible.gateway_configuration.aap_token:
        existing_token: "{{ aap_token }}"
        state: absent

    - name: Create a new token using username/password
      ansible.gateway_configuration.aap_token:
        description: '{{ token_description }}'
        scope: "write"
        state: present
        aap_gateway: "{{ aap_gateway }}"
        aap_username: "{{ my_username }}"
        aap_password: "{{ my_password }}"

    - name: Use our new token to make another call
      namespace:
        aap_token: "{{ aap_token }}"

  always:
    - name: Delete our Token with the token we created
      ansible.gateway_configuration.aap_token:
        existing_token: "{{ aap_token }}"
        state: absent
      when: token is defined

- name: Delete a token by its id
  ansible.gateway_configuration.aap_token:
    existing_token_id: 4
    state: absent
...
"""

RETURN = """
aap_token:
  type: dict
  description: An Ansible Fact variable representing a token object which can be used for auth in subsequent modules. See examples for usage.
  contains:
    token:
      description: The token that was generated. This token can never be accessed again, make sure this value is noted before it is lost.
      type: str
    id:
      description: The numeric ID of the token created
      type: str
  returned: on successful create
"""

from ..module_utils.aap_module import AAPModule


def return_token(module, last_response):
    # A token is special because you can never get the actual token ID back from the API.
    # So the default module return would give you an ID but then the token would forever be masked on you.
    # This method will return the entire token object we got back so that a user has access to the token

    module.json_output["ansible_facts"] = {
        "aap_token": last_response,
    }
    module.exit_json(**module.json_output)


def main():
    # Any additional arguments that are not fields of the item can be added here
    argument_spec = dict(
        description=dict(),
        application=dict(),
        scope=dict(choices=['read', 'write']),
        existing_token=dict(type='dict'),
        existing_token_id=dict(),
        state=dict(choices=['present', 'absent'], default='present'),
    )

    # Create a module for ourselves
    module = AAPModule(
        argument_spec=argument_spec,
        mutually_exclusive=[
            ('existing_token', 'existing_token_id'),
        ],
        required_if=[
            [
                'state',
                'absent',
                ('existing_token', 'existing_token_id'),
                True,
            ],
        ],
    )

    # Extract our parameters
    description = module.params.get('description')
    application = module.params.get('application')
    scope = module.params.get('scope')
    existing_token = module.params.get('existing_token')
    existing_token_id = module.params.get('existing_token_id')
    state = module.params.get('state')

    if state == 'absent':
        if not existing_token:
            existing_token = module.get_one(
                'tokens',
                **{
                    'data': {
                        'id': existing_token_id,
                    }
                },
            )

        # If the state was absent we can let the module delete it if needed, the module will handle exiting from this
        module.delete_if_needed(existing_token)

    # Attempt to look up the related items the user specified (these will fail the module if not found)
    application_id = None
    if application:
        application_id = module.resolve_name_to_id('applications', application)

    # Create the data that gets sent for create and update
    new_fields = {}
    if description is not None:
        new_fields['description'] = description
    if application is not None:
        new_fields['application'] = application_id
    if scope is not None:
        new_fields['scope'] = scope

    # If the state was present and we can let the module build or update the existing item, this will return on its own
    module.create_or_update_if_needed(
        None,
        new_fields,
        endpoint='tokens',
        item_type='token',
        associations={},
        on_create=return_token,
    )


if __name__ == '__main__':
    main()
