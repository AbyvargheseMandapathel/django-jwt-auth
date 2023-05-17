import React, { useState } from 'react';
import axios from 'axios';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();

    // Make API request to login endpoint
    axios.post('/api/auth/login/', { username, password })
      .then(response => {
        // Store token in local storage or state (depending on your preference)
        const token = response.data.token;
        // Handle successful login (e.g., redirect to home page)
        // Replace '/home' with the actual URL of your home page route
        window.location.href = '/home';
      })
      .catch(error => {
        console.error(error);
        // Handle login error (e.g., display error message)
      });
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Username:
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
        </label>
        <br />
        <label>
          Password:
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </label>
        <br />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;
