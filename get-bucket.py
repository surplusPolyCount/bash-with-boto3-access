import boto3
import sys

def main():
        print(f"attempting access bucket {sys.argv[1]}")
        s3_client = boto3.client(
                service_name = 's3',
                endpoint_url = sys.argv[1]
        )
        response = s3_client.list_buckets()
        print('These are buckets that are accessible:')
        try:
                for bucket in response['Buckets']:
                        print(f"   {bucket['Name']}")
        except:
                print("could not find any buckets")

if __name__ == '__main__':
        main()