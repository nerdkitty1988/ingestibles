import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { NavLink, useHistory } from "react-router-dom";
import { updateUser } from "../../store/session";

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

	useEffect(() => {
		async function fetchData() {
			const response = await fetch(`/api/users/${sessionUser.id}`);
			const responseData = await response.json();
			setUser(responseData);
		}
		fetchData();
	}, []);

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
		}else{
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
			history.push(`/users/${data.id}`);
		}
	};

	if (!sessionUser) return null;

	return (
		<form>
			<div>
				{errors.map((error, ind) => (
					<div key={ind}>{error}</div>
				))}
			</div>
			<p hidden={!usernameShow}>{username}</p>
			<button
				type="button"
				onClick={(e) => setUsernameShow(false)}
				hidden={!usernameShow}
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
			>
				Save
			</button>
			<button
				type="button"
				onClick={(e) => setUsernameShow(false)}
				hidden={usernameShow}
			>
				Cancel
			</button>
			<p hidden={!emailShow}>{email}</p>
			<button
				type="button"
				onClick={(e) => setEmailShow(false)}
				hidden={!emailShow}
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
			>
				Save
			</button>
			<button
				type="button"
				onClick={(e) => setEmailShow(false)}
				hidden={emailShow}
			>
				Cancel
			</button>
			<p hidden={!biographyShow}>{biography}</p>
			<button
				type="button"
				onClick={(e) => setBiographyShow(false)}
				hidden={!biographyShow}
			>
				Edit Biography
			</button>
			<input
				hidden={biographyShow}
				className="editProfInput"
				type="text"
				defaultValue={biography}
				onChange={(e) => setBiography(e.target.value)}
			/>
			<button
				type="button"
				onClick={(e) => handleSave(e)}
				hidden={biographyShow}
			>
				Save
			</button>
			<button
				type="button"
				onClick={(e) => setBiographyShow(false)}
				hidden={biographyShow}
			>
				Cancel
			</button>
			<button
				type="button"
				onClick={(e) => setPasswordShow(false)}
				hidden={!passwordShow}
			>
				Edit Password
			</button>
			<input
				hidden={passwordShow}
				className="editProfInput"
				type="password"
				defaultValue={password}
				onChange={(e) => setPassword(e.target.value)}
			/>
			<input
				hidden={passwordShow}
				className="editProfInput"
				type="password"
				defaultValue={repeatPassword}
				onChange={(e) => setRepeatPassword(e.target.value)}
			/>
			<button
				type="button"
				onClick={(e) => handleSave(e)}
				hidden={passwordShow}
			>
				Save
			</button>
			<button
				type="button"
				onClick={() => setPasswordShow(false)}
				hidden={passwordShow}
			>
				Cancel
			</button>
		</form>
	);
}

export default Profile;
