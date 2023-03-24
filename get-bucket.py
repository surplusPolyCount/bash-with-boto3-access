import boto3
import sys

def main():
        print(f"attempting access bucket {sys.argv[1]}")

        s3 = boto3.client("s3")
        bucket = 'my-bucket'
        #Make sure you provide / in the end
        prefix = 'hospital17/'  

        all_objects = s3.list_objects(Bucket = 'foxseq-input-bacteria') 
        for ob in all_objects['Contents']:
                print(ob['Key'])

if __name__ == '__main__':
        main()