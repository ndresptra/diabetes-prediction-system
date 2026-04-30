// script.js
document.getElementById("predictionForm").addEventListener("submit", async function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    const data = {};
    formData.forEach((value, key) => {
      data[key] = value;
    });
  
    const response = await fetch("/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
  
    const result = await response.json();
    const resultDiv = document.getElementById("result");
  
    if (result.status === "success") {
      resultDiv.innerHTML = `
        <h2 class="text-xl font-bold text-green-600">Prediction: ${result.prediction}</h2>
        <ul class="mt-4 text-left">
          ${result.health_tips.tips.map(tip => `<li class="text-gray-600">${tip}</li>`).join("")}
        </ul>
      `;
    } else {
      resultDiv.innerHTML = `<p class="text-red-600">${result.message}</p>`;
    }
  });
  