export type BuyDecision='BUY'|'WAIT'|'AVOID';
export interface Analysis{id:number;stock_symbol:string;stock_price:number;risk_price:number;reward_price:number;buy_decision:BuyDecision;notes?:string|null;created_at?:string;}
export type CreateAnalysisPayload=Omit<Analysis,'id'|'created_at'>;
