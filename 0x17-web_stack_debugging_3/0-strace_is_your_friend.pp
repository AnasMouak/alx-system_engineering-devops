# configuring server with Puppet

exec {'fix':
  command  =>'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path     =>'/usr/local/bin/:/bin/'
}
