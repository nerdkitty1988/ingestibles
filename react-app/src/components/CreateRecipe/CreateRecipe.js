import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import AddTag from './AddTag';
import './CreateRecipe.css';

const CreateRecipe = () => {
    const dispatch = useDispatch();
    const sessionUser = useSelector(state => state.session.user);
    
    const [title, setTitle] = useState("");
    const [introduction, setIntroduction] = useState("");
    [this.tagName1, this.setTagName1] = useState("");
    [this.tagName2, this.setTagName2] = useState("");
    const [tagCounter, setTagCounter] = useState(0);

    const [errors, setErrors] = useState([]);

    // require login is handled by ProtectedRoute
    // if (!sessionUser) {
    //     return (<h3 style={{ color: '#f0a04b' }}>
    //         Please login/signup to create a recipe.
    //     </h3>)
    // };
    
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log(tagName1, tagName2)
    }
    
    // count how many tags the user would like to have
    const tagCounterClick = async (e) => {
        e.preventDefault();
        setTagCounter(tagCounter+1)
    }


    return ( 
        <form onSubmit={handleSubmit}>
            <div>
                <NavLink to='/profile' exact={true}>Cancel</NavLink>
                <button>Create Recipe</button>
            </div>
            <div>
                {errors.map((error, ind) => (
                    <div key={ind}>{error}</div>
                ))}
            </div>
            <div>
                <div>
                    <h2>Recipe Basics</h2>
                    <label>Project Title</label>
                    <input
                        className='listingInput'
                        type="text"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        placeholder='Title'
                        // required  
                    />
                </div>
                <div>
                    <label>Tag #1</label>
                    <input
                        className='listingInput'
                        type="text"
                        value={tagName1}
                        onChange={(e) => setTagName1(e.target.value)}
                        placeholder='Tag'
                    // required
                    />
                    {/* per number of tags, render the tag input component */}
                    {[...Array(tagCounter)].map((el, i) => <AddTag 
                                                            key={i} count={i}
                                                            value={this['tagName'+(i+2)]}
                                                            onChange={(e) => this['tagName'+(i+2)](e.target.value)}
                                                            />)}
                    <button onClick={tagCounterClick}>Add more tag</button>
            
                </div>
            </div>

            <div>
                <label>Introduction</label>
                <textarea
                    className='listingInput'
                    value={introduction}
                    onChange={(e) => setIntroduction(e.target.value)}
                    placeholder='Briefly describe what you made.'
                    //required
                />
            </div>
               
        </form>

    );
}

export default CreateRecipe;