import boto3

# Initialize AWS clients
ec2 = boto3.client('ec2', region_name='us-east-1')
rds = boto3.client('rds', region_name='us-east-1')

def create_vpc_infrastructure():
    print("--- STARTING INFRASTRUCTURE PROVISIONING ---")
    
    # 1. Create VPC
    print("1. Creating Virtual Private Cloud (VPC)...")
    vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = vpc['Vpc']['VpcId']
    print(f"   Success! VPC ID: {vpc_id}")
    
    # 2. Add Tags (
    ec2.create_tags(Resources=[vpc_id], Tags=[{'Key': 'Name', 'Value': 'Release-Automation-VPC'}])
    
    print(f"--- INFRASTRUCTURE SETUP COMPLETE for {vpc_id} ---")
    return vpc_id

if __name__ == "__main__":
    # You need AWS CLI configured for this to run locally, 
    # but for the repo, the code is what matters.
    try:
        create_vpc_infrastructure()
    except Exception as e:
        print(f"Error (Make sure AWS CLI is configured): {e}")