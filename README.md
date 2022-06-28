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



