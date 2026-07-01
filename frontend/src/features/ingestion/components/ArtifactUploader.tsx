import { useRef } from "react";

import {
  useArtifactExtraction,
} from "../hooks";

import type {
  ExtractionSession,
} from "../types";

interface ArtifactUploaderProps {
  onExtractionComplete: (
    session: ExtractionSession,
  ) => void;
}

export default function ArtifactUploader({
  onExtractionComplete,
}: ArtifactUploaderProps) {
  const inputRef =
    useRef<HTMLInputElement>(
      null,
    );

  const {
    extract,
    isPending,
  } =
    useArtifactExtraction();

  async function handleChange(
    event: React.ChangeEvent<HTMLInputElement>,
  ) {
    const file =
      event.target.files?.[0];

    if (!file) {
      return;
    }

    try {
      const result =
        await extract(file);

      const session: ExtractionSession = {
        artifactUuid: result.artifactUuid,
        transactions: result.extraction.transactions,
      };

      onExtractionComplete(session);
    } catch (error) {
      // Extraction failed silently - could add toast notification later
    }
  }

  return (
    <div className="rounded-lg border p-6">

      <button
        className="rounded bg-blue-600 px-4 py-2 text-white"
        disabled={isPending}
        onClick={() =>
          inputRef.current?.click()
        }
      >
        {isPending
          ? "Extracting transactions..."
          : "Upload Artifact"}
      </button>

      <input
        ref={inputRef}
        hidden
        accept="image/*"
        type="file"
        onChange={
          handleChange
        }
      />

    </div>
  );
}
