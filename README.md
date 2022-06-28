# Devops_MS_Thesis
Dedicated repository for Master thesis


# Steps to replicate the setup

## Prerequisites
Hardware
* Computer with at least 8 GB memory (recommended 16 GB, ideally 32 GB)

Software
* Operating System - Ubuntu/Mac
* VirtualBox(v 6.0, or higher)
* Vagrant (v 2.2.5, or higher)
* Ansible (v 2.7.5, or higher)

## Creating Environments

## Devolpment Environment
### Generate WAR file
1. go to directory: `cd ~/<root_folder>/Devops/pipeline/dev-vm-welcome`
2. run command `mvn clean install`
#### _Test:_ 
Test case: Check if the war file generated in Target folder.\
Initial conditions: "mvn clean install" command should have completed.\
  _Test Steps:_
  1. `cd ~/<root_folder>/devops/pipeline/dev-vm-welcome/target`
  2. check if file "welcome-webapplication-0.0.1-SNAPSHOT.war" exists in target folder

### Test Product in Dev Environment
1. go to the directory `cd ~/<root_folder>/devops/pipeline/dev-vm-welcome`
2. run command `vagrant up`

#### _Test:_ 
Test case: Check if Dev-vm-welcome is create\
Initial conditions: "vagrant up" command should have completed\
_Test Steps:_
1. `cd ~/<root_folder>/devops/pipeline/dev-vm-welcome`
2. `vagrant ssh`

Post conditions:
- Should be able to connect "dev-vm-welcome" virtual machine

3. run command `vagrant ssh`
4. go to folder (inside the "dev-vm-welcome" VM) `cd /vagrant_scripts/`
5. run commamnd `sudo ./deploy-snapshot.sh`

#### _Test:_ 
Test case: Check if Product is accessible\
Initial conditions: script "deploy-snapshot.sh" should have run and completed in previous step\
_Test Steps:_
1. open url http://192.168.56.14:8080/welcome/welcome in a web browser

Post conditions:
- Should be able to see the web page with text as "Welcome Stranger!"

6- exit from _dev-vm-welcome_ virtual machine usig command `exit`

## Continuous Integration Server

### Create VM for Integration server
1. go to `cd <root_folder>/devops/pipeline/integration-server`
2. run command `vagrant up`
3. reload virtual machine with command `vagrant reload` (***Important Step***)
