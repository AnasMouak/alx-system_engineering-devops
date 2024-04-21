#config file using Puppet
file { '/etc/ssh/sshd_config':
  ensure  => present,
  content => "PasswordAuthentication no\n",
}

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "IdentityFile ~/.ssh/school\n",
}
