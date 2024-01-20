0x0A. Configuration management

Skynet Auto-Remediation Tool

This repository contains Puppet manifests for Skynet, an auto-remediation tool developed during my tenure at SlideShare. Skynet was designed to monitor, scale, and fix Cloud infrastructure, utilizing the MCollective parallel job-execution system.

Background Context
During the development of Skynet, a critical bug emerged in the code that led to unexpected consequences. A nil value was inadvertently sent to the filter method of MCollective, resulting in the following issues:

MCollective interpreted nil as 'all servers' for its filter method.
The action applied was to terminate the selected servers.
This oversight led to the inadvertent shutdown of 75% of SlideShare's conversion infrastructure servers, disrupting users' ability to convert PDFs, PowerPoints, and videos.

Fortunately, the use of Puppet enabled a swift restoration of the infrastructure within one hour. Manual recovery would have been a daunting task, involving launching servers, configuring and linking them, importing application code, starting processes, and addressing bugs.

For a humorous take on the incident, check out this tweet.

Resources
For a better understanding of the concepts and tools involved, consider reviewing the following:

Intro to Configuration Management
Puppet resource type: file (check "Resource types" for all manifest types in the left menu)
Puppet’s Declarative Language: Modeling Instead of Scripting
Puppet lint
Puppet emacs mode
Requirements
General
All files will be interpreted on Ubuntu 20.04 LTS.
All files should end with a new line.
A README.md file at the root of the project folder is mandatory.
Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
Puppet manifests must run without error.
The first line of Puppet manifests must be a comment explaining the manifest's purpose.
Puppet manifest files must end with the extension .pp.
Note on Versioning
Ensure that your Ubuntu 20.04 VM has Puppet 5.5 preinstalled.

Getting Started
To use these Puppet manifests, follow the steps below:

Clone this repository to your local machine.
Ensure that you have an Ubuntu 20.04 VM with Puppet 5.5 preinstalled.
Execute the Puppet manifests to configure and manage your infrastructure.
License
This project is licensed under the MIT License - see the LICENSE file for details.
