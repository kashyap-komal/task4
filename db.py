import boto3

client = boto3.client('rds')

response =client.create_db_instance(
    AllocatedStorage=123,
    DBInstanceClass='db.t2.micro',
    DBInstanceIdentifier='database-instance-01',
    DBName='task4',
    Engine='MySQL',
    MasterUserPassword='kyubataye25',
    MasterUsername='komal25',
)

print(response)
