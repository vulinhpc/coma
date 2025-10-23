# COMA_RUNBOOK

## P1 (Sự cố nghiêm trọng)

1. Xác định: alert/logs, version vừa deploy.
2. Ổn định: rollback Vercel, tắt feature flag.
3. Chẩn đoán: last change, logs/traces, DB status.
4. Khắc phục: hotfix qua PR nhỏ.
5. Hậu kiểm: Postmortem trong 48h.

## Kiểm tra nhanh

- /health routes (nếu có)
- DB connections ok
- Migrations up-to-date
