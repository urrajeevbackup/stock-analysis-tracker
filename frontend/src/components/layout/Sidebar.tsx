import { NavLink } from 'react-router-dom';

const items = [
  ['/', 'Dashboard', '🏠'],
  ['/analysis', 'Analysis', '📈'],
  ['/log-trade', 'Log Trade', '📝'],
  ['/live-monitor', 'Live Monitor', '🛰️'],
  ['/alert-centre', 'Alert Centre', '🔔'],
  ['/reports', 'Reports', '📊'],
];

export default function Sidebar() {
  return (
    <aside className="hidden md:flex fixed left-0 top-0 h-screen w-64 flex-col border-r border-slate-200 bg-white p-4">
      <h1 className="px-3 text-lg font-bold text-indigo-600">Stock Tracker</h1>
      <nav className="mt-6 space-y-1">
        {items.map(([to, label, icon]) => (
          <NavLink key={to} to={to} className={({ isActive }) => `flex items-center gap-3 rounded-xl px-3 py-2 text-sm ${isActive ? 'bg-indigo-50 text-indigo-700' : 'text-slate-600 hover:bg-slate-100'}`}>
            <span>{icon}</span><span>{label}</span>
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}
