import api from './api';import type { Analysis, CreateAnalysisPayload } from '../types/analysis';
export const listAnalysis=async()=> (await api.get<Analysis[]>('/analysis')).data;
export const createAnalysis=async(payload:CreateAnalysisPayload)=> (await api.post<Analysis>('/analysis', payload)).data;
