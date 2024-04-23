# configuring server with Puppet

# Update package repositories
exec { 'apt-update':
  command => 'apt-get update',
  path    => '/usr/bin',
  before  => Package['nginx'],
}

# Install Nginx package
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-update'],
}

# Allow Nginx HTTP traffic in UFW
exec { 'allow-nginx-http':
  command => 'ufw allow "Nginx HTTP"',
  path    => '/usr/bin',
  require => Package['nginx'],
}

# Create index file with "Hello World!"
file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure Nginx site with custom location block
file { '/etc/nginx/sites-available/default':
  content => template('my_module/nginx_site.erb'),
  notify  => Service['nginx'],
  require => Package['nginx'],
}

# Restart Nginx service after configuration changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [
    Package['nginx'],
    File['/etc/nginx/sites-available/default'],
  ],
}
