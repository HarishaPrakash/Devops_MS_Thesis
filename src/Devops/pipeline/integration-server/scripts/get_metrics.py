#!/bin/bash -e
#Import packages
from bdb import effective
from traceback import print_tb
import requests
import json
import csv 
import pandas as pd
import mysql.connector
import base64
import sys
import os
import datetime

#Varibale Initialization

url_gitlab = 'http://192.168.56.15/gitlab'
url_sonarqube = 'http://192.168.56.15:9000'

sonarqube_token = 'paste the sonarqube token here'
gitlab_token = 'paste the gitlab token here'
gitlab_project_id = 'paste the Project ID here'

mysql_host = 'localhost'
mysql_database='devops'
mysql_user='devops'
mysql_password='devops@2022'


query_metrics_table = """CREATE TABLE  IF NOT EXISTS metrics(commit_id varchar(100),
                            commiter_name varchar(100),
                            committed_date datetime,
                            nloc integer(100),
                            nloc_added integer(100),
                            nloc_deleted integer(100),
                            change_rate DOUBLE,
                            cyclomatic_complexity integer(100),
                            effective_cylomatic_complexity DOUBLE,
                            unit_test_case integer(100),
                            failed_unit_test_case integer(100),
                            integration_test_case integer(100),
                            failed_integration_test_case integer(100),
                            production_deployment datetime
                            );"""
   
query_commit = """COMMIT;"""


inputArgumentLength= len(sys.argv)
if (inputArgumentLength == 2):
    pass
else:
    raise Exception("Error: Input argument is missing")

#Github API URL
url_commit = url_gitlab+"/api/v4/projects/"+gitlab_project_id+"/repository/commits/"
url_commit_ind = url_gitlab+"/api/v4/projects/"+gitlab_project_id+"/repository/commits/master"

#Sonarqube API URL
url_nloc = url_sonarqube+"/api/measures/component?component=com.harish:welcome-webapplication&metricKeys=ncloc"
url_complexity = url_sonarqube+"/api/measures/component?component=com.harish:welcome-webapplication&metricKeys=complexity"
url_unit_test = url_sonarqube+"/api/measures/component?component=com.harish:welcome-webapplication&metricKeys=tests"
url_failed_unit_test = url_sonarqube+"/api/measures/component?component=com.harish:welcome-webapplication&metricKeys=test_failures"
url_integration_test = url_sonarqube+"/api/measures/component?component=com.harish:welcome-webapplication.testing.testng&metricKeys=tests"
url_failed_integration_test = url_sonarqube+"/api/measures/component?component=com.harish:welcome-webapplication.testing.testng&metricKeys=test_failures"

#Convert sonarqube token into base64 string
raw_token = sonarqube_token + ':' + ""
sonar_token_base64 = base64.b64encode(raw_token.encode()).decode()

#Function to API call to sonarqube 
def api_call_sonarqube(url):
    payload_sonar = {}
    headers_sonar = {
        'Authorization': 'Basic '+sonar_token_base64
        }
    response = requests.request("GET", url, headers=headers_sonar, data=payload_sonar)
    #Check status
    checkAPICallStatus(response.status_code, url)
    response_json = json.loads(response.text)
    inner_response_json = response_json['component']['measures'][0]
    metric_value = inner_response_json['value']

    return metric_value

#Function to check API call status
def checkAPICallStatus(statusCode, URL):
    if(statusCode == 200):
        pass
    elif(statusCode == 404):
        print("Check if the API token is mentioned correclty")
        raise Exception("ERROR: Page Not Found Error for URL {}".format(URL))
    else:
        print("Check if the API token is mentioned correclty")
        raise Exception("ERROR: Issue in accessing the URL {}".format(URL))

def mysql_connnection():
    return mysql.connector.connect(
        host=mysql_host,
        database=mysql_database,
        user=mysql_user,
        password=mysql_password)

def api_call_gitlab(url):
    payload_gitlab={}
    headers_gitlab = {
    'Authorization': 'Bearer '+gitlab_token
    }

    response = requests.request("GET", url, headers=headers_gitlab, data=payload_gitlab)
    checkAPICallStatus(response.status_code, url)
    json_data = json.loads(response.text)
    return json_data

commit_metrics_json = api_call_gitlab(url_commit_ind)
commit_id  = commit_metrics_json['id']

