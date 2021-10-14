
import React from "react";
import { useSelector } from "react-redux";
import { NavLink } from 'react-router-dom';
import ProfileButton from './ProfileButton';
import './NavBar.css';




const NavBar = ({ loaded }) => {

  const sessionUser = useSelector((state) => state.session?.user);

  let sessionLinks;
  if (sessionUser) {
    sessionLinks = (
      <ProfileButton user={sessionUser} />
    );
  } else {
    sessionLinks = (
      <div id="you-menu-container" className="right-col">
        <div id="login-menu">
            <NavLink id="login" to='/login' exact={true} activeClassName='active'>
              Log In
            </NavLink>
            <span className="pipe">|</span>
            <NavLink id="sign-up" to='/sign-up' exact={true} activeClassName='active'>
              Sign Up
            </NavLink>
        </div>
      </div>
    );
  }

  return (
    <header id="site-header" className="site-header">
      <div className="site-header-top">
        <div className="left-col">
          <nav className="site-header-nav site-header-primary-nav" aria-label="Categories menu">
            <ul className="category-nav-link">
              <li>
                <a href='/'>
                  <i className="fas fa-home"></i>
                </a>
              </li>
              <li>
                <a href='/recipes/beef'>Beef</a>
              </li>
              <li>
                <a href='/recipes/chicken'>Chicken</a>
              </li>
              <li>
                <a href='/recipes/desserts'>Desserts</a>
              </li>
              <li>
                <a href='/recipes/fish'>Fish</a>
              </li>
              <li>
                <a href='/recipes/pasta'>Pasta</a>
              </li>
              <li>
                <a href='/recipes/pastries'>Pastries</a>
              </li>
              <li>
                <a href='/recipes/vegetarian'>Vegetarian</a>
              </li>
            </ul>
          </nav>
        </div>
        {loaded && sessionLinks}
      </div>
      <div className="site-header-bottom">
        <div className="left-col">
          <a className="site-logo " href="/">
            <img className="ingestibles-logo" alt="Ingestibles" src="/logo.png"/>
            <span id="site-header-category-brand">ingestibles</span>
            <span className="site-header-category category-"></span>
          </a>
          <a href="/recipes" className="btn btn-category-header">Recipes</a>
          <a href="/recipes/my_plate" className="btn btn-category-header">My Plate</a>
        </div>
        <div className="right-col">
          <nav className="site-header-nav site-header-secondary-nav" aria-label="Contest and classes">
            <ul>
              <li>
                <a id="site-header-secondary-link" href="/recipes/new_recipe">PUBLISH</a>
              </li>
            </ul>
          </nav>
          <form id="header-search-form" className="site-search-form" title="Search Form" action="/recipes/" method="get">
            <label className="sr-only">Enter search term</label>
            <input className="input-medium site-search-input" id="site-search-input" type="text" placeholder="Let's Make..."/>
            <button className="submit-btn" type="submit">
              <i className="fas fa-search fa-sm fa-flip-horizontal"></i>
            </button>
          </form>
        </div>
      </div>
    </header>
  );
}

export default NavBar;
