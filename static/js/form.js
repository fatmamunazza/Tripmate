

/***************NAVBAR*********************/
var mediaWidth = window.matchMedia("(min-width: 640px)")

function openNav() {
    if (mediaWidth.matches) {
        document.querySelector(".sidenav").style.width = "30vw";
      } else {
        document.querySelector(".sidenav").style.width = "60vw";
      }
      document.querySelector(".navSlideMenu").style.display = "None";
  }
  
  function closeNav() {
    document.querySelector(".sidenav").style.width = "0";
    document.querySelector(".navSlideMenu").style.display = "flex";
  }
