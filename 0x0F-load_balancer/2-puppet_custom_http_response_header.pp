# configuring server with Puppet

exec {'install':
  provider => shell,
  command  =>' apt-get -y update ; apt-get -y install nginx ; ufw allow "Nginx HTTP" ; service nginx start; sed -i "s,server_name _;,server_name _;\n\n\tadd_header X-Served-By $HOSTNAME;," "/etc/nginx/sites-available/default"; service nginx restart',
}
