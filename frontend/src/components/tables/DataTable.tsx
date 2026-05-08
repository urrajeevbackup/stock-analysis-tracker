export default function DataTable({ headers, rows }: { headers: string[]; rows: (string | number)[][] }) {
  return <div className="overflow-x-auto rounded-xl border bg-white"><table className="min-w-full text-sm"><thead><tr>{headers.map(h => <th key={h} className="p-3 text-left">{h}</th>)}</tr></thead><tbody>{rows.length===0?<tr><td className="p-4 text-slate-500" colSpan={headers.length}>No data available.</td></tr>:rows.map((r,i)=><tr key={i} className="border-t">{r.map((c,j)=><td key={j} className="p-3">{c}</td>)}</tr>)}</tbody></table></div>;
}
