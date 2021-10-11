
import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import './NavBar.css';

const NavBar = () => {
  return (
    <header id="site-header" className="site-header">
      <div className="site-header-top">
        <div className="left-col">
          <nav className="site-header-nav site-header-primary-nav" aria-label="Categories menu">
            <ul className="category-nav-link">
              <li>
                <a href='/'>
                  <i class="fas fa-home"></i>
                </a>
              </li>
              <li>
                <a href='/beef'>Beef</a>
              </li>
              <li>
                <a href='/chicken'>Chicken</a>
              </li>
              <li>
                <a className="category-nav-link" href='/desserts'>Desserts</a>
              </li>
              <li>
                <a href='/fish'>Fish</a>
              </li>
              <li>
                <a href='/pasta'>Pasta</a>
              </li>
              <li>
                <a href='/pastries'>Pastries</a>
              </li>
              <li>
                <a href='/vegetarian'>Vegetarian</a>
              </li>
              {/* <li>
                <NavLink to='/users' exact={true} activeClassName='active'>
                  Users
                </NavLink>
              </li> */}
              <li>
                <LogoutButton />
              </li>
            </ul>
          </nav>
        </div>
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
      </div>



      <div className="site-header-bottom">
        <div className="left-col">
          <a className="site-logo " href="/">
            <img className="ingestibles-logo" alt="Ingestibles" src="/logo.png"/>
            <span id="site-header-category-brand">ingestibles</span>
            <span className="site-header-category category-"></span>
          </a>
          <a href="/recipes/" className="btn btn-category-header">Recipes</a>
          <a href="/myplate/" className="btn btn-category-header">My Plate</a>
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
            <label className="sr-only" for="site-search-input">Enter search term</label>
            <input className="input-medium site-search-input" id="site-search-input" type="text" placeholder="Let's Make..."/>
            <button className="submit-btn" type="submit">
              <i class="fas fa-search fa-sm fa-flip-horizontal"></i>
            </button>
          </form>
        </div>
      </div>
    </header>
  );
}

export default NavBar;
