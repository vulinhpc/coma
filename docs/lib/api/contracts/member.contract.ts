import { z } from 'zod';

export const MemberInput = z.object({
  userId: z.string().min(1).optional(),
  invitedEmail: z.string().email().optional(),
  role: z.enum(['OWNER', 'ADMIN', 'PM', 'SITE', 'ACCOUNTANT']),
});

export const MemberResponse = z.object({
  id: z.string(),
  projectId: z.string(),
  userId: z.string().optional(),
  invitedEmail: z.string().email().optional(),
  role: z.string(),
  createdAt: z.string(),
});

export type MemberInputType = z.infer<typeof MemberInput>;
export type MemberResponseType = z.infer<typeof MemberResponse>;
