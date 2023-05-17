import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Home = () => {
  const [username, setUsername] = useState('');
  const [token, setToken] = useState('');

  useEffect(() => {
    // Make API request to fetch user data
    axios.get('/api/auth/home/')  // Replace '/api/auth/home/' with the actual URL of your home page endpoint
      .then(response => {
        console.log(response.data); // Log the response data to the console
        setUsername(response.data.username);
        setToken(response.data.token);
      })
      .catch(error => {
        console.error(error);
        // Handle error
      });
  }, []);

  const handleLogout = () => {
    // Make API request to logout endpoint
    axios.post('/api/auth/logout/')  // Replace '/api/auth/logout/' with the actual URL of your logout endpoint
      .then(response => {
        // Handle successful logout (e.g., redirect to login page)
        // Replace '/login' with the actual URL of your login page route
        window.location.href = '/login';
      })
      .catch(error => {
        console.error(error);
        // Handle error
      });
  };

  return (
    <div>
      <h2>Welcome, { username }!!</h2>
      <p>Token: {token}</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default Home;
