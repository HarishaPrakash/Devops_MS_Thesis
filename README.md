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

## Create Token in Gitlab
1. Login to gitlab http://192.168.56.15/gitlab with username **_devops_** and **_$PROJECT_PASSWORD_**
2. Click on the profile picture
3. Click on **Edit profile**
4. Click on **Access Tokens** on the left side bar
5. Enter name `devops`
6. Click the Check box **api** under the sources
7. Click on **Create personal access token**
8. Copy the generated token and save it somewhere

## Create Token in SonarQube
1. Login to gitlab http://192.168.56.15/gitlab with username **_devops_** and **_$PROJECT_PASSWORD_**
2. Click on the profile
3. Click on **My account**
4. Select the tab **Security** 
5. Enter a token name: **devops**
6. Click on **Generate**
7. Copy the generated token and save it somewhere

## Get the Gitlan PROJECT ID
1. Login to Sonarqube http://192.168.56.15:9000/ with username **_admin_** and **_$SONAR_PASSWORD_** 
2. Click on the project **welcomewebapplication**
3. Get the **Project ID** (Note: It will be displayed below the project name)

## Paste the Gitlab and Sonarqube tokens and Gitlab Project ID in file

1. Go to `cd <root_folder>/devops/pipeline/integration-server`
2. Run command\
`vagrant ssh`
3. Go to `cd /vagrant_scripts`
4. Open file **get_metrics.py** : `sudo nano get_metrics`
5. Edit the below lines in the file with sonarqube token, gitlab token and gitlab project id respectively\
sonarqube_token = 'paste the sonarqube token here'\
gitlab_token = 'paste the gitlab token here'\
gitlab_project_id = 'paste the Project ID here'
  
## Create .gitlab-ci.yml file

1. Login to gitlab http://192.168.56.15/gitlab with username **_devops_** and **_$PROJECT_PASSWORD_**
2. Open the "welcomeWebApplication" repository
3. create a new file with the name `.gitlab-ci.yml`\
`
image: maven:3.6.2-jdk-8

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
    - sudo sh $APACHE_BIN/startup.sh
    `
 



