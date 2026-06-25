import { post } from "./client";

export interface IngestTextRequest {
  text: string;
}

export function ingestText(
  request: IngestTextRequest,
) {
  return post(
    "/ingestion/text",
    request,
  );
}