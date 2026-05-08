import type { Trade } from '../types/trade';
export const tradePnlPct=(t:Trade)=> t.exit_price?((t.trade_type==='SHORT'?t.entry_price-t.exit_price:t.exit_price-t.entry_price)/t.entry_price)*100:0;
export const isWin=(t:Trade)=> t.status==='CLOSED' && !!t.exit_price && ((t.trade_type==='SHORT'&&t.exit_price<t.entry_price)||(t.trade_type!=='SHORT'&&t.exit_price>t.entry_price));
