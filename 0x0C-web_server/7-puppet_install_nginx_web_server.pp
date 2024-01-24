#!/usr/bin/env bash
# Configure server using puppet

class nginx_server {
  # Install Nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Configure Nginx
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        return 200 'Hello World!';
    }

    location /redirect_me {
        return 301 http://new-redirect-url;
    }
}
",
    notify => Service['nginx'],
  }

  # Restart Nginx after configuration changes
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => File['/etc/nginx/sites-available/default'],
  }

  # Create a simple HTML page with "Hello World!"
  file { '/var/www/html/index.html':
    ensure  => file,
    content => '<html><body><h1>Hello World!</h1></body></html>',
  }
}

# Apply the nginx_server class
include nginx_server
