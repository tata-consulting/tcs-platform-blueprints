# Python FastAPI Microservice - Golden Path Template

**Maturity:** Beta | **Owner:** Platform Team

This Backstage scaffolder template generates a production-ready Python FastAPI microservice, pre-configured with TCS platform standards.

## What It Generates

```
<service-name>/
├── app/
│   ├── main.py               # FastAPI app with lifespan, health endpoint, router inclusion
│   ├── models.py             # Pydantic BaseModel examples
│   └── routers/
│       └── example.py        # Example router with dependency injection pattern
├── .github/
│   └── workflows/
│       └── ci.yml            # ruff lint/format, pytest, checkov scan, build, push to ECR
├── helm/
│   └── <service-name>/
│       ├── Chart.yaml
│       ├── values.yaml       # HPA, resource limits, probes pre-configured
│       └── templates/
│           └── deployment.yaml  # Deployment + HPA + PodDisruptionBudget
├── docs/
│   └── index.md              # TechDocs entry point
├── catalog-info.yaml         # Pre-populated with mandatory TCS annotations
├── mkdocs.yml                # TechDocs MkDocs configuration
├── pyproject.toml            # Project metadata, deps, ruff config, pytest config
├── .python-version           # Pinned Python version for pyenv
└── Dockerfile                # Multi-stage, python:3.12-alpine, non-root user
```

## Prerequisites

- Backstage instance with scaffolder plugin enabled
- GitHub App or OAuth token with repo creation permissions
- AWS ECR repository provisioned for the service
- `AWS_ROLE_ARN` secret configured in the target GitHub organization

## Template Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `name` | Service name (kebab-case, becomes repo name) | - |
| `description` | Short service description | - |
| `team` | Owning team slug | - |
| `tier` | Service tier (tier-1/tier-2/tier-3) | `tier-2` |
| `awsRegion` | AWS region for ECR | `us-east-1` |
| `ecrRepo` | ECR repository name | - |
| `repoOwner` | GitHub organization or user | `tata-consulting` |

## Key Decisions

**Dockerfile:** Multi-stage build using `python:3.12-alpine`. Alpine reduces final image size significantly vs slim. Non-root `appuser` for security. `HEALTHCHECK` instruction included.

**Linting:** `ruff` replaces the flake8 + isort + black combination in a single tool. Configuration lives in `pyproject.toml` under `[tool.ruff]`.

**Testing:** `pytest-asyncio` with `asyncio_mode = "auto"` configured from the start. FastAPI endpoints are async; sync test patterns cause issues when testing async endpoints with `httpx.AsyncClient`.

**FastAPI skeleton:** Uses the modern `lifespan` context manager (replaces deprecated `on_event` startup/shutdown hooks). Dependency injection pattern shown with `Annotated[T, Depends(f)]` - the current idiomatic approach.

**Python version:** `.python-version` file pins to `3.12.0` for pyenv compatibility. `pyproject.toml` sets `requires-python = ">=3.12"`.

**CI:** checkov runs on Dockerfile and Helm chart with `--output github-actions` for PR annotation output. AWS authentication uses OIDC.

**Helm chart:** Same as Node.js template - `autoscaling.minReplicas: 2`, `PodDisruptionBudget.minAvailable: 1`.

## Using This Template

In your Backstage instance, navigate to Create > Python FastAPI Microservice and fill in the parameters. The template will:

1. Generate the repository from the skeleton
2. Push it to GitHub under the specified owner
3. Register the service in the Backstage catalog automatically

<!-- Screenshot placeholder: Backstage scaffolder form for this template -->

## Support

Raise issues or questions in [tata-consulting/tcs-platform-blueprints](https://github.com/tata-consulting/tcs-platform-blueprints/issues) or contact the platform team.
