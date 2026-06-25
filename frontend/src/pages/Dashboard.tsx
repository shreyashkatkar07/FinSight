import AddTransaction from "../components/dashboard/AddTransaction";
import SummaryCards from "../components/dashboard/SummaryCards";
import TopMerchants from "../components/dashboard/TopMerchants";
import Insights from "../components/dashboard/Insights";
import RecentTransactions from "../components/dashboard/RecentTransactions";

export default function Dashboard() {
  return (
    <div className="mx-auto max-w-5xl px-4 py-6">
      <h1 className="mb-8 text-3xl font-bold">
        PFIS
      </h1>

      <AddTransaction />

      <div className="mt-8">
        <SummaryCards />
      </div>

      <div className="mt-8">
        <TopMerchants />
      </div>

      <div className="mt-8">
        <Insights />
      </div>

      <div className="mt-8">
        <RecentTransactions />
      </div>
    </div>
  );
}