import { useState } from "react";

import { useAddTransaction } from "../../hooks";

export default function AddTransaction() {
  const [text, setText] = useState("");

  const {
    mutate,
    isPending,
    isError,
  } = useAddTransaction();

  function handleSubmit(
    e: React.FormEvent<HTMLFormElement>,
  ) {
    e.preventDefault();

    const transaction = text.trim();

    if (!transaction) {
      return;
    }

    mutate(
      {
        text: transaction,
      },
      {
        onSuccess: () => {
          setText("");
        },
      },
    );
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="rounded-lg border p-4"
    >
      <h2 className="mb-4 text-xl font-semibold">
        Add Transaction
      </h2>

      <div className="flex flex-col gap-3 md:flex-row">
        <input
          value={text}
          onChange={(e) =>
            setText(e.target.value)
          }
          placeholder="Zomato 250 dinner"
          className="flex-1 rounded border p-2"
        />

        <button
          type="submit"
          disabled={isPending}
          className="rounded bg-black px-4 py-2 text-white transition-opacity disabled:cursor-not-allowed disabled:opacity-50"
        >
          {isPending
            ? "Adding..."
            : "Add"}
        </button>
      </div>

      <p className="mt-3 text-sm text-gray-500">
        Format: Merchant Amount Description
      </p>

      <p className="text-sm text-gray-500">
        Example: Zomato 250 dinner
      </p>

      {isError && (
        <p className="mt-3 text-sm text-red-600">
          Failed to add transaction.
        </p>
      )}
    </form>
  );
}