import { useQuery } from "@tanstack/react-query";

import { financialEventsApi } from "../api/financialEvents";

export function useTopMerchants() {
  return useQuery({
    queryKey: ["dashboard", "top-merchants"],
    queryFn: financialEventsApi.getTopMerchants,
  });
}