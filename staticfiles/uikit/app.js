// Invoke Functions Call on Document Loaded
// document.addEventListener('DOMContentLoaded', function () {
//   hljs.highlightAll();
// });

let alertwrapper = document.querySelector('.alert')
let alertclose = document.querySelector('.alert__close')

if (alertwrapper) {
  alertclose.addEventListener('click', () =>
    alertwrapper.style.display = 'none'
  )
}

// document.getElementsByClassName("butter").style.marginLeft = "1000px"

// document.addEventListener('DOMContentLoaded', function () {
//   hljs.highlightAll();
// });


