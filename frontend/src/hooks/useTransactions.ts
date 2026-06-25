import { useQuery } from "@tanstack/react-query";

import { financialEventsApi } from "../api/financialEvents";

export function useTransactions() {
  return useQuery({
    queryKey: ["dashboard", "transactions"],
    queryFn: financialEventsApi.getTransactions,
  });
}