#!/usr/bin/env bash

file { '/etc/ssh/sshd_config':
  ensure  => present,
  content => epp('puppet/templates/sshd_config.epp'),
}

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => epp('puppet/templates/ssh_config.epp'),
}
