// ---------- Start Save Value Script ---------- \\

// After click submit this function save the select type of cipher, text, key and mode,
// and reload the value again after the page load to not lose the last values after submit or reload

// Wrap the code in an event listener that waits for the page to load
window.addEventListener('load', function() {

  // Function to save form values to local storage
  function saveFormValues() {

    // Get input fields and select element type of cipher, text, key and mode
    const inputFields = document.querySelectorAll('input, textarea, select');

    // Save values for each field to local storage
    inputFields.forEach(field => {
      localStorage.setItem(field.id, field.value);
    });
  }
  // Add event listener to the submit button
  const submitBtn = document.querySelector('input[type="submit"]');

  // run the save function after click submit
  submitBtn.addEventListener('click', saveFormValues);

  // Function to load saved form values from local storage
  function loadFormValues() {

    // Get input fields and select element
    const inputFields = document.querySelectorAll('input, textarea, select');

    // Set input values
    inputFields.forEach(field => {
      const savedValue = localStorage.getItem(field.id);
      if (savedValue) {
        field.value = savedValue;
      }
    });
  }
  // Load saved form values when the page loads
  loadFormValues();
});
  
// ---------- End Save Value Script ---------- \\


// ---------- Start Copy Button Script ---------- \\

// This script defines a function that copies the text content of the result text
// to the user's clipboard. The function adds a click event listener to the copy button 

// Function to copy result text to clipboard
function copyResultToClipboard() {

  // Find the result text element That have the class "result_text"
  const resultText = document.querySelector('.result_text');

  // Create a new range object
  const range = document.createRange();

  // Select the contents of the "result_text" element
  range.selectNode(resultText);

  // Add the range to the current selection
  window.getSelection().addRange(range);
  
  // Copy trimmed text to clipboard
  // Get the text content of the "result_text" element and remove any leading/trailing whitespace or emply lines
  const trimmedText = resultText.textContent.trim();

  // Write the trimmed text to the clipboard
  navigator.clipboard.writeText(trimmedText);
  
  // Deselect text
  // Remove all ranges from the current selection
  window.getSelection().removeAllRanges();
}

// Wrap the code in an event listener that waits for the page to load
window.addEventListener('load', function() {

  // Find the HTML copy button with the ID "copy-button"
  const copyButton = document.getElementById('copy-button');

  // Add a click event listener to the copy button that calls the copy function
  copyButton.addEventListener('click', copyResultToClipboard);
});

// ---------- End Copy Button Script ---------- \\


// ---------- Start toggle Script ---------- \\

// Tthis function is toggle the visibility of the key input elements based on the selected cipher
// By default all keys fields and descriptions are hiden with style
// the script track the change in the select field "cipher", then change style to block to make it appear,
// and hide everything else from the key section

function toggleCipherKeyInput() {

  // Get a reference to the select cipher by id "type"
  var selectBox = document.getElementById("type");
  
  // Get current cipher by take the value from selected option's
  var selectedValue = selectBox.options[selectBox.selectedIndex].value;

  // Find the key input element with a class name that matches the selected cipher
  const keyInput = document.querySelector(`.${selectedValue}-key-input`);
  
  // If the key input element exists, show it by setting its display style to "block"
  if (keyInput) {
    keyInput.style.display = 'block';
  }
  
  // Retrieve all the key input elements
  const allKeyInputs = document.querySelectorAll('.cipher-key-input');
  
  // Loop through each key section
  allKeyInputs.forEach(input => {

    // If the key section is not much the selected cipher, hide it by setting its display style to "none"
    if (input !== keyInput) {
      input.style.display = 'none';
    }
  });
}

// ---------- End toggle Script ---------- \\


// ---------- Start Clear And Paste Buttons Script ---------- \\

// This script adds functionality to two buttons, "Clear Text" and "Paste Text",
// which clear and paste text into the textarea, respectively

// wait for the page to fully load before running the code
window.addEventListener('load', function() {

  // Get the button element with the id "clear-text-btn" and assign it to a variable called clearTextBtn
  var clearTextBtn = document.querySelector('#clear-text-btn');
  
  // Get the button element with the id "paste-text-btn" and assign it to a variable called pasteTextBtn
  var pasteTextBtn = document.querySelector('#paste-text-btn');
  
  // Get the textarea element with the id "plaintext" and assign it to a variable called plaintextTextarea
  var plaintextTextarea = document.querySelector('#plaintext');
  
  // Add an event listener to the clearTextBtn that listens for a click.
  clearTextBtn.addEventListener('click', () => {

    // Sets the value of the plaintextTextarea to an empty string
    plaintextTextarea.value = '';
  });
  
  // Add an event listener to the pasteTextBtn that listens for a click.
  pasteTextBtn.addEventListener('click', () => {

    // Reads the text from the clipboard
    navigator.clipboard.readText().then((text) => {

      // Sets the value of the plaintextTextarea to the text that was read
      plaintextTextarea.value = text;
    });
  });
});

// ---------- End Clear And Paste Buttons Script ---------- \\


// ---------- Start Download Button Script ---------- \\

// When the button is clicked, the script start downloading
// the file that already created by main app in "static/file.txt" is downloaded.
// with the text appear in result area

// Add event to make sure that the script run with the page load
window.addEventListener('load', function() {

  // Get the download button element by ID
  const downloadBtn = document.getElementById('download-btn');
  
  // Define the URL based on file location to be downloaded
  const downloadUrl = "static/file.txt";
  
  // Add a click event listener to the download button
  downloadBtn.addEventListener('click', () => {
    
    // Create a new anchor element
    const anchor = document.createElement('a');
    
    // Set the href attribute of the anchor element to the download URL
    anchor.href = downloadUrl;
    
    // Set the download attribute of the anchor element to the file name
    anchor.setAttribute('download', 'file.txt');
    
    // Simulate a click on the anchor element to start the download
    anchor.click();
  });
});

// ---------- End Download Button Script ---------- \\


// ---------- Start Button onClick (Change text) ---------- \\

// This script modifies the text of all buttons with type="button" when clicked,
// showing a message stored in the button's "value" attribute for 1.5 seconds,
// then restoring the original button text.

// Define a function to handle button clicks
function ClickButtons() {

  // Get all buttons with type="button"
  const buttons = document.querySelectorAll('button');

  // Loop through each button
  buttons.forEach(button => {

    // Save the original button text
    const originalText = button.textContent;

    // Add a click event listener to the button
    button.addEventListener('click', () => {

      // Get the message to show from the button's "value" attribute
      const message = button.value;

      // Change the button text to the message
      button.textContent = message;
      
      // After 1.5 seconds, change the button text back to the original text
      setTimeout(() => {
        button.textContent = originalText;
      }, 1500);
    });
  });
}

// Call the ClickButtons function when the page finishes loading
window.addEventListener('load', function() {
  ClickButtons();
});

// ---------- End Button onClick (Change text) ---------- \\

