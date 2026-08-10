export type Provider = "openai" | "gemini";

export function getApiBase(provider: Provider) {
  if (provider === "openai") {
    return process.env.NEXT_PUBLIC_OPENAI_API_URL || "http://localhost:8892";
  }
  return (
    process.env.NEXT_PUBLIC_GEMINI_API_URL ||
    process.env.NEXT_PUBLIC_API_URL ||
    "http://localhost:8891"
  );
}

export function buildAuthBody(
  provider: Provider,
  apiKey: string,
  model?: string
) {
  return {
    provider,
    api_key: apiKey,
    openai_api_key: provider === "openai" ? apiKey : undefined,
    gemini_api_key: apiKey,
    model: model || undefined,
  };
}

export const DEFAULT_OPENAI_MODEL = "gpt-5-mini";
export const DEFAULT_GEMINI_MODEL = "gemini-3-flash-preview";
