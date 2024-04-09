import React from 'react';
import { useHistory } from 'react-router-dom';

function Header({ isLoggedIn, handleLogout }) {
  const history = useHistory();

  const logout = () => {
    // Remove token from sessionStorage
    sessionStorage.removeItem('token');

    // Redirect to the home page
    history.push('/');
  };

  return (
    <header>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          {isLoggedIn ? (
            <li>
              <button onClick={logout}>Logout</button>
            </li>
          ) : (
            <React.Fragment>
              <li>
                <Link to="/login">Login</Link>
              </li>
              <li>
                <Link to="/signup">Sign Up</Link>
              </li>
            </React.Fragment>
          )}
        </ul>
      </nav>
    </header>
  );
}

export default Header;
