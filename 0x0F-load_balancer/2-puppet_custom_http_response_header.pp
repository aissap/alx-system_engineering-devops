#!/usr/bin/env bash
fest to add a custom HTTP header response

# Define custom HTTP header configuration for Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
}

# Define template for custom HTTP header configuration
# The template will add the custom header X-Served-By with the hostname of the server
file { '/etc/nginx/sites-available/default.erb':
  ensure  => present,
  content => "\
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    location / {
        add_header X-Served-By $hostname;
        try_files $uri $uri/ =404;
    }
}",
}

