import { useState } from 'react';
import HomePage from './pages/HomePage';
import MainLayout from './layouts/MainLayout/MainLayout';

function App() {
  return (
    <MainLayout>
      <HomePage />
    </MainLayout>
  );
}

export default App;

