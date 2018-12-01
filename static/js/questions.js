// Slider for Q20.
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

var n = 10;
var percent = 100 / n;
for (var x = 1; x < n; x++) {
  $(".range-slider" ).append("<span class='dots' style='left:"+ x * percent * .87 + "%'></span>");
};

rangeSlider();

// Green text for 'tick all' type questions.
$('h1').each(function() {
  var ques = $(this).text();
  if (ques.indexOf('Please tick all options that apply') >= 0) {
    ques = ques.replace("Please tick all options that apply","<span style='color: #00b050;'>Please tick <strong>all</strong> options that apply</span>");
    $(this).html(ques);
  } else if (ques.indexOf('Please tick all body areas that apply') >= 0) {
    ques = ques.replace("Please tick all body areas that apply","<span style='color: #00b050;'>Please tick <strong>all</strong> body areas that apply</span>");
    $(this).html(ques);
  }
})

// Code for back and next button.
function back() {
  console.log("Back button");
  var direction = document.getElementById("direction").value;
  document.getElementById("direction").value = "back"
  var calculation = document.getElementById("questnum").value;
  var counter = document.getElementById("counter").innerHTML;
  console.log(direction);
  if (counter == calculation && counter != 1 ) {
    document.getElementById("questnum").value -= 1
  }
  if (calculation-counter == 1) {
    document.getElementById("questnum").value = calculation - 2;
  }
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

// Make sure user has selected at least one option.
function validate() {
  var valid = document.getElementsByName("option-text[]");
  var hasChecked = false;
  for (var i = 0; i < valid.length; i++) {
    if (valid[i].checked) {
      hasChecked = true;
      break;
    };
  };
  if (hasChecked == false) {
    alert("Please select at least one option");
    return false;
  };
  return true;
};

// Disable other checkboxes if certain option is selected.
// Array of hard coded values.
disableOptions = ["I don't take any medication for my back pain", "I am unable to ease my back pain", "Any activity that I do for a long period of time increases my back pain", "Everything I do causes me pain", "Nothing I do stops my pain", "Nothing helped"];
// Add click event to each option.
$(".options").click(function() {
  // Store option text.
  option = $(this).find("label").text();
  // Create boolean.
  found = false;
  // Cycle through the array.
  disableOptions.forEach(function(value, index) {
    // Check if chosen option equals current element in array.
    if (option == value) {
      // Mark the found boolean as true.
      found = true;
    };
  });
  // Check if entry matched a value in the array.
  if (found == true) {
    // Check if the box has been checked.
    if ($(this).find("input").prop("checked") == true) {
      // Disable the options for this question and uncheck.
      $(this).parent().find(".options input").prop({'disabled': true, 'checked': false});
      // Re-enable the checkbox and mark it checked.
      $(this).find("input").prop({'disabled': false, 'checked': true});
    } else {
      // Re-enable all checkboxes.
      $(this).parent().find(".options input").prop('disabled', false);
    };
  };
});

function onLoad() {
  patient_id = localStorage.getItem("PatientID");
  document.getElementById("patient_id").value = patient_id;
};

function sendRadio(value) {
  console.log(value);
  option = value.innerHTML.split('<')[0];
  document.getElementById("radio").value = option;
};

function sendCheckbox(value) {
  if (value.checked == true) {
    if ((document.getElementById("counter").innerHTML == 5 && value.id.substring(12) == 16 ) || (document.getElementById("counter").innerHTML == 12 && value.id.substring(12) == 11 ) || (document.getElementById("counter").innerHTML == 14 && (value.id.substring(12) == 7 || value.id.substring(12) == 8) ) || (document.getElementById("counter").innerHTML == 15 && value.id.substring(12) == 8 ) || (document.getElementById("counter").innerHTML == 17 && value.id.substring(12) == 5 )){
      document.getElementById("checkbox").value = "[]"
      document.getElementById("checkbox").value = document.getElementById("checkbox").value.substring(0, document.getElementById("checkbox").value.length-1) + value.id.substring(12) + "," + document.getElementById("checkbox").value[document.getElementById("checkbox").value.length - 1];
    }else{
      document.getElementById("checkbox").value = document.getElementById("checkbox").value.substring(0, document.getElementById("checkbox").value.length-1) + value.id.substring(12) + "," + document.getElementById("checkbox").value[document.getElementById("checkbox").value.length - 1];
    }

  } else {
    console.log("unchecked");
    console.log(value.id.substring(12));
    document.getElementById("checkbox").value = document.getElementById("checkbox").value.replace(value.id.substring(12) + ",", "");
    };
};

function sendTextArea(value) {
  document.getElementById("textarea").value = value.value;
};

// Display body map.
$('#human-body').maphilight();
