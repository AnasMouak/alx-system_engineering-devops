# configuring server with Puppet

exec {'install':
  provider => shell,
  command  =>' sed -i "s,phpp,php," "/var/www/html/wp-settings.php"; sed -i "s,phpp,php," "/var/www/html/zxcvbn.min.js",
}
