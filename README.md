# aws-assume-role
	1. Create user in account 1 with no permission.
	2. Create and attach policy to user created in step 1
	Policy should be : assume-role-policy (this policy is required to assume role of another account)
	{
	    "Version": "2012-10-17",
	    "Statement": [
	        {
	            "Effect": "Allow",
	            "Action": [
	                "iam:ListRoles",
	                "sts:AssumeRole"
	            ],
	            "Resource": "*"
	        }
	    ]
	}
	3. Create role for the service need to be accessed by the user
	e.g. create RDS access role of type 'Another aws account'
	
	Add below json in the trust relationship of the role
	
	{
	  "Version": "2012-10-17",
	  "Statement": [
	    {
	      "Effect": "Allow",
	      "Principal": {
	        "AWS": "arn:aws:iam::6784537:role/<role_name>"
	      },
	      "Action": "sts:AssumeRole"
	    }
	  ]
	}
	
	71820820 - account 1 id
	assume-role-user-cli -user created in account 1
	
	4. To Access role of another account. Login(switch) to other account
	a) Create role for the service.
	e.g. create RDS access role of type 'Another aws account'
	
	Add below json in the trust relationship of the role
	
	{
	  "Version": "2012-10-17",
	  "Statement": [
	    {	
	      "Effect": "Allow",
	      "Principal": {
	        "AWS": "arn:aws:iam::71820820:user/assume-role-user-cli"
	      },
	      "Action": "sts:AssumeRole"
	    }
	  ]
	}
	
	71820820 - account 1 id
	assume-role-user-cli -user created in account 1

[Script for assume role](boto3-assume-role.py)

