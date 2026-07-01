import { useQuery } from "@tanstack/react-query";

import { dashboardApi } from "./api";

export function useSummary() {
  return useQuery({
    queryKey: ["dashboard", "summary"],
    queryFn: dashboardApi.getSummary,
  });
}

export function useInsights() {
  return useQuery({
    queryKey: ["dashboard", "insights"],
    queryFn: dashboardApi.getInsights,
  });
}

export function useTransactions() {
  return useQuery({
    queryKey: ["dashboard", "transactions"],
    queryFn: dashboardApi.getTransactions,
  });
}

export function useTopMerchants() {
  return useQuery({
    queryKey: ["dashboard", "top-merchants"],
    queryFn: dashboardApi.getTopMerchants,
  });
}