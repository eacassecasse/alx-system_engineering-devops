# Use the exec resource to updates the user limits in /etc/security/limits.conf

exec { 'replace-nofile-soft':
  command => 'sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
  before  => Exec['replace-nofile-hard'],
}

exec { 'replace-nofile-hard':
  command => 'sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
}
