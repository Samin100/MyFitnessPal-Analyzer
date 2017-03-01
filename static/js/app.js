

/*TODO for vdvUpdate:
Button should not do anything if calorie field is empty. If there is a number in the
calorie field, then you should close/hide the modal, and then submit the value via
AJAX to a POST endpoint URL.
*/
function vdvUpdate(){
  calories = document.getElementById("cal").value;
  if (calories == ""){
    console.log("Empty calories value");
    return true;
  };
  console.log("Submitted " + calories);
}
