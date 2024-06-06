# configuring server with Puppet

exec {'fix':
  command  =>' sed -i "s,phpp,php," "/var/www/html/wp-settings.php"; sed -i "s,phpp,php," "/var/www/html/zxcvbn.min.js",
  path     =>'/usr/local/bin/:/bin/'
}
