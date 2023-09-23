# Installs a package from pip3 provider
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
