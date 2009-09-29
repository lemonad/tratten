    $(".rounded-corners").corner();
    $(".rounded-top").corner("top");
    $(".rounded-bottom").corner("bottom");

    $("#set-focus").focus();
    $("#logo").hover(function() {
        $(this).attr('src', "{{ MEDIA_URL }}/images/tratten-logo-blue-hover.png");
      }, function() {
        $(this).attr('src', "{{ MEDIA_URL }}/images/tratten-logo-blue.png");
    });
    $("#small-logo").hover(function() {
        $(this).attr('src', "{{ MEDIA_URL }}/images/tratten-logo-small-blue-hover.png");
      }, function() {
        $(this).attr('src', "{{ MEDIA_URL }}/images/tratten-logo-small-blue.png");
    });
