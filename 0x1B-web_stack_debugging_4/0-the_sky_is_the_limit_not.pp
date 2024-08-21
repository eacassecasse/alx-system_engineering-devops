# Use the exec resource to update or add the ULIMIT variable in /etc/default/nginx

exec { 'replace_ulimit':
  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
  before  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => 'service nginx restart',
  path        => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
  refreshonly => true,  # This ensures that the restart happens only if triggered
}
