# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "bento/ubuntu-19.04"
  config.vbguest.auto_update = true
  config.vm.synced_folder "./example", "/home/vagrant/example"

  config.vm.network "private_network", ip: "192.168.33.11"
end
