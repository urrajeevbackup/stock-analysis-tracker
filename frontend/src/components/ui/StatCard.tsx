export default function StatCard({ title, value }: { title: string; value: string | number }) {
  return <div className="rounded-xl bg-white p-4 shadow-sm border"><p className="text-sm text-slate-500">{title}</p><p className="text-2xl font-semibold">{value}</p></div>;
}
