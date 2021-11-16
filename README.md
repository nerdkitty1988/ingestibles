# Welcome to Ingestibles

Ingestibles, an Instructables clone, for people to explore, share, and create recipes. We make it easy to learn how to cook anything, one step at a time.

Live Link: [Ingestibles](https://ingestibles-app.herokuapp.com/)


## Ingestibles at a Glance

### Splash, All Recipes Page, Profile dropdown....
User can ..........

### Single Recipe Page, comments, likes....
User can .......

### My-plate, search, profile....
User can ..........

### Recipes
User can create recipes, edit and delete their own recipes. As each recipe would have customized number and content of ingredients, steps and tags, a dynamic recipe creation form and a pre-filled recipe edit form will capture the difference and allow customization.

##### Edit Recipe:
![Edit Recipes at a glance](/react-app/src/static/readMe/editRecipe.gif) 


## Technologies used
* Python
* Flask
* PostgreSQL
* SQLAlchemy
* HTML
* Vanilla CSS
* JavaScript
* React
* Redux
* AWS S3

The Virtual DOM in React allows dynamic and interactive components. The following code is used to dynamically display tags and manage their states per change of input, in the pre-filled recipe edit form. 

##### Dynamically displaying tags at Recipe Edit Form
```jsx
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
```

## Future Implementations
- View other users' Ingestibles pages including their profiles and recipes
- Follow other users
