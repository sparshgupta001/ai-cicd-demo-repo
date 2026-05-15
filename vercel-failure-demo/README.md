# Vercel Failure Demo

This small Next.js app is used to test failed Vercel deployments for an AI
CI/CD failure diagnosis system.

## Demo Flow

1. Push the working version.
2. Import this repo into Vercel.
3. Set the Vercel project Root Directory to `vercel-failure-demo`.
4. Confirm the first deployment succeeds.
5. Configure a Vercel webhook for `deployment.error`.
6. Push the broken commit.
7. Vercel fails the deployment and sends the webhook to your backend.
8. Your backend fetches deployment logs and diagnoses the issue.

## Webhook Setup

In Vercel, open your project and go to:

```text
Settings -> Webhooks -> Create Webhook
```

Use:

```text
Event: Deployment Error
URL: https://your-backend.com/api/vercel/webhook
Secret: create or copy the secret shown by Vercel
```

Save the secret in your backend as:

```text
VERCEL_WEBHOOK_SECRET=your_secret_here
```

## API Token

Create a Vercel API token from your Vercel account settings and save it in your
backend environment:

```text
VERCEL_TOKEN=vercel_xxxxxxxxx
```

Your backend can use this token to fetch deployment events/logs after it
receives the webhook.

## Fetch Deployment Logs

Use the deployment ID from the webhook payload:

```text
GET https://api.vercel.com/v3/deployments/{deploymentId}/events
Authorization: Bearer $VERCEL_TOKEN
```

## Broken Version

The broken commit imports a package that is not installed:

```js
import missingPackage from "missing-package";
```

Vercel build logs should clearly show:

```text
Module not found: Can't resolve 'missing-package'
```

This failure is deterministic, fast, and easy for an AI backend to diagnose.

## Run Locally

```bash
npm install
npm run build
```
