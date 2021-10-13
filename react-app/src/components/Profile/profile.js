import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { NavLink, useHistory } from "react-router-dom";
import { updateUser } from "../../store/session";

function Profile() {
	const dispatch = useDispatch();
	const sessionUser = useSelector((state) => state.session.user);
	const userId = sessionUser.id;

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

	const handleSave = (updateData) => {
		const data = dispatch(updateUser(updateData));
		if (data.errors) {
			setErrors(data.errors);
		} else {
			setUsernameShow(true);
			setEmailShow(true);
			setPasswordShow(true);
			setBiographyShow(true);
			setProfilePicShow(true);
		}
	};

	const updateUsername = (e) => {
		setUsername(e.target.value);
		handleSave({ id: userId, username: username });
	};

	const updateEmail = (e) => {
		setEmail(e.target.value);
		handleSave({ id: userId, email: email });
	};

	const updatePassword = (e) => {
		setPassword(e.target.value);
		handleSave({ id: userId, password: password });
	};

	const updateRepeatPassword = (e) => {
		setRepeatPassword(e.target.value);
	};

	const updateBiography = (e) => {
		setBiography(e.target.value);
		handleSave({ id: userId, biography: biography });
	};

	const updateProfilePic = (e) => {
		setProfilePic(e.target.value);
		handleSave({ id: userId, profilePic: profilePic });
	};

	return (
		<form onSubmit={handleSave}>
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
			/>
			<button
				type="button"
				onClick={(e) => updateUsername(e)}
				hidden={usernameShow}
			>
				Save
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
			/>
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
			/>
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
			/>
			<input
				hidden={passwordShow}
				className="editProfInput"
				type="password"
				defaultValue={repeatPassword}
			/>
		</form>
	);
}

export default Profile;
