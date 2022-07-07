#!/bin/sh

echo going to directory Devops/product/
cd ../../../product/

echo initialising git
git init

echo cloning welcomewebapplication 
git clone http://192.168.56.15/gitlab/devops/welcomewebapplication.git

echo source files into welcomewebapplication folder
cp -R welcome-webapplication welcomewebapplication
cp -R welcome-webapplication.testing.testng welcomewebapplication

echo goto welcomewebapplication folder
cd welcomewebapplication

echo pushing code into gitlab
git add .
git commit -m "Initial commit"
git push -u origin master

