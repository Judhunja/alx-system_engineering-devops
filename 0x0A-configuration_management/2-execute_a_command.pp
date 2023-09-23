# Executes a command using puppet
exec { 'pkill -f killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/bin',
}
