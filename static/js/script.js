//sidenav
const sideNav = document.querySelector('.sidenav');
M.Sidenav.init(sideNav, {edge: "right"});

//slider
const slider = document.querySelector('.slider');
M.Sidenav.init(slider, {
    indicators: false,
    height: 500,
    transition: 500,
    interval: 6000    
});
