import React, { useEffect } from 'react';
import { Route, Redirect } from 'react-router-dom';

const PrivateRoute = ({ component: Component, ...rest }) => {
  useEffect(() => {
    const token = sessionStorage.getItem('token');
    if (!token) {
      // Redirect to login if token is not present
      window.location.href = '/login';
    }
  }, []);

  return (
    <Route
      {...rest}
      render={(props) =>
        sessionStorage.getItem('token') ? (
          <Component {...props} />
        ) : (
          <Redirect to="/login" />
        )
      }
    />
  );
};

export default PrivateRoute;
