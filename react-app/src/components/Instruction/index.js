import { React } from "react";
import "./Instruction.css"

const Instruction = (instruction) => {
  return(
  <div id="step">
    <p><strong> Step {instruction.instruction.id}: {instruction.instruction.stepTitle}</strong></p>
    <img src={instruction.instruction.imageUrl} alt="step"/>
    <br/><br/>
    <p>{instruction.instruction.directions}</p>
    <button>Comment</button>
  </div>
)

}


export default Instruction
