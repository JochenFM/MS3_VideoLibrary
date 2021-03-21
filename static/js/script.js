//sidenav
const sideNav = document.querySelector('.sidenav');
M.Sidenav.init(sideNav, {edge: "right"});

//slider

const carousel = document.querySelector('.carousel');
M.Carousel.init(carousel,{
    height: 500,
    transition: 500,
    interval: 6000,
    fullWidth: true,
    indicators: true
  });


//slider
//const slider = document.querySelector('.slider');
//M.Sidenav.init(slider, {
  //  indicators: false,
    //height: 500,
    //transition: 500,
    //interval: 6000    
//});
