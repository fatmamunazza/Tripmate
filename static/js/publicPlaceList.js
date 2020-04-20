//CATEGORIES CAN BE A TABLE IN DATABASE (ALTHOUGH NOT NECESSARY)

/*
var categories = [
    {label:'PARK',iconLink:'static/img/park256.png'},
    {label:'MUSEUM',iconLink:'static/img/museum256.png'},
    {label:'MONUMENT',iconLink:'static/img/monument256.png'},
    {label:'WORSHIP',iconLink:'static/img/worship256.png'},
    {label:'LAKE',iconLink:'static/img/lake256.png'},
    {label:'LIBRARY',iconLink:'static/img/library256.png'},
    {label:'AMUSEMENT PARK',iconLink:'static/img/park256.png'},
    {label:'HOTEL',iconLink:'static/img/museum256.png'},
    {label:'ZOO',iconLink:'static/img/park256.png'},
];
*/

//ITERATIVELY LOAD THE TABLE ROWS AND CREATE HTML CONTENT FOR EACH CATEGORY
/*
var htmlcontent;
for (var j = 0; j < categories.length ; j++){
    var htmlcontent = '<div class = "categoryBox"><img class = "categoryIcon" src="'+categories[j].iconLink+'"><p class = "categoryLabel">'+categories[j].label+'</p></div>';
	document.querySelector('.containerBox').insertAdjacentHTML('beforeend',htmlcontent);
}

var categoryBoxes = Array.from(document.querySelectorAll('.categoryBox'));
var selectedLabel;

// GET THE SELECTED CATEGORY
categoryBoxes.forEach(function(current,index){
	current.addEventListener('click',function(){
        selectedLabel = current.children[1].innerHTML;
        console.log(selectedLabel);

        //SEND THE SELECTED CATEGORY TO NEXT PAGE (LINK THE NEXT PAGE USING DJANGO!!!)
         window.location = 'selectedList/'+ selectedLabel;

	});
});

*/

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