/** Centralized error types for COMA */
export class AppError extends Error {
  code: string;
  status: number;
  constructor(code: string, message: string, status = 400) {
    super(message);
    this.code = code;
    this.status = status;
  }
}

export function isAppError(err: unknown): err is AppError {
  return (
    typeof err === 'object' && err !== null && 'code' in (err as any) && 'status' in (err as any)
  );
}

export function errorPayload(err: unknown) {
  if (isAppError(err)) {
    return { error: (err as AppError).message, code: (err as AppError).code };
  }
  return { error: 'Internal Server Error', code: 'INTERNAL_ERROR' };
}

export function errorStatus(err: unknown) {
  if (isAppError(err)) {
    return (err as AppError).status;
  }
  return 500;
}
