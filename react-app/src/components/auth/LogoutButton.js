import React from 'react';
import { useDispatch } from 'react-redux';
import { logout } from '../../store/session';
import '../NavBar/NavBar.css';

const LogoutButton = () => {
  const dispatch = useDispatch()
  const onLogout = async (e) => {
    await dispatch(logout());
    window.location.href = "/";
  };

  return <button className="btn btn-default btn-logout" onClick={onLogout}>Logout</button>;
};

export default LogoutButton;
