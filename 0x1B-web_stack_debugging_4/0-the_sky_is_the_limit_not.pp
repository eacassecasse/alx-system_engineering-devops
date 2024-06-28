# Fixing huge amount of requests failure

exec {'increase_amount_of_resources':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['reboot_server'],
}

exec {'reboot_server':
  provider => shell,
  command  => 'sudo service nginx restart',
}
