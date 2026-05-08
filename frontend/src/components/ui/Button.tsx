import type { ButtonHTMLAttributes } from 'react';
export default function Button({className='',...p}:ButtonHTMLAttributes<HTMLButtonElement>){return <button {...p} className={`rounded-lg px-4 py-2 bg-slate-900 text-white disabled:opacity-50 ${className}`}/>}
