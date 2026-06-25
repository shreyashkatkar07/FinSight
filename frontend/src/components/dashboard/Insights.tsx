import { useInsights } from "../../hooks";

export default function Insights() {
  const {
    data,
    isLoading,
    isError,
  } = useInsights();

  if (isLoading) {
    return <div>Loading insights...</div>;
  }

  if (isError || !data) {
    return (
      <div className="text-red-500">
        Failed to load insights.
      </div>
    );
  }

  if (data.insights.length === 0) {
    return (
      <div>
        <h2 className="mb-4 text-xl font-semibold">
          AI Insights
        </h2>

        <div className="rounded-lg border p-4 text-gray-500">
          No insights available.
        </div>
      </div>
    );
  }

  return (
    <div>
      <h2 className="mb-4 text-xl font-semibold">
        AI Insights
      </h2>

      <div className="rounded-lg border">
        {data.insights.map((insight, index) => (
          <div
            key={index}
            className="flex gap-3 border-b p-4 last:border-b-0"
          >
            <span className="text-lg">💡</span>

            <p>{insight}</p>
          </div>
        ))}
      </div>
    </div>
  );
}