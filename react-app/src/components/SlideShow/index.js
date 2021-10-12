import React from "react";

function SlideShow(recipe) {
  return (
    <>
      {recipe?.map(img => <img src={img} alt="recipe"/>)}
    </>
  )
}

export default SlideShow
