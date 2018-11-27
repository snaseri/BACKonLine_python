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

function back() {
  console.log("Back button");
  var direction = document.getElementById("direction").value;
  document.getElementById("direction").value = "back"
  var calculation = document.getElementById("questnum").value;
  var counter = document.getElementById("counter").innerHTML;
  console.log(direction);
  if (counter == calculation && counter !=1 ) {
    document.getElementById("questnum").value -= 1
  };
  if (calculation-counter == 1) {
    document.getElementById("questnum").value = calculation - 2;
  };
};

function forward() {
  console.log("Next button");
  var direction = document.getElementById("direction").value;
  document.getElementById("direction").value = "forward";
  var calculation = parseInt(document.getElementById("questnum").value);
  var counter = document.getElementById("counter").innerHTML;
  console.log("Next button");
  var direction = document.getElementById("direction").value;
  document.getElementById("direction").value = "forward";
  var calculation = parseInt(document.getElementById("questnum").value);
  var counter = document.getElementById("counter").innerHTML;
  if (counter == calculation) {
    document.getElementById("questnum").value = calculation + 1;
  };
  if (counter-calculation == 1) {
    document.getElementById("questnum").value = calculation + 2;
  };
  console.log(direction);
};

function validate() {
  var valid = document.getElementsByName("option-text[]");
  var hasChecked = false;
  for (var i = 0; i < valid.length; i++) {
    if (valid[i].checked) {
      hasChecked = true;
      break
    }
  };
  if (hasChecked == false) {
    alert("Please select at least one option");
    return false;
  };
  return true;
};
