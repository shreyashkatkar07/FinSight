import { useQuery } from "@tanstack/react-query";

import { financialEventsApi } from "../api/financialEvents";

export function useInsights() {
  return useQuery({
    queryKey: ["dashboard", "insights"],
    queryFn: financialEventsApi.getInsights,
  });
}