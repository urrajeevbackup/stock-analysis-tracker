import { Route, Routes } from 'react-router-dom';
import AppLayout from '../components/layout/AppLayout';
import Dashboard from '../pages/Dashboard';
import Analysis from '../pages/Analysis';
import LogTrade from '../pages/LogTrade';
import TradeDetail from '../pages/TradeDetail';
import LiveMonitor from '../pages/LiveMonitor';
import AlertCentre from '../pages/AlertCentre';
import Reports from '../pages/Reports';

export default function AppRoutes() {
  return <AppLayout><Routes><Route path='/' element={<Dashboard/>}/><Route path='/analysis' element={<Analysis/>}/><Route path='/log-trade' element={<LogTrade/>}/><Route path='/trade-detail' element={<TradeDetail/>}/><Route path='/live-monitor' element={<LiveMonitor/>}/><Route path='/alert-centre' element={<AlertCentre/>}/><Route path='/reports' element={<Reports/>}/></Routes></AppLayout>;
}
