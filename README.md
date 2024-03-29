# Devops_MS_Thesis
Dedicated repository for Master thesis


# Steps to replicate the setup

## Prerequisites
#### Hardware
* Computer with at least 8 GB memory (recommended 16 GB, ideally 32 GB)

#### Software
* Operating System - Ubuntu/Mac
* VirtualBox(v 6.0, or higher)
* Vagrant (v 2.2.5, or higher)
* Ansible (v 2.7.5, or higher)

#### Download the replication package
* Download the folder **Devops** inside the **src** folder in this repository
* Unzip the file
* Follow the below instructions to replicate the experiment setup


## Development Environment
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
  2. Check if file "welcome-webapplication-0.0.1-SNAPSHOT.war" exists
#### *** Test End *** 

### Create Development VM
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
- exit from Dev-vm-welcome vm using command `exit`

#### *** Test Case End ***

### Deploy the Product Development VM
1. Run command\
`vagrant ssh`
2. Go to folder (inside the **_dev-vm-welcome_** VM)\
`cd /vagrant_scripts/`
3. Run commamnd\
`sudo sh deploy-snapshot.sh`

#### *** Test Case ***
Test case: Check if Product is accessible\
Initial conditions: script "deploy-snapshot.sh" should have run and completed in previous step\
_Test Steps:_
1. Open URL http://192.168.56.14:8080/welcome/welcome in a web browser

Post conditions:
- Should be able to see the web page with text as **Welcome Stranger!**
#### *** Test Case End ***

6. Exit from **_dev-vm-welcome_** virtual machine usig command `exit`

## Continuous Integration Server

### Create VM for Integration server
1. Go to\
`cd <root_folder>/devops/pipeline/integration-server`
2. Run command\
`vagrant up`
3. Reload virtual machine with command (***Important Step***)\
`vagrant reload` 

#### *** Test Case ***
Test case: Check if the **Gitlab** is accessible in below URL\

_Test Steps:_
1. Open URL http://192.168.56.15/gitlab/ in a web browser

Post conditions:
- GitLab is accessible at the indicated URL
- It asks to enter password for the root credentials
#### *** Test Case End ***

#### *** Test Case ***
Test case: Check if the **Grafana** is accessible in below URL\

_Test Steps:_
1. Open URL http://192.168.56.15:3000 in a web browser

Post conditions:
- Grafana is accessible at the indicated URL
#### *** Test Case End ***

#### *** Test Case ***
Test case: Check if the **Sonarqube** is accessible in below URL\

_Test Steps:_
1. Open URL http://192.168.56.15:9000/ in a web browser

Post conditions:
- Sonarqube is accessible at the indicated URL
#### *** Test Case End ***

## Set up GITLAB

### Setup root password

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

### Create a non-root user in Gitlab
3. Create a new user with username **_devops_**
* Goto **admin area** (small settings icon on the left side corner)
* Click on **new user**
* enter below details
  * name : **devops**
  * username: **devops**
  * email: **your email id**

* Click on **Create user**

#### Set a password for user **_devops_**
1. Set password for user **_devops_**
2. Edit the user **_devops_**
3. Enter the password (referred as **_$PROJECT_TEMP_PASSWORD_** in future)
4. Enter the password confirmation
5. Click on **Save changes**
6. Logout from **_root_** user

#### Login to Gitlab with user **_devops_**
1. Login with user **_devops_**
2. Username: **_devops_**
3. Password: **_$PROJECT_TEMP_PASSWORD_**
4. Click **Login**
5. First time it will ask to reset password
* Current password: **_$PROJECT_TEMP_PASSWORD_**
* New password (referred as **_$PROJECT_PASSWORD_** in future)
* Confirm new password
* Click on **Set new password**

### **** Test Case ****

Initial conditions: you have successfully changed a password for the **_devops_** user

Test Steps:
1. Go to http://192.168.56.15/gitlab
2. Login using the user name **_devops_** and password(**_$PROJECT_PASSWORD_**) the one entered in the previous step.

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

### Get the Gitlab PROJECT ID

1. Click on the project **welcomewebapplication**

2. Get the **Project ID** (Note: It will be displayed below the project name)

3. Save the Project ID somewhere (we need this Project ID for future use)

### Create API Token in Gitlab

1. Login to gitlab http://192.168.56.15/gitlab with username **_devops_** and **_$PROJECT_PASSWORD_**

2. Click on the profile picture

3. Click on **Edit profile**

4. Click on **Access Tokens** on the left side bar

5. Enter name **devops**

6. Click the Check box **api** under the Scopes section

