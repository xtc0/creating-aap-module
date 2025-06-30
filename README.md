
# creating-aap-module
In this repository, I will be sharing the steps to create, build and publish an ansible collection

1) Successfully install AAP
2) Go into “collections” folder and then into the “ansible_collections” folder
3) Enter this command “ansible-galaxy collection init xtc0.basic”
4) After xtc0 directory has been created, use this command “cd xtc0/basic”
5) You will see a structure like:
xtc0/basic/
├── plugins/
│   └── modules/
├── README.md
├── galaxy.yml
└── meta
   └── runtime.yml

6) Go into plugins folder and create a subfolder called “modules”
7) Create this directory in plugins: “plugins/modules/hello_world.py”
8) Make sure to add documentation inside hello_world.py (Ansible Galaxy will extract info from here and fill in categories like Synopsis, Parameters, Examples, Return Values on Ansible Galaxy website)
9) Go to directory where inventory file lies and create a playbook called test_hello.yml
10) To run test_hello.yml playbook, use command: “ansible-playbook test_hello.yml”
11) Fill in galaxy.yml (as seen in step 5’s tree structure). galaxy.yml file is essential metadata that tells Ansible Galaxy and users what your collection is, who made it, and how it should be used.
12) Go to this file: xtc0/basic directory/meta/runtime.yml
13) Uncomment the variable “requires_ansible” in runtime.yml
14) Build the collection using “ansible-galaxy collection build”
15) A tarball like “xtc0-basic-1.0.0.tar.gz” is created
16) To publish collection to Ansible Galaxy, go to: https://galaxy.ansible.com
17) Sign in with GitHub (must be GitHub — Galaxy syncs with GitHub repos).
18) Make sure your GitHub username matches the namespace in galaxy.yml — e.g. if your namespace is xtc0, your GitHub user/org must also be xtc0.
19) If it doesn't match, you need to request a namespace or use one you own.
20) Once you’ve logged into Galaxy, get your API token.
21) Use this command: “ansible-galaxy collection publish xtc0-basic-1.0.0.tar.gz --api-key <your_api_key>”
22) Once done, your collection will be live at: https://galaxy.ansible.com/xtc0/basic (change xtc0 to your own namespace/ Github username)
23) You and others can now install your module using: “ansible-galaxy collection install xtc0.basic”



