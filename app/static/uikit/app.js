// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  // hljs.highlightAll();
});

let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')


if (alertWrapper) {
  // console.log('alert wrapper found')
  alertClose.addEventListener('click', () => {
    // console.log('alert close clicked')
    alertWrapper.style.display = 'none'
    }
  )
}