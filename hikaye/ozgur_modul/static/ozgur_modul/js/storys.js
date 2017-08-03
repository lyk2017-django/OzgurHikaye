$(function () {

  /* Functions */

  var likeDislikeUpdate = function () {
    $(".js-btn-like, .js-btn-dislike").hide("slow")
    $("#LikeDislikeBtn").html("Teşekkürler...")
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      success: function (data) {
        // Hikaye listesini refrest et
        if(data.html_story_list != "") $("#storys-table tbody").html(data.html_story_list);
      }
    });
  };

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

  // Yeni Hikaye Başlatma Ekranını aç
  $(".js-create-story").click(loadForm);

  // Yeni Hikayeyi Kaydet
  $("#modal-book").on("submit", ".js-story-create-form", saveForm);

  // Hikayeye yapılan katkıları listele
  $("#storys-table").on("click", ".js-view-story", loadForm);

  // Hikayeye katkıda bulun ekranını aç
  $("#storys-table").on("click", ".js-new-cont", loadForm);
  
  // Hikayeye yapılan katkıyı kaydet
  $("#modal-book").on("submit", ".js-cont-create-form", saveForm);
  
  // Beğendim ve Beğenmedim düğmeleri
  $("#modal-book").on("click", ".js-btn-like", likeDislikeUpdate);
  $("#modal-book").on("click", ".js-btn-dislike", likeDislikeUpdate);
  


});
