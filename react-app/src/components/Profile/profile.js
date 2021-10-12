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
			const response = await fetch(`/api/users/${userId}`);
			const responseData = await response.json();
			setUser(responseData);
		}
		fetchData();
	}, [user]);

	const handleSave = (updateData) => {
		e.preventDefault();
		const data = await dispatch(updateUser(updatedata));
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
        handleSave({"username":username});

	};

	const updateEmail = (e) => {
		setEmail(e.target.value);
        handleSave({"email":email});
	};

	const updatePassword = (e) => {
		setPassword(e.target.value);
        handleSave({"password":password});
	};

	const updateRepeatPassword = (e) => {
		setRepeatPassword(e.target.value);
	};

	const updateBiography = (e) => {
		setBiography(e.target.value);
        handleSave({"biography":biography});
	};

	const updateProfilePic = (e) => {
		setProfilePic(e.target.value);
        handleSave({"profilePic":profilePic});
	};

	return (
		<form onSubmit={handleSave}>
			<p>{username}</p>
			<input
            hidden={usernameShow}
            className="editProfInput"
            type="text"
            value={username}
            onChange={(e) => updateUsername(e)}
            />
            <p>{email}</p>
			<input
            hidden={emailShow}
            className="editProfInput"
            type="text"
            value={email}
            onChange={(e) => updateEmail(e)}
            />
            <p>{biography}</p>
			<input
            hidden={biographyShow}
            className="editProfInput"
            type="text"
            value={biography}
            onChange={(e) => updateBiography(e)}
            />

			<input
            hidden={passwordShow}
            className="editProfInput"
            type="password"
            value={password}
            onChange={(e) => updatePassword(e)}
            />

			<input
            hidden={passwordShow}
            className="editProfInput"
            type="password"
            value={repeatPassword}
            onChange={(e) => updateRepeatPassword(e)}
            />
		</form>
	);
}
