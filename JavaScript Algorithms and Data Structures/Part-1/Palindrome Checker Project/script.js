const checkBtn = document.getElementById("check-btn");
let textInput = document.getElementById("text-input");

const checkPalindrome = () => {
  let input = textInput.value;

  if (!input) {
    alert("Please input a value");
    return;
  }

  let cleanStr = input.toLowerCase().replace(/[^a-z0-9]/g, "");
  let reversedStr = cleanStr.split("").reverse().join("");
  let resultText = input + (cleanStr === reversedStr ? " is a palindrome." : " is not a palindrome.");
  
  document.getElementById("user-input").textContent = resultText;
  document.querySelector(".hidden").style.display = "block";
}


checkBtn.addEventListener("click", checkPalindrome);