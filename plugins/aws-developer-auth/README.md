# Sign-in

Set up and verify secure short-lived AWS CLI and SDK credentials for local development.

## Included skills

- **signing-in-to-aws** — Gets AWS credentials for CLI/SDK access via `aws login`. ([procedure](skills/signing-in-to-aws/SKILL.md))

## Requirements and authentication

Use the AWS CLI or SDK credential provider chain named by the selected skill. Authentication occurs on use; installing this plugin does not sign in or store credentials.

Commands that create, update, deploy, or delete AWS resources require the user’s explicit task authorization.

