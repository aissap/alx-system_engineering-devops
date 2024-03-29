#!/usr/bin/env bash
#Connect without password

file { '/etc/ssh/ssh_config':
  ensure  => present,
}
file_line { '/etc/ssh/ssh_config':
	path => '/etc/ssh/ssh_config',
	line => 'PasswordAuthentication no',
}

file_line { 'Identity file':
        path	=> '/etc/ssh/ssh_config',
        line	=> 'IdentityFile ~/.ssh/school',
	match	=> '^#IdentityFile',
}
