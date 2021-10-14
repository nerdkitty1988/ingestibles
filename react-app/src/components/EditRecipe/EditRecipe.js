import React, { useState, useEffect } from 'react';
import { NavLink, useHistory, useParams } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { editRecipeThunk } from '../../store/editRecipe';
import './EditRecipe.css';

const EditRecipe = () => {
    const dispatch = useDispatch();
    const history = useHistory();
    const sessionUser = useSelector(state => state.session.user);

    const [title, setTitle] = useState('');
    const [tags, setTags] = useState({});
    const [tagCounter, setTagCounter] = useState(0);

    const [introduction, setIntroduction] = useState("");
    const [media1_old, setMedia1_Old] = useState("");
    const [media2_old, setMedia2_Old] = useState("");
    const [media3_old, setMedia3_Old] = useState("");
    const [media4_old, setMedia4_Old] = useState("");
    const [media5_old, setMedia5_Old] = useState("");
    // use the following array to preload them in useEffect
    const oldMediaArr = [setMedia1_Old, setMedia2_Old, setMedia3_Old, setMedia4_Old, setMedia5_Old]
    const [media1, setMedia1] = useState("");
    const [media2, setMedia2] = useState("");
    const [media3, setMedia3] = useState("");
    const [media4, setMedia4] = useState("");
    const [media5, setMedia5] = useState("");
    
    const [ingredientPhoto_Old, setIngredientPhoto_Old] = useState(null);
    const [ingredientPhoto, setIngredientPhoto] = useState(null);
    const [ingredients, setIngredients] = useState({});
    const [ingredientCounter, setIngredientCounter] = useState(0);

    const [steps, setSteps] = useState({'oldSteps':{}});
    const [stepCounter, setStepCounter] = useState(0);
    const [errors, setErrors] = useState([]);

    // fetch current recipe to pre-load data on edit form
    const { recipeId } = useParams();
    let recipe = {}
    useEffect(() => {
        if (!recipeId) {
            return;
        }
        (async () => {
            const response = await fetch(`/api/recipes/edit/${recipeId}`);
            recipe = await response.json();
            console.log(recipe, recipe.tags)
            // pre-load data on edit form - recipe table 
            setTitle(recipe.title)
            setIntroduction(recipe.description)
            setIngredientPhoto_Old(recipe.ingredientPhoto)
            // pre-load data on edit form - tag table 
            recipe.tags.forEach((tag,i)=>{
                setTags(tags => {
                    tags[`tag${i+1}`] = tag.name
                    return tags
                })
                setTagCounter(tagCounter=>tagCounter + 1)
            })
            // pre-load ingredients on edit form - ingredients table
            recipe.ingredients.forEach((ingredient, i) => {
                setIngredients(ingredients => {
                    ingredients[`ingredient${i + 1}`] = ingredient.info
                    return ingredients
                })
                setIngredientCounter(ingredientCounter => ingredientCounter + 1)
            })
            // pre-load media on edit form - media table
            recipe.medias.forEach((media, i) => {
                oldMediaArr[i](media.mediaUrl)          
            })
            // pre-load steps on edit form - steps table
            recipe.instructions.forEach((instruction, i) => {
                setSteps(steps => {
                    steps[`oldSteps`][`step${i+1}`]={}
                    steps[`oldSteps`][`step${i + 1}`].photo = instruction.imageUrl
                    steps[`oldSteps`][`step${i + 1}`].title = instruction.stepTitle
                    steps[`oldSteps`][`step${i + 1}`].direction = instruction.directions
                    return steps
                })
                setStepCounter(stepCounter => stepCounter + 1)
            })
            

        })();
    }, [recipeId]);






    // require login is handled by ProtectedRoute
    
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        setErrors([]);

        // filter out null/empty/only spaces input
        const tags_notNull = {}
        Object.keys(tags).forEach(key=>{
        if (tags[key] && tags[key].replace(/\s/g, '').length){
                tags_notNull[key] = tags[key]
            }
        })
        const media_notNull = {}

        // if there is new media, then replace old, otherwise use old media url
        const mediaArr = [media1 ? media1 : media1_old, media2 ? media2 : media2_old, media3 ? media3 : media3_old, media4 ? media4 : media4_old, media5 ? media5 : media5_old]
        mediaArr.forEach((media,i) => {
            if (media) {
                media_notNull[`media${i+1}`] = media
                }
        })

        const ingredients_notNull = {}
        Object.keys(ingredients).forEach(key => {
            if (ingredients[key] && ingredients[key].replace(/\s/g, '').length) {
                ingredients_notNull[key] = ingredients[key]
            }
        })

        // title and direction are required input, photo of steps is not required; thus delete the inputs that does not have title and does not have direction; backend will handle if one of those two are missing;
        const steps_notNull = {...steps}
        Object.keys(steps_notNull).forEach(key => {
            if (!(steps_notNull[key].title?steps_notNull[key].title.replace(/\s/g, '') :steps_notNull[key].title) && !(steps_notNull[key].direction?steps_notNull[key].direction.replace(/\s/g, '').length:steps_notNull[key].direction)) {
                delete steps_notNull[key]
            } 
        })


        // prepare recipe input data ready for AWS
        const formData = new FormData();
        formData.append("authorId", sessionUser.id);
        formData.append("recipeTitle", title);
        // ingredientPhoto is required; when there is one file to replace, then replace it, otherwise keep the old image url
        formData.append("ingredientPhoto", ingredientPhoto ? ingredientPhoto : ingredientPhoto_Old);
        formData.append("introduction", introduction);
        
        // prepare tags input data ready for AWS
        Object.keys(tags_notNull).forEach(key => {
            formData.append(key, tags_notNull[key]);       
        })
        // prepare ingredients input data ready for AWS
        Object.keys(ingredients_notNull).forEach(key => {
            formData.append(key, ingredients_notNull[key]);
        })
        // prepare media input data ready for AWS
        Object.keys(media_notNull).forEach(key => {
            formData.append(key, media_notNull[key]);
        })
        // prepare steps data ready for AWS
        // Object.keys(steps_notNull).forEach(key => {
        //     // console.log('outside', key, steps_notNull[key])
        //     Object.keys(steps_notNull[key]).forEach(k=>{
        //         // console.log('inside', k, steps_notNull[key][k])
        //         formData.append(key + '_' + k, steps_notNull[key][k]);
        //     })
            
        // })
        
    
        // formData.values() creates iterator and use for loop to print out values
        for (let value of formData.values()) {
            console.log('formData.values Start');
            console.log(value);
            console.log('formData.values End');
        }
        
        // when not using AWS note: tags,media,ingredients,instructions need to be {}, otherwise wtforms will not capture data correctly; e.g. if it is an [], it will only capture the first element
        const newRecipe = {
            recipe:{
                recipeId: +recipeId,
                authorId: sessionUser.id,
                title,
                introduction,
                ingredientPhoto:ingredientPhoto?ingredientPhoto:ingredientPhoto_Old
            },            
            tags:tags_notNull,
            media:media_notNull,
            ingredients:ingredients_notNull,
            // steps: steps_notNull,
        }
        console.log('dictionary-recipe:', newRecipe)

        const data = await dispatch(editRecipeThunk({formData,recipeId}));
        if (data.errors) {
            setErrors(data.errors);
            // console.log('!!!!', typeof errors)
        } else{
            history.push(`/recipes/my_plate`)
        }

    }
    
    // count how many tags the user would like to have
    const tagCounterClick = async (e) => {
        e.preventDefault();
        setTagCounter(tagCounter+1)
        // console.log(tags)
    }

    // count how many ingredients the user would like to have
    const ingredientCounterClick = async (e) => {
        e.preventDefault();
        setIngredientCounter(ingredientCounter + 1)
        // console.log(ingredients)
    }

    // count how many steps the user would like to have
    const stepCounterClick = async (e) => {
        e.preventDefault();
        // to save the place at dictionary to keep orders of steps, in case user add a bunch of steps and then start to fill at a random step, instead of by order, because dictionary/pojo will be ordered by the order.
        steps[`step${stepCounter+1}`] = {}

        setStepCounter(stepCounter + 1)
        // console.log(steps)
    }


    return ( 
        <form onSubmit={handleSubmit} >
            <div className='newRecipeButtonWrapper'>

                <NavLink to='/recipes/my_plate' exact={true}
                className='btn-category-header' 
                    style={{ display: 'block', marginTop: '1%', backgroundColor:'#FAD7BB', maxHeight:'20px'}}>Cancel</NavLink>

                <div style={{ color:'#F27D21'}}>
                    {errors.map((error, ind) => (
                    <li style={{ marginLeft:'15%', textAlign:'start'}}
                            key={ind}>{error}</li>
                    ))}
                </div>

                <button className='btn-category-header'
                style={{ display: 'block', marginTop: '1%', backgroundColor: '#FAD7BB', maxHeight:'35px' }}
                >Edit Recipe</button>
                

            </div>
            
            <div className='createRecipeWrapper'>
                <h4 style={{textAlign:'center'}}>Recipe Basics</h4>
                <div className='createRecipeEl'>                   
                <label className='editRecipeLabel'>Recipe Title </label>
                    <input
                        className='listingInput'
                        type="text"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        placeholder='Recipe Title'
                        // required  
                    />
                </div>
                
                {[...Array(tagCounter)].map((el, i) => (<div className='createRecipeEl' key={`tag${i + 1}`}>
                    <label className='editRecipeLabel'>Tag #{i + 1} </label>
                    <input
                        className='listingInput'
                        type="text" 
                        defaultValue={tags[`tag${i+1}`]}
                        onChange={(e) => {
                            setTags(tags=>{                               
                            tags[`tag${i+1}`] = e.target.value
                            return tags
                            })
                        }}
                        placeholder='At least 1 Tag'
                            />
                    </div>))}
                    <button onClick={tagCounterClick} 
                            style={{ marginRight: '12%' }}
                            className="btn-category-header"
                            >Add Tag</button>
                           
            </div>
            
            <div className='createRecipeWrapper'>
             <h4 style={{ textAlign: 'center' }}>Introduction</h4>
             <div className='createRecipeEl'>
                
                    <label className='editRecipeLabel'>Recipe Introduction </label>
                <textarea
                    className='listingInput'
                    value={introduction}
                    onChange={(e) => setIntroduction(e.target.value)}
                    placeholder='Briefly describe what you made.'
                    //required
                />
              </div>
             <div>
                    {media1_old ?<img
                    className='EditImg'
                    src={media1_old} alt='OriginalMedia1Photo' />:null}
                   <div className='createRecipeEl'>
                
                        <label className='editRecipeLabel'>Replace Photo/Video#1 above by: </label>
                    <input
                        className='listingInput'
                        type="file"
                        // value={media1}
                        accept="image/*,video/mp4,video/mov,video/wmv"
                        onChange={(e) => setMedia1(e.target.files[0])}
                        // placeholder='Include 1-5 photo and/or video about your finished dish'
                    />
              </div>
                {media2_old?<img
                    className='EditImg'
                        src={media2_old} alt='OriginalMedia2Photo' />:null
                }
                <div className='createRecipeEl'>
                        <label className='editRecipeLabel'>Replace Photo/Video#2 above by </label>
                <input
                    className='listingInput'
                    type="file"
                    accept="image/*,video/mp4,video/mov,video/wmv"
                    onChange={(e) => setMedia2(e.target.files[0])}
                    // placeholder='Include 1-5 photo and/or video about your finished dish' 
                />
              </div>
                    {media3_old ? <img
                        className='EditImg'
                        src={media3_old} alt='OriginalMedia3Photo' /> : null
                    }
              <div className='createRecipeEl'>
                        <label className='editRecipeLabel'>Replace Photo/Video#3 above by </label>
                <input
                    className='listingInput'
                    type="file"
                    accept="image/*,video/mp4,video/mov,video/wmv"
                    onChange={(e) => setMedia3(e.target.files[0])}
                    // placeholder='Include 1-5 photo and/or video about your finished dish' 
                // required  
                />
              </div>
                    {media4_old ? <img
                        className='EditImg'
                        src={media4_old} alt='OriginalMedia4Photo' /> : null
                    }

                <div className='createRecipeEl'>
                        <label className='editRecipeLabel'>Replace Photo/Video#4 above by </label>
                <input
                    className='listingInput'
                    type="file"
                   accept="image/*,video/mp4,video/mov,video/wmv"
                    onChange={(e) => setMedia4(e.target.files[0])}
                    // placeholder='Include 1-5 photo and/or video about your finished dish' 
                
                />
              </div>
                    {media5_old ? <img
                        className='EditImg'
                        src={media5_old} alt='OriginalMedia5Photo' /> : null
                    }
                <div className='createRecipeEl'>
                        <label className='editRecipeLabel'>Replace Photo/Video#5 above by </label>
                <input
                    className='listingInput'
                    type="file"
                    accept="image/*,video/mp4,video/mov,video/wmv"
                    onChange={(e) => setMedia5(e.target.files[0])}
                    // placeholder='Include 1-5 photo and/or video about your finished dish' 
            
                />
              </div>
             </div>
            </div>

             <div className='createRecipeWrapper'>
                <h4 style={{ textAlign: 'center' }}>Ingredients</h4>
                <img
                    className='EditImg'
                    src={ingredientPhoto_Old} alt='OriginalIngredientPhoto' />
                <div className='createRecipeEl'>
                    <label className='editRecipeLabel'>Replace ingredient photo above by </label>
                
                <input
                    className='listingInput'
                    type="file"
                    // value={ingredientPhoto}
                    accept="image/*"
                    onChange={(e) => setIngredientPhoto(e.target.files[0])}
                    // placeholder='at least 1 ingredient photo for your dish'             
                />
                </div>

                {[...Array(ingredientCounter)].map((el, i) => (<div className='createRecipeEl' key={`ingredient${i + 1}`}>
                    <label className='editRecipeLabel'>Ingredient #{i + 1} </label>
                    <input
                        className='listingInput'
                        type="text"
                        defaultValue={ingredients[`ingredient${i + 1}`]}
                        onChange={(e) => setIngredients(ingredients => {
                        ingredients[`ingredient${i + 1}`] = e.target.value
                        return ingredients
                        })}
                        placeholder='At least 1 ingredient for your dish'
                    />
                </div>))}
                <button onClick={ingredientCounterClick}
                        style={{ marginRight: '12%' }}
                        className="btn-category-header">Add Ingredient</button>
            </div>
            
            <div className='createRecipeWrapper'>
            <h4 style={{ textAlign: 'center' }}>Your Recipe Steps</h4>
            {/* <div className='createRecipeEl'>
                <h5 style={{ textAlign: 'center' }}>Step #1</h5>
                <div className='createRecipeStep'>
                        <label className='editRecipeLabel'>Title </label >
                <input
                    className='listingInput'
                    type="text"
                    onChange={(e) => setSteps(steps=>{
                        steps['step1'] ? steps['step1'].title = e.target.value : steps['step1'] ={}
                        steps['step1'].title = e.target.value
                        return steps

                    })}
                    placeholder='Enter step title - Required input'
          
                />
               </div>

                <div className='createRecipeStep'>
                        <label className='editRecipeLabel'>Instruction </label>
                <textarea
                    className='listingInput'
                    onChange={(e) => setSteps(steps=>{
                        steps['step1'] ? steps['step1'].direction = e.target.value : steps['step1'] ={}
                        steps['step1'].direction = e.target.value
                        return steps

                    })}
                    placeholder='Write a detailed description of this step - Required input'
                        
                />
                </div>
                <div className='createRecipeStep'>
                        <label className='editRecipeLabel'>Photo </label>
                <input
                    className = 'listingInput'
                    type = "file"
                    accept = "image/*"
                    onChange={(e) => setSteps(steps => {
                    steps['step1'] ? steps['step1'].photo = e.target.files[0] : steps['step1'] = {}
                    steps['step1'].photo = e.target.files[0]
                    return steps

                })}
                />
                </div>
            </div> */}

            {[...Array(stepCounter)].map((el, i) => (<div key={`step${i + 1}`} className='createRecipeEl'>
                <h5 style={{ textAlign: 'center' }}>Step #{i + 1} </h5>
                < div className='createRecipeStep' >
                    <label className='editRecipeLabel'>Title </label>
                <input
                    className='listingInput'
                    type="text"
                    defaultValue={steps.oldSteps[`step${i + 1}`]?.title}
                    onChange={(e) => setSteps(steps => {
                        steps[`step${i + 1}`] ? steps[`step${i + 1}`].title = e.target.value : steps[`step${i + 1}`] = {}
                        steps[`step${i + 1}`].title = e.target.value
                        return steps

                    })}
                    placeholder='Enter step title'

                />
                </div>
                <div className='createRecipeStep'>
                    <label className='editRecipeLabel'>Instruction </label>
                <textarea
                    className='listingInput'
                    defaultValue={steps.oldSteps[`step${i + 1}`]?.direction}
                    onChange={(e) => setSteps(steps => {
                        steps[`step${i + 1}`] ? steps[`step${i + 1}`].direction = e.target.value : steps[`step${i + 1}`] = {}
                        steps[`step${i + 1}`].direction = e.target.value
                        return steps

                    })}
                    placeholder='Write a detailed description of this step'

                />
                </div>
                <img
                    className='EditImg'
                    
                    src={steps.oldSteps[`step${i + 1}`]?.photo ? steps.oldSteps[`step${i + 1}`]?.photo : null} 
                    
                    alt={`PhotoForOriginalStep${i + 1}`} />

                <div className='createRecipeStep'>
                    < label className='editRecipeLabel'> Photo </label>
                <input   
                    className = 'listingInput'
                    type = "file"
                    accept = "image/*"                       
                    onChange = {(e) => setSteps(steps => {
                    steps[`step${i + 1}`] ? steps[`step${i + 1}`].photo = e.target.files[0] : steps[`step${i + 1}`] = {}
                    steps[`step${i + 1}`].photo = e.target.files[0]
                    return steps
                    })}

                />
                </div>
                
            </div>))}
            <button onClick={stepCounterClick}
                    style={{ marginRight: '12%' }}
                    className="btn-category-header">Add Step</button>
           </div>
            

               
        </form>

    );
}

export default EditRecipe;