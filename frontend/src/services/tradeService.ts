import api from './api';import type { CreateTradePayload, Trade } from '../types/trade';
export const listTrades = async()=> (await api.get<Trade[]>('/trades')).data;
export const getTrade = async(id:string)=> (await api.get<Trade>(`/trades/${id}`)).data;
export const createTrade = async(payload:CreateTradePayload)=> (await api.post<Trade>('/trades', payload)).data;