if(sys.argv[1] == 'build'):
    committed_date = commit_metrics_json['committed_date']
    commiter_name = commit_metrics_json['committer_name']
    inner_response_json = commit_metrics_json['stats']
    nloc_added = inner_response_json['additions']
    nloc_deleted = inner_response_json['deletions']

    #API call to get NLOC(Number of line of code)
    nloc = api_call_sonarqube(url_nloc)
    #API call to get cyclomatic complexity
    complexity = api_call_sonarqube(url_complexity)
    eff_cyclomatic_complexity= (float(complexity)/15)*100
    eff_cyclomatic_complexity= round(eff_cyclomatic_complexity, 2)
    #API call to get unit test
    unit_test_case = api_call_sonarqube(url_unit_test)
    #API call to get unit test falied
    failed_unit_test_case = api_call_sonarqube(url_failed_unit_test)
    #API call to get integration test case
    
    try:
        mysql_connnection = mysql_connnection()
    
        cursor = mysql_connnection.cursor()
        cursor.execute(query_metrics_table)

        #To calculate metric - Change Rate
        cursor.execute("SELECT COUNT(1) FROM metrics;")
        countResult = cursor.fetchall()
        rowCount = countResult[0][0]
    
        if (rowCount==0):
            change_rate = ((float(nloc_added)+float(nloc_deleted))/float(nloc))*100
            change_rate = round(change_rate, 2)
        else:
            #Get nloc value of the previous run
            cursor.execute("SELECT nloc FROM metrics ORDER BY committed_date DESC LIMIT 1;")
            nlocResult = cursor.fetchall()
            prev_nloc = nlocResult[0][0]
            change_rate = ((float(nloc_added)+float(nloc_deleted))/float(prev_nloc))*100
            change_rate = round(change_rate, 2)
  
        cursor.execute("INSERT INTO metrics(commit_id, commiter_name, committed_date, nloc, nloc_added, nloc_deleted, change_rate, cyclomatic_complexity, effective_cylomatic_complexity, unit_test_case, failed_unit_test_case) values(\""+str(commit_id)+"\",\""+str(commiter_name)+"\",\""+str(committed_date)[0:22]+"\",\""+str(nloc)+"\",\""+str(nloc_added)+"\",\""+str(nloc_deleted)+"\",\""+str(change_rate)+"\",\""+str(complexity)+"\",\""+str(eff_cyclomatic_complexity)+"\",\""+str(unit_test_case)+"\",\""+str(failed_unit_test_case)+"\");")
        cursor.execute(query_commit)
        print("Metrics data for Build stage is recorded in Database")

    except mysql.connector.Error as error:
        print("SQL Failed {}".format(error))
        raise Exception("ERROR: Please check the SQL connection OR SQL objects")
    finally:
        if mysql_connnection.is_connected():
            cursor.close()
            mysql_connnection.close()
            print("INFO:MySQL connection is closed successfully")

    if(True):
        print("commit_id",commit_id)
        print("committed_date",committed_date)
        print("commiter_name",commiter_name)
        print("nloc_added",nloc_added)
        print("nloc_deleted",nloc_deleted)
        print("nloc",nloc)
        print("complexity",complexity)
        print("eff_cycmlomatic_complexity",eff_cyclomatic_complexity)
        print("unit_test_case",unit_test_case)
        print("failed_unit_test_case",failed_unit_test_case)
        print("change_rate",change_rate)

elif(sys.argv[1] == 'test'):
    #API call to get integration test case
    integration_test_case = api_call_sonarqube(url_integration_test)

    #API call to get failed integration test case
    failed_integration_test_case = api_call_sonarqube(url_failed_integration_test)
   
    try:
        mysql_connnection = mysql_connnection()

        cursor = mysql_connnection.cursor()
        cursor.execute(query_metrics_table)
   
        cursor.execute("UPDATE metrics SET integration_test_case =\""+str(integration_test_case)+"\" , failed_integration_test_case = \""+str(failed_integration_test_case)+"\" WHERE commit_id=\""+str(commit_id)+"\";")     
        cursor.execute(query_commit)
        print("Metrics data for Test stage is recorded in Database")

    except mysql.connector.Error as error:
        print("SQL Failed {}".format(error))
        raise Exception("ERROR: Please check the SQL connection OR SQL objects")
    finally:
        if mysql_connnection.is_connected():
            cursor.close()
            mysql_connnection.close()
            print("INFO:MySQL connection is closed successfully")

    if(True):
        print("integration_test_case",integration_test_case)
        print("failed_integration_test_case",failed_integration_test_case)

elif(sys.argv[1] == 'production'):
    try:
        mysql_connnection = mysql_connnection()
        cursor = mysql_connnection.cursor()
        datetime_now = datetime.datetime.now()
        cursor.execute("UPDATE metrics SET production_deployment =\""+str(datetime_now)+"\"WHERE commit_id=\""+str(commit_id)+"\";")     
        cursor.execute(query_commit)
        print("Metrics data for Production stage is recorded in Database")

    except mysql.connector.Error as error:
        print("SQL Failed {}".format(error))
        raise Exception("ERROR: Please check the SQL connection OR SQL objects")
    finally:
        if mysql_connnection.is_connected():
            cursor.close()
            mysql_connnection.close()
            print("INFO:MySQL connection is closed successfully")
else:
    raise Exception("ERROR: Please check argument value passed is correct")
