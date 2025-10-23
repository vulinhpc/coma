import { z } from 'zod';

export const ReportQuery = z.object({
  from: z.string().optional(),
  to: z.string().optional(),
});

export const ReportKPIResponse = z.object({
  totalPhotos: z.number().int(),
  logsThisMonth: z.number().int(),
  expenseThisMonth: z.string(),
  incomeThisMonth: z.string(),
  recentActivity: z.array(
    z.object({
      type: z.enum(['LOG', 'MEDIA', 'TXN']),
      id: z.string(),
      at: z.string(),
      title: z.string().optional(),
    }),
  ),
});

export type ReportQueryType = z.infer<typeof ReportQuery>;
export type ReportKPIResponseType = z.infer<typeof ReportKPIResponse>;
