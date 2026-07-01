import {
  useMutation,
  useQueryClient,
} from "@tanstack/react-query";

import {
  uploadArtifact,
  extractArtifact,
  confirmArtifact,
} from "./api";

import type {
  ConfirmArtifactRequest,
  ExtractArtifactResponse,
} from "./types";

export function useUploadArtifact() {
  return useMutation({
    mutationFn: uploadArtifact,
  });
}

export function useExtractArtifact() {
  return useMutation({
    mutationFn: ({
      artifactUuid,
    }: {
      artifactUuid: string;
    }) =>
      extractArtifact(
        artifactUuid,
      ),
  });
}

export function useConfirmArtifact() {
  const queryClient =
    useQueryClient();

  return useMutation({
    mutationFn: ({
      artifactUuid,
      request,
    }: {
      artifactUuid: string;
      request: ConfirmArtifactRequest;
    }) =>
      confirmArtifact(
        artifactUuid,
        request,
      ),

    onSuccess: async () => {
      await queryClient.invalidateQueries({
        queryKey: ["dashboard"],
      });
    },
  });
}

/*
|--------------------------------------------------------------------------
| Workflow Hook
|--------------------------------------------------------------------------
*/

export function useArtifactExtraction() {
  const uploadMutation =
    useUploadArtifact();

  const extractMutation =
    useExtractArtifact();

  async function extract(
    file: File,
  ): Promise<{
    artifactUuid: string;
    extraction: ExtractArtifactResponse;
  }> {
    const upload =
      await uploadMutation.mutateAsync(
        file,
      );

    const extraction =
      await extractMutation.mutateAsync({
        artifactUuid:
          upload.artifact_uuid,
      });

    return {
      artifactUuid:
        upload.artifact_uuid,
      extraction,
    };
  }

  return {
    extract,

    isPending:
      uploadMutation.isPending ||
      extractMutation.isPending,
  };
}