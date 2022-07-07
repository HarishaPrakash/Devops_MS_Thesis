#!/bin/bash


# Define Tomcat's variables
APACHE_HOME=/opt/tomcat
APACHE_BIN=$APACHE_HOME/bin
APACHE_WEBAPPS=$APACHE_HOME/webapps

# Define product's variables
PRODUCT_SNAPSHOT_NAME=welcome-webapplication-0.0.1-SNAPSHOT.war
RESOURCE_NAME=welcome.war

# Shutdown Tomcat
sudo sh $APACHE_BIN/shutdown.sh


# Deploy generated SNAPSHOT into the dev-env  
sudo cp /vagrant_target/$PRODUCT_SNAPSHOT_NAME $APACHE_WEBAPPS

sudo mv $APACHE_WEBAPPS/$PRODUCT_SNAPSHOT_NAME $APACHE_WEBAPPS/$RESOURCE_NAME
sudo chown tomcat:tomcat $APACHE_WEBAPPS/$RESOURCE_NAME

# Start up Tomcat
sudo sh $APACHE_BIN/startup.sh
