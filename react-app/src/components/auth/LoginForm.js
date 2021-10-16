import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { NavLink, Redirect } from "react-router-dom";
import { login } from "../../store/session";
import "./auth.css"

const LoginForm = () => {
	const [errors, setErrors] = useState([]);
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const user = useSelector((state) => state.session.user);
	const dispatch = useDispatch();

	const onLogin = async (e) => {
		e.preventDefault();
		const data = await dispatch(login(email, password));
		if (data) {
			setErrors(data);
		}
	};

	const demoUser = async (e) => {
		e.preventDefault();
		await dispatch(login('demo@aa.io', 'password'));
	};

	const updateEmail = (e) => {
		setEmail(e.target.value);
	};

	const updatePassword = (e) => {
		setPassword(e.target.value);
	};

	if (user) {
		return <Redirect to="/" />;
	}

	return (
		<div className="loginPage">
			<div className="loginformContainer">
				<form onSubmit={onLogin}>
					<div>
						{errors.map((error, ind) => (
							<li key={ind} sytle={{ color:'#F27D21'}}>{error}</li>
						))}
					</div>
					<div>
						<input
														className="loginInput"
							name="email"
							type="text"
							placeholder="Email"
							value={email}
							onChange={updateEmail}
						/>
					</div>
					<div>
						<input
														className="loginInput"
							name="password"
							type="password"
							placeholder="Password"
							value={password}
							onChange={updatePassword}
						/>
						<button type="submit" className="loginButton">Log In</button>
					</div>
					<button className="loginButton" onClick={demoUser}>Demo User</button>
										<div className="loginSignupText">
						New to Ingestibles? <NavLink to="/sign-up">Sign Up >></NavLink>
										</div>
				</form>
			</div>
		</div>
	);
};

export default LoginForm;
