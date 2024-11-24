function encodeData() {
    const data = document.getElementById("inputData").value;
    
    fetch('/encode', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data })
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById("outputData").innerText = result.result;
    });
}

function decodeData() {
    const data = document.getElementById("inputData").value;

    fetch('/decode', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data })
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById("outputData").innerText = result.result;
    });
}