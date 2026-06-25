import { useTopMerchants } from "../../hooks";

export default function TopMerchants() {
  const {
    data: merchants,
    isLoading,
    isError,
  } = useTopMerchants();

  if (isLoading) {
    return <div>Loading merchants...</div>;
  }

  if (isError || !merchants) {
    return (
      <div className="text-red-500">
        Failed to load merchants.
      </div>
    );
  }

  if (merchants.length === 0) {
    return (
      <div>
        <h2 className="mb-4 text-xl font-semibold">
          Top Merchants
        </h2>

        <div className="rounded-lg border p-4 text-gray-500">
          No merchants found.
        </div>
      </div>
    );
  }

  return (
    <div>
      <h2 className="mb-4 text-xl font-semibold">
        Top Merchants
      </h2>

      <div className="overflow-hidden rounded-lg border">
        {merchants.map((merchant) => (
          <div
            key={merchant.merchant}
            className="flex items-center justify-between border-b p-4 last:border-b-0"
          >
            <span className="font-medium">
              {merchant.merchant}
            </span>

            <span className="font-semibold">
              ₹{merchant.total_amount}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}