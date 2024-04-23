# configuring server with Puppet

exec {'install':
  provider => shell,
  command  =>' apt-get -y update ; apt-get -y install nginx ; ufw allow "Nginx HTTP"; echo "Hello World!" > /var/www/html/index.nginx-debian.html ;  service nginx start; sed -i "s,server_name _;,server_name _;\n\n\tlocation = /redirect_me/ {\n\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}," "/etc/nginx/sites-available/default"; service nginx restart',
}
