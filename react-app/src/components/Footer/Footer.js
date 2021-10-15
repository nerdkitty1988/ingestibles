import React, { useState, useEffect } from "react";
import { NavLink } from "react-router-dom";
import "./Footer.css";

const Footer = () => {

	return (
		<footer id="footer" className="footer footer-desktop ">
      <div className="footer-row footer-row-top">
        <div className="footer-robot robot-icon robot-icon-">
          <img src="/logo.png" />
        </div>
        <div className="footer-categories">
          <span className="title">Categories</span>
          <ul className="footer-categories-links">
            <li className="beef">
              <a href="recipes/tags/beef">
                <i className="fas fa-hamburger"></i>
                 Beef
              </a>
            </li>
            <li className="chicken ">
              <a href="recipes/tags/chicken">
                <i className="fas fa-drumstick-bite"></i>
                Chicken
              </a>
            </li>
            <li className="dessert ">
              <a href="/recipes/tags/dessert">
                <i className="fas fa-ice-cream"></i>
                Dessert
              </a>
            </li>
            <li className="fish ">
              <a href="/recipes/tags/fish">
                <i className="fas fa-fish"></i>
                Fish
              </a>
            </li>
            <li className="pasta ">
              <a href="/recipes/tags/pasta">
                <i className="fas fa-utensils"></i>
                Pasta
              </a>
            </li>
            <li className="pastry ">
              <a href="/recipes/tags/pastry">
                <i className="fas fa-birthday-cake"></i>
                Pastry
              </a>
            </li>
            <li className="vegetarian ">
              <a href="recipes/tags/vegetarian">
                <i className="fas fa-carrot"></i>
                Vegetarian
              </a>
            </li>
          </ul>
        </div>
        <div className="footer-about-us">
          <span className="title">Find Us</span>
          <ul>
            <li className='group-name'>
              <span className='member-name'>Johnny Park</span>
              <span>{` | `}</span>
              <span className="groupmates">
                <a href="https://www.linkedin.com/in/johnny-park-b81857212">
                  <i className="fab fa-linkedin"></i>
                </a>
                <a href="https://github.com/gobugi">
                  <i className="fab fa-github-square"></i>
                </a>
              </span>
            </li>
            <li className='group-name'>
              <span className='member-name'>Meitong Qu</span>
              <span>{` | `}</span>
              <span className="groupmates">
                <a href="https://www.linkedin.com/in/meitongqu/">
                  <i className="fab fa-linkedin"></i>
                </a>
                <a href="https://github.com/MayUWish">
                  <i className="fab fa-github-square"></i>
                </a>
              </span>
            </li>
            <li className='group-name'>
              <span className='member-name'>Jami Travers</span>
              <span>{` | `}</span>
              <span className="groupmates">
                <a href="https://www.linkedin.com/in/jami-travers-3393711aa/">
                  <i className="fab fa-linkedin"></i>
                </a>
                <a href="https://github.com/nerdkitty1988">
                  <i className="fab fa-github-square"></i>
                </a>
              </span>
            </li>
            <li className='group-name'>
              <span className='member-name'>Darren Via II</span>
              <span>{` | `}</span>
              <span className="groupmates">
                <a className="groupmates" href="https://www.linkedin.com/in/darren-via-ii-552667159/">
                  <i className="fab fa-linkedin"></i>
                </a>
                <a className="groupmates" href="https://github.com/aivnerrad">
                  <i className="fab fa-github-square"></i>
                </a>
              </span>
            </li>

          </ul>
        </div>
      </div>
      <div className="footer-rule">
        <hr />
      </div>
      <div className="footer-row footer-row-bottom">
        <div className="footer-links">
          <p></p>
          <ul className="footer-links-list">
            <li>
              <p>Copyright 2021 © All Rights Reserved</p>
            </li>
          </ul>
          <p></p>
        </div>
      </div>
    </footer>
	);
};

export default Footer;
