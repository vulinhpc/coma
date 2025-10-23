import { z } from 'zod';

export const TransactionInput = z.object({
  txnType: z.enum(['EXPENSE', 'INCOME']),
  category: z.string().min(1).max(80),
  amount: z.string(), // decimal as string
  currency: z.enum(['VND', 'USD']).default('VND'),
  note: z.string().optional(),
  occurredAt: z.string(), // ISO date
});

export const TransactionResponse = z.object({
  id: z.string(),
  projectId: z.string(),
  txnType: z.string(),
  category: z.string(),
  amount: z.string(),
  currency: z.string(),
  note: z.string().optional(),
  occurredAt: z.string(),
  createdAt: z.string(),
});

export type TransactionInputType = z.infer<typeof TransactionInput>;
export type TransactionResponseType = z.infer<typeof TransactionResponse>;
