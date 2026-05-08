import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { listTrades } from '../services/tradeService';
import type { Trade } from '../types/trade';
import { isWin } from '../utils/calculations';

const Stat = ({ title, value, sub }: { title: string; value: string | number; sub: string }) => <div className="rounded-2xl border border-slate-200 bg-white p-4 shadow-sm"><p className="text-xs text-slate-500">{title}</p><p className="mt-1 text-2xl font-semibold">{value}</p><p className="text-xs text-emerald-600">{sub}</p></div>;

export default function Dashboard() {
  const [trades, setTrades] = useState<Trade[]>([]); const [loading, setLoading] = useState(true);
  useEffect(() => { listTrades().then(setTrades).catch(console.error).finally(() => setLoading(false)); }, []);
  const closed = trades.filter((t) => t.status === 'CLOSED');
  const wins = closed.filter(isWin).length;
  return <section className="space-y-6"><div><h1 className="text-2xl font-semibold">Dashboard</h1><p className="text-sm text-slate-500">Professional overview of trading performance.</p></div>
  <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-5">
    <Stat title="Total Trades" value={trades.length} sub="All records" />
    <Stat title="Open Trades" value={trades.filter((t) => t.status === 'OPEN').length} sub="Active positions" />
    <Stat title="Strike Rate" value={`${closed.length ? ((wins / closed.length) * 100).toFixed(1) : 0}%`} sub="Closed trades" />
    <Stat title="Avg Reward %" value="--" sub="Coming soon" />
    <Stat title="Avg Risk %" value="--" sub="Coming soon" />
  </div>
  <div className="flex flex-wrap gap-2">{[['/analysis','New Analysis'],['/log-trade','Log Trade'],['/reports','Reports']].map(([to,label])=><Link key={to} to={to} className="rounded-xl bg-indigo-600 px-4 py-2 text-sm text-white hover:bg-indigo-700">{label}</Link>)}</div>
  <div className="rounded-2xl border bg-white p-4 shadow-sm"><h2 className="mb-3 font-semibold">Recent Trades</h2>{loading ? <div className='h-32 animate-pulse rounded bg-slate-100' /> : <div className="overflow-auto"><table className="min-w-full text-sm"><thead><tr className="text-left text-slate-500"><th>Stock</th><th>Status</th><th>Type</th></tr></thead><tbody>{trades.slice(0,8).map(t=><tr key={t.id} className="border-t"><td className="py-2">{t.stock_symbol}</td><td>{t.status}</td><td>{t.trade_type}</td></tr>)}</tbody></table>{trades.length===0 && <div className='py-8 text-center text-slate-500'>No trades yet. Start by logging a trade.</div>}</div>}</div></section>;
}
