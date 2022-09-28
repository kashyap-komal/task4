import pymysql
import boto3
import  json

client = boto3.client('secretmanager')

response = client.get_secret_value(
    SecretId='input your secret id'
)
secretDict = json.loads(response['SecretString'])
db = pymysql.connect(
    host=secretDict['host'],
    user=secretDict['username'],
    password=secretDict['password']
)


cursor = db.cursor()
# cursor.execute("CREATE DATABASE TESTING")
# cursor.connection.commit()
cursor.execute("USE TESTING")

execute=["CREATE TABLE CUSTOMERR(custid varchar(7))","CREATE TABLE ACCOUNT(accno int(11))","CREATE TABLE TRANSCTION(amount int(42))"]
for i in execute:
    cursor.execute(i)
    
