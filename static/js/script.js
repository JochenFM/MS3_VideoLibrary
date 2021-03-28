//sidenav
const sideNav = document.querySelector('.sidenav');
M.Sidenav.init(sideNav, { edge: "right" });

//slider

const slider = document.querySelector('.slider');
M.Slider.init(slider, {
    indicators: true,
    height: 600,
    transition: 700,
    interval: 6000
});

//category selector

const select = document.querySelector('select');
M.FormSelect.init(select, {
});


//datepicker

const datepicker = document.querySelector('.datepicker');
M.Datepicker.init(datepicker, {
    format: "dd mmmm, yyyy",
    yearRange: 15,
    showClearBtn: true,
    i18n: {
        done: "Select"
    }
});

//collapsible video card

const collapsible = document.querySelector('.collapsible');
M.Collapsible.init(collapsible, {
});


//tooltips delete/edit icons library.html goes here

// modal for delete icon library.html goes here




//document.addEventListener('DOMContentLoaded', function() {
    //const modal = document.querySelectorAll('.modal');
    //M.Modal.init(modal);
  //});






//slider
//const slider = document.querySelector('.slider');
//M.Sidenav.init(slider, {
//  indicators: false,
//height: 500,
//transition: 500,
//interval: 6000    
//});


//category select validation from CI's TIm Nelson

validateMaterializeSelect();
function validateMaterializeSelect() {
    let classValid = "border-bottom: 1px solid #4caf50; box-shadow: 0 1px 0 0 #4caf50;";
    let classInvalid = "border-bottom: 1px solid #f44336; box-shadow: 0 1px 0 0 #f44336;";
    let selectValidate = document.querySelector("select.validate");
    let selectWrapperInput = document.querySelector(".select-wrapper input.select-dropdown");
    if (selectValidate.hasAttribute("required")) {
        selectValidate.style.cssText = "display: block; height: 0; padding: 0; width: 0; position: absolute;";
    }
    selectWrapperInput.addEventListener("focusin", (e) => {
        e.target.parentNode.addEventListener("change", () => {
            ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
            for (let i = 0; i < ulSelectOptions.length; i++) {
                if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled") {
                    e.target.style.cssText = classValid;
                }
            }
        });
    });
    selectWrapperInput.addEventListener("click", (e) => {
        ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
        for (let i = 0; i < ulSelectOptions.length; i++) {
            if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled" && ulSelectOptions[i].style.backgroundColor == "rgba(0, 0, 0, 0.03)") {
                e.target.style.cssText = classValid;
            } else {
                e.target.addEventListener("focusout", () => {
                    if (e.target.parentNode.childNodes[3].hasAttribute("required")) {
                        if (e.target.style.borderBottom != "1px solid rgb(76, 175, 80)") {
                            e.target.style.cssText = classInvalid;
                        }
                    }
                });
            }
        }
    });
}