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

  //datepicker

  const elems = document.querySelector('.datepicker');
  M.Datepicker.init(elems, {
        format: "dd mmmm, yyyy",
        yearRange: 15,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });


//slider
//const slider = document.querySelector('.slider');
//M.Sidenav.init(slider, {
  //  indicators: false,
    //height: 500,
    //transition: 500,
    //interval: 6000    
//});
