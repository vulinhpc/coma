import { relations } from "drizzle-orm";
import {
  boolean,
  decimal,
  integer,
  jsonb,
  pgTable,
  text,
  timestamp,
  uuid,
  varchar,
} from "drizzle-orm/pg-core";

// Projects table - Main entity
export const projects = pgTable("projects", {
  id: uuid("id").primaryKey().defaultRandom(),
  name: varchar("name", { length: 255 }).notNull(),
  description: text("description"),
  code: varchar("code", { length: 50 }).notNull().unique(),
  status: varchar("status", { length: 20 }).notNull().default("active"), // active, completed, paused
  startDate: timestamp("start_date"),
  endDate: timestamp("end_date"),
  budget: decimal("budget", { precision: 15, scale: 2 }),
  createdBy: varchar("created_by", { length: 255 }).notNull(), // Clerk user ID
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
});

// Members table - Project team members
export const members = pgTable("members", {
  id: uuid("id").primaryKey().defaultRandom(),
  projectId: uuid("project_id")
    .notNull()
    .references(() => projects.id, { onDelete: "cascade" }),
  userId: varchar("user_id", { length: 255 }).notNull(), // Clerk user ID
  role: varchar("role", { length: 20 }).notNull(), // owner, admin, member, viewer
  name: varchar("name", { length: 255 }).notNull(),
  email: varchar("email", { length: 255 }).notNull(),
  phone: varchar("phone", { length: 20 }),
  isActive: boolean("is_active").notNull().default(true),
  joinedAt: timestamp("joined_at").notNull().defaultNow(),
  createdBy: varchar("created_by", { length: 255 }).notNull(),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
});

// Daily logs table - Construction daily reports
export const dailyLogs = pgTable("daily_logs", {
  id: uuid("id").primaryKey().defaultRandom(),
  projectId: uuid("project_id")
    .notNull()
    .references(() => projects.id, { onDelete: "cascade" }),
  logDate: timestamp("log_date").notNull(),
  title: varchar("title", { length: 255 }).notNull(),
  content: text("content").notNull(),
  weather: varchar("weather", { length: 50 }),
  temperature: decimal("temperature", { precision: 5, scale: 2 }),
  workHours: decimal("work_hours", { precision: 5, scale: 2 }),
  progress: integer("progress"), // percentage 0-100
  issues: text("issues"),
  nextDayPlan: text("next_day_plan"),
  createdBy: varchar("created_by", { length: 255 }).notNull(),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
});

// Media table - Images and videos
export const media = pgTable("media", {
  id: uuid("id").primaryKey().defaultRandom(),
  projectId: uuid("project_id")
    .notNull()
    .references(() => projects.id, { onDelete: "cascade" }),
  dailyLogId: uuid("daily_log_id").references(() => dailyLogs.id, { onDelete: "cascade" }),
  fileName: varchar("file_name", { length: 255 }).notNull(),
  originalName: varchar("original_name", { length: 255 }).notNull(),
  fileSize: integer("file_size").notNull(),
  mimeType: varchar("mime_type", { length: 100 }).notNull(),
  cloudinaryPublicId: varchar("cloudinary_public_id", { length: 255 }).notNull(),
  cloudinaryUrl: varchar("cloudinary_url", { length: 500 }).notNull(),
  thumbnailUrl: varchar("thumbnail_url", { length: 500 }),
  width: integer("width"),
  height: integer("height"),
  description: text("description"),
  tags: jsonb("tags"), // Array of strings
  createdBy: varchar("created_by", { length: 255 }).notNull(),
  createdAt: timestamp("created_at").notNull().defaultNow(),
});

// Transactions table - Income and expenses
export const transactions = pgTable("transactions", {
  id: uuid("id").primaryKey().defaultRandom(),
  projectId: uuid("project_id")
    .notNull()
    .references(() => projects.id, { onDelete: "cascade" }),
  type: varchar("type", { length: 20 }).notNull(), // income, expense
  category: varchar("category", { length: 100 }).notNull(),
  description: text("description").notNull(),
  amount: decimal("amount", { precision: 15, scale: 2 }).notNull(),
  currency: varchar("currency", { length: 3 }).notNull().default("VND"),
  transactionDate: timestamp("transaction_date").notNull(),
  vendor: varchar("vendor", { length: 255 }),
  reference: varchar("reference", { length: 100 }), // Invoice number, receipt number
  attachments: jsonb("attachments"), // Array of media IDs
  isApproved: boolean("is_approved").notNull().default(false),
  approvedBy: varchar("approved_by", { length: 255 }),
  approvedAt: timestamp("approved_at"),
  createdBy: varchar("created_by", { length: 255 }).notNull(),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
});

// Reports table - Generated reports and KPIs
export const reports = pgTable("reports", {
  id: uuid("id").primaryKey().defaultRandom(),
  projectId: uuid("project_id")
    .notNull()
    .references(() => projects.id, { onDelete: "cascade" }),
  reportType: varchar("report_type", { length: 50 }).notNull(), // daily, weekly, monthly, custom
  title: varchar("title", { length: 255 }).notNull(),
  description: text("description"),
  periodStart: timestamp("period_start").notNull(),
  periodEnd: timestamp("period_end").notNull(),
  data: jsonb("data").notNull(), // Report data as JSON
  status: varchar("status", { length: 20 }).notNull().default("draft"), // draft, published, archived
  generatedBy: varchar("generated_by", { length: 255 }).notNull(),
  generatedAt: timestamp("generated_at").notNull().defaultNow(),
  publishedAt: timestamp("published_at"),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
});

// Define relations
export const projectsRelations = relations(projects, ({ many }) => ({
  members: many(members),
  dailyLogs: many(dailyLogs),
  media: many(media),
  transactions: many(transactions),
  reports: many(reports),
}));

export const membersRelations = relations(members, ({ one }) => ({
  project: one(projects, {
    fields: [members.projectId],
    references: [projects.id],
  }),
}));

export const dailyLogsRelations = relations(dailyLogs, ({ one, many }) => ({
  project: one(projects, {
    fields: [dailyLogs.projectId],
    references: [projects.id],
  }),
  media: many(media),
}));

export const mediaRelations = relations(media, ({ one }) => ({
  project: one(projects, {
    fields: [media.projectId],
    references: [projects.id],
  }),
  dailyLog: one(dailyLogs, {
    fields: [media.dailyLogId],
    references: [dailyLogs.id],
  }),
}));

export const transactionsRelations = relations(transactions, ({ one }) => ({
  project: one(projects, {
    fields: [transactions.projectId],
    references: [projects.id],
  }),
}));

export const reportsRelations = relations(reports, ({ one }) => ({
  project: one(projects, {
    fields: [reports.projectId],
    references: [projects.id],
  }),
}));
