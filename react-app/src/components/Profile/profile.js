import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { NavLink, useHistory } from "react-router-dom";
import { updateUser, deleteUser } from "../../store/session";
import "./profile.css";

function Profile() {
	const dispatch = useDispatch();
	const history = useHistory();
	const sessionUser = useSelector((state) => state.session.user);

	const [user, setUser] = useState(sessionUser);
	const [username, setUsername] = useState(user?.username);
	const [email, setEmail] = useState(user?.email);
	const [password, setPassword] = useState("");
	const [repeatPassword, setRepeatPassword] = useState("");
	const [biography, setBiography] = useState(user?.biography);
	const [profilePic, setProfilePic] = useState(user?.profilePic);
	const [errors, setErrors] = useState([]);
	const [usernameShow, setUsernameShow] = useState(true);
	const [emailShow, setEmailShow] = useState(true);
	const [passwordShow, setPasswordShow] = useState(true);
	const [biographyShow, setBiographyShow] = useState(true);
	const [profilePicShow, setProfilePicShow] = useState(true);

	const handleSave = async (e) => {
		e.preventDefault();
		let updatedUser;
		if (password === repeatPassword && password) {
			updatedUser = {
				id: sessionUser.id,
				username: username,
				email: email,
				biography: biography,
				profilePic: profilePic,
				password: password,
			};
		} else {
			updatedUser = {
				id: sessionUser.id,
				username: username,
				email: email,
				biography: biography,
				profilePic: profilePic,
			};
		}

		const data = await dispatch(updateUser(updatedUser));
		if (data.errors) {
			return data.errors;
		} else {
			setUsernameShow(true);
			setProfilePicShow(true);
			setEmailShow(true);
			setBiographyShow(true);
			history.push(`/users/${data.id}`);
		}
	};

    const handleDelete = async (e) => {
        e.preventDefault();
        const userId = sessionUser.id
        await dispatch(deleteUser(userId));
    }

	useEffect(() => {
		async function fetchData() {
			const response = await fetch(`/api/users/${sessionUser.id}`);
			const responseData = await response.json();
			setUser(responseData);
		}
		fetchData();
	}, []);

	if (!sessionUser) return null;

	return (
		<div className="profileBox">
			<form>
				<div>
					{errors.map((error, ind) => (
						<div key={ind}>{error}</div>
					))}
				</div>
				<div className="profileData">
					<img
						hidden={!profilePicShow}
						id="profPic"
						src={profilePic}
					/>
					<button
						type="button"
						onClick={(e) => setProfilePicShow(false)}
						hidden={!profilePicShow}
                        className="editButtons"
					>
						Edit Profile Picture
					</button>
					<input
						hidden={profilePicShow}
						className="editProfInput"
						type="url"
						defaultValue={profilePic}
						onChange={(e) => setProfilePic(e.target.value)}
					/>
					<button
						type="button"
						onClick={(e) => handleSave(e)}
						hidden={profilePicShow}
                        className="saveButton"
					>
						Save
					</button>
					<button
						type="button"
						onClick={(e) => setProfilePicShow(true)}
						hidden={profilePicShow}
                        className="cancelButton"
					>
						Cancel
					</button>
				</div>
				<div className="profileData">
					<p hidden={!usernameShow} id="profUsername">
						Username: {username}
					</p>
					<button
						type="button"
						onClick={(e) => setUsernameShow(false)}
						hidden={!usernameShow}
                        className="editButtons"
					>
						Edit Username
					</button>
					<input
						hidden={usernameShow}
						className="editProfInput"
						type="text"
						defaultValue={username}
						onChange={(e) => setUsername(e.target.value)}
					/>
					<button
						type="button"
						onClick={(e) => handleSave(e)}
						hidden={usernameShow}
                        className="saveButton"
					>
						Save
					</button>
					<button
						type="button"
						onClick={(e) => setUsernameShow(true)}
						hidden={usernameShow}
                        className="cancelButton"
					>
						Cancel
					</button>
				</div>
				<div className="profileData">
					<p hidden={!emailShow} id="profEmail">
						Email: {email}
					</p>
					<button
						type="button"
						onClick={(e) => setEmailShow(false)}
						hidden={!emailShow}
                        className="editButtons"
					>
						Edit Email
					</button>
					<input
						hidden={emailShow}
						className="editProfInput"
						type="email"
						defaultValue={email}
						onChange={(e) => setEmail(e.target.value)}
					/>
					<button
						type="button"
						onClick={(e) => handleSave(e)}
						hidden={emailShow}
                        className="saveButton"
					>
						Save
					</button>
					<button
						type="button"
						onClick={(e) => setEmailShow(true)}
						hidden={emailShow}
                        className="cancelButton"
					>
						Cancel
					</button>
				</div>
				<div className="profileData">
					<p hidden={!biographyShow} id="profBiography">
						Bio: {biography}
					</p>
					<button
						type="button"
						onClick={(e) => setBiographyShow(false)}
						hidden={!biographyShow}
                        className="editButtons"
					>
						Edit Biography
					</button>
					<textarea
						hidden={biographyShow}
						className="editProfBio"
						type="text"
						defaultValue={biography}
						onChange={(e) => setBiography(e.target.value)}
					/>
					<button
						type="button"
						onClick={(e) => handleSave(e)}
						hidden={biographyShow}
                        className="saveButton"
					>
						Save
					</button>
					<button
						type="button"
						onClick={(e) => setBiographyShow(true)}
						hidden={biographyShow}
                        className="cancelButton"
					>
						Cancel
					</button>
				</div>
				<div className="passwordButtons">
					<button
						type="button"
						onClick={(e) => setPasswordShow(false)}
						hidden={!passwordShow}
                        className="editButtons"
					>
						Edit Password
					</button>
					<input
						hidden={passwordShow}
						className="editProfInput"
						type="password"
						defaultValue={password}
                        placeholder="Password"
						onChange={(e) => setPassword(e.target.value)}
					/>
					<input
						hidden={passwordShow}
						className="editProfInput"
						type="password"
						defaultValue={repeatPassword}
                        placeholder="Re-enter Password"
						onChange={(e) => setRepeatPassword(e.target.value)}
					/>
					<button
						type="button"
						onClick={(e) => handleSave(e)}
						hidden={passwordShow}
                        className="saveButton"
					>
						Save
					</button>
					<button
						type="button"
						onClick={() => setPasswordShow(true)}
						hidden={passwordShow}
                        className="cancelButton"
					>
						Cancel
					</button>
				</div>
                <button type="button" className="deleteAccount" onClick={(e) => {handleDelete(e)}}>Delete Account</button>
			</form>
		</div>
	);
}

export default Profile;
