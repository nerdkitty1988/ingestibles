import { React } from "react";
import "./Instruction.css"

const Instruction = (instruction) => {
  return(
    <div id="step-details">
      <img src={instruction.instruction.imageUrl} alt="step"/>
      <br/><br/>
      <p>{instruction.instruction.directions}</p>
      <div id="comment-button-container">
        <a href="#comments-section" id="comment-button"><i className="fas fa-comments"></i>Comment</a>
      </div>
    </div>
  )
}


export default Instruction
