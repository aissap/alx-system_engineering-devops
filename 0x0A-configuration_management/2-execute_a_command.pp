# Execute the command to kill the process

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
