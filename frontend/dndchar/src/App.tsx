import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'
import Home from './components/Home'
import About from './components/About';
import SpellPickerForm from './components/SpellPicker';

function App() {
  
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} /> 
        <Route path="/spell-picker" element={<SpellPickerForm />} /> 
      </Routes>
    </Router>
  )
}

export default App
