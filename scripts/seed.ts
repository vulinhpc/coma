// scripts/seed.ts
// Seed demo data for COMA
// Run: pnpm tsx scripts/seed.ts
import "dotenv/config";

import { Client } from "pg";

async function main() {
  const url = process.env.DATABASE_URL;
  if (!url) {
    throw new Error("Missing DATABASE_URL");
  }

  const client = new Client({ connectionString: url });
  await client.connect();

  const now = new Date();

  try {
    // Create sample project
    const projectRes = await client.query(
      `INSERT INTO projects (id, name, description, code, status, start_date, budget, created_by, created_at, updated_at)
       VALUES (gen_random_uuid(), $1, $2, $3, 'active', $4, $5, $6, $7, $8) RETURNING id`,
      [
        "Nhà phố An Khánh",
        "Dự án nhà phố 3 tầng tại An Khánh, Hà Nội",
        "AK-001",
        new Date("2024-01-01"),
        5000000000, // 5 tỷ VND
        "demo_owner",
        now,
        now,
      ],
    );
    const projectId = projectRes.rows[0].id;

    // Add members
    await client.query(
      `INSERT INTO members (id, project_id, user_id, role, name, email, phone, is_active, joined_at, created_by, created_at, updated_at)
       VALUES (gen_random_uuid(), $1, $2, 'owner', $3, $4, $5, true, $6, $7, $8, $9)`,
      [
        projectId,
        "demo_owner",
        "Nguyễn Văn A",
        "nguyenvana@example.com",
        "0123456789",
        now,
        "demo_owner",
        now,
        now,
      ],
    );

    await client.query(
      `INSERT INTO members (id, project_id, user_id, role, name, email, phone, is_active, joined_at, created_by, created_at, updated_at)
       VALUES (gen_random_uuid(), $1, $2, 'admin', $3, $4, $5, true, $6, $7, $8, $9)`,
      [
        projectId,
        "demo_admin",
        "Trần Thị B",
        "tranthib@example.com",
        "0987654321",
        now,
        "demo_owner",
        now,
        now,
      ],
    );

    // Daily logs
    const log1 = await client.query(
      `INSERT INTO daily_logs (id, project_id, log_date, title, content, weather, temperature, work_hours, progress, created_by, created_at, updated_at)
       VALUES (gen_random_uuid(), $1, CURRENT_DATE, $2, $3, $4, $5, $6, $7, $8, $9, $10) RETURNING id`,
      [
        projectId,
        "Đổ bê tông sàn tầng 1",
        "Thời tiết nắng đẹp, tiến độ đúng kế hoạch. Đội ngũ 15 người làm việc hiệu quả.",
        "Nắng",
        28.5,
        8.0,
        25,
        "demo_owner",
        now,
        now,
      ],
    );

    const log2 = await client.query(
      `INSERT INTO daily_logs (id, project_id, log_date, title, content, weather, temperature, work_hours, progress, created_by, created_at, updated_at)
       VALUES (gen_random_uuid(), $1, CURRENT_DATE - INTERVAL '1 day', $2, $3, $4, $5, $6, $7, $8, $9, $10) RETURNING id`,
      [
        projectId,
        "Lắp dựng cốt pha",
        "Thi công an toàn, kiểm tra kỹ thuật đầy đủ. Không có sự cố.",
        "Nắng nhẹ",
        26.0,
        7.5,
        20,
        "demo_owner",
        now,
        now,
      ],
    );

    const log1Id = log1.rows[0].id;
    const log2Id = log2.rows[0].id;

    // Media (link to logs)
    await client.query(
      `INSERT INTO media (id, project_id, daily_log_id, file_name, original_name, file_size, mime_type, cloudinary_public_id, cloudinary_url, thumbnail_url, width, height, description, created_by, created_at)
       VALUES (gen_random_uuid(), $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14)`,
      [
        projectId,
        log1Id,
        "concrete_pour_001.jpg",
        "IMG_20241023_001.jpg",
        2048000,
        "image/jpeg",
        "coma/concrete_pour_001",
        "https://res.cloudinary.com/dy44qfit2/image/upload/v1732252800/coma/concrete_pour_001.jpg",
        "https://res.cloudinary.com/dy44qfit2/image/upload/w_300,h_200,c_fill/v1732252800/coma/concrete_pour_001.jpg",
        1920,
        1080,
        "Đổ bê tông sàn tầng 1",
        "demo_owner",
        now,
      ],
    );

    await client.query(
      `INSERT INTO media (id, project_id, daily_log_id, file_name, original_name, file_size, mime_type, cloudinary_public_id, cloudinary_url, thumbnail_url, width, height, description, created_by, created_at)
       VALUES (gen_random_uuid(), $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14)`,
      [
        projectId,
        log2Id,
        "formwork_001.jpg",
        "IMG_20241022_001.jpg",
        1856000,
        "image/jpeg",
        "coma/formwork_001",
        "https://res.cloudinary.com/dy44qfit2/image/upload/v1732252800/coma/formwork_001.jpg",
        "https://res.cloudinary.com/dy44qfit2/image/upload/w_300,h_200,c_fill/v1732252800/coma/formwork_001.jpg",
        1920,
        1080,
        "Lắp dựng cốt pha",
        "demo_owner",
        now,
      ],
    );

    // Transactions
    await client.query(
      `INSERT INTO transactions (id, project_id, type, category, description, amount, currency, transaction_date, vendor, reference, is_approved, created_by, created_at, updated_at)
       VALUES (gen_random_uuid(), $1, 'expense', 'Vật tư', $2, $3, 'VND', CURRENT_DATE, $4, $5, true, $6, $7, $8)`,
      [
        projectId,
        "Mua xi măng, cát, đá cho đổ bê tông",
        12000000.0,
        "Công ty VLXD ABC",
        "HD-001",
        "demo_owner",
        now,
        now,
      ],
    );

    await client.query(
      `INSERT INTO transactions (id, project_id, type, category, description, amount, currency, transaction_date, vendor, reference, is_approved, created_by, created_at, updated_at)
       VALUES (gen_random_uuid(), $1, 'expense', 'Nhân công', $2, $3, 'VND', CURRENT_DATE, $4, $5, true, $6, $7, $8)`,
      [
        projectId,
        "Tiền công thợ xây, thợ bê tông",
        8000000.0,
        "Đội thợ Nguyễn Văn C",
        "HD-002",
        "demo_owner",
        now,
        now,
      ],
    );

    await client.query(
      `INSERT INTO transactions (id, project_id, type, category, description, amount, currency, transaction_date, vendor, reference, is_approved, created_by, created_at, updated_at)
       VALUES (gen_random_uuid(), $1, 'income', 'Tạm ứng', $2, $3, 'VND', CURRENT_DATE, $4, $5, true, $6, $7, $8)`,
      [
        projectId,
        "Tạm ứng từ chủ đầu tư",
        30000000.0,
        "Chủ đầu tư Nguyễn Văn D",
        "TA-001",
        "demo_owner",
        now,
        now,
      ],
    );

    // Reports
    await client.query(
      `INSERT INTO reports (id, project_id, report_type, title, description, period_start, period_end, data, status, generated_by, generated_at, created_at, updated_at)
       VALUES (gen_random_uuid(), $1, 'daily', $2, $3, $4, $5, $6, 'published', $7, $8, $9, $10)`,
      [
        projectId,
        "Báo cáo ngày 23/10/2024",
        "Báo cáo tiến độ thi công ngày 23/10/2024",
        new Date("2024-10-23"),
        new Date("2024-10-23"),
        JSON.stringify({
          totalLogs: 2,
          totalMedia: 2,
          totalExpenses: 20000000,
          totalIncome: 30000000,
          progress: 25,
        }),
        "demo_owner",
        now,
        now,
        now,
      ],
    );

    console.log("✅ Seed completed successfully!");
    console.log("📊 Project ID:", projectId);
    console.log("👥 Members: 2");
    console.log("📝 Daily logs: 2");
    console.log("📸 Media: 2");
    console.log("💰 Transactions: 3");
    console.log("📊 Reports: 1");
  } catch (error) {
    console.error("❌ Seed error:", error);
    throw error;
  } finally {
    await client.end();
  }
}

main().catch((e) => {
  console.error("Seed error:", e);
  process.exit(1);
});
