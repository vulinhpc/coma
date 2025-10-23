// scripts/seed.ts
// Seed demo data for COMA
// Run: pnpm tsx scripts/seed.ts
import 'dotenv/config';

import { Client } from 'pg';

async function main() {
  const url = process.env.DATABASE_URL;
  if (!url) {
    throw new Error('Missing DATABASE_URL');
  }

  const client = new Client({ connectionString: url });
  await client.connect();

  const now = new Date();

  // Create sample project
  const projectRes = await client.query(
    `INSERT INTO projects (id, name, code, status, created_by, created_at)
     VALUES (gen_random_uuid(), $1, $2, 'ACTIVE', $3, $4) RETURNING id`,
    ['Nhà phố An Khánh', 'AK-001', 'demo_owner', now],
  );
  const projectId = projectRes.rows[0].id;

  // Add member (OWNER)
  await client.query(
    `INSERT INTO project_members (id, project_id, user_id, role, created_at)
     VALUES (gen_random_uuid(), $1, $2, 'OWNER', $3)`,
    [projectId, 'demo_owner', now],
  );

  // Daily logs
  const log1 = await client.query(
    `INSERT INTO daily_logs (id, project_id, log_date, title, content, created_by, created_at)
     VALUES (gen_random_uuid(), $1, CURRENT_DATE, 'Đổ bê tông sàn 1', 'Thời tiết nắng đẹp', 'demo_owner', $2) RETURNING id`,
    [projectId, now],
  );
  const _log2 = await client.query(
    `INSERT INTO daily_logs (id, project_id, log_date, title, content, created_by, created_at)
     VALUES (gen_random_uuid(), $1, CURRENT_DATE - INTERVAL '1 day', 'Lắp dựng cốt pha', 'Thi công an toàn', 'demo_owner', $2) RETURNING id`,
    [projectId, now],
  );
  const log1Id = log1.rows[0].id;

  // Media (link to log1)
  await client.query(
    `INSERT INTO media_assets (id, project_id, daily_log_id, public_id, format, url, created_by, created_at)
     VALUES (gen_random_uuid(), $1, $2, 'sample_public_id', 'jpg', 'https://res.cloudinary.com/demo/image/upload/sample.jpg', 'demo_owner', $3)`,
    [projectId, log1Id, now],
  );

  // Transactions
  await client.query(
    `INSERT INTO transactions (id, project_id, txn_type, category, amount, currency, occurred_at, created_by, created_at)
     VALUES (gen_random_uuid(), $1, 'EXPENSE', 'Vật tư', 1200000.00, 'VND', CURRENT_DATE, 'demo_owner', $2)`,
    [projectId, now],
  );
  await client.query(
    `INSERT INTO transactions (id, project_id, txn_type, category, amount, currency, occurred_at, created_by, created_at)
     VALUES (gen_random_uuid(), $1, 'INCOME', 'Tạm ứng', 3000000.00, 'VND', CURRENT_DATE, 'demo_owner', $2)`,
    [projectId, now],
  );

  // console.log('✅ Seed xong. Project ID:', projectId);
  await client.end();
}

main().catch((e) => {
  console.error('Seed error:', e);
  process.exit(1);
});
