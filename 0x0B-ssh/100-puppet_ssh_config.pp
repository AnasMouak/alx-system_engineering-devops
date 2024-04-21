#config file using Puppet

include stdlib

file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  content => "PasswordAuthentication no",
  replace => true,
}

file_line { 'Declare identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  content => "IdentityFile ~/.ssh/school",
  replace => true,
}
