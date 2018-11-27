// View password when eye icon is clicked.
var pwd = document.getElementById('password');
var eye = document.getElementById('eye');

eye.addEventListener('click', togglePass);

function togglePass() {
  eye.classList.toggle('active');
  (pwd.type == 'password') ? pwd.type='text' : pwd.type='password';
};

// Make sure age is valid.
$('#age').keyup(function() {
  if (!this.value.match(/^\d{1,3}$/)) {
    alert("Invalid age");
    this.value = this.value.replace(this.value, '');
  };
});
