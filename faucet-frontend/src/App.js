import React, { useState } from "react";
import "./App.css";
import Logo from "./logo_teal-transparent-125.png";

function App() {
  const [address, setAddress] = useState("");
  const [responseMessage, setResponseMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setResponseMessage("");
    setIsLoading(true);

    try {
      const res = await fetch(
        "https://faucet-backend-testnet.r5labs.org/drip",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ address })
        }
      );

      const data = await res.json();
      if (res.ok) {
        setResponseMessage(`Success! Transaction Hash: ${data.tx_hash}`);
      } else {
        setResponseMessage(`Error: ${data.error || "Something went wrong"}`);
      }
    } catch (error) {
      setResponseMessage(`Error: ${error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <img src={Logo} alt="R5" />
      <h1>R5 Testnet Faucet</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter your R5 wallet address..."
          value={address}
          onChange={(e) => setAddress(e.target.value)}
          required
          style={{
            padding: "10px",
            borderRadius: "5px",
            margin: "5px",
            minWidth: "64ch"
          }}
        />
        <button type="submit" disabled={isLoading} style={{ padding: '10px 15px' }}>
          {isLoading ? "Processing..." : "Get TR5"}
        </button>
      </form>
      {responseMessage && <p>{responseMessage}</p>}
    </div>
  );
}

export default App;
