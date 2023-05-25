let passwords = [document.getElementById('password1'),document.getElementById('password2')];
let eyes = document.getElementsByClassName('eye');
eyes = Array.from(eyes);
console.log(eyes);


eyes[0].addEventListener('click',(event)=>{

    const showHideEye = eyes[0].firstElementChild;
    if(showHideEye.classList.contains('fa-eye'))
        {

            showHideEye.classList.remove('fa-eye');
            showHideEye.classList.add('fa-eye-slash');
        }
        else{

            showHideEye.classList.remove('fa-eye-slash');
            showHideEye.classList.add('fa-eye');

        }



    if(passwords[0].type === 'password')
    {
        passwords[0].type = 'text';
    }else{
        passwords[0].type = 'password';
    }




});

eyes[1].addEventListener('click',(event)=>{

    const showHideEye = eyes[1].firstElementChild;
    if(showHideEye.classList.contains('fa-eye'))
        {

            showHideEye.classList.remove('fa-eye');
            showHideEye.classList.add('fa-eye-slash');
        }
        else{

            showHideEye.classList.remove('fa-eye-slash');
            showHideEye.classList.add('fa-eye');

        }
    if(passwords[1].type == 'password')
    {
        passwords[1].type = 'text';
    }else{
        passwords[1].type = 'password';
    }




})
