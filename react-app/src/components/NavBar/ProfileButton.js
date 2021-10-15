import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import LogoutButton from '../auth/LogoutButton';

function ProfileButton() {
  const [showMenu, setShowMenu] = useState(false);

  const [createdRecipes, setCreatedRecipes] = useState([]);

  const sessionUser = useSelector((state) => state.session?.user);
  const userId = sessionUser?.id;

  useEffect(() => {
		async function fetchData() {
			const response = await fetch(`/api/recipes/my_plate/${userId}`);
			const responseData = await response.json();
			setCreatedRecipes(responseData.created);
		}
		fetchData();
	}, [userId]);

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = () => {
      setShowMenu(false);
    };

    document.addEventListener('click', closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);


  return (
    <div id="you-menu-container" className="right-col">
      {/* <span className="site-header-nav-feed-link" >
        <NavLink className="category-nav-link feed-link" rel="nofollow" to="/recipes/my_plate">Following</NavLink>
      </span> */}
      <div id="you-menu" className="dropdown">
        <i onClick={openMenu} className="fas fa-user-circle fa-2x" data-toggle="dropdown"></i>
        {showMenu && (
          <ul id="you-menu-dropdown" className="dropdown-menu pull-right">
            <li>
              <NavLink to={`/users/${sessionUser?.id}`} style={{textDecoration: 'none'}}>Profile</NavLink>
            </li>
            <li>
              <NavLink to={`/recipes`} style={{textDecoration: 'none'}}>All Recipes </NavLink>
            </li>
            <li>
              <NavLink to={`/recipes/my_plate`} style={{textDecoration: 'none'}}>Favorites </NavLink>
            </li>
            <li className="divider"></li>
            <li className="multi-link">
              <NavLink className="published-link" to="/recipes/my_plate">
                Ingestibles
                &nbsp;<span className="badge">{`${createdRecipes?.length}`}</span>
              </NavLink>
            </li>
            <li>
              <div className="button-actions">
                <LogoutButton />
                <NavLink className="btn btn-yellow btn-block btn-large create-btn verification-required" to="/recipes/new_recipe">New Ingestible</NavLink>
              </div>
            </li>
          </ul>
        )}
      </div>
    </div>
  );
}




export default ProfileButton;
