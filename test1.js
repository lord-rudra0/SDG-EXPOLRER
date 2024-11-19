// Get user inputs
key = "Quest";
value ="explain sdg 16";

// Send the key and value to the Python server
fetch("http://localhost:5000/dashboard/api", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ key, value }),
})
  .then((response) => response.json())
  .then((data) => console.log(data));


fetch("http://localhost:5000/dashboard/api")
  .then((response) => response.json())
  .then((data) => console.log(data["Prompt"]));


