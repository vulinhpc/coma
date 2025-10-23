import { z } from 'zod';

export const ProjectInput = z.object({
  name: z.string().min(3).max(160),
  code: z
    .string()
    .regex(/^[A-Z0-9-]+$/)
    .max(40),
  status: z.enum(['ACTIVE', 'ON_HOLD', 'CLOSED']),
  startDate: z.string().optional(),
  endDate: z.string().optional(),
});

export const ProjectResponse = z.object({
  id: z.string(),
  name: z.string(),
  code: z.string(),
  status: z.string(),
  createdAt: z.string(),
});

export type ProjectInputType = z.infer<typeof ProjectInput>;
export type ProjectResponseType = z.infer<typeof ProjectResponse>;
