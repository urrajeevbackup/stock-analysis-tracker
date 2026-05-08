import api, { unwrapList } from './api';
import type { CreateTradePayload, Trade } from '../types/trade';

export const listTrades = async () => {
  const response = await api.get('/trades');
  return unwrapList<Trade>(response.data);
};
export const getTrade = async (id: string) => (await api.get<Trade>(`/trades/${id}`)).data;
export const createTrade = async (payload: CreateTradePayload) => (await api.post<Trade>('/trades', payload)).data;
