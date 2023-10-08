import React from 'react';  
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';  
import HomePage from './components/HomePage';  
import AboutPage from './components/AboutPage';  
import ContactPage from './components/ContactPage';  
import LoginPage from './components/LoginPage';
  
function App() {  
  return (  
    <Router>  
      <nav className="navbar navbar-expand-lg navbar-light bg-light">  
        <div className="container-fluid">  
          <Link className="navbar-brand" to="/">My Website</Link>  
          <div className="collapse navbar-collapse">  
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">  
              <li className="nav-item">  
                <Link className="nav-link" to="/">Home</Link>  
              </li>  
              <li className="nav-item">  
                <Link className="nav-link" to="/about">About</Link>  
              </li>  
              <li className="nav-item">  
                <Link className="nav-link" to="/contact">Contact</Link>  
              </li>  
              <li className="nav-item">  
                <Link className="nav-link" to="/login">Login</Link> {/* Add link to LoginPage */}  
              </li>  
            </ul>  
          </div>  
        </div>  
      </nav>  
      <Routes>  
        <Route path="/" element={<HomePage />} />  
        <Route path="/about" element={<AboutPage />} />  
        <Route path="/contact" element={<ContactPage />} />  
        <Route path="/login" element={<LoginPage />} /> {/* Add route for LoginPage */}  
      </Routes>  
    </Router>  
  );  
}  
  
export default App;  
