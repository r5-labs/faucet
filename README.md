# Faucet

A simple faucet implementation for the R5 Testnet. You can run your own faucet and help decentralize access to the testnet for developers all across the world.

## App Composition

The app is comprised of a **backend** server written in Python, and a **frontend** written in ReactJs/Javascript.

## Backend

You can run the backend by installing the required libraries:

- flask
- flask-cors
- web3

And running it with Python:

```bash
python3 faucet.py
```

Don't forget to replace the placeholder `FAUCET_PRIVATE_KEY_HERE` and you can also set your own RPC server by changing the `WEB3_PROVIDER_URI` property.

**Important!** If you are running Linux or macOS, you might have to use `venv` to install the libraries in a separate virtual environment. You can follow the link below for more information:

https://docs.python.org/3/library/venv.html

## Frontend

To run the frontend, install the dependencies with `npm`:

```bash
npm install
```

Replace the API URL declared on the `handleSubmit` function inside `App.js` with your own backend URL.

Run the code using `npm`:

```bash
npm start
```

If you want to deploy a static application, you can create an optimized build by running:

```bash
npm run build
```

And copying the contents from within the `/build` folder into your own hosting.
