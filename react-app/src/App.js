import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch } from "react-redux";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar/NavBar";
import Homepage from "./components/Homepage/Homepage";
import MyPlate from "./components/MyPlate/MyPlate";
import Profile from "./components/Profile/profile";
import EditRecipe from "./components/EditRecipe/EditRecipe"
import ProtectedRoute from "./components/auth/ProtectedRoute";
import User from "./components/User";
import CreateRecipe from "./components/CreateRecipe/CreateRecipe";
import { authenticate } from "./store/session";

function App() {
	const [loaded, setLoaded] = useState(false);
	const dispatch = useDispatch();

	useEffect(() => {
		(async () => {
			await dispatch(authenticate());
			setLoaded(true);
		})();
	}, [dispatch]);

	if (!loaded) {
		return null;
	}

	return (
		<BrowserRouter>
			<NavBar loaded={loaded} />
			{loaded && (
				<Switch>
					<Route path="/" exact={true}>
						<Homepage />
					</Route>
					<Route path="/login" exact={true}>
						<LoginForm />
					</Route>
					<Route path="/sign-up" exact={true}>
						<SignUpForm />
					</Route>
					<ProtectedRoute path="/recipes/my_plate" exact={true}>
						<MyPlate />
					</ProtectedRoute>
					<Route path="/users/:userId" exact={true}>
						<Profile />
					</Route>
					<ProtectedRoute path="/recipes/new_recipe" exact={true}>
						<CreateRecipe />
					</ProtectedRoute>
					<ProtectedRoute path="/recipes/edit/:recipeId" exact={true}>
						<EditRecipe />
					</ProtectedRoute>
					<ProtectedRoute path="/" exact={true}>
						<h1>My Home Page</h1>
					</ProtectedRoute>
				</Switch>
			)}
		</BrowserRouter>
	);
}

export default App;
