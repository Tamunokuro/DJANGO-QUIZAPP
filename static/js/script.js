'use strict';
console.log('Hello quizapp')


let i;
let score = 0;
var checkBtn = document.getElementById("next");

function selectAnswer() {
  let option = document.getElementsByName("option");
  for (i = 0; i < option.length; i++) {
    if (option[i].checked) {
      let checked_val = option[i].value;
      if (checked_val == answerLabel.value) {
        console.log("Correct");
        document.getElementById("check").disabled = true;
        document.getElementById("option1").disabled = true;
        document.getElementById("option2").disabled = true;
        document.getElementById("option3").disabled = true;
        document.getElementById("option4").disabled = true;
        result_div.innerHTML = `
				<div class="h5 mb-3"><b>Correct</b></div>
				`;
      } else {
        console.log("Wrong");
        document.getElementById("check").disabled = true;
        document.getElementById("option1").disabled = true;
        document.getElementById("option2").disabled = true;
        document.getElementById("option3").disabled = true;
        document.getElementById("option4").disabled = true;
        result_div.innerHTML = `
				<div class="h5 mb-3"><b>Wrong, Correct answer is ${answerLabel.value}</b></div>
				`;
      }
    }
  }
}

let totalScore = document.getElementById("totalScore"); //id of the total score text field
let userScore = 0;
function scoreAdd(){
  if(checkBtn){
    checkBtn.addEventListener("click", function (e){
      
      let ele = document.getElementsByName("option");
      for (i = 0; i < ele.length; i++) {
        if (ele[i].checked) {
          let checked_val = ele[i].value;
          if (checked_val == answerLabel.value) {
            userScore += 1;
            score = Number(totalScore.value) + userScore;
            sessionStorage.setItem("userScore", score);
            console.log(score);
          }
        }
      }
    })
    
    }
  }


