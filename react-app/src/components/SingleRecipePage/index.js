import { React, useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { useParams } from "react-router";
import EditComment from "../EditComment";
import Instruction from "../Instruction"
import NewComment from "../NewComment"
import "./SingleRecipePage.css"
import ReactPlayer from 'react-player'
import { useHistory } from 'react-router-dom';
import defaultPhoto from "./profileDefaultPhoto.png";

const SingleRecipePage = () => {
  const { recipeId } = useParams();
  const sessionUser = useSelector((state) => state.session.user);
  //console.log(sessionUser)
  const [currentRecipe, setCurrentRecipe] = useState({});
  const [otherRecipes, setOtherRecipes] = useState([]);
  const [comments, setComments] = useState([])
  const [canComment, setCanComment] = useState(false);
  const [canEdit, setCanEdit] = useState(false)
  const [commenting, setCommenting] = useState(false)
  const history = useHistory();
  // async function retrieveRecipe() {
  //   const recipeFetch = await fetch(`/api/recipes/${recipeId}`)
  //   const currentRecipeData = await recipeFetch.json();
  //   const recipeData = currentRecipeData.recipe[0]
  //   setCurrentRecipe(recipeData)
  // }

  // async function retrieveOtherRecipes() {
  //   const recipeData = await fetch(`/api/recipes`)
  //   const currentRecipeData = await recipeData.json();
  //   const recipeArray = currentRecipeData.recipes.filter(recipe => recipe.authorId === currentRecipe.authorId)
  //   const othersArray = recipeArray.filter(recipe => recipe.id !== currentRecipe.id)
  //   console.log("WE GET HERE")
  //   setOtherRecipes(othersArray)
  // }

  useEffect(() => {
    const fetchData = () => {
      const thisRecipe = fetch(`/api/recipes/${recipeId}`).then((res) => res.json())//.then((data) => setCurrentRecipe(data.recipe[0]))
      const others = fetch(`/api/recipes/`).then((res) => res.json())//.then((data) => setOtherRecipes([...data recipes.filter(recipe => recipe.authorId === currentRecipe.authorId && recipe.id !== currentRecipe.id)]))
      const comments = fetch(`/api/recipes/comments`).then((res) => res.json())
      Promise.all([thisRecipe, others, comments]).then((allData) => {
        setCurrentRecipe(allData[0].recipe[0])
        setOtherRecipes(allData[1].recipes)
        setComments(allData[2].comments)
      })
    }
    fetchData()
    //console.log(recipeFetch)
    //retrieveOtherRecipes()
    //console.log("NOW IM GOING")
  }, [])

  const currentRecipeComments = comments?.filter(comment => comment.recipeId === currentRecipe.id)

  const whatIWant = otherRecipes.filter(recipe => recipe.authorId === currentRecipe.authorId && recipe.id !== currentRecipe.id)

  const recipeImages = currentRecipe?.instructions?.map(instruction => instruction.imageUrl)
  //for 1-5 photos/video start
  const media1To5 = currentRecipe && currentRecipe.medias ? currentRecipe.medias.map(media => media.mediaUrl) : []
  const [play1, setPlay1] = useState(false);
  const [play2, setPlay2] = useState(false);
  const [play3, setPlay3] = useState(false);
  const [play4, setPlay4] = useState(false);
  const [play5, setPlay5] = useState(false);
  const videoArr = [[media1To5[0], play1, setPlay1], [media1To5[1], play2, setPlay2], [media1To5[2], play3, setPlay3], [media1To5[3], play4, setPlay4], [media1To5[4], play5, setPlay5]]
  const isVideo = (url) => {
    if (url) {
      return ['.mp4', '.mov', '.wmv'].includes(url.slice(url.length - 4, url.length))
    } else {
      return false
    }
  }


  const authorsIds = otherRecipes.map(recipe => recipe.author.id)
  const authorsImages = otherRecipes.map(recipe => recipe.author.profilePic)
  const authorIdsArr = [...new Set(authorsIds)]
  const authorImagesArr = [...new Set(authorsImages)]
  const authorsObject = {}
  for (let i = 0; i < authorIdsArr.length; i++) {
    let image = authorImagesArr[i];
    let id = authorIdsArr[i];
    authorsObject[id] = image;
  }

  let newCommentBox;
  if (sessionUser) {
    newCommentBox = (
      <NewComment currentRecipe={currentRecipe} setCanComment={setCanComment} setComments={setComments} setCommenting={setCommenting} />
    )
  }
  else {

  }
  //console.log(today.toLocaleDateString("en-US"));


  // Codes about Likes start here:
  const [likeResponse, setLikeResponse] = useState('')
  useEffect(() => {
    if (sessionUser) {
      (async () => {
        const response = await fetch(`/api/likes/${recipeId}/`);
        const like = await response.json();
        (like.like) ? setLikeResponse(like.like) : setLikeResponse('')
      })();

    }
  }, [recipeId, sessionUser]);


  const likeRecipe = async (e) => {
    e.preventDefault();
    const response = await fetch(`/api/likes/${recipeId}`, {
      method: 'POST'
    })
    const like = await response.json();
    (like.like) ? setLikeResponse(like.like) : setLikeResponse('')
    if (like.errors) {
      history.push('/login')
    }

  }

  const deleteComment = async (event, id) => {
    event.preventDefault();
    await fetch(`/api/recipes/delete/comments/${id}`, {
      method: 'DELETE'
    })
    const newComments = await fetch(`/api/recipes/comments`).then((res) => res.json())
    return setComments(newComments.comments)
  }
  let singularOrPlural;
  if (currentRecipe?.comments?.length > 1) {
    singularOrPlural = "Comments"
  } else {
    singularOrPlural = "Comment"
  }
  const postingComment = () => {
    setCanComment(true)
    setCommenting(true)
  }

  let innerWhiteBox;
  if (commenting) {
    innerWhiteBox = (
      <>
        {canComment && newCommentBox}
      </>
    )
  } else {
    innerWhiteBox = (
      <>
        <button id="post-comment-button" onClick={() => postingComment()}><i className="fas fa-comments" id="fasComments"></i>Post Comment</button>
      </>
    )
  }
  // Code about Likes end here
  // console.log(currentRecipe)
  return (
    <div id="main">
      <div id="recipe-info">
        <h1 id="recipe-title">{currentRecipe.title}</h1>
        <p id="author-and-tags">By {currentRecipe?.author?.username} {">"} {currentRecipe.tags && currentRecipe.tags[0].name.charAt(0).toUpperCase() + currentRecipe.tags[0].name.slice(1)}</p>
        <p id="likes-display"><i className="fas fa-heart"
          style={{ color: '#F27D21' }} id="likeButton"></i>{currentRecipe.likes && currentRecipe.likes.length} </p>
      </div>
      <div id="like-button-and-photo-container">
        <div id="like-license-buttons">
          <button id="like-button" onClick={likeRecipe} >
            {likeResponse ? <i className="fas fa-heart"
              style={{ color: '#F27D21' }} id="likeButton"></i> : <i className="fas fa-heart" id="likeButton"></i>} Like
          </button>
        </div>
        <div style={{ display: 'flex', justifyContent: 'space-around', gap: '10px', alignItems: 'end', flexWrap: 'wrap', marginBottom: '1%' }}>
          {media1To5?.map((el, i) => (
            <div key={`mediaDiv${i}`}
            >{
                !isVideo(el) && <img
                  key={`recipePhoto${i}`}
                  style={{ width: '400px', height: '400px', borderRadius: '7px' }}
                  src={el} alt='RecipePhoto' />}
            </div>
          ))}

          {videoArr.map((el, i) => (
            el && isVideo(el[0]) &&
            <div key={`videoDiv${i}`} style={{ display: 'flex', alignItems: 'end' }}>
              <ReactPlayer
                key={`videoRecactPlayer${i}`}
                url={el[0]}
                playing={el[1]}
                loop
                style={{
                  display: 'inline',
                  marginBottom: '10px',
                  padding: '0',
                  width: "600px",
                  height: "600px",
                }} />
              <button
                key={`videoRecactPlayButton${i}`}
                style={{ maxHeight: '48px' }}
                className='btn-category-header'
                onClick={e => {
                  e.preventDefault()
                  el[2](play => !play)
                }}>{el[1] ? 'Pause' : 'Play'}</button>
            </div>
          ))}
        </div>
      </div>
      <div id="author-info">
        <div id="top-author-info">
          <div id="author-image">
            <img className="profileCircleRecipe" src={(currentRecipe?.author?.profilePic) ? currentRecipe?.author?.profilePic : defaultPhoto} alt="profile" />
          </div>
          <span id="by-prefix">{` By `}</span>
          <span id="by-username">{(currentRecipe?.author?.username)}</span>
          <div id="more-by-author">
            <p id="more-by-author-text">More by <br />
              the author:</p>
          <div id="other-recipes-by-author">
            {whatIWant && whatIWant.map((recipe, i) => {
              return (<><a key={`linktoRecipe${i}`} href={`/recipes/${recipe.id}`}>{recipe.title}</a> <br key={`linktoRecipeBr${i}`} /></>)
            })}
          </div>
          </div>
          <div id="author-bio-container">
            <div id="author-bio">
              <p>About: {currentRecipe?.author?.biography}</p>
            </div>
          </div>
        </div>
      </div>
      <div id="recipe-description">
        <p>{currentRecipe?.description}</p>
      </div>
      <div id="comment-button-container">
        <a href="#comments-section" id="comment-button"><i className="fas fa-comments" id="fasComments"></i>Comment</a>
      </div>
      <div id="ingredients-container">
        <h1 id="ingredients-title">Ingredients</h1>
        <div id="ingredients-list-container">
          <ul id="ingredients-list">
            {currentRecipe?.ingredients?.map((ingredient, index) => {
              return (
                <li key={'currentIngredient' + index} id="ingredient">{ingredient.info}</li>
              )
            })}
          </ul>
        </div>
        <a href="#comments-section" id="comment-button"><i className="fas fa-comments" id="fasComments"></i>Comment</a>
      </div>
      {currentRecipe?.instructions?.map((instruction, index) => {
        return (
          <div key={'currentRec' + index} id="step">
            <p key={'p' + index}><strong> Step {index + 1}: {instruction.stepTitle}</strong></p>
            <Instruction key={'instruction' + index} instruction={instruction} />
          </div>
        )
      })}
      <div id="centering-div">
        <div id="add-comment-box">
          <div id="user-image">
            <img id="comment-profileCircle" className="profileCircle" src={sessionUser?.profilePic? sessionUser.profilePic : 'https://www.pngitem.com/pimgs/m/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png'} alt="profile" />
          </div>
          <div id="inner-white-box">
            {innerWhiteBox}
          </div>
          <div id="bottom-of-the-white-box">
            <p id="comment-note">If you ain't got nothin' nice to say, don't say nothin' at all.</p>
            <div id="post-comment-button-div">
              <button id="little-post-comment-button" type='submit' form="comment-form">Post</button>
            </div>
          </div>
        </div>
      </div>
      <div id="comments-section">
        <h1>{currentRecipeComments?.length} {singularOrPlural} </h1>
        {currentRecipeComments?.map((comment, i) => {
          const thisIsMyComment = sessionUser && sessionUser.id === comment.userId
          return (
            <div id="comment" key={`comment${i}`} style={{ backgroundColor: canEdit ? "#f6f6f6" : "white", border: canEdit ? "1px solid #dedede" : "none", borderRadius: canEdit ? "5px" : "none" }}>
              <div id="owner-name-and-buttons-container" style={{ width: !canEdit ? "100%" : "30%" }}>
                <div id="comment-image-username-date">
                  <img className="profileCircle" id="comment-profileCircle" src={comment.user.profilePic? comment.user.profilePic : 'https://www.pngitem.com/pimgs/m/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png'} alt="author" />
                  <a id="comment-owner-username" href={`/users/${comment.userId}`}>{comment.user.username}</a>
                  {!canEdit && <p id="comment-date">{new Date(comment.time_created).toLocaleDateString("en-US")}</p>}
                </div>
                {thisIsMyComment && !canEdit &&
                  <div id="comment-owner-buttons">
                    <button className="commentButtons" onClick={() => setCanEdit(true)}>Edit</button>
                    <button className="commentButtons" onClick={(e) => deleteComment(e, comment.id)}>Delete</button>
                  </div>}
              </div>
              {thisIsMyComment && canEdit && <EditComment currentRecipe={currentRecipe} setCanEdit={setCanEdit} setComments={setComments} comment={comment} />}
              {(!canEdit || !thisIsMyComment) && <p id="comment-text">{comment.comment}</p>}
            </div>
          )
        })}
      </div>
    </div>
  )
}
export default SingleRecipePage
