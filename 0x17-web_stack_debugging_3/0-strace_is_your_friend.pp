# configuring server with Puppet

exec {'fix':
  command  =>' sed -i "s/phpp/php/g" "/var/www/html/wp-settings.php"; sed -i "s/phpp/php/g" "/var/www/html/zxcvbn.min.js",
  path     =>'/usr/local/bin/:/bin/'
}
