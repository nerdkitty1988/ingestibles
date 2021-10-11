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
    const [media1, setMedia1] = useState("");
    const [media2, setMedia2] = useState("");
    const [media3, setMedia3] = useState("");
    const [media4, setMedia4] = useState("");
    const [media5, setMedia5] = useState("");

    // [this.tagName1, this.setTagName1] = useState("");
    // [this.tagName2, this.setTagName2] = useState("");
    const [tags, setTags] = useState({});
    // let tags =[]
    
    const [tagCounter, setTagCounter] = useState(0);

    const [ingredient1, setIngredient1] = useState("");
    
    const [stepTitle1, setStepTitle1] = useState("");
    const [insturction1, setInsturction1] = useState("");
    const [stepMedia1, setStepMedia1] = useState("");

    const [errors, setErrors] = useState([]);

    // require login is handled by ProtectedRoute
    // if (!sessionUser) {
    //     return (<h3 style={{ color: '#f0a04b' }}>
    //         Please login/signup to create a recipe.
    //     </h3>)
    // };
    
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log(tags)

    }
    
    // count how many tags the user would like to have
    const tagCounterClick = async (e) => {
        e.preventDefault();
        setTagCounter(tagCounter+1)
        console.log(tags)
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
                        key = 'tag1'
                        onChange={(e) => setTags({...tags, 'tag1': e.target.value})}
                        placeholder='Tag'
                    // required
                    />
                    {/* per number of tags, render the tag input component */}
                        {[...Array(tagCounter)].map((el, i) => (<div>
                            <label>Tag #{i + 2}</label>
                            <input
                                className='listingInput'
                                type="text"
                                key={`tag${i+2}`}
                                onChange={(e) => setTags(tags=>{
                                    tags[`tag${i+2}`] = e.target.value
                                    return tags
                                })}
                                placeholder='Tag'
                            // required
                            />
                        </div>))}
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
            <div>
                <label>Photo/Video #1</label>
                    <input
                        className='listingInput'
                        type="text"
                        value={media1}
                        onChange={(e) => setMedia1(e.target.value)}
                        placeholder='Include at most photo and/or video about your finished dish'
                    // required  
                    />
            </div>
            <div>
                <label>Photo/Video #2</label>
                <input
                    className='listingInput'
                    type="text"
                    value={media2}
                    onChange={(e) => setMedia2(e.target.value)}
                    placeholder='Include at most photo and/or video about your finished dish'
                    // required  
                />
            </div>
            <div>
                <label>Photo/Video #3</label>
                <input
                    className='listingInput'
                    type="text"
                    value={media3}
                    onChange={(e) => setMedia3(e.target.value)}
                    placeholder='Include at most photo and/or video about your finished dish'
                // required  
                />
            </div>

            <div>
                <label>Photo/Video #4</label>
                <input
                    className='listingInput'
                    type="text"
                    value={media4}
                    onChange={(e) => setMedia4(e.target.value)}
                    placeholder='Include at most photo and/or video about your finished dish'
                
                />
            </div>
            <div>
                <label>Photo/Video #5</label>
                <input
                    className='listingInput'
                    type="text"
                    value={media5}
                    onChange={(e) => setMedia5(e.target.value)}
                    placeholder='Include at most photo and/or video about your finished dish'
            
                />
            </div>

             <div>
                <label>Ingredient</label>
                <input
                    className='listingInput'
                    type="text"
                    value={ingredient1}
                        onChange={(e) => setIngredient1(e.target.value)}
                    placeholder='ingredients for your dish'
              
                />
            </div>

            <div>
                <h2>Step #1</h2>
                <input
                    className='listingInput'
                    type="text"
                    value={stepTitle1}
                    onChange={(e) => setStepTitle1(e.target.value)}
                    placeholder='Enter step title'
          
                />
                <textarea
                    className='listingInput'
                    value={insturction1}
                    onChange={(e) => setInsturction1(e.target.value)}
                    placeholder='Write a detailed description of this step'
   
                />
                <input
                    className='listingInput'
                    type="text"
                    value={stepMedia1}
                    onChange={(e) => setStepMedia1(e.target.value)}
                    placeholder='Photo for this step'

                />
            </div>

            

               
        </form>

    );
}

export default CreateRecipe;