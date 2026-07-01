import { get } from "../../api/client";

import type {
    Summary,
    TopMerchant,
    Insights,
    FinancialEvent,
} from "./types";

export const dashboardApi = {

    getSummary() {
        return get<Summary>(
            "/financial-events/summary",
        );
    },

    getTopMerchants() {
        return get<TopMerchant[]>(
            "/financial-events/top-merchants",
        );
    },

    getInsights() {
        return get<Insights>(
            "/financial-events/insights",
        );
    },

    getTransactions() {
        return get<FinancialEvent[]>(
            "/financial-events",
        );
    },

};