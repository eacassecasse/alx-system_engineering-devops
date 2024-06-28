# Fixing huge amount of requests failure

exec {'increase_amount_of_opened_files_5000':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['increase_amount_of_opened_files_4000'],
}

exec {'increase_amount_of_opened_files_4000':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}