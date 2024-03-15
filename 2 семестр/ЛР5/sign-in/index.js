

var forms = document.querySelectorAll('.needs-validation')
  
Array.prototype.slice.call(forms)
    .forEach(function (form) {
        form.addEventListener('submit', function (event) {
            let checkboxes = document.querySelectorAll("input[type=checkbox]");
            
            let isLangSelected = false;

            checkboxes.forEach(checkbox => {
                isLangSelected = isLangSelected || checkbox.checked;
            });


            if(!isLangSelected || !form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();

                form.classList.add('was-validated');

                return;
            }
            
            form.classList.remove('was-validated');
            form.reset();   
        }, false)
    });



