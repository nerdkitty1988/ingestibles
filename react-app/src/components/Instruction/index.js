import { React } from "react";


const Instruction = (instruction) => {
  return(
  <>
    <p>**** Instruction Step Name **** <br/><br/> {instruction.instruction.stepTitle}</p>
    <img src={instruction.instruction.imageUrl} alt="step"/>
    <p>**** Instruction Step Directions **** <br/><br/> {instruction.instruction.directions}</p>
    <button>Comment</button>

  </>
)

}


export default Instruction
