import { useSummary } from "../hooks";

export default function SummaryCards() {
  const {
    data: summary,
    isLoading,
    isError,
  } = useSummary();

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (isError || !summary) {
    return <div>Failed to load summary.</div>;
  }

  const netFlow = Number(summary.net_flow);

  return (
    <div>
      <h2 className="mb-4 text-xl font-semibold">
        Monthly Summary
      </h2>

      <div className="grid grid-cols-1 gap-4 md:grid-cols-3">
        <div className="rounded-lg border p-4">
          <p className="text-sm text-gray-500">
            Income
          </p>

          <p className="text-2xl font-bold text-green-600">
            ₹{summary.total_income}
          </p>
        </div>

        <div className="rounded-lg border p-4">
          <p className="text-sm text-gray-500">
            Expense
          </p>

          <p className="text-2xl font-bold text-red-600">
            ₹{summary.total_expense}
          </p>
        </div>

        <div className="rounded-lg border p-4">
          <p className="text-sm text-gray-500">
            Net Flow
          </p>

          <p
            className={`text-2xl font-bold ${
              netFlow >= 0
                ? "text-green-600"
                : "text-red-600"
            }`}
          >
            {netFlow >= 0
              ? `₹${summary.net_flow}`
              : `-₹${Math.abs(netFlow).toFixed(2)}`}
          </p>
        </div>
      </div>
    </div>
  );
}