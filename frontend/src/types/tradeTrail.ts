export interface TradeTrail{id:number;trade_id:number;old_stop_loss?:number|null;new_stop_loss?:number|null;old_target?:number|null;new_target?:number|null;notes?:string|null;created_at?:string;}
export interface CreateTradeTrailPayload{trade_id:number;new_stop_loss:number;new_target:number;notes?:string;}
