import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [initialData, setInitialData] = useState<{title?: string; body?: string }>({});
  
  useEffect(()=>{
    fetch('http://localhost:5000/home').then(
      response => response.json()
    )
    .then(data => setInitialData(data))
  }, []);
  
  return (
    <div className='App'>
      <h1>{initialData.title}</h1>
      <h2>{initialData.body}</h2>
    </div>
  )
}

export default App
