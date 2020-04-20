/*
//CATEGORY LIST WILL BE OBTAINED FROM A TABLE IN DATABASE OR OBTAINED THROUGH API
var categoryList = [
    {name:'Gandhi Maidan',location:'Gandhi Maidan, Patna',distance:1.9,congestion:1},
    {name:'Buddha Smriti Park',location:'Near Patna Junction, Patna',distance:2.2,congestion:3},
    {name:'Eco Park',location:'Rajbansi Nagar, Patna',distance:3.6,congestion:0},
    {name:'Lohiya Park',location:'Kankarbagh, Patna',distance:5.6,congestion:4},
    {name:'S. K. Puri Park',location:'Kidwaipuri, Patna',distance:10.3,congestion:2},
    {name:'Shivaj Park',location:'Lohia Nagar, Patna',distance:18.2,congestion:1},
    {name:'Kumhrar Park',location:'Kumhrar Patna',distance:21.2,congestion:1}
];

//CONGESTIONMAP CAN BE A TABLE IN DATABASE (ALTHOUGH NOT NECESSARY)
var congestionMap = [
    {congestionLabel:'closed',iconLink:'static/img/closed.png'},
    {congestionLabel:'low',iconLink:'static/img/free.png'},
    {congestionLabel:'moderate',iconLink:'static/img/moderate.png'},
    {congestionLabel:'high',iconLink:'static/img/crowded.png'},
    {congestionLabel:'very high',iconLink:'static/img/overcrowded.png'}
];

//ITERATIVELY LOAD THE TABLE ROWS AND CREATE HTML CONTENT FOR EACH ELEMENT OF A CATEGORY (FOR PARK OR MUSEUM ETC.)
var htmlcontent;
for (var j = 0; j < categoryList.length ; j++){
    var htmlcontent = '<div class = "categoryElement"><div class="labelsLeft"><p class="nameLabel">'+categoryList[j].name+'</p><p class="secondaryLabel">'+categoryList[j].location+'</p></div><div class="rightBlock"><div class="distanceBlock"><p class="distanceLabel">'+categoryList[j].distance+'</p><p class="distanceLowerLabel">km away</p></div><div class="borderline"></div><div class="congestionBlock"><img class="congestionIcon" src="'+congestionMap[categoryList[j].congestion].iconLink+'"><p class="congestionLabel">'+congestionMap[categoryList[j].congestion].congestionLabel+'</p></div></div></div>';
	document.querySelector('.containerBox').insertAdjacentHTML('beforeend',htmlcontent);
}

var categoryElements = Array.from(document.querySelectorAll('.categoryElement'));
var selectedElement;

// GET THE SELECTED ELEMENT
categoryElements.forEach(function(current,index){
	current.addEventListener('click',function(){
        selectedElement = current.children[0].children[0].innerHTML;
        console.log(selectedElement);
        //GO TO VIEW DETAILS PAGE

        //window.location = 'selected/detailsPage'
        
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

/***************DIV*********************/
function detailsPage(value){
 window.location ='detailsPage/' + value
}