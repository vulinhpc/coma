# 🚦 CI/CD CHECKLIST — COMA

- Pre-commit: lint + typecheck.
- CI(PR): install (frozen), lint, typecheck, test, build.
- CD: merge main -> Vercel Production; rollback 1 click; feature flags cho rollout.
- Dependency policy: lý do, so sánh, license, reviewer đồng ý.
- Release: CHANGELOG, tag semver.
