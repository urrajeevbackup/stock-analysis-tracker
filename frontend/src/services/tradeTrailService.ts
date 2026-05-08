import api from './api';import type { CreateTradeTrailPayload, TradeTrail } from '../types/tradeTrail';
export const listTradeTrails = async(tradeId:string)=> (await api.get<TradeTrail[]>(`/trade-trails/${tradeId}`)).data;
export const createTradeTrail=async(payload:CreateTradeTrailPayload)=> (await api.post<TradeTrail>('/trade-trails', payload)).data;
