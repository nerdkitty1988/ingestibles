import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect, NavLink } from 'react-router-dom';
import { signUp, login  } from '../../store/session';

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const [biography, setBiography] = useState('');
  const [profilePic, setProfilePic] = useState(null);
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      // prepare recipe input data ready for AWS
      const formData = new FormData();
      formData.append("username", username);
      formData.append("email", email);
      formData.append("password", password);
      formData.append("biography", biography);
      formData.append("profilePic", profilePic);

      const data = await dispatch(signUp(formData));
      if (data) {
        setErrors(data)
      }
    }
  };

  const demoUser = async (e) => {
    e.preventDefault();
    await dispatch(login('demo@aa.io', 'password'));
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  const updateBiography = (e) => {
    setBiography(e.target.value);
  };

  const updateProfilePic = (e) => {
    setProfilePic(e.target.files[0]);
  };

  if (user) {
    return <Redirect to='/' />;
  }

  return (
    <div className="loginPage">
      <div className="loginformContainer" style = {{width:'450px'}}>
        <form onSubmit={onSignUp}>
          <div>
            {errors.map((error, ind) => (
              <li key={ind} sytle={{ color: '#F27D21' }}>{error}</li>
            ))}
          </div>
          <div>
            <label>User Name</label>
            <input
              type='text'
              name='username'
              onChange={updateUsername}
              value={username}
              className="signupInput"
            ></input>
          </div>
          <div>
            <label>Email</label>
            <input
              type='text'
              name='email'
              onChange={updateEmail}
              value={email}
              className="signupInput"
            ></input>
          </div>
          <div>
            <label>Biography</label>
            <textarea
              name='biography'
              onChange={updateBiography}
              value={biography}
              className="signupInput"
              style={{resize:'none', height:'100px'}}
            ></textarea>
          </div>
          <div>
            <label>Profile Picture</label>
            <input
              // type='url'
              name='profilePic'
              type="file"
              accept="image/*"
              onChange={updateProfilePic}
              // value={profilePic}
              className="signupInput"
              style={{backgroundColor:'white'}}
            ></input>
          </div>
          <div>
            <label>Password</label>
            <input
              type='password'
              name='password'
              onChange={updatePassword}
              value={password}
              className="signupInput"
            ></input>
          </div>
          <div>
            <label>Repeat Password</label>
            <input
              type='password'
              name='repeat_password'
              onChange={updateRepeatPassword}
              value={repeatPassword}
              // required={true}
              className="signupInput"
            ></input>
          </div>
          <button type='submit' className="loginButton" >Sign Up</button>
					<button className="loginButton" onClick={demoUser}>Demo User</button>
          <div className="loginSignupText">
						Already have an account? <NavLink to="/login">Log In >></NavLink>
          </div>
        </form>
      </div>
    </div>
  );
};

export default SignUpForm;
