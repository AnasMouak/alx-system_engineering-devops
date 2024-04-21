#config file using Puppet
file { 'Turn off passwd auth':
  ensure  => present,
  path   => '/etc/ssh/ssh_config',
  content => "PasswordAuthentication no\n",
}

file { 'Declare identity file':
  ensure  => present,
  path   => '/etc/ssh/ssh_config',
  content => "IdentityFile ~/.ssh/school\n",
}
