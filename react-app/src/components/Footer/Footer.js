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
          <div id="quote1" className="title">"No one is born a great cook,</div>
          <div id="quote2" className="title">One learns by doing."</div>
          <p id="julia">- Julia Child</p>
        </div>
        <div className="footer-find-us">
          <span className="title">Find Us</span>
          <ul>

            <li className='group-name'>
              <span>{`Johnny Park`}</span>
              <span>{` | `}</span>
              <a href="https://www.linkedin.com/in/johnny-park-b81857212">
                <i className="fab fa-linkedin"></i>
              </a>
              <a href="https://github.com/gobugi">
                <i className="fab fa-github-square"></i>
              </a>
            </li>

            <li className='group-name'>
              <span>{`Meitong Qu `}</span>
              &nbsp;
              <span>{`| `}</span>
              <a href="https://www.linkedin.com/in/meitongqu/">
                <i className="fab fa-linkedin"></i>
              </a>
              <a href="https://github.com/MayUWish">
                <i className="fab fa-github-square"></i>
              </a>
            </li>

            <li className='group-name'>
              <span>{`Jami Travers | `}</span>
              <a href="https://www.linkedin.com/in/jami-travers-3393711aa/">
                <i className="fab fa-linkedin"></i>
              </a>
              <a href="https://github.com/nerdkitty1988">
                <i className="fab fa-github-square"></i>
              </a>
            </li>

            <li className='group-name'>
              <span>{`Darren Via II | `}</span>
              <a href="https://www.linkedin.com/in/darren-via-ii-552667159/">
                <i className="fab fa-linkedin"></i>
              </a>
              <a href="https://github.com/aivnerrad">
                <i className="fab fa-github-square"></i>
              </a>
            </li>

          </ul>
        </div>
      </div>
      <div className="footer-rule">
        <hr />
      </div>
      <div className="footer-row footer-row-bottom">
        <p>Copyright 2021 © All Rights Reserved</p>
      </div>
    </footer>
	);
};

export default Footer;
