#Increase the ULIMIT of the default file
exec { 'increase_nginx_ulimit':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin:/bin',
}

# Restart Nginx
service { 'nginx':
  ensure  => 'running',
  enable  => 'true',
  require => Exec['increase_nginx_ulimit'],
}
