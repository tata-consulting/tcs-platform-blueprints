# Pre-Production Checklist

Use this checklist before promoting any service to production. Code reviewers and platform engineers should verify all applicable items.

## Health and Reliability

- [ ] Readiness probe configured and tested
- [ ] Liveness probe configured and tested
- [ ] Health endpoint returns 200 when service is healthy, non-200 when degraded
- [ ] Resource `requests` defined (cpu + memory)
- [ ] Resource `limits` defined (cpu + memory)
- [ ] HPA configured with `minReplicas: 2` (production)
- [ ] `PodDisruptionBudget` configured with `minAvailable: 1`

## Observability

- [ ] `/metrics` endpoint exposed and returning Prometheus-format metrics
- [ ] OpenTelemetry SDK instrumented (traces)
- [ ] Logs are structured JSON to stdout
- [ ] Log lines include `trace_id` for correlation
- [ ] Runbook written and linked in `catalog-info.yaml` or TechDocs

## Security

- [ ] No secrets in environment variables, Helm values, or Kubernetes manifests
- [ ] Secrets sourced from AWS Secrets Manager or Vault
- [ ] Dedicated IAM role (IRSA) with least-privilege permissions
- [ ] mTLS configured (via service mesh or cert-manager)
- [ ] Network policy defined (if using Kubernetes NetworkPolicy)
- [ ] Container runs as non-root user
- [ ] Base image is minimal (alpine or distroless)
- [ ] checkov passes on Dockerfile and Helm chart

## API and Contracts

- [ ] OpenAPI spec committed to repo (for REST services)
- [ ] AsyncAPI spec committed to repo (for Kafka producers/consumers)
- [ ] API entity registered in Backstage catalog
- [ ] API versioning strategy documented

## Catalog and Documentation

- [ ] `catalog-info.yaml` present with all mandatory TCS annotations
- [ ] `tcs.io/tier` set correctly
- [ ] `tcs.io/lifecycle` set to `production`
- [ ] TechDocs present (`docs/` + `mkdocs.yml`)
- [ ] Architecture section in TechDocs completed
- [ ] Runbook in TechDocs completed

## SLOs (Tier-1 services only)

- [ ] SLOs defined (availability, latency p99)
- [ ] SLO targets documented in TechDocs
- [ ] On-call schedule configured (`tcs.io/oncall` annotation set)
- [ ] Alerting rules deployed for SLO breach

## CI/CD

- [ ] CI workflow passes (lint, test, security scan)
- [ ] Image pushed to ECR
- [ ] Deployment pipeline tested in non-production environment
- [ ] Rollback procedure documented
