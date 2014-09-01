$(document).ready(function() {
  $('#main-menu').onePageNav();
  $('.tabnav').click(function (event){
    $('#contact a[href="#' + this.dataset['tab'] + '"]').tab('show');
  });
});
