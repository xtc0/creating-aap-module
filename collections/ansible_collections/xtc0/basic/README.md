# Ansible Collection - xtc0.basic

### About

This Ansible Collection has a module called "hello_world" which allows the user to print "Hello" followed by a user-provided name or "World" if no name is given.

## I know nothing about Ansible, but I want to install xtc0.basic collection, can I?

```yaml
ansible-galaxy collection install xtc0.basic
```

## What's inside the xtc0.basic collection?
- The collection contains a module called "hello_world".
- This module allows the user to print "Hello" followed by a user-provided name or "World" if no name is given.

## How can I use xtc0.basic's module?
- Go to the playbook named "test_hello.yml".
- Under the variable "user_name", change it to the input that you'd like.

```yaml
### this prints "Hello Sally"
- name: Say hello to Sally
  xtc0.basic.hello_world:
    user_name: Sally
```

```yaml
### this prints "Hello John"
- name: Say hello to Sally
  xtc0.basic.hello_world:
    user_name: John
```


