import { useState } from "react";

import SummaryCards from "../features/dashboard/components/SummaryCards";
import TopMerchants from "../features/dashboard/components/TopMerchants";
import Insights from "../features/dashboard/components/Insights";
import RecentTransactions from "../features/dashboard/components/RecentTransactions";
import ArtifactUploader from "../features/ingestion/components/ArtifactUploader";
import ReviewTransactions from "../features/ingestion/components/ReviewTransactions";

import type {
  ExtractionSession,
} from "../features/ingestion/types";

export default function Dashboard() {
  const [session, setSession] =
    useState<ExtractionSession | null>(
      null,
    );

  return (
    <div className="mx-auto max-w-5xl px-4 py-6">
      <h1 className="mb-8 text-3xl font-bold">
        PFIS
      </h1>

      <ArtifactUploader
        onExtractionComplete={setSession}
      />

      {session && (
        <div className="mt-8">
          <ReviewTransactions
            session={session}
            onSessionChange={setSession}
          />
        </div>
      )}

      <div className="mt-8">
        <SummaryCards />
      </div>

      <div className="mt-8">
        <TopMerchants />
      </div>

      <div className="mt-8">
        <Insights />
      </div>

      <div className="mt-8">
        <RecentTransactions />
      </div>
    </div>
  );
}