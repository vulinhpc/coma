import { NextResponse } from 'next/server';

import { AppError, errorPayload, errorStatus } from '../errors';

type Handler = (req: Request, params?: Record<string, any>) => Promise<Response> | Response;

export function withApiHandler(fn: Handler): Handler {
  return async (req, params) => {
    try {
      return await fn(req, params);
    } catch (err) {
      if (process.env.NODE_ENV !== 'production') {
        console.warn('[API ERROR]', err);
      }
      return NextResponse.json(errorPayload(err), { status: errorStatus(err) });
    }
  };
}

export function assert(
  condition: any,
  code = 'BAD_REQUEST',
  message = 'Bad request',
  status = 400,
) {
  if (!condition) {
    throw new AppError(code, message, status);
  }
}

export function okJson<T>(data: T, init?: ResponseInit) {
  return NextResponse.json(data as any, init);
}
