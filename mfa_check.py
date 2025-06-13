import boto3

def get_users_without_mfa():
    iam = boto3.client('iam')
    users = iam.list_users()['Users']
    users_without_mfa = []

    for user in users:
        username = user['UserName']
        mfa_devices = iam.list_mfa_devices(UserName=username)['MFADevices']
        if not mfa_devices:
            users_without_mfa.append(username)

    return users_without_mfa


def notify_admin(users_without_mfa, topic_arn):
    if not users_without_mfa:
        return

    sns = boto3.client('sns')
    message = "Users without MFA:\n" + "\n".join(users_without_mfa)
    sns.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject='AWS MFA Enforcement Alert'
    )


if __name__ == "__main__":
    users = get_users_without_mfa()
    if users:
        print("Users without MFA:")
        for user in users:
            print(f"- {user}")
    else:
        print("All users have MFA enabled.")
