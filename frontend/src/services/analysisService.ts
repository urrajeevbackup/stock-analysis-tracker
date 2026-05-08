import api, { unwrapList } from './api';
import type { Analysis, CreateAnalysisPayload } from '../types/analysis';

export const listAnalysis = async () => {
  const response = await api.get('/analysis');
  return unwrapList<Analysis>(response.data);
};

export const createAnalysis = async (payload: CreateAnalysisPayload) => (await api.post<Analysis>('/analysis', payload)).data;
