# configuring server with Puppet

exec {'fix':
  provider => shell,
  command  => 'sudo sed -i "s,15,4096," "/etc/default/nginx" ; sudo service nginx restart',
}
