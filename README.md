# Welcome to Ingestibles

Ingestibles, an Instructables clone, for people to explore, share, and create recipes. We make it easy to learn how to cook anything, one step at a time.

Live Link: [Ingestibles](https://ingestibles-app.herokuapp.com/)


## Ingestibles at a Glance

### Home Page & All Recipes Page
On home page, users can peruse through different recipes, which are grouped by tags/categories.

Users can view all recipes by either clicking on the "Recipes" button in the nav bar or clicking on the user profile dropdown and clicking "All Recipes."  Once on this page, user can see all the recipes ordered by date of post starting with the most recent.

![Recipes at a glance](/react-app/src/static/readMe/recipes.gif) 

### Profile & My-plate
Once logged in, user can click on the profile pic to access the dropdown links and navigate to one's own profile page, all recipes page, my-plate page including recipes created by logged-in user and user's favorite recipes, and the form to create a new recipe.

![profileAndMyPlate at a glance](/react-app/src/static/readMe/profileAndMyPlate.gif) 

### Single Recipe Page, Comments & likes
Users can explore single recipe page and logged-in users can like and comment on all recipes.

![singleRecipe at a glance](/react-app/src/static/readMe/singleRecipe.gif)

###  search
Users can search recipes by their titles, ingredients, tags on any page through nav bar.

![search at a glance](/react-app/src/static/readMe/search.gif)

### Recipes
Logged-in users can create recipes, edit and delete their own recipes. As each recipe would have customized number and content of ingredients, steps and tags, a dynamic recipe creation form and a pre-filled recipe edit form will capture the difference and allow customization.

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
