import { NavLink } from 'react-router-dom';

const items = [['/', 'Home', '🏠'], ['/analysis', 'Analysis', '📈'], ['/log-trade', 'Trade', '📝'], ['/reports', 'Reports', '📊']];

export default function MobileNav() {
  return <nav className="fixed bottom-0 inset-x-0 z-20 grid grid-cols-4 border-t bg-white md:hidden">{items.map(([to, label, icon]) => <NavLink key={to} to={to} className={({ isActive }) => `p-2 text-center text-xs ${isActive ? 'text-indigo-600' : 'text-slate-500'}`}><div>{icon}</div><div>{label}</div></NavLink>)}</nav>;
}
