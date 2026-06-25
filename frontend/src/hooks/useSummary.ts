import { useQuery } from "@tanstack/react-query";

import { financialEventsApi } from "../api/financialEvents";

export function useSummary() {
  return useQuery({
    queryKey: ["dashboard", "summary"],
    queryFn: financialEventsApi.getSummary,
  });
}