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
1. Go to\
`cd ~/<root_folder>/Devops/pipeline/dev-vm-welcome`
3. Run command\
`mvn clean install`

#### *** Test Case *** 
Test case: Check if the war file generated in Target folder.\
Initial conditions: "mvn clean install" command should have completed.\
  _Test Steps:_
  1. Go to\
  `cd ~/<root_folder>/devops/pipeline/dev-vm-welcome/target`
  2. check if file "welcome-webapplication-0.0.1-SNAPSHOT.war" exists
#### *** Test End *** 

### Create Devolpment VM
1. Go to\
`cd ~/<root_folder>/devops/pipeline/dev-vm-welcome`
2. Run command\
`vagrant up`

#### *** Test Case ***
Test case: Check if Dev-vm-welcome is create\
Initial conditions: "vagrant up" command should have completed\
_Test Steps:_
1. `cd ~/<root_folder>/devops/pipeline/dev-vm-welcome`
2. `vagrant ssh`

Post conditions:
- Should be able to connect "dev-vm-welcome" virtual machine

#### *** Test Case End ***

### Deploy the Product
1. run command\
`vagrant ssh`
2. go to folder (inside the **dev-vm-welcome** VM)\
`cd /vagrant_scripts/`
3. run commamnd\
`sudo ./deploy-snapshot.sh`

#### *** Test Case ***
Test case: Check if Product is accessible\
Initial conditions: script "deploy-snapshot.sh" should have run and completed in previous step\
_Test Steps:_
1. open url http://192.168.56.14:8080/welcome/welcome in a web browser

Post conditions:
- Should be able to see the web page with text as "Welcome Stranger!"
#### *** Test Case End ***

6. exit from **dev-vm-welcome** virtual machine usig command `exit`

## Continuous Integration Server

### Create VM for Integration server
1. go to `cd <root_folder>/devops/pipeline/integration-server`
2. run command `vagrant up`
3. reload virtual machine with command `vagrant reload` (***Important Step***)

#### _Test:_ 
Test case: Check if the **Gitlab** is accessible in below URL\

_Test Steps:_
1. open url http://192.168.56.15/gitlab/ in a web browser

Post conditions:
- GitLab is accessible at the indicated URL
- It asks to enter password for the root credentials


#### _Test:_ 
Test case: Check if the **Grafana** is accessible in below URL\

_Test Steps:_
1. open URL http://192.168.56.15/gitlab/-/grafana in a web browser

Post conditions:
- Grafana is accessible at the indicated URL

#### _Test:_ 
Test case: Check if the **Sonarqube** is accessible in below URL\

_Test Steps:_
1. open URL http://192.168.56.15:9000/ in a web browser

Post conditions:
- Sonarqube is accessible at the indicated URL

## Set up GITLAB

### Setup root password and create a non-root user

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

### Create repository in Gitlab

1. Login to Gitlab with user **_devops_** with latest password (**_$PROJECT_PASSWORD_**)

2. After login, Create a new project(repository) with name _welcomeWebApplication_

3. Click on **Create a project**

4. Click on **Create blank project**

5. Enter Project Name: **welcomeWebApplication**

6. Click on **Create project**

## Get the Gitlab PROJECT ID

1. Click on the project **welcomewebapplication**

2. Get the **Project ID** (Note: It will be displayed below the project name)

3. Save the Project ID somewhere (we need this Project ID for future use)

### Create API Token in Gitlab

1. Login to gitlab http://192.168.56.15/gitlab with username **_devops_** and **_$PROJECT_PASSWORD_**

2. Click on the profile picture

3. Click on **Edit profile**

4. Click on **Access Tokens** on the left side bar

5. Enter name `devops`

6. Click the Check box **api** under the sources

7. Click on **Create personal access token**

8. Copy the generated API token and save it somewhere (we need this Token for future use)

## Set up SONARQUBE

### Set the password for user admin

1. Open URL http://192.168.56.15:9000/

2. Set the password for user **admin** (referred as **$SONAR_PASSWORD** in future)

## Create API Token in SonarQube

1. Login to Sonarqube http://192.168.56.15:9000/ with username **_admin_** and **_$SONAR_PASSWORD_** 

2. Click on the profile

3. Click on **My account**

4. Select the tab **Security** 

5. Enter a token name: **devops**

6. Click on **Generate**

7. Copy the generated token and save it somewhere (we need this Token for future use)

## Setup GRAFANA

### Reset Grafana Password

1. Open URL http://192.168.56.15/gitlab/-/grafana in a web browser

2. Enter the details\
username: `admin`\
password: `admin`

3. set a new password for grafana user **admin** (referred as **$GRAFANA_PASSWORD** in future)

### Create Datasource in Grafana

1. Open URL http://192.168.56.15/gitlab/-/grafana in a web browser

2. Login with user **admin** and password (**$GRAFANA_PASSWORD**)

3. Click on **Configuration** icon on the left hand side bar (**Settings** symbol)

4. Select the **Data Sources** tab

5. Click on **Add data source**

6. Search for **MySQL** and select it

7. Enter the below details\
```
Host: localhost:3306
Database: devops
User: devops
Password: devops@2022
```

9. Click on **Save and Test**

10. It should display message as ** Database Connection OK**

11. Click on **Back**

### Import dashboard into Grafana

1. Click on **Create** icon on the left hand side bar (**+** symbol)

2. Select the **Import** option

3. Click on **Upload JSON file**

4. Select the below file\
`cd <root_folder>/devops/pipeline/integration-server/scripts/grafana_dashboard.json`

5. Click on **Import**

6. Grafana set up completed

## Paste the Gitlab and Sonarqube API token and Gitlab Project ID in get_metrics.py file 

1. Go to `cd <root_folder>/devops/pipeline/integration-server`

2. Run command\
`vagrant ssh`

3. Go to `cd /vagrant_scripts`

4. Open file **get_metrics.py** :\
`sudo nano get_metrics`

5. Edit the below lines in the file with sonarqube token, gitlab token and gitlab project id respectively\
sonarqube_token = 'paste the sonarqube token here'\
gitlab_token = 'paste the gitlab token here'\
gitlab_project_id = 'paste the Project ID here'

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

4. For the gitlab-ci token enter the generated token:(**Note: Get the token from Gitlab**)\
For Example: `85y84QhgbyaqWo38b7qg`

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


### Clone “welcomewebapplication” repository on your local working computer

1. go to `cd <root_folder>/devops/product/`

2. Enter command\
`git init`

3. Enter command\
`git clone http://192.168.56.15/gitlab/seeproject/welcomewebapplication.git`

4.It will ask for the credentials. Enter the Gitlab details
* username: devops
* password: $PROJECT_PASSWORD

#### **** Test Case ****

Test Steps:

1. go to `cd ~/<root_folder>/devops/product/`

Post conditions:
* A folder with name _welcomewebapplication_ should have created

#### **** Test Case End ****

### Push source code to Gitlab repository

1. go to `cd <root_folder>/devops/pipeline/integration-server/scripts`

2. run command\
`sh push_sourcecode_to_gitlab.sh`

#### **** Test Case ****

Test Steps:
1. Go to `http://192.168.56.15/gitlab`
2. Log in using the user name **_devops_** and password(**_$PROJECT_PASSWORD_**)
3. Open repository _welcomewebapplication_

Post conditions:
* You should be able to see folders **_welcome-webapplication_** and **_welcome-webapplication.testing.testng_** in Gitlab

#### **** Test Case End ****

## Stage Environment

**NOTE: Integration server should be up and running to execute these steps**

1. Get to `cd <root_folder>/devops/pipeline/stage-vm-welcome`

2. Run command
`vagrant up`

#### **** Test Case ***

Test Steps:

1. run command `vagrant ssh`

Post conditions:
- You have successfully logged in to **_stage-vm-welcome_** virtual machine

#### **** Test Case End ***

### Register a runner on the staging environment

1. Get to `cd <root_folder>/devops/pipeline/stage-vm-welcome`

2. Run command
`vagrant ssh`

3. Run command
`sudo gitlab-runner register`

3.Then enter the information related to the GitLab instance.

4. For GitLab instance URL enter:\
`http://192.168.56.15/gitlab/`

5. For the gitlab-ci token enter the generated token:\
For Example: `85y84QhgbyaqWo38b7qg`

6. For a description for the runner enter:\
[stage-vm-welcome] `shell`

7. For the gitlab-ci tags for this runner enter:\
`stage-vm-welcome-shell`

8. Enter optional maintenance note for the runner:\
`shellRunner`

9. For the executor enter:\
`shell`

10. Restart the runner:\
`sudo gitlab-runner restart`

11. Finally, in GitLab change the configuration of the runner to accept jobs without TAGS

12. Grant sudo permissions to the gitlab-runner:
`sudo usermod -a -G sudo gitlab-runner`\
`sudo visudo`

13. Now add the following to the bottom of the file:\
`gitlab-runner ALL=(ALL) NOPASSWD: ALL`

14. Restart the staging environment:\
`exit`\
`vagrant reload`

## Production Environment 

**NOTE: Integration server should be up and running to execute these steps**

1. Go to `cd <root_folder>/devops/pipeline/prod-vm-welcome`

2. Run command
`vagrant up`

#### *** Test Case ***

Initial conditions: you have successfully completed step 1
Test Steps:

1. run command `vagrant ssh`

Post conditions:
- You have successfully logged in to **_prod-vm-welcome_** virtual machine

#### *** Test Case End ***

### Register a runner on the production environment

1. Get to `cd <root_folder>/devops/pipeline/prod-vm-welcome`

2. Run command
`vagrant ssh`

3. Run command
`sudo gitlab-runner register`

3.Then enter the information related to the GitLab instance.

4. For GitLab instance URL enter:\
`http://192.168.56.15/gitlab/`

5. For the gitlab-ci token enter the generated token:\
For Example: `85y84QhgbyaqWo38b7qg`

6. For a description for the runner enter:\
[prod-vm-welcome] `shell`

7. For the gitlab-ci tags for this runner enter:\
`prod-vm-welcome-shell`

8. Enter optional maintenance note for the runner:\
`shellRunner`

9. For the executor enter:\
`shell`

10. Restart the runner:\
`sudo gitlab-runner restart`

11. Finally, in GitLab change the configuration of the runner to accept jobs without TAGS

12. Grant sudo permissions to the gitlab-runner:
`sudo usermod -a -G sudo gitlab-runner`\
`sudo visudo`

13. Now add the following to the bottom of the file:\
`gitlab-runner ALL=(ALL) NOPASSWD: ALL`

14. Restart the staging environment:\
`exit`\
`vagrant reload`



  
## Create .gitlab-ci.yml file

1. Login to gitlab http://192.168.56.15/gitlab with username **_devops_** and **_$PROJECT_PASSWORD_**
2. Open the "welcomeWebApplication" repository
3. create a new file with the name `.gitlab-ci.yml`

```image: maven:3.6.2-jdk-8

stages:
  - build
  - upload
  - deploy
  - test
  - production

variables:
  MAVEN_CLI_OPTS: "--batch-mode --errors --fail-at-end --show-version -DinstallAtEnd=true -DdeployAtEnd=true"

  STAGE_BASE_URL: "http://192.168.56.17:8080"
  
   # Define Tomcat's variables on Staging environment
  APACHE_HOME: "/opt/tomcat"
  APACHE_BIN: "$APACHE_HOME/bin"
  APACHE_WEBAPPS: "$APACHE_HOME/webapps"
  
  # Define product's variables
  PRODUCT_SNAPSHOT_NAME: "welcome-webapplication-0.0.1-SNAPSHOT.war"
  RESOURCE_NAME: "welcome.war"
  
cache:
  paths:
    - .m2/repository
    - welcome-webapplication/target/

build_app:
  stage: build
  tags:
    - integration
  script:
    - mvn -f welcome-webapplication/pom.xml $MAVEN_CLI_OPTS clean install

upload_app:
  stage: upload
  tags:
    - integration
  script:
    - echo "Upload WAR file"
  artifacts:
    name: "welcome"
    paths:
      - welcome-webapplication/target/*.war

deploy:
  stage: deploy
  tags:
    - stage-vm-welcome-shell
  script:
    - echo "Shutdown Tomcat"
    - sudo sh $APACHE_BIN/shutdown.sh
    
    - echo "Deploy generated product into the stage-vm-welcome environment" 
    - sudo cp welcome-webapplication/target/$PRODUCT_SNAPSHOT_NAME $APACHE_WEBAPPS
    
    - echo "Set right name"
    - sudo mv $APACHE_WEBAPPS/$PRODUCT_SNAPSHOT_NAME $APACHE_WEBAPPS/$RESOURCE_NAME
    
    - echo "Set user and group rights"
    - sudo chown tomcat:tomcat $APACHE_WEBAPPS/$RESOURCE_NAME
    
    - echo "Start up Tomcat"
    - sudo sh $APACHE_BIN/startup.sh

testng:
  stage: test
  tags:
    - integration
  services:
    - name: selenium/standalone-chrome:latest 
  script:
    - mvn -f welcome-webapplication.testing.testng/pom.xml $MAVEN_CLI_OPTS -Denv.BASEURL=$STAGE_BASE_URL test

prod_deployment:
  stage: production
  tags:
    - prod-vm-welcome-shell
  script:
    - echo "Shutdown Tomcat"
    - sudo sh $APACHE_BIN/shutdown.sh

    - echo "Deploy generated product into the prod-vm-welcome environment" 
    - sudo cp welcome-webapplication/target/$PRODUCT_SNAPSHOT_NAME $APACHE_WEBAPPS

    - echo "Set right name"
    - sudo mv $APACHE_WEBAPPS/$PRODUCT_SNAPSHOT_NAME $APACHE_WEBAPPS/$RESOURCE_NAME

    - echo "Set user and group rights"
    - sudo chown tomcat:tomcat $APACHE_WEBAPPS/$RESOURCE_NAME

    - echo "Start up Tomcat"
    - sudo sh $APACHE_BIN/startup.sh```
 



