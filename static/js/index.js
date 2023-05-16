var $fileInput = $('.file-input');
var $droparea = $('.file-drop-area');

// highlight drag area
$fileInput.on('dragenter focus click', function() {
  $droparea.addClass('is-active');
});

// back to normal state
$fileInput.on('dragleave blur drop', function() {
  $droparea.removeClass('is-active');
});

// change inner text
$fileInput.on('change', function() {
  var filesCount = $(this)[0].files.length;
  var $textContainer = $(this).prev();

  if (filesCount === 1) {
    // if single file is selected, show file name
    var fileName = $(this).val().split('\\').pop();
    $textContainer.text(fileName);
  } else {
    // otherwise show number of files
    $textContainer.text(filesCount + ' files selected');
  }
});

  

// const pdfInput = document.getElementById("pdf-input");
// const uploadButton = document.getElementById("upload-button");
// const output = document.getElementById("output");

// uploadButton.addEventListener("click", () => {
//   // Get the selected file
//   const file = pdfInput.files[0];

//   // Check if the file is a PDF file
//   if (!file.type.startsWith("application/pdf")) {
//     alert("Please select a PDF file.");
//     return;
//   }

//   // Get the file name
//   const fileName = file.name;

//   // Check if the file name is correct
//   if (!fileName.endsWith(".pdf")) {
//     alert("Please select a valid PDF file.");
//     return;
//   }

//   // Redirect to the new page
//   window.location.href = "chat.html";
// });



// Send the received file to the server/host
const fileInput = document.querySelector('input[type="file"]');

fileInput.addEventListener('change', (event) => {
  const file = event.target.files[0];
  const formData = new FormData();
  formData.append('file', file);

  fetch('/upload', {
    method: 'POST',
    body: formData
  })
  .then(response => response.text())
  .then(() => {
    window.location.href = '/process';
  })
  .catch(error => {
    console.error('Error:', error);
  });
});
