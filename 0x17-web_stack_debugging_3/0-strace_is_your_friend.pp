# Automated puppet fix (Find out why Apache is returning a 500 error)

exec { 'Fixing a website':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
