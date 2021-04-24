function myFunction() {
    var x = document.getElementById("pageHeader");
    if (x.className === "header") {
      x.className += " responsive";
    } else {
      x.className = "header";
    }
  }