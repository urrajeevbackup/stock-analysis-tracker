export type TradeType='LONG'|'SHORT'|'OPTIONS';export type TradeStatus='OPEN'|'CLOSED';
export interface Trade{id:number;stock_symbol:string;trade_type:TradeType;entry_price:number;entry_date:string;exit_price?:number|null;exit_date?:string|null;stop_loss:number;target_price:number;status:TradeStatus;notes?:string|null;created_at?:string;}
export type CreateTradePayload=Omit<Trade,'id'|'created_at'>;
