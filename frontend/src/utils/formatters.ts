export const fMoney=(n?:number|null)=> n==null?'-':`₹${n.toFixed(2)}`; export const fPct=(n:number)=>`${n.toFixed(2)}%`; export const fDate=(d?:string|null)=> d?new Date(d).toLocaleDateString():'-';
