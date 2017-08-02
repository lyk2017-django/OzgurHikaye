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
        $("#modal-book .modal-content").html(data.html_form);
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
          $("#book-table tbody").html(data.html_story_list);
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

  $("#model-book").on("click", ".js-new-cont", loadForm);

  // Update book
  $("#book-table").on("click", ".js-update-book", loadForm);
  $("#modal-book").on("submit", ".js-book-update-form", saveForm);

  // Delete book
  $("#book-table").on("click", ".js-delete-book", loadForm);
  $("#modal-book").on("submit", ".js-book-delete-form", saveForm);

  // Like Add
  $("#book-table").on("click", ".js-like-book", likeForm);

});
