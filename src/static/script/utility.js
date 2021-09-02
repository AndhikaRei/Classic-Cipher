// Utility for client-side.

/*--------------------------------------------------------------
# Capturing HTML element
--------------------------------------------------------------*/

// Capture the uploading ciphertext/plaintext related element with dom manipulation.
const fileCiphertext = document.getElementById('file-ciphertext');
const filePlaintext = document.getElementById('file-plaintext');
const plainText = document.getElementById('plaintext');
const cipherText = document.getElementById('ciphertext');

// Capture the downloading ciphertext/plaintext related element with dom manipulation.
const btnDownloadCipher = document.getElementById('download-ciphertext');
const btnDownloadPlain = document.getElementById('download-plaintext');
const resultCipher = document.getElementById('result-ciphertext');
const resultPlain = document.getElementById('result-plaintext');

// Capture Grouping result radio Button element
const ciphertextNoSpace = document.getElementById('ciphertext-nospace');
const ciphertext5 = document.getElementById('ciphertext-5');

// Capture file and byte uploading (only used in extended vigenere page) and it's related element.
const radioEncFile = document.getElementById('encrypt-file');
const radioEncByte = document.getElementById('encrypt-byte');
const radioDecFile = document.getElementById('decrypt-file');
const radioDecByte = document.getElementById('decrypt-byte');
const plaintextInput = document.getElementById('plaintext-forminput');
const ciphertextInput = document.getElementById('ciphertext-forminput');

/*--------------------------------------------------------------
# Function and Procedure declaration
--------------------------------------------------------------*/

// Function to add space every 5 character.
function fiveCharGrouping(result){
    return result.split('').reduce((a, e, i) => a + e + (i % 5 === 4 ? ' ' : ''), '');
}

// Function to make no space in a string.
function noSpaceGrouping(result){
    return result.replace(/\s/g, '');
}

// Function for downloading decrypted or encrypted data.
function downloadFile(data) {
    const filename = Date.now();
    const filetype = "text/plain";
    const filecontent = [data]

    var file = new Blob(filecontent, {
        filetype
    });

    // Handling unsupported browser.
    if (window.navigator.msSaveOrOpenBlob)
        window.navigator.msSaveOrOpenBlob(file, filename);
    else {

        var a = document.createElement("a")
        var url = URL.createObjectURL(file);

        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();

        setTimeout(function () {
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        }, 0);
    }
}

/*--------------------------------------------------------------
# Event Listener.
--------------------------------------------------------------*/

// Add event listener for loading plaintext file, so it will automaticaly change 
// plaintext textarea value.
filePlaintext.addEventListener('change', (event) => {
    const fileList = event.target.files;
    if (fileList[0].type != "text/plain") {
        return;
    }
    const fr = new FileReader();
    fr.onload = function () {     
        plainText.value = fr.result.replace(/[\W_0-9]/g, '');
    }
    fr.readAsText(fileList[0]);
});

// Add event listener for loading ciphertext file, so it will automaticaly change 
// ciphertext textarea value.
fileCiphertext.addEventListener('change', (event) => {
    const fileList = event.target.files;
    if (fileList[0].type != "text/plain"){
        return;
    }
    const fr = new FileReader();
    fr.onload = function () {
        const cipher = fr.result.replace(/[\W_0-9]/g, '');
        cipherText.value = cipher.toUpperCase();
    }
    fr.readAsText(fileList[0]);
});

// Add event listener for grouping result.
if (ciphertextNoSpace) {
    ciphertextNoSpace.addEventListener("click", () => {
        resultCipher.value = noSpaceGrouping(resultCipher.value);
    });
}
if (ciphertext5) {
    ciphertext5.addEventListener("change", () => {
        resultCipher.value = fiveCharGrouping(resultCipher.value);
    });
}

// Add event listener for extended vigenere cipher page.
if (radioEncFile){
    radioEncFile.addEventListener("click", () => {
        plaintextInput.classList.remove("d-none");
        filePlaintext.setAttribute("accept", ".txt");
    });
    radioEncByte.addEventListener("click", () => {
        plaintextInput.classList.add("d-none");
        filePlaintext.setAttribute("accept", "*");
    });
    radioDecFile.addEventListener("click", () => {
        ciphertextInput.classList.remove("d-none");
        fileCiphertext.setAttribute("accept", ".txt");
    });
    radioDecByte.addEventListener("click", () => {
        ciphertextInput.classList.add("d-none");
        fileCiphertext.setAttribute("accept", "*");
    });
};