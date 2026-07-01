import {
  useMutation,
  useQueryClient,
} from "@tanstack/react-query";

import {
  confirmArtifact,
} from "../api";

import type {
  ExtractionSession,
  ExtractedTransaction,
} from "../types";

interface ReviewTransactionsProps {
  session: ExtractionSession;
  onSessionChange: (
    session: ExtractionSession,
  ) => void;
}

export default function ReviewTransactions({
  session,
  onSessionChange,
}: ReviewTransactionsProps) {
  const queryClient = useQueryClient();

  const confirmMutation = useMutation({
    mutationFn: ({
      artifactUuid,
      request,
    }: {
      artifactUuid: string;
      request: {
        transactions: ExtractedTransaction[];
      };
    }) =>
      confirmArtifact(
        artifactUuid,
        request,
      ),

    onSuccess: async () => {
      await queryClient.invalidateQueries({
        queryKey: ["dashboard"],
      });

      onSessionChange(null);
    },
  });

  if (session.transactions.length === 0) {
    return (
      <div className="rounded-lg border p-6">
        <h2 className="mb-4 text-xl font-semibold">
          Review Extracted Transactions
        </h2>

        <div className="rounded bg-gray-50 p-4 text-center text-gray-600">
          <p className="text-lg">
            No transactions detected
          </p>
          <p className="mt-2 text-sm">
            Try another image or enter transactions manually
          </p>
        </div>

        <div className="mt-6 flex justify-end">
          <button
            onClick={() =>
              onSessionChange(null)
            }
            className="rounded border px-4 py-2"
          >
            Cancel
          </button>
        </div>
      </div>
    );
  }

  function updateTransaction(
    index: number,
    updates: Partial<ExtractedTransaction>,
  ) {
    const updatedTransactions = [
      ...session.transactions,
    ];

    updatedTransactions[index] = {
      ...updatedTransactions[index],
      ...updates,
    };

    onSessionChange({
      ...session,
      transactions: updatedTransactions,
    });
  }

  function deleteTransaction(index: number) {
    const updatedTransactions =
      session.transactions.filter(
        (_, i) => i !== index,
      );

    onSessionChange({
      ...session,
      transactions: updatedTransactions,
    });
  }

  function handleConfirm() {
    confirmMutation.mutate({
      artifactUuid: session.artifactUuid,
      request: {
        transactions: session.transactions,
      },
    });
  }

  return (
    <div className="rounded-lg border p-6">
      <h2 className="mb-4 text-xl font-semibold">
        Review Extracted Transactions
      </h2>

      <div className="space-y-4">
        {session.transactions.map((
          transaction,
          index,
        ) => (
          <div
            key={index}
            className="rounded border bg-gray-50 p-4"
          >
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="text-sm font-medium text-gray-500">
                  Merchant
                </label>
                <input
                  type="text"
                  value={transaction.merchant}
                  onChange={(e) =>
                    updateTransaction(
                      index,
                      { merchant: e.target.value },
                    )
                  }
                  className="mt-1 w-full rounded border px-3 py-2"
                />
              </div>

              <div>
                <label className="text-sm font-medium text-gray-500">
                  Amount
                </label>
                <input
                  type="text"
                  value={transaction.amount}
                  onChange={(e) =>
                    updateTransaction(
                      index,
                      { amount: e.target.value },
                    )
                  }
                  className="mt-1 w-full rounded border px-3 py-2"
                />
              </div>

              <div>
                <label className="text-sm font-medium text-gray-500">
                  Category
                </label>
                <select
                  value={transaction.category}
                  onChange={(e) =>
                    updateTransaction(
                      index,
                      { category: e.target.value },
                    )
                  }
                  className="mt-1 w-full rounded border px-3 py-2"
                >
                  <option value="FOOD">Food</option>
                  <option value="SHOPPING">
                    Shopping
                  </option>
                  <option value="TRAVEL">
                    Travel
                  </option>
                  <option value="BILLS">Bills</option>
                  <option value="HEALTH">
                    Health
                  </option>
                  <option value="ENTERTAINMENT">
                    Entertainment
                  </option>
                  <option value="TRANSFER">
                    Transfer
                  </option>
                  <option value="INCOME">
                    Income
                  </option>
                  <option value="OTHER">
                    Other
                  </option>
                </select>
              </div>

              <div>
                <label className="text-sm font-medium text-gray-500">
                  Event Type
                </label>
                <select
                  value={transaction.event_type}
                  onChange={(e) =>
                    updateTransaction(
                      index,
                      { event_type: e.target.value },
                    )
                  }
                  className="mt-1 w-full rounded border px-3 py-2"
                >
                  <option value="EXPENSE">
                    Expense
                  </option>
                  <option value="INCOME">
                    Income
                  </option>
                </select>
              </div>

              <div>
                <label className="text-sm font-medium text-gray-500">
                  Date
                </label>
                <input
                  type="date"
                  value={
                    transaction.transaction_date || ""
                  }
                  onChange={(e) =>
                    updateTransaction(
                      index,
                      {
                        transaction_date:
                          e.target.value,
                      },
                    )
                  }
                  className="mt-1 w-full rounded border px-3 py-2"
                />
              </div>

              <div>
                <label className="text-sm font-medium text-gray-500">
                  Confidence
                </label>
                <p className="mt-1 font-semibold">
                  {(transaction.confidence * 100).toFixed(0)}%
                </p>
              </div>
            </div>

            <div className="mt-3">
              <label className="text-sm font-medium text-gray-500">
                Description
              </label>
              <input
                type="text"
                value={
                  transaction.description || ""
                }
                onChange={(e) =>
                  updateTransaction(
                    index,
                    {
                      description:
                        e.target.value,
                    },
                  )
                }
                className="mt-1 w-full rounded border px-3 py-2"
              />
            </div>

            <button
              onClick={() =>
                deleteTransaction(index)
              }
              className="mt-3 rounded border border-red-300 bg-red-50 px-3 py-1 text-sm text-red-700 hover:bg-red-100"
            >
              Delete Transaction
            </button>
          </div>
        ))}
      </div>

      <div className="mt-6 flex justify-end gap-3">
        <button
          onClick={() =>
            onSessionChange(null)
          }
          disabled={confirmMutation.isPending}
          className="rounded border px-4 py-2 disabled:opacity-50"
        >
          Cancel
        </button>

        <button
          onClick={handleConfirm}
          disabled={confirmMutation.isPending}
          className="rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 disabled:opacity-50"
        >
          {confirmMutation.isPending
            ? "Saving transactions..."
            : "Confirm Transactions"}
        </button>
      </div>
    </div>
  );
}
