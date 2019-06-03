function inputValidation() {
  let valid = true;
  let num = 0;
  let bowl_name = document.getElementById("bowl_name");
  if (bowl_name.value == "") {
    bowl_name.className += " is-invalid";
    valid = false;
  }

  let ingredients = document.getElementsByClassName("ingredients");
  for (i = 0; i < ingredients.length; i++) {
    if (ingredients[i].checked) {
      num++;
    }
  }
  if (num < 3) {
    document.getElementById("error").innerHTML =
      "Please select at least 3 ingredients (you have chosen " + num + ").";
    valid = false;
  } else {
    document.getElementById("error").innerHTML = "";
  }
  return valid;
}
