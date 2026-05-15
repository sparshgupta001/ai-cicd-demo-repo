# GitHub Actions Failure Demo

This repository is a tiny Python project for testing failed GitHub Actions runs.
The failure is deliberate so a backend service can inspect the workflow logs and
source code, then later propose an automated fix.

## Project Shape

- `app.py` contains the application function used by the test.
- `math_utils.py` contains a small helper function.
- `tests/test_app.py` contains a pytest test.
- `.github/workflows/ci.yml` runs the test suite in GitHub Actions.

## Deliberate Failure

The broken version imports `add_numbers` from `math_utils.py`, but the helper
file defines `add`. This creates a clear import error:

```text
ImportError: cannot import name 'add_numbers' from 'math_utils'
```

This is intentionally simple and realistic for a hackathon demo because the
logs point directly to the broken import and the source context is small.

## Webhook Setup

Before pushing to GitHub, replace `YOUR_BACKEND_URL` in
`.github/workflows/ci.yml` with your ngrok URL.

Example:

```yaml
curl -X POST "https://your-ngrok-url.ngrok-free.app/api/webhook"
```

## Run Locally

```bash
pip install -r requirements.txt
pytest
```
