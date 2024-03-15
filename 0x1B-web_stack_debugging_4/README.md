##0x1B. Web stack debugging #4

##Overview

This project aims to address issues related to web stack debugging on an Ubuntu 14.04 LTS environment. Specifically, it focuses on resolving performance issues encountered with a web server setup featuring Nginx, as observed through ApacheBench benchmarking.

## Requirements

### General

- All files are interpreted on Ubuntu 14.04 LTS.
- All files end with a new line.
- A mandatory README.md file is present at the root of the project folder.
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Puppet manifests must run without errors.
- Puppet manifests' first lines must be comments explaining their purpose.
- Puppet manifests files must end with the extension .pp.
- Files will be checked with Puppet v3.4.

### Installation of puppet-lint

To install puppet-lint version 2.1.1, execute the following commands:

```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
