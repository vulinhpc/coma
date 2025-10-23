import { z } from 'zod';

export const MediaInput = z.object({
  dailyLogId: z.string().optional(),
  publicId: z.string().min(1),
  format: z.string().optional(),
  width: z.number().int().optional(),
  height: z.number().int().optional(),
  bytes: z.number().int().optional(),
  url: z.string().url(),
});

export const MediaResponse = z.object({
  id: z.string(),
  projectId: z.string(),
  dailyLogId: z.string().nullable(),
  publicId: z.string(),
  format: z.string().nullable().optional(),
  width: z.number().int().nullable().optional(),
  height: z.number().int().nullable().optional(),
  bytes: z.number().int().nullable().optional(),
  url: z.string(),
  createdAt: z.string(),
});

export type MediaInputType = z.infer<typeof MediaInput>;
export type MediaResponseType = z.infer<typeof MediaResponse>;
