import boto3
import uuid
# Let's use Amazon S3
s3 = boto3.resource('s3')
# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
# Upload a new file
data = open('abhi.JPG', 'rb')
s3.Bucket('application1-py-s3').put_object(Key='abhi.JPG', Body=data)
# First, we'll start with Client API for Amazon S3. Let's instantiate a new
# client object. With no parameters or configuration, boto3 will look for
s3client = boto3.client('s3')
bucket_name = 'python-sdk-sample-{}'.format(uuid.uuid4())
print('Creating new bucket with name: {}'.format(bucket_name))
s3client.create_bucket(Bucket=bucket_name)
# Now the bucket is created, and you'll find it in your list of buckets.

list_buckets_resp = s3client.list_buckets()
for bucket in list_buckets_resp['Buckets']:
    if bucket['Name'] == bucket_name:
        print('(Just created) --> {} - there since {}'.format(
            bucket['Name'], bucket['CreationDate']))

# Files in Amazon S3 are called "objects" and are stored in buckets. A
# specific object is referred to by its key (i.e., name) and holds data. Here,
# we create (put) a new object with the key "python_sample_key.txt" and
# content "Hello World!".

object_key = 'python_sample_key.txt'

print('Uploading some data to {} with key: {}'.format(
    bucket_name, object_key))
s3client.put_object(Bucket=bucket_name, Key=object_key, Body=b'Hello World!')
#using the client, you can generate a pre-signed URL that you can give
# others to securely share the object without making it publicly accessible.
# By default, the generated URL will expire and no longer function after one
# hour. You can change the expiration to be from 1 second to 604800 seconds
# (1 week).

url = s3client.generate_presigned_url(
    'get_object', {'Bucket': bucket_name, 'Key': object_key})
print('\nTry this URL in your browser to download the object:')
print(url)
try:
    input = raw_input
except NameError:
    pass
input("\nPress enter to continue...")
print('\nNow using Resource API')
# First, create the service resource object
s3resource = boto3.resource('s3')
# Now, the bucket object
bucket = s3resource.Bucket(bucket_name)
# Then, the object object
obj = bucket.Object(object_key)
print('Bucket name: {}'.format(bucket.name))
print('Object key: {}'.format(obj.key))
print('Object content length: {}'.format(obj.content_length))
print('Object body: {}'.format(obj.get()['Body'].read()))
print('Object last modified: {}'.format(obj.last_modified))

# Buckets cannot be deleted unless they're empty. Let's keep using the
# Resource API to delete everything. Here, we'll utilize the collection
# 'objects' and its batch action 'delete'. Batch actions return a list
# of responses, because boto3 may have to take multiple actions iteratively to
# complete the action.

print('\nDeleting all objects in bucket {}.'.format(bucket_name))
delete_responses = bucket.objects.delete()
for delete_response in delete_responses:
    for deleted in delete_response['Deleted']:
        print('\t Deleted: {}'.format(deleted['Key']))

# Now that the bucket is empty, let's delete the bucket.

print('\nDeleting the bucket.')
bucket.delete()

# For more details on what you can do with boto3 and Amazon S3, see the API
# reference page:
# https://boto3.readthedocs.org/en/latest/reference/services/s3.html

print('New git chnages")

