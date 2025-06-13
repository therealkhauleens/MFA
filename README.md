# AWS MFA Enforcer

This script checks IAM users in your AWS account and identifies which ones do **not** have MFA enabled.

## 🔧 Requirements
- Python 3.x
- `boto3` library (`pip install boto3`)
- AWS credentials (via CLI or environment variables)

## 🚀 Usage
```bash
python mfa_check.py
```

### Optional: Enable Admin Notification
Set your SNS Topic ARN in the script and call `notify_admin()` function.

## ✅ Features
- Lists users without MFA
- Sends alerts via SNS (optional)
- Deployable as AWS Lambda (coming soon)
