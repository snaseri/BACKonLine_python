var rangeSlider = function() {
  var slider = $('.range-slider');
  var range = $('.range-slider-range');
  var value = $('.range-slider-value');

  slider.each(function() {
    value.each(function() {
      var value = $(this).prev().attr('value');
      $(this).html(value);
    });

    range.on('input', function() {
      $(this).next(value).html(this.value);
    });
  });
};

rangeSlider();

$('h1').each(function() {
  var ques = $(this).text();
  if (ques.indexOf('Please tick all options that apply') >= 0) {
    ques = ques.replace("Please tick all options that apply","<span style='color: #00b050;'>Please tick <strong>all</strong> options that apply</span>");
    $(this).html(ques);
  } else if (ques.indexOf('Please tick all body areas that apply') >= 0) {
    ques = ques.replace("Please tick all body areas that apply","<span style='color: #00b050;'>Please tick <strong>all</strong> body areas that apply</span>");
    $(this).html(ques);
  };
});