7. Click on **Create personal access token**

8. Copy the generated API token and save it somewhere (we need this Token for future use)

## Set up SONARQUBE

### Set the password for user admin

1. Open URL http://192.168.56.15:9000/
2. Enter the user name **admin**
3. Enter the password **admin** (This is default password for the first time login)
4. Update your password window will open
5. Enter your old password
6. Enter a new password user **_admin_** (referred as **_$SONAR_PASSWORD_** in future)
7. Click on **Update**


### Create API Token in SonarQube

1. Login to Sonarqube http://192.168.56.15:9000/ with username **_admin_** and **_$SONAR_PASSWORD_** 

2. Click on the profile

3. Click on **My account**

4. Select the tab **Security** 

5. Enter a token name: **devops** in the Generate Tokens field

6. Click on **Generate**

7. Copy the generated token and save it somewhere (we need this Token for future use)

## Setup GRAFANA

### Reset Grafana Password

1. Open URL http://192.168.56.15:3000 in a web browser

2. Enter the details\
username: `admin`\
password: `admin`

3. set a new password for grafana user **_admin_** (referred as **_$GRAFANA_PASSWORD_** in future)

### Create Datasource in Grafana

1. Open URL http://192.168.56.15:3000 in a web browser

2. Login with user **_admin_** and password (**_$GRAFANA_PASSWORD_**)

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

10. It should display message as **Database Connection OK**

11. Click on **Back**

### Import 1st dashboard into Grafana

1. Click on **Create** icon on the left hand side bar (**+** symbol)

2. Select the **Import** option

3. Click on **Upload JSON file**

4. Select the below file\
`cd <root_folder>/devops/pipeline/integration-server/scripts/Grafana_Dashboard_Devops.json`

5. Click on **Import**

### Import 2nd dashboard into Grafana
1. Click on **Create** icon on the left hand side bar (**+** symbol)

2. Select the **Import** option

3. Click on **Upload JSON file**

4. Select the below file\
`cd <root_folder>/devops/pipeline/integration-server/scripts/Grafana_Dashboard_Test_Case.json`

5. Click on **Import**

6. Grafana set up completed

7. **Note: We have only set up Grafana now. No data will be visible at this stage. Only after running the Pipeline, data can be seen on the dashboard**

## Paste the Gitlab and Sonarqube API token and Gitlab Project ID in get_metrics.py file 

1. Go to `cd <root_folder>/devops/pipeline/integration-server`

2. Run command\
`vagrant ssh`

3. Go to `cd /vagrant_scripts`

4. Open file **get_metrics.py** :\
`sudo nano get_metrics`

**Note: If file is not visible at this location. Then you have to reload the integration-server VM**

5. Edit the below lines in the file with sonarqube token, gitlab token and gitlab project id respectively
```
sonarqube_token = 'paste the sonarqube token here'
gitlab_token = 'paste the gitlab token here'
gitlab_project_id = 'paste the Project ID here'
```
6. Exit using command `exit`

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

## Setup Runner in Integration server
### Download and Install Runner in Integration server
1. Download Gitlab runner\
`curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash`

2. Install Gitlab runner\
`sudo apt-get install gitlab-runner`

### Get the CI Token from runner in Gitlab

1. Login to Gitlab with user **_devops_**
2. Open the repository **welcomeWebApplication**
3. Go to **Settings** (Left hand side bar)
4. Select the option **CI/CD**
5. Click on **Runners**
6. Copy the **registration token**

### Register 1st runner in Integration server
1. Execute the following command\
`sudo gitlab-runner register`

2. Enter the requested information as follows

3. For GitLab instance URL enter:\
`http://192.168.56.15/gitlab/`

4. Enter the registration token: (**Note: Use the Registration token copied in the previous step)**)\
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

11. Finally, in GitLab change the configuration of the runner to accept jobs without TAGS\
**_Follow below steps_**
* Open **Gitlab**
* Select the project **welcomeWebApllication**
* Click on **Settings**
* Select **CI/CD**
* Click on **Runners** (Scroll down)
* You will see a runner registered
* Click on **Edit**
* Click the check box **Indicates whether this runner can pick jobs without tags**
* Click Save changes

### Register 2nd runner in Integration server
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

## Push Source Code to Gitlab

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

### Create Stage VM 
1. Get to `cd <root_folder>/devops/pipeline/stage-vm-welcome`

2. Run command
`vagrant up`

#### **** Test Case ***

Test Steps:

1. run command `vagrant ssh`

Post conditions:
- You have successfully logged in to **_stage-vm-welcome_** virtual machine
- Exit from the VM using command `exit`

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

12. Grant sudo permissions to the gitlab-runner:\
`sudo usermod -a -G sudo gitlab-runner`\
`sudo visudo`

13. Now add the following to the bottom of the file:\
`gitlab-runner ALL=(ALL) NOPASSWD: ALL`

14. Restart the staging environment:\
`exit`\
`vagrant reload`

## Production Environment 

**NOTE: Integration server should be up and running to execute these steps**

### Creat Production VM
1. Go to `cd <root_folder>/devops/pipeline/prod-vm-welcome`

2. Run command
`vagrant up`

#### *** Test Case ***

Initial conditions: you have successfully completed step 1
Test Steps:

1. run command `vagrant ssh`

Post conditions:
- You have successfully logged in to **_prod-vm-welcome_** virtual machine
- Exit from the VM using command `exit`

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

12. Grant sudo permissions to the gitlab-runner:\
`sudo usermod -a -G sudo gitlab-runner`\
`sudo visudo`

13. Now add the following to the bottom of the file:\
`gitlab-runner ALL=(ALL) NOPASSWD: ALL`

14. Restart the staging environment:\
`exit`\
`vagrant reload`

## Enter SonarQube details in Gitlab
1. Login to gitlab http://192.168.56.15/gitlab with username **_devops_** and **_$PROJECT_PASSWORD_**
2. Open the "welcomeWebApplication" repository
3. Click on **Settings**
4. Select **CI/CD**
5. Click on **Variables** section
6. Add below 3 variables one after the other
```
Key : SONAR_URL
Value: http://192.168.56.15:9000

Key: SONAR_USER
Value: admin

Key: SONAR_PASSWORD
Value: $SONAR_PASSWORD (Insert the actual password)
```

  
## Create .gitlab-ci.yml file

1. Login to gitlab http://192.168.56.15/gitlab with username **_devops_** and **_$PROJECT_PASSWORD_**
2. Open the "welcomeWebApplication" repository
3. create a new file with the name `.gitlab-ci.yml`

```
image: maven:3.6.2-jdk-8

stages:
  - sonar_build
  - metrics_build
  - build
  - upload
  - deploy
  - sonar_test
  - test
  - metrics_test
  - production
  - metrics_production

variables:
  MAVEN_CLI_OPTS: "--batch-mode --errors --fail-at-end --show-version -DinstallAtEnd=true -DdeployAtEnd=true"
  SONAR_ARGS: "sonar:sonar -Dsonar.host.url=$SONAR_URL -Dsonar.login=$SONAR_USER -Dsonar.password=$SONAR_PASSWORD"
    
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

sonarqube_build_app:
  stage: sonar_build
  tags:
    - integration
  script:
    - mvn -f welcome-webapplication/pom.xml --batch-mode verify --fail-never $SONAR_ARGS

metrics_build_app:
  stage: metrics_build
  tags:
    - integration-shell
  script: python /vagrant_scripts/get_metrics.py "build"

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
    expire_in: 10 minutes

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

    - echo "Set Execute right"
    - sudo chmod +x $APACHE_WEBAPPS/$RESOURCE_NAME
    
    - echo "Set user and group rights"
    - sudo chown tomcat:tomcat $APACHE_WEBAPPS/$RESOURCE_NAME
    
    - echo "Start up Tomcat"
    - sudo sh $APACHE_BIN/startup.sh

sonar_testing:
  stage: sonar_test
  tags:
    - integration
  services:
    - name: selenium/standalone-chrome:latest 
  script:
    - mvn -f welcome-webapplication.testing.testng/pom.xml --batch-mode verify --fail-never -Denv.BASEURL=$STAGE_BASE_URL test $SONAR_ARGS

metrics_test_app:
  stage: metrics_test
  tags:
    - integration-shell
  script: python /vagrant_scripts/get_metrics.py "test"

testing:
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
    - sudo sh $APACHE_BIN/startup.sh

metrics_production_app:
  stage: metrics_production
  tags:
    - integration-shell
  script: python /vagrant_scripts/get_metrics.py "production"
```

## Monitor the Metrics in Grafana Dashboard

**Prerequistes:**
- Grafana, Gitlab and Sonarqube are set up properly
- Grafana dashboard is imported successfully
- Mysql source connection is created successfully
- The pipeline should have run for multiple times (for better visualization of data).

### Login to Grafana

1. Open URL http://192.168.56.15:3000 in a web browser

2. Login with user **_admin_** and password (**_$GRAFANA_PASSWORD_**)

3. Referesh the dashboard to visualize the data



