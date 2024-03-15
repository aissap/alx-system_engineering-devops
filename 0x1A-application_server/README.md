# 0x1A. Application Server

## Background Context

Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make it serve your Airbnb clone project.

## Resources

Read or watch:

- [Application server vs web server](https://www.digitalocean.com/community/tutorials/apache-vs-nginx-practical-considerations)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04)
- [Running Gunicorn](http://docs.gunicorn.org/en/stable/run.html)
- Be careful with the way Flask manages slash in route - [strict_slashes](https://werkzeug.palletsprojects.com/en/0.15.x/routing/#werkzeug.routing.Map.strict_slashes)
- [Upstart documentation](http://upstart.ubuntu.com/getting-started.html)

## Requirements

### General

- A README.md file, at the root of the folder of the project, is mandatory
- Everything Python-related must be done using python3
- All config files must have comments

### Bash Scripts

- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing

