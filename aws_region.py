import boto3

def list_regions():
    ec2 = boto3.client("ec2")
    response = ec2.describe_regions(AllRegions=True)

    print("Available AWS Regions:")
    for region in response["Regions"]:
        print(f"- {region['RegionName']}")

if __name__ == "__main__":
    list_regions()
muid = "kailasrpillai@mulearn"
print("submitted_by:", muid)
