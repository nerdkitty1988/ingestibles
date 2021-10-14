import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
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
        <a className="category-nav-link feed-link" rel="nofollow" href="/recipes/my_plate">Following</a>
      </span> */}
      <div id="you-menu" className="dropdown">
        <i onClick={openMenu} className="fas fa-user-circle fa-2x" data-toggle="dropdown"></i>
        {showMenu && (
          <ul id="you-menu-dropdown" className="dropdown-menu pull-right">
            <li>
              <a href={`/users/${sessionUser?.id}`} style={{textDecoration: 'none'}}>Profile</a>
            </li>
            <li>
              <a href={`/users/${sessionUser?.id}`} style={{textDecoration: 'none'}}>Inbox </a>
            </li>
            <li>
              <a href={`/recipes/my_plate`} style={{textDecoration: 'none'}}>Favorites </a>
            </li>
            <li>
              <a href={`/recipes/my_plate`} style={{textDecoration: 'none'}}>Discussions </a>
            </li>
            <li>
              <a href={`/users/${sessionUser?.id}`} style={{textDecoration: 'none'}}>Settings</a>
            </li>
            <li className="divider"></li>
            <li className="multi-link">
              <a className="published-link" href="/recipes/my_plate">
                Ingestibles
                &nbsp;<span className="badge">{`${createdRecipes?.length}`}</span>
              </a>
            </li>
            <li>
              <div className="button-actions">
                <LogoutButton />
                <a className="btn btn-yellow btn-block btn-large create-btn verification-required" href="/recipes/new_recipe">New Ingestible</a>
              </div>
            </li>
          </ul>
        )}
      </div>
    </div>
  );
}




export default ProfileButton;
