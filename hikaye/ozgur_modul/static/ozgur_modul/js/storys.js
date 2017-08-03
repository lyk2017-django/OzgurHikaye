$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-book").modal("show");
      },
      success: function (data) {
        // Form verisini model window içine yazdır
        $("#modal-book .modal-content").html(data.html_form);

        // Hikaye listesini refrest et
        if(data.html_story_list != "") $("#storys-table tbody").html(data.html_story_list);

      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#storys-table tbody").html(data.html_story_list);
          $("#modal-book").modal("hide");
        }
        else {
          $("#modal-book .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  var likeForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      success: function (data) {
        if (data.basarili) {
            alert("Başarılı "+data.like+" adet beğeni var")
        }
        else {
            alert("Hata oluştu tekrar deneyin")
        }
      }
    });
  };

  /* Binding */

  // Create book
  $(".js-create-story").click(loadForm);
  $("#modal-book").on("submit", ".js-story-create-form", saveForm);

  $("#storys-table").on("click", ".js-view-story", loadForm);

  $("#storys-table").on("click", ".js-new-cont", loadForm);
  $("#modal-book").on("submit", ".js-cont-create-form", saveForm);


});
