import { postForm, postJson } from "../../api/client";

import type {
  UploadArtifactResponse,
  ExtractArtifactResponse,
  ConfirmArtifactRequest,
  ConfirmArtifactResponse,
} from "./types";

export async function uploadArtifact(
  file: File,
): Promise<UploadArtifactResponse> {
  const formData = new FormData();

  formData.append(
    "file",
    file,
  );

  return postForm<UploadArtifactResponse>(
    "/artifacts/upload",
    formData,
  );
}

export function extractArtifact(
  artifactUuid: string,
): Promise<ExtractArtifactResponse> {
  return postJson<ExtractArtifactResponse>(
    `/artifacts/${artifactUuid}/extract`,
    {},
  );
}

export function confirmArtifact(
  artifactUuid: string,
  request: ConfirmArtifactRequest,
): Promise<ConfirmArtifactResponse> {
  return postJson<ConfirmArtifactResponse>(
    `/artifacts/${artifactUuid}/confirm`,
    request,
  );
}