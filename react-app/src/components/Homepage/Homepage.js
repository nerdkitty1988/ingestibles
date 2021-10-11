
import React from 'react';
import { NavLink } from 'react-router-dom';
import './Homepage.css';

const Homepage = () => {
  return (
    <main>
      <div id="home-container" class="home-wrapper-wrapper full-wrapper home-content clearfix">
        <div id="site-announcements-page" class="site-announcements-page">
          <div class="site-announcements-page-content"></div>
        </div>
        <div id="home-content-rotator" class="home-content-rotator carousel carousel-fade">
          <div class="home-content-rotator-inner carousel-inner">
            <div className="home-content-rotator-slide item home-content-rotator-slide-align-middle" data-link="https://www.instructables.com/halloween/" style={{backgroundImage: 'url(https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2340&q=80)'}}><div className="home-content-rotator-slide-overlay" /><div className="home-content-rotator-slide-wrap"><div className="home-content-adspot-wrap"><div className="home-content-adspot-text"><h1>YOURS FOR THE MAKING</h1><p>Instructables is a community for people who like to make things. Come explore, share, and make your next project with us!</p></div></div></div></div>

            <div className="home-content-rotator-slide item  home-content-rotator-slide-align-middle" data-link="https://www.instructables.com/halloween/" style={{backgroundImage: 'url(https://content.instructables.com/ORIG/F0N/PIUP/KU8DPHZR/F0NPIUPKU8DPHZR.jpg?auto=webp&width=1600)'}}><div className="home-content-rotator-slide-overlay" /><div className="home-content-rotator-slide-wrap"><div className="home-content-adspot-wrap"><div className="home-content-adspot-text"><h1>YOURS FOR THE MAKING</h1><p>Instructables is a community for people who like to make things. Come explore, share, and make your next project with us!</p></div></div></div></div>

            <div className="home-content-rotator-slide item  home-content-rotator-slide-align-middle" data-link="https://www.instructables.com/halloween/" style={{backgroundImage: 'url(https://content.instructables.com/ORIG/FVC/7NPF/KU8DPF4T/FVC7NPFKU8DPF4T.jpg?auto=webp&width=1600)'}}><div className="home-content-rotator-slide-overlay" /><div className="home-content-rotator-slide-wrap"><div className="home-content-adspot-wrap"><div className="home-content-adspot-text"><h1>YOURS FOR THE MAKING</h1><p>Instructables is a community for people who like to make things. Come explore, share, and make your next project with us!</p></div></div></div></div>

            <div className="home-content-rotator-slide item  home-content-rotator-slide-align-middle" data-link="https://www.instructables.com/halloween/" style={{backgroundImage: 'url(https://content.instructables.com/ORIG/FIM/ZL4H/KU8DPG87/FIMZL4HKU8DPG87.jpg?auto=webp&width=1600)'}}><div className="home-content-rotator-slide-overlay" /><div className="home-content-rotator-slide-wrap"><div className="home-content-adspot-wrap"><div className="home-content-adspot-text"><h1>YOURS FOR THE MAKING</h1><p>Instructables is a community for people who like to make things. Come explore, share, and make your next project with us!</p></div></div></div></div>

            <div className="home-content-rotator-slide item  home-content-rotator-slide-align-middle" data-link="https://www.instructables.com/halloween/" style={{backgroundImage: 'url(https://cdn.instructables.com/ORIG/FOR/XNE5/K0MP5D8J/FORXNE5K0MP5D8J.jpg?auto=webp&width=1600)'}}><div className="home-content-rotator-slide-overlay" /><div className="home-content-rotator-slide-wrap"><div className="home-content-adspot-wrap"><div className="home-content-adspot-text"><h1>YOURS FOR THE MAKING</h1><p>Instructables is a community for people who like to make things. Come explore, share, and make your next project with us!</p></div></div></div></div>

            <div className="home-content-rotator-slide item  home-content-rotator-slide-align-middle active" data-link="https://www.instructables.com/halloween/" style={{backgroundImage: 'url(https://images.unsplash.com/photo-1540432797114-187727adf19b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2274&q=80'}}><div className="home-content-rotator-slide-overlay" /><div className="home-content-rotator-slide-wrap"><div className="home-content-adspot-wrap"><div className="home-content-adspot-text"><h1>YOURS FOR THE MAKING</h1><p>Instructables is a community for people who like to make things. Come explore, share, and make your next project with us!</p></div></div></div></div>

          </div>
            <div class="home-content-rotator-indicator-wrap">
              <ol class="home-content-rotator-indicator carousel-indicators">
                <li data-target="#home-content-rotator" data-slide-to="0" class=""></li>
                <li data-target="#home-content-rotator" data-slide-to="1" class=""></li>
                <li data-target="#home-content-rotator" data-slide-to="2" class=""></li>
                <li data-target="#home-content-rotator" data-slide-to="3" class=""></li>
                <li data-target="#home-content-rotator" data-slide-to="4" class=""></li>
                <li data-target="#home-content-rotator" data-slide-to="5" class=""></li>
              </ol>
            </div>
          </div>
        <div class="home-content-text">
          <div class="home-content-text-wrap">
            <div class="home-content-text-box">
              <h2>Step-by-step</h2>
              <p>
                We make it easy to learn how to make anything, one step at a time. From the stovetop to the workshop, you are sure to be inspired by the awesome projects that are shared everyday.
              </p>
            </div>
            <div class="home-content-text-box">
              <h2>Made By You</h2>
              <p>
                Instructables are created by you. No matter who you are, we all have secret skills to share. Come join our community of curious makers, innovators, teachers, and life long learners who love to share what they make.
              </p>
            </div>
            <div class="home-content-text-box">
              <h2>A Happy Place</h2>
              <p>
                Making things makes people happy. We can't prove it, but we know it to be true. Find your happy place, and join one of the friendliest online communities anywhere.
              </p>
            </div>
          </div>
        </div>
        <hr />
      </div>
    </main>

  );
}

export default Homepage;
