$(document).ready(function() {
  $('#contact a[href="#employers"]').tab('show');
  $('#contact a[href="#candidates"]').tab('show');
  $('#main-menu').onePageNav();
  $('.tabnav').click(function (event){
    $('#contact a[href="#' + this.dataset['tab'] + '"]').tab('show');
  });
  $('form button').click(function (event){
    $('#' + this.classList[this.classList.length-1] + '_form').submit();
  });
});
