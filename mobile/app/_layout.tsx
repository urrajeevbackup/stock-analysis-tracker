import { Tabs } from 'expo-router';

export default function RootLayout() {
  return (
    <Tabs>
      <Tabs.Screen name="index" options={{ title: 'Dashboard' }} />
      <Tabs.Screen name="analysis" options={{ title: 'Analysis' }} />
      <Tabs.Screen name="log-trade" options={{ title: 'Trade Log' }} />
      <Tabs.Screen name="reports" options={{ title: 'Reports' }} />
    </Tabs>
  );
}
