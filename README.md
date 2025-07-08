In this repository, I will be sharing the steps to create, build and publish an ansible collection. I will create a module called "hello_world" in this collection.

1) Successfully install AAP
2) Go into “collections” folder and then into the “ansible_collections” folder
3) Enter this command “ansible-galaxy collection init xtc0.basic”
4) After xtc0 directory has been created, use this command “cd xtc0/basic”
5) You will see a structure like:
```text
xtc0/basic/
├── plugins/
│   └── modules/
├── README.md
├── galaxy.yml
└── meta
   └── runtime.yml
```
7) Go into plugins folder and create a subfolder called “modules”
8) Create this directory in plugins: “plugins/modules/hello_world.py”
9) Make sure to add documentation inside hello_world.py (Ansible Galaxy will extract info from here and fill in categories like Synopsis, Parameters, Examples, Return Values on Ansible Galaxy website)
10) Go to directory where inventory file lies and create a playbook called test_hello.yml
11) To run test_hello.yml playbook, use command: “ansible-playbook test_hello.yml”
12) Fill in galaxy.yml (as seen in step 5’s tree structure). galaxy.yml file is essential metadata that tells Ansible Galaxy and users what your collection is, who made it, and how it should be used.
13) Go to this file: xtc0/basic directory/meta/runtime.yml
14) Uncomment the variable “requires_ansible” in runtime.yml
15) Build the collection using “ansible-galaxy collection build”
16) A tarball like “xtc0-basic-1.0.0.tar.gz” is created
17) To publish collection to Ansible Galaxy, go to: https://galaxy.ansible.com
18) Sign in with GitHub (must be GitHub — Galaxy syncs with GitHub repos).
19) Make sure your GitHub username matches the namespace in galaxy.yml — e.g. if your namespace is xtc0, your GitHub user/org must also be xtc0.
20) If it doesn't match, you need to request a namespace or use one you own.
21) Once you’ve logged into Galaxy, get your API token.
22) Use this command: “ansible-galaxy collection publish xtc0-basic-1.0.0.tar.gz --api-key <your_api_key>”
23) Once done, your collection will be live at: https://galaxy.ansible.com/xtc0/basic (change xtc0 to your own namespace/ Github username)
24) You and others can now install your collection using: “ansible-galaxy collection install xtc0.basic”
