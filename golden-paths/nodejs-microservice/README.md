# Node.js Microservice - Golden Path Template

**Maturity:** Beta | **Owner:** Platform Team

This Backstage scaffolder template generates a production-ready Node.js Express microservice, pre-configured with TCS platform standards.

## What It Generates

```
<service-name>/
├── src/
│   └── index.ts              # Express app entry point with health endpoint
├── .github/
│   └── workflows/
│       └── ci.yml            # Lint, test, checkov scan, build, push to ECR
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
├── Dockerfile                # Multi-stage, node:20-alpine, non-root user
└── README.md
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

**Dockerfile:** Multi-stage build using `node:20-alpine`. Alpine reduces final image size by ~200MB vs the full node image. Non-root `appuser` for security. `HEALTHCHECK` instruction included for Docker Desktop visibility and Kubernetes probe compatibility.

**CI:** checkov runs against both Dockerfile and Helm chart with `--output github-actions` so failures surface as PR annotations. AWS authentication uses OIDC (no long-lived secrets).

**Helm chart:** `autoscaling.minReplicas: 2` by default - single-replica prod deployments are not permitted. `PodDisruptionBudget` with `minAvailable: 1` prevents all pods being evicted during node drains.

## Using This Template

In your Backstage instance, navigate to Create > Node.js Microservice and fill in the parameters. The template will:

1. Generate the repository from the skeleton
2. Push it to GitHub under the specified owner
3. Register the service in the Backstage catalog automatically

<!-- Screenshot placeholder: Backstage scaffolder form for this template -->

## Support

Raise issues or questions in [tata-consulting/tcs-platform-blueprints](https://github.com/tata-consulting/tcs-platform-blueprints/issues) or contact the platform team.
