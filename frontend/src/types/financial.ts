export interface Summary {
  period: {
    start_date: string;
    end_date: string;
  };
  total_income: string;
  total_expense: string;
  net_flow: string;
}

export interface TopMerchant {
  merchant: string;
  total_amount: string;
}

export interface Insights {
  insights: string[];
}

export interface FinancialEvent {
  uuid: string;
  merchant: string;
  amount: string;
  currency: string;
  event_type: string;
  description: string;
  transaction_date: string;
}