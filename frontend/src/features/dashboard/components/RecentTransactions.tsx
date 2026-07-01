import { useTransactions } from "../hooks";

export default function RecentTransactions() {
  const {
    data: transactions,
    isLoading,
    isError,
  } = useTransactions();

  if (isLoading) {
    return <div>Loading transactions...</div>;
  }

  if (isError || !transactions) {
    return (
      <div className="text-red-500">
        Failed to load transactions.
      </div>
    );
  }

  return (
    <div>
      <h2 className="mb-4 text-xl font-semibold">
        Recent Transactions
      </h2>

      <div className="overflow-hidden rounded-lg border">
        {transactions.map((transaction) => (
          <div
            key={transaction.uuid}
            className="flex items-center justify-between border-b p-4 last:border-b-0"
          >
            <div>
              <p className="font-medium">
                {transaction.merchant}
              </p>

              <p className="text-sm text-gray-500">
                {transaction.description}
              </p>
            </div>

            <div className="text-right">
              <p className="font-semibold">
                ₹{transaction.amount}
              </p>

              <p className="text-sm text-gray-500">
                {transaction.transaction_date}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}