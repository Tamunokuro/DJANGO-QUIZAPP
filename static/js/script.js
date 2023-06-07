'use strict';
console.log('Hello quizapp')


let i;
var checkBtn = document.getElementById("check");
var dummyBtn = document.getElementById("dummy");

function selectAnswer() {
  let option = document.getElementsByName("option");
  for (i = 0; i < option.length; i++) {
    if (option[i].checked) {
      let checked_val = option[i].value;
      if (checked_val == answerLabel.value) {
        
        document.getElementById("check").disabled = true;
        document.getElementById("option1").disabled = true;
        document.getElementById("option2").disabled = true;
        document.getElementById("option3").disabled = true;
        document.getElementById("option4").disabled = true;
        result_div.innerHTML = `
				<div class="alert alert-primary" role="alert">
        <b>Saved</b>
        </div>
				`;
      } else {
       
        document.getElementById("check").disabled = true;
        document.getElementById("option1").disabled = true;
        document.getElementById("option2").disabled = true;
        document.getElementById("option3").disabled = true;
        document.getElementById("option4").disabled = true;
        result_div.innerHTML = `
				<div class="alert alert-primary" role="alert">
        <b>Saved</b>
        </div>
				`;
      }
    }
  }
}

const submit = document.getElementById("submit"); //id of the total score text field
const totalScore = document.getElementById("totalScore")
const next = document.getElementById("next");
let userScore = 0;
if(submit){
  submit.addEventListener("click", function (){
    
    var ele = document.getElementsByName("option");
    for (i = 0; i < ele.length; i++) {
      if (ele[i].checked) {
        var checked_val = ele[i].value;
        if (checked_val == answerLabel.value) {
          userScore += 1;
          var score = Number(totalScore.value) + userScore;
          let myscore = sessionStorage.setItem("userScore", score);
          console.log(userScore)
         
        }
      }
    }
  })
}
if (dummyBtn) {
 dummyBtn.addEventListener("click", function () {
    totalScore.value = sessionStorage.getItem("userScore");
    console.log(totalScore)
  });
}
  