# AAP containerized installer

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Table of Contents
* [Configuration](#configuration)
   * [Common](#common)
   * [Images](#images)
   * [Automation Controller](#automation-controller)
   * [Automation EDA](#automation-eda)
   * [Automation Gateway](#automation-gateway)
   * [Automation Hub](#automation-hub)
   * [Database](#database)
   * [Receptor](#receptor)
   * [Redis](#redis)

## Configuration

### Common

| Name                  | Description                 | Required | Optional | Default                        |
| --------------------- | --------------------------- | -------- | -------- | ------------------------------ |
| bundle_dir            | Bundle directory            |     x    |          | ./bundle                       |
| bundle_install        | Use offline installation    |          |    x     | true                           |
| ca_tls_cert           | TLS CA certificate          |          |    x     |                                |
| ca_tls_key            | TLS CA key                  |          |    x     |                                |
| ca_tls_key_passphrase | TLS CA key passphrase       |          |    x     |                                |
| ca_tls_remote         | TLS CA remote files         |          |    x     | false                          |
| container_compress    | Container compress software |          |    x     | gzip                           |
| container_keep_images | Keep container images       |          |    x     | false                          |
| container_pull_images | Pull newer container images |          |    x     | true                           |
| custom_ca_cert        | Custom TLS CA certificate   |          |    x     |                                |
| feature_flags         | Feature flags dictionary    |          |    x     |                                |
| registry_auth         | Use registry authentication |          |    x     | true                           |
| registry_ns_aap       | AAP registry namespace      |          |    x     | ansible-automation-platform-25 |
| registry_ns_rhel      | RHEL registry namespace     |          |    x     | rhel8                          |
| registry_tls_verify   | Verify registry TLS         |          |    x     | true                           |
| registry_url          | The registry URL            |          |    x     | registry.redhat.io             |
| registry_username     | The registry username       |          |    x     |                                |
| registry_password     | The registry password       |          |    x     |                                |

### Images

| Name                | Description                           | Required | Optional | Default                        |
| ------------------- | ------------------------------------- | -------- | -------- | ------------------------------ |
| controller_image    | Automation Controller image           |          |    x     | controller-rhel8:latest        |
| de_extra_images     | Decision Environment extra images     |          |    x     | []                             |
| de_supported_image  | Decision Environment supported image  |          |    x     | de-supported-rhel8:latest      |
| eda_image           | Automation EDA image                  |          |    x     | eda-controller-rhel8:latest    |
| eda_web_image       | Automation EDA web image              |          |    x     | eda-controller-ui-rhel8:latest |
| ee_extra_images     | Execution Environment extra images    |          |    x     | []                             |
| ee_minimal_image    | Execution Environment minimal image   |          |    x     | ee-minimal-rhel8:latest        |
| ee_supported_image  | Execution Environment supported image |          |    x     | ee-supported-rhel8:latest      |
| gateway_image       | Automation Gateway image              |          |    x     | gateway-rhel8:latest           |
| gateway_proxy_image | Automation Gateway Proxy image        |          |    x     | gateway-proxy-rhel8:latest     |
| hub_image           | Automation Hub image                  |          |    x     | hub-rhel8:latest               |
| hub_web_image       | Automation Hub web image              |          |    x     | hub-web-rhel8:latest           |
| pcp_image           | Performance Co-Pilot image            |          |    x     | pcp:latest                     |
| postgresql_image    | Postgresql image                      |          |    x     | postgresql-15:latest           |
| receptor_image      | Receptor image                        |          |    x     | receptor-rhel8:latest          |
| redis_image         | Redis image                           |          |    x     | redis-6:latest                 |

### Automation Controller

| Name                                  | Description                                   | Required | Optional | Default            |
| ------------------------------------- | --------------------------------------------- | -------- | -------- | ------------------ |
| controller_admin_password             | Automation Controller admin password          |     x    |          |                    |
| controller_admin_user                 | Automation Controller admin user              |          |    x     | admin              |
| controller_event_workers              | Automation Controller event workers           |          |    x     |  4                 |
| controller_extra_settings             | Automation Controller extra settings          |          |    x     | []                 |
| controller_license_file               | Automation Controller license file            |          |    x     |                    |
| controller_nginx_client_max_body_size | Nginx maximum body size                       |          |    x     | 5m                 |
| controller_nginx_disable_hsts         | Disable Nginx HSTS                            |          |    x     | false              |
| controller_nginx_disable_https        | Disable Nginx HTTPS                           |          |    x     | false              |
| controller_nginx_hsts_max_age         | Nginx HSTS maximum age                        |          |    x     | 63072000           |
| controller_nginx_http_port            | Nginx HTTP port                               |          |    x     | 8080               |
| controller_nginx_https_port           | Nginx HTTPS port                              |          |    x     | 8443               |
| controller_nginx_https_protocols      | Nginx HTTPS protocols                         |          |    x     | [TLSv1.2, TLSv1.3] |
| controller_nginx_user_headers         | Custom Nginx headers                          |          |    x     | []                 |
| controller_percent_memory_capacity    | Automation Controller memory capacity         |          |    x     | 1.0                |
| controller_pg_cert_auth               | Postgresql Controller TLS auth                |          |    x     | false              |
| controller_pg_database                | Postgresql Controller database                |          |    x     | awx                |
| controller_pg_host                    | Postgresql Controller host                    |     x    |          |                    |
| controller_pg_password                | Postgresql Controller password                |          |    x     |                    |
| controller_pg_port                    | Postgresql Controller port                    |          |    x     | 5432               |
| controller_pg_socket                  | Postgresql Controller unix socket             |          |    x     |                    |
| controller_pg_sslmode                 | Postgresql Controller SSL mode                |          |    x     | prefer             |
| controller_pg_tls_cert                | Postgresql Controller TLS certificate         |          |    x     |                    |
| controller_pg_tls_key                 | Postgresql Controller TLS key                 |          |    x     |                    |
| controller_pg_username                | Postgresql Controller user                    |          |    x     | awx                |
| controller_postinstall                | Enable Controller postinstall                 |          |    x     | false              |
| controller_postinstall_dir            | Postinstall directory                         |          |    x     |                    |
| controller_secret_key                 | Automation Controller secret key              |          |    x     |                    |
| controller_tls_cert                   | Automation Controller TLS certificate         |          |    x     |                    |
| controller_tls_key                    | Automation Controller TLS key                 |          |    x     |                    |
| controller_tls_remote                 | Automation Controller TLS remote files        |          |    x     | false              |
| controller_uwsgi_listen_queue_size    | Automation Controller uwsgi listen queue size |          |    x     | 2048               |

Extra parameters will need to be passed through an ansible `controller_extra_settings` variable.

For example, you may set:

```yaml
controller_extra_settings:
  - setting: USE_X_FORWARDED_HOST
    value: true
```

#### Automation Controller - Postinstall

The controller postinstall allows one to create resources (projects, users, roles, etc..) after the controller deployment.
This requires the controller license to be installed first (see controller_license_file variable).

| Name                                 | Description                                 | Required | Optional | Default |
| ------------------------------------ | ------------------------------------------- | -------- | -------- | --------|
| controller_postinstall               | Enable Automation Controller postinstall    |          |     x    | false   |
| controller_postinstall_async_delay   | Postinstall delay between retries           |          |     x    | 1       |
| controller_postinstall_async_retries | Postinstall number of tries to attempt      |          |     x    | 30      |
| controller_postinstall_dir           | Automation Controller postinstall directory |          |     x    |         |
| controller_postinstall_ignore_files  | Automation Controller ignore files          |          |     x    | []      |
| controller_postinstall_repo_ref      | Automation Controller repository branch/tag |          |     x    | main    |
| controller_postinstall_repo_url      | Automation Controller repository URL        |          |     x    |         |

The `controller_postinstall_repo_url` variable can be used to define the postinstall repository URL which may include
authentication information.

- `http(s)://<host>/<repo>.git` (public repository without http(s) authentication)
- `http(s)://<user>:<password>@<host>:<repo>.git` (private repository with http(s) authentication)
- `git@<host>:<repo>.git` (public/private repository with ssh authentication)

When using ssh based authentication, the installer doesn't configure anything (ssh key or so) for you and you need
to have everything configured on the installer node.

### Automation EDA

| Name                           | Description                             | Required | Optional | Default            |
| ------------------------------ | --------------------------------------- | -------- | -------- | ------------------ |
| eda_activation_workers         | Automation EDA activation workers count |          |    x     | 2                  |
| eda_admin_password             | Automation EDA admin password           |     x    |          |                    |
| eda_debug                      | Automation EDA debug                    |          |    x     | false              |
| eda_extra_settings             | Automation EDA extra settings           |          |    x     | []                 |
| eda_max_running_activations    | Automation EDA max running activations  |          |    x     | 12                 |
| eda_nginx_client_max_body_size | Nginx maximum body size                 |          |    x     | 1m                 |
| eda_nginx_disable_hsts         | Disable Nginx HSTS                      |          |    x     | false              |
| eda_nginx_disable_https        | Disable Nginx HTTPS                     |          |    x     | false              |
| eda_nginx_hsts_max_age         | Nginx HSTS maximum age                  |          |    x     | 63072000           |
| eda_nginx_http_port            | Nginx HTTP port                         |          |    x     | 8082               |
| eda_nginx_https_port           | Nginx HTTPS port                        |          |    x     | 8445               |
| eda_nginx_https_protocols      | Nginx HTTPS protocols                   |          |    x     | [TLSv1.2, TLSv1.3] |
| eda_nginx_user_headers         | Custom Nginx headers                    |          |    x     | []                 |
| eda_pg_cert_auth               | Postgresql EDA TLS auth                 |          |    x     | false              |
| eda_pg_database                | Postgresql EDA database                 |          |    x     | eda                |
| eda_pg_host                    | Postgresql EDA host                     |     x    |          |                    |
| eda_pg_password                | Postgresql EDA password                 |          |    x     |                    |
| eda_pg_port                    | Postgresql EDA port                     |          |    x     | 5432               |
| eda_pg_socket                  | Postgresql EDA unix socket              |          |    x     |                    |
| eda_pg_sslmode                 | Postgresql EDA SSL mode                 |          |    x     | prefer             |
| eda_pg_tls_cert                | Postgresql EDA TLS certificate          |          |    x     |                    |
| eda_pg_tls_key                 | Postgresql EDA TLS key                  |          |    x     |                    |
| eda_pg_username                | Postgresql EDA user                     |          |    x     | eda                |
| eda_redis_disable_tls          | Disable TLS Redis (for multiple nodes)  |          |    x     | false              |
| eda_redis_host                 | Redis EDA host (for multiple nodes)     |          |    x     |                    |
| eda_redis_password             | Redis EDA password (for multiple nodes) |          |    x     |                    |
| eda_redis_port                 | Redis EDA port (for multiple nodes)     |          |    x     | 6379               |
| eda_redis_tls_cert             | Automation EDA redis TLS certificate    |          |    x     |                    |
| eda_redis_tls_key              | Automation EDA redis TLS key            |          |    x     |                    |
| eda_redis_username             | Redis EDA username (for multiple nodes) |          |    x     | eda                |
| eda_safe_plugins               | Automation EDA safe plugins             |          |    x     | []                 |
| eda_secret_key                 | Automation EDA secret key               |          |    x     |                    |
| eda_tls_cert                   | Automation EDA TLS certificate          |          |    x     |                    |
| eda_tls_key                    | Automation EDA TLS key                  |          |    x     |                    |
| eda_tls_remote                 | Automation EDA TLS remote files         |          |    x     | false              |
| eda_type                       | Automation EDA node type                |          |    x     | hybrid             |
| eda_event_stream_prefix_path   | Automation EDA event stream prefix path |          |    x     | /eda-event-streams |
| eda_event_stream_url           | Automation EDA event stream URL         |          |    x     |                    |
| eda_workers                    | Automation EDA workers count            |          |    x     | 2                  |

Extra parameters will need to be passed through an ansible `eda_extra_settings` variable.

For example, you may set:

```yaml
eda_extra_settings:
  - setting: RULEBOOK_READINESS_TIMEOUT_SECONDS
    value: 120
```

### Automation Gateway

| Name                                         | Description                                | Required | Optional | Default            |
| -------------------------------------------- | ------------------------------------------ | -------- | -------- | -------------------|
| gateway_admin_password                       | Automation Gateway admin password          |     x    |          |                    |
| gateway_admin_user                           | Automation Gateway admin user              |          |    x     | admin              |
| gateway_extra_settings                       | Automation Gateway extra settings          |          |    x     | []                 |
| gateway_main_url                             | Automation Gateway main URL                |          |    x     |                    |
| gateway_nginx_client_max_body_size           | Nginx maximum body size                    |          |    x     | 5m                 |
| gateway_nginx_disable_hsts                   | Disable Nginx HSTS                         |          |    x     | false              |
| gateway_nginx_disable_https                  | Disable Nginx HTTPS                        |          |    x     | false              |
| gateway_nginx_hsts_max_age                   | Nginx HSTS maximum age                     |          |    x     | 63072000           |
| gateway_nginx_http_port                      | Nginx HTTP port                            |          |    x     | 8083               |
| gateway_nginx_https_port                     | Nginx HTTPS port                           |          |    x     | 8446               |
| gateway_nginx_https_protocols                | Nginx HTTPS protocols                      |          |    x     | [TLSv1.2, TLSv1.3] |
| gateway_nginx_user_headers                   | Custom Nginx headers                       |          |    x     | []                 |
| gateway_pg_cert_auth                         | Postgresql Gateway TLS auth                |          |    x     | false              |
| gateway_pg_database                          | Postgresql Gateway database                |          |    x     | gateway            |
| gateway_pg_host                              | Postgresql Gateway host                    |     x    |          |                    |
| gateway_pg_password                          | Postgresql Gateway password                |          |    x     |                    |
| gateway_pg_port                              | Postgresql Gateway port                    |          |    x     | 5432               |
| gateway_pg_sslmode                           | Postgresql Gateway SSL mode                |          |    x     | prefer             |
| gateway_pg_tls_cert                          | Postgresql Gateway TLS certificate         |          |    x     |                    |
| gateway_pg_tls_key                           | Postgresql Gateway TLS key                 |          |    x     |                    |
| gateway_pg_username                          | Postgresql Gateway user                    |          |    x     | gateway            |
| gateway_redis_disable_tls                    | Disable TLS Redis                          |          |    x     | false              |
| gateway_redis_host                           | Redis Gateway host                         |          |    x     |                    |
| gateway_redis_password                       | Redis Gateway password                     |          |    x     |                    |
| gateway_redis_port                           | Redis Gateway port                         |          |    x     | 6379               |
| gateway_redis_tls_cert                       | Automation Gateway redis TLS certificate   |          |    x     |                    |
| gateway_redis_tls_key                        | Automation Gateway redis TLS key           |          |    x     |                    |
| gateway_redis_username                       | Redis Gateway username                     |          |    x     | gateway            |
| gateway_secret_key                           | Automation Gateway secret key              |          |    x     |                    |
| gateway_tls_cert                             | Automation Gateway TLS certificate         |          |    x     |                    |
| gateway_tls_key                              | Automation Gateway TLS key                 |          |    x     |                    |
| gateway_tls_remote                           | Automation Gateway TLS remote files        |          |    x     | false              |
| gateway_grpc_server_processes                | Gateway auth server processes              |     x    |    x     | 5                  |
| gateway_grpc_server_max_threads_per_process  | Gateway auth server threads/process        |     x    |    x     | 10                 |
| gateway_grpc_auth_service_timeout            | Gateway auth server timeout                |     x    |    x     | 30s                |
| gateway_uwsgi_listen_queue_size              | Automation Gateway uwsgi listen queue size |          |    x     | 4096               |

Extra parameters will need to be passed through an ansible `gateway_extra_settings` variable.

For example, you may set:

```yaml
gateway_extra_settings:
  - setting: OAUTH2_PROVIDER['ACCESS_TOKEN_EXPIRE_SECONDS']
    value: 600
```

### Automation Hub

| Name                           | Description                            | Required | Optional | Default            |
| ------------------------------ | -------------------------------------- | -------- | -------- | ------------------ |
| hub_admin_password             | Automation Hub admin password          |     x    |          |                    |
| hub_extra_settings             | Automation hub extra settings          |          |    x     | []                 |
| hub_galaxy_importer            | Automation Hub galaxy importer         |          |    x     |                    |
| hub_nginx_client_max_body_size | Nginx maximum body size                |          |    x     | 20m                |
| hub_nginx_disable_hsts         | Disable Nginx HSTS                     |          |    x     | false              |
| hub_nginx_disable_https        | Disable Nginx HTTPS                    |          |    x     | false              |
| hub_nginx_hsts_max_age         | Nginx HSTS maximum age                 |          |    x     | 63072000           |
| hub_nginx_http_port            | Nginx HTTP port                        |          |    x     | 8081               |
| hub_nginx_https_port           | Nginx HTTPS port                       |          |    x     | 8444               |
| hub_nginx_https_protocols      | Nginx HTTPS protocols                  |          |    x     | [TLSv1.2, TLSv1.3] |
| hub_nginx_user_headers         | Custom Nginx headers                   |          |    x     | []                 |
| hub_pg_cert_auth               | Postgresql Hub TLS auth                |          |    x     | false              |
| hub_pg_database                | Postgresql Hub database                |          |    x     | pulp               |
| hub_pg_host                    | Postgresql Hub host                    |     x    |          |                    |
| hub_pg_password                | Postgresql Hub password                |          |    x     |                    |
| hub_pg_port                    | Postgresql Hub port                    |          |    x     | 5432               |
| hub_pg_socket                  | Postgresql Hub unix socket             |          |    x     |                    |
| hub_pg_sslmode                 | Postgresql Hub SSL mode                |          |    x     | prefer             |
| hub_pg_tls_cert                | Postgresql Hub TLS certificate         |          |    x     |                    |
| hub_pg_tls_key                 | Postgresql Hub TLS key                 |          |    x     |                    |
| hub_pg_username                | Postgresql Hub user                    |          |    x     | pulp               |
| hub_secret_key                 | Automation Hub secret key              |          |    x     |                    |
| hub_storage_backend            | Automation Hub storage backend         |          |    x     | file               |
| hub_tls_cert                   | Automation Hub TLS certificate         |          |    x     |                    |
| hub_tls_key                    | Automation Hub TLS key                 |          |    x     |                    |
| hub_tls_remote                 | Automation Hub TLS remote files        |          |    x     | false              |
| hub_workers                    | Automation Hub workers count           |          |    x     | 2                  |
| hub_use_archive_compression    | Automation Hub compress backup files   |          |    x     | true               |

Extra parameters will need to be passed through an ansible `hub_extra_settings` variable.

For example, you may set:

```yaml
hub_extra_settings:
  - setting: REDIRECT_IS_HTTPS
    value: True
```
#### Automation Hub - Shared Storage

Shared storage is required when installing more than one Automation Hub with `file` storage backend.
When installing a single instance of the Automation Hub, it is optional

| Name                       | Description                          | Required | Optional | Default      |
| -------------------------- | ------------------------------------ | -------- | -------- | ------------ |
| hub_shared_data_path       | Path to an NFS share with RWX access |    x     |          |              |
| hub_shared_data_mount_opts | Mount options for NFS share          |          |    x     | rw,sync,hard |

#### Automation Hub - Azure Blob Storage

When using Azure blob storage backend then `hub_storage_backend` needs to be set to `azure`.
The Azure container needs to exist before running the installer.

| Name                     | Description          | Required | Optional | Default |
| ------------------------ | -------------------- | -------- | -------- | ------- |
| hub_azure_account_key    | Azure account key    |    x     |          |         |
| hub_azure_account_name   | Azure account name   |    x     |          |         |
| hub_azure_container      | Azure container name |          |    x     | pulp    |
| hub_azure_extra_settings | Azure extra settings |          |    x     | {}      |

Extra parameters will need to be passed through an ansible `hub_azure_extra_settings` dictionary.

For example, you may set:

```yaml
hub_azure_extra_settings:
  AZURE_LOCATION: foo
  AZURE_SSL: True
  AZURE_URL_EXPIRATION_SECS: 60
```

The list of all possible configuration can be found [here](https://django-storages.readthedocs.io/en/latest/backends/azure.html#settings)

#### Automation Hub - S3 Storage

When using AWS S3 storage backend then `hub_storage_backend` needs to be set to `s3`.
The AWS S3 bucket needs to exist before running the installer.

| Name                  | Description           | Required | Optional | Default |
| --------------------- | --------------------- | -------- | -------- | ------- |
| hub_s3_access_key     | AWS S3 access key     |    x     |          |         |
| hub_s3_secret_key     | AWS S3 secret name    |    x     |          |         |
| hub_s3_bucket_name    | AWS S3 bucket name    |          |    x     | pulp    |
| hub_s3_extra_settings | AWS S3 extra settings |          |    x     | {}      |

Extra parameters will need to be passed through an ansible `hub_s3_extra_settings` dictionary.

For example, you may set:

```yaml
hub_s3_extra_settings:
  AWS_S3_MAX_MEMORY_SIZE: 4096
  AWS_S3_REGION_NAME: eu-central-1
  AWS_S3_USE_SSL: True
```

The list of all possible configuration can be found [here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings)

#### Automation Hub - Postinstall

The hub postinstall allows one to create resources (collections, users, groups, etc..) after the hub deployment.

| Name                          | Description                            | Required | Optional | Default |
| ----------------------------- | -------------------------------------- | -------- | -------- | --------|
| hub_postinstall               | Enable Automation Hub postinstall      |          |     x    | false   |
| hub_postinstall_async_delay   | Postinstall delay between retries      |          |     x    | 1       |
| hub_postinstall_async_retries | Postinstall number of tries to attempt |          |     x    | 30      |
| hub_postinstall_dir           | Automation Hub postinstall directory   |          |     x    |         |
| hub_postinstall_ignore_files  | Automation Hub ignore files            |          |     x    | []      |
| hub_postinstall_repo_ref      | Automation Hub repository branch/tag   |          |     x    | main    |
| hub_postinstall_repo_url      | Automation Hub repository URL          |          |     x    |         |

The `hub_postinstall_repo_url` variable can be used to define the postinstall repository URL which may include
authentication information.

- `http(s)://<host>/<repo>.git` (public repository without http(s) authentication)
- `http(s)://<user>:<password>@<host>:<repo>.git` (private repository with http(s) authentication)
- `git@<host>:<repo>.git` (public/private repository with ssh authentication)

When using ssh based authentication, the installer doesn't configure anything (ssh key or so) for you and you need
to have everything configured on the installer node.

#### Automation Hub - Signing

By default, Automation Hub doesn't sign collections and containers.
It's possible to turn on this feature via the `hub_collection_signing` and/or `hub_container_signing` variables.
For collections and/or containers you'll need to provide a GPG key to sign the artifacts.

| Name                           | Description                                  | Required | Optional | Default           |
| ------------------------------ | -------------------------------------------- | -------- | -------- | ----------------- |
| hub_collection_auto_sign       | Enable Automation Hub collection auto sign   |          |    x     |      false        |
| hub_collection_signing         | Enable Automation Hub collection signing     |          |    x     |      false        |
| hub_collection_signing_key     | Automation Hub collection signing key        |          |    x     |                   |
| hub_collection_signing_pass    | Automation Hub collection signing passphrase |          |    x     |                   |
| hub_collection_signing_service | Automation Hub collection signing service    |          |    x     | ansible-default   |
| hub_container_signing          | Enable Automation Hub container signing      |          |    x     |      false        |
| hub_container_signing_key      | Automation Hub container signing key         |          |    x     |                   |
| hub_container_signing_pass     | Automation Hub container signing passphrase  |          |    x     |                   |
| hub_container_signing_service  | Automation Hub container signing service     |          |    x     | container-default |

Note that if the GPG key is protected by a passphrase then you need to provide it via the `hub_collection_signing_pass`
and/or `hub_container_signing_pass` variables.

### Database

| Name                            | Description                     | Required | Optional | Default       |
| ------------------------------- | ------------------------------- | -------- | -------- | ------------- |
| postgresql_admin_database       | Postgresql admin database       |          |    x     | postgres      |
| postgresql_admin_username       | Postgresql admin user           |          |    x     | postgres      |
| postgresql_admin_password       | Postgresql admin password       |     x    |          |               |
| postgresql_disable_tls          | Disable Postgresql TLS          |          |    x     | false         |
| postgresql_effective_cache_size | Postgresql effective cache size |          |    x     |               |
| postgresql_keep_databases       | Keep databases during uninstall |          |    x     | false         |
| postgresql_max_connections      | Postgresql max connections      |          |    x     | 1024          |
| postgresql_log_destination      | Postgresql log file location    |          |    x     | /dev/stderr   |
| postgresql_password_encryption  | Postgresql password encryption  |          |    x     | scram-sha-256 |
| postgresql_port                 | Postgresql port                 |          |    x     | 5432          |
| postgresql_shared_buffers       | Postgresql shared buffers       |          |    x     |               |
| postgresql_tls_cert             | Postgresql TLS certificate      |          |    x     |               |
| postgresql_tls_key              | Postgresql TLS key              |          |    x     |               |
| postgresql_tls_remote           | Postgresql TLS remote files     |          |    x     | false         |

### Receptor

| Name                         | Description                   | Required | Optional |   Default   |
| ---------------------------- | ----------------------------- | -------- | -------- | ----------- |
| receptor_disable_signing     | Disable receptor signing      |          |    x     |    false    |
| receptor_disable_tls         | Disable receptor TLS          |          |    x     |    false    |
| receptor_log_level           | Receptor loggging level       |          |    x     |     info    |
| receptor_mintls13            | Receptor TLS 1.3 minimal      |          |    x     |    false    |
| receptor_peers               | Receptor peers list           |          |    x     |     []      |
| receptor_port                | Receptor port                 |          |    x     |    27199    |
| receptor_protocol            | Receptor protocol             |          |    x     |     tcp     |
| receptor_signing_private_key | Receptor signing private key  |          |    x     |             |
| receptor_signing_public_key  | Receptor signing public key   |          |    x     |             |
| receptor_signing_remote      | Receptor signing remote files |          |    x     |    false    |
| receptor_tls_cert            | Receptor TLS certificate      |          |    x     |             |
| receptor_tls_key             | Receptor TLS key              |          |    x     |             |
| receptor_tls_remote          | Receptor TLS remote files     |          |    x     |    false    |
| receptor_type                | Receptor node type            |          |    x     |  execution  |

### Redis

| Name                         | Description                       | Required | Optional |   Default   |
| ---------------------------- | --------------------------------- | -------- | -------- | ----------- |
| redis_cluster_ip             | Redis cluster IP address          |          |    x     |             |
| redis_mode                   | Redis mode cluster or standalone  |          |    x     |   cluster   |

### Performance Co-Pilot Monitoring

| Name                         | Description                                             | Required | Optional |   Default   |
| ---------------------------- | ------------------------------------------------------- | -------- | -------- | ----------- |
| setup_monitoring             | Setup Performance Co-Pilot on AAP control plane nodes   |          |    x     |    false    |
| pcp_pmcd_port                | Port to serve Performance Metrics Collection Daemon on  |          |    x     |    44321    |
| pcp_pmproxy_port             | Port to serve Performance Metrics Proxy on              |          |    x     |    44322    |
| pcp_firewall_zone            | Firewall zone for pcp services                          |          |    x     |    public   |

The minimal configuration for running the containerized install will look like the following:

```yaml
---
controller_admin_password: foo
controller_pg_host: 127.0.0.1
controller_pg_password: bar
hub_admin_password: supersecret
hub_pg_host: 127.0.0.1
hub_pg_password: secretsuper
postgresql_admin_password: foobar
...

```

These variables can be put in a `vars.yml` and passed as `-e @vars.yml` to `ansible-playbook` command.
Otherwise, they can be put in the inventory. A sample inventory is included in the `samples` folder.


