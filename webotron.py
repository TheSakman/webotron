import boto3
import click

session = boto3.Session(profile_name='sakland_admin')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS S3"
    pass

@cli.command('listbuckets')
def list_buckets():
    "List all S3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('listbucketobjects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List objects in an S3 bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

if __name__ == '__main__':
    cli()   
    # control is passed to click


