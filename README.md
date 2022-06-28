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

#### _Test:_ 
Test case: Check if the Gitlab is accessible in below URL\

_Test Steps:_
1. open url http://192.168.56.15/gitlab/ in a web browser

Post conditions:
- GitLab is accessible at the indicated URL
- It asks to enter password for the root credentials


#### _Test:_ 
Test case: Check if the Grafana is accessible in below URL\

_Test Steps:_
1. open url http://192.168.56.15/gitlab/-/grafana in a web browser

Post conditions:
- Grafana is accessible at the indicated URL

## Set up GITLAB

1. Create a password for the **_root_** user and remember this password for future use. (referred as **_$ROOT_PASSWORD_** later)
2. Login into Gitlab with **_root_** user and **_$ROOT_PASSWORD_**

#### **** Test Case ****

Initial conditions: you have successfully entered a password for the **_root_** user

Test Steps:
1. Go to http://192.168.56.15/gitlab in a web broswer
2. Log in using the user name **_root_** and **_$ROOT_PASSWORD_**

Post conditions:
- You have successfully logged in as administrator

#### **** Test Case End ****

3. Create a new user with username **_devops_**
* Goto _admin area_ (small settings icon on the left side corner)
* Click on _new user_
* enter below details
  * name : _devops_
  *  username: _devops_
  *  email: _your email id_
* Click on _Create user_

4. Set password for user **_devops_**
* edit the user _devops_
* enter the password (referred as **_$PROJECT_TEMP_PASSWORD_** in future)
* enter the password confirmation
* click on _Save changes_

5. Logout from **_root_** user
6. Login with user **_devops_**
* username: devops
* password: $PROJECT_TEMP_PASSWORD

7. First time it will ask to reset password
* Current password: _$PROJECT_TEMP_PASSWORD_
* New password (referred as _$PROJECT_PASSWORD_ in future)
* Confirm new password

### **** Test Case ****

Initial conditions: you have successfully changed a password for the **_devops_** user

Test Steps:
1. Go to http://192.168.56.15/gitlab
2. Log in using the user name **_devops_** and password(**_$PROJECT_PASSWORD_**) the one entered in the previous step.

Post conditions:
- You have successfully logged in as user **_devops_**

### **** Test Case End ****

8. Again Login to Gitlab with user **_devops_** with latest password (**_$PROJECT_PASSWORD_**)
9. After login, Create a new project(repository) with name _welcomeWebApplication_
* Click on "Create a project"
* Click on "Create blank project"
* Enter Project Name: welcomeWebApplication
* Click on "Create project"

## Configure Docker in Integration server

1. Get to `cd <root_folder>/devops/pipeline/integration-server`
2. Run command `vagrant ssh`
3. Add a user to the docker group to be able to access the docker CLI\
`sudo usermod -aG docker vagrant`
4. Validate the installation and access by running a hello world container\
`docker run --name hello-world hello-world`
5. The expected output should be.\
Hello from Docker!
6. Remove the docker container and image\
`docker rm hello-world`\
`docker rmi hello-world`

## Download and Install Runner in Integration server
1. Download Gitlab runner\
`curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash`

2. Install Gitlab runner\
`sudo apt-get install gitlab-runner`

## Register 1st runner in Integration server
1. Execute the following command\
`sudo gitlab-runner register`

2. Enter the requested information as follows

3. For GitLab instance URL enter:\
`http://192.168.56.15/gitlab/`

4. For the gitlab-ci token enter the generated token:\(**Note: Get the token from Gitlab**)
For Example: 85y84QhgbyaqWo38b7qg

5. For a description for the runner enter:\
[integration-server] `docker`

6. For the gitlab-ci tags for this runner enter:\
`integration`

7. Enter optional maintenance note for the runner:\
`integrationRunner`

8. For the executor enter:\
`docker`

9. For the Docker image (eg. ruby:2.1) enter:\
`alpine:latest`

10. Restart the runner:\
`sudo gitlab-runner restart`

11. Finally, in GitLab change the configuration of the runner to accept jobs without TAGS

## Register 2nd runner in Integration server
Note: This shell runner for executing the python script to extract the metrics details

1. Run the below command
`sudo gitlab-runner register`

2.Then enter the information related to the GitLab instance.

3. For GitLab instance URL enter:\
`http://192.168.56.15/gitlab/`

4. For the gitlab-ci token enter the generated token:\
For Example: `85y84QhgbyaqWo38b7qg`

5. For a description for the runner enter:\
[stage-vm-welcome] `shell`

6. For the gitlab-ci tags for this runner enter:\
`integration-shell`

7. Enter optional maintenance note for the runner:\
`shellRunner`

8. For the executor enter:\
`shell`

9. Restart the runner:\
`sudo gitlab-runner restart`

10. Finally, in GitLab change the configuration of the runner to accept jobs without TAGS






