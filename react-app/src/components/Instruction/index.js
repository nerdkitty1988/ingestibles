import { React } from "react";
import "./Instruction.css"

const Instruction = (instruction) => {
  return(
  <div id="step">
    <p>**** Instruction Step Name **** <br/><br/> {instruction.instruction.stepTitle}</p>
    <img src={instruction.instruction.imageUrl} alt="step"/>
    <p>**** Instruction Step Directions **** <br/><br/> {instruction.instruction.directions}</p>
    <button>Comment</button>
  </div>
)

}


export default Instruction
