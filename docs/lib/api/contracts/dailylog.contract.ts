import { z } from 'zod';

export const DailyLogInput = z.object({
  logDate: z.string(), // ISO date
  title: z.string().min(1).max(160),
  content: z.string().optional(),
  weather: z.string().optional(),
});

export const DailyLogResponse = z.object({
  id: z.string(),
  projectId: z.string(),
  logDate: z.string(),
  title: z.string(),
  content: z.string().optional(),
  weather: z.string().optional(),
  createdAt: z.string(),
});

export type DailyLogInputType = z.infer<typeof DailyLogInput>;
export type DailyLogResponseType = z.infer<typeof DailyLogResponse>;
