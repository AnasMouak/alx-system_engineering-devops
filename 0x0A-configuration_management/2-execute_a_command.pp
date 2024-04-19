# create a process named killmenow 
exec { 'kill_process':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin'],
}
