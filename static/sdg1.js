function checkAnswers() {
    let score = 0;

    let q1Answer = document.querySelector('input[name="q1"]:checked');
    if (q1Answer && q1Answer.value === "right") {
        score++;
    }

   
    let q2Answer = document.querySelector('input[name="q2"]:checked');
    if (q2Answer && q2Answer.value === "right") {
        score++;
    }

 
    let q3Answer = document.querySelector('input[name="q3"]:checked');
    if (q3Answer && q3Answer.value === "right") {
        score++;
    }


    let q4Answer = document.querySelector('input[name="q4"]:checked');
    if (q4Answer && q4Answer.value === "right") {
        score++;
    }
  
    let q5Answer = document.querySelector('input[name="q5"]:checked');
    if (q5Answer && q5Answer.value === "right") {
        score++;
    }
 
    let result = document.getElementById("result");
    if (score === 5) {
        result.textContent = "Excellent! You got all the answers right! 🌟";
        result.style.color = "green";
    } else {
        result.textContent = "You got " + score + " out of 5 correct. Try again!";
        result.style.color = "orange";
    }

}