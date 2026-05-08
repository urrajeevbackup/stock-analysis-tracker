import StatCard from '../components/ui/StatCard';
import DataTable from '../components/tables/DataTable';
export default function Dashboard(){return <section className='space-y-4'><h1 className='text-2xl font-semibold'>Dashboard</h1><div className='grid grid-cols-2 md:grid-cols-5 gap-3'><StatCard title='Total Trades' value='0'/><StatCard title='Open Trades' value='0'/><StatCard title='Strike Rate' value='0%'/><StatCard title='Average Reward %' value='0%'/><StatCard title='Average Risk %' value='0%'/></div><DataTable headers={['Symbol','Type','Status','Entry']} rows={[]}/></section>}
