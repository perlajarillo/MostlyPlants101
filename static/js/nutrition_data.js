$(function() {
  $(".ingredients").change(function() {
    let nutrients = $(this)
      .prop("name")
      .split("|");
    if (nutrients[0] !== "None") {
      const previousCalories = parseFloat($("#calories").val());
      const calories = parseFloat(nutrients[0]);
      const previousCarbs = parseFloat($("#carbs").val());
      let carbs = parseFloat(nutrients[1]);
      const previousFat = parseFloat($("#fat").val());
      const fat = parseFloat(nutrients[2]);
      const previousProtein = parseFloat($("#protein").val());
      const protein = parseFloat(nutrients[3]);
      if ($(this).prop("checked")) {
        $("#calories").val((calories + previousCalories).toFixed(2));
        $("#carbs").val((carbs + previousCarbs).toFixed(2));
        $("#fat").val((fat + previousFat).toFixed(2));
        $("#protein").val((protein + previousProtein).toFixed(2));
      } else {
        $("#calories").val((previousCalories - calories).toFixed(2));
        $("#carbs").val((previousCarbs - carbs).toFixed(2));
        $("#fat").val((previousFat - fat).toFixed(2));
        $("#protein").val((previousProtein - protein).toFixed(2));
      }
    }
  });
});
