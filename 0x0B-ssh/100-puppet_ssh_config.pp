# Seting up my client config file
include stdlib

file_line { 'Refuse password authentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'Identify the private key locaton':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '     IdentityFile ~/.ssh/school',
  replace => true,
}
