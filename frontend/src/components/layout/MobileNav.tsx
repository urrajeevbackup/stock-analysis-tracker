import { NavLink } from 'react-router-dom'; const items=[['/','Home'],['/analysis','Analysis'],['/log-trade','Trade'],['/reports','Reports']];
export default function MobileNav(){return <nav className='md:hidden fixed bottom-0 inset-x-0 bg-white border-t grid grid-cols-4 text-xs'>{items.map(([to,l])=><NavLink key={to} to={to} className='p-3 text-center'>{l}</NavLink>)}</nav>}
