//disallows button submit if text fields are empty
function empty() {
  var x;
  var y;
  x = document.getElementById("username").value;
  y = document.getElementById("password").value;
  if (x == "" || y == "") {
      return false;

  };
}
