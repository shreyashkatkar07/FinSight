export interface UploadArtifactResponse {
  artifact_uuid: string;
  file_name: string;
  file_type: string;
  status: string;
}

export interface ExtractedTransaction {
  merchant: string;
  amount: string;
  currency: string;
  event_type: string;
  confidence: number;
  category: string;
  description: string;
  transaction_date: string;
}

export interface ExtractArtifactResponse {
  transactions: ExtractedTransaction[];
}

export interface ConfirmArtifactRequest {
  transactions: ExtractedTransaction[];
}

export interface ConfirmArtifactResponse {
  artifact_uuid: string;
  status: string;
  events_created: number;
}

export interface ExtractionSession {
  artifactUuid: string;
  transactions: ExtractedTransaction[];
}