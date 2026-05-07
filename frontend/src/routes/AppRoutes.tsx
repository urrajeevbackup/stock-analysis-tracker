import { Link, Route, Routes } from 'react-router-dom';
import Dashboard from '../pages/Dashboard';
import Analysis from '../pages/Analysis';
import LogTrade from '../pages/LogTrade';
import TradeDetail from '../pages/TradeDetail';
import LiveMonitor from '../pages/LiveMonitor';
import AlertCentre from '../pages/AlertCentre';
import Reports from '../pages/Reports';

const navItems = [
  ['/', 'Dashboard'],
  ['/analysis', 'Analysis'],
  ['/log-trade', 'Log Trade'],
  ['/trade-detail', 'Trade Detail'],
  ['/live-monitor', 'Live Monitor'],
  ['/alert-centre', 'Alert Centre'],
  ['/reports', 'Reports'],
] as const;

const Layout = ({ children }: { children: React.ReactNode }) => (
  <div className="min-h-screen bg-slate-50 text-slate-900">
    <header className="border-b bg-white">
      <nav className="mx-auto flex max-w-7xl flex-wrap gap-3 p-4">
        {navItems.map(([to, label]) => (
          <Link key={to} to={to} className="rounded-md px-3 py-2 text-sm font-medium hover:bg-slate-100">
            {label}
          </Link>
        ))}
      </nav>
    </header>
    <main className="mx-auto max-w-7xl p-6">{children}</main>
  </div>
);

export default function AppRoutes() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/analysis" element={<Analysis />} />
        <Route path="/log-trade" element={<LogTrade />} />
        <Route path="/trade-detail" element={<TradeDetail />} />
        <Route path="/live-monitor" element={<LiveMonitor />} />
        <Route path="/alert-centre" element={<AlertCentre />} />
        <Route path="/reports" element={<Reports />} />
      </Routes>
    </Layout>
  );
}
