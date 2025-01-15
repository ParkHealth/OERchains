# Developer Guide for OERchains

Welcome to the **OERchains Developer Guide**! This document provides developers with all the resources they need to get started contributing to the OERchains project. Whether you're looking to improve existing features, build new components, or integrate with the platform, this guide will help you navigate the codebase and contribute effectively.

## Table of Contents
1. [Introduction](#introduction)
2. [Setting Up Your Development Environment](#setting-up-your-development-environment)
3. [Code Structure](#code-structure)
4. [How to Contribute](#how-to-contribute)
5. [Building and Running Locally](#building-and-running-locally)
6. [Testing and Quality Assurance](#testing-and-quality-assurance)
7. [Deploying Changes](#deploying-changes)
8. [Code of Conduct](#code-of-conduct)

---

## Introduction

OERchains is an open-source, decentralized platform that empowers the creation and sharing of Open Educational Resources (OERs). Built using blockchain technology, it enables transparent licensing, attribution, and fair usage tracking for educational content.

As a developer, you’ll contribute to various aspects of the project, such as:

- Building new features for the OERchains ecosystem.
- Integrating with other platforms.
- Improving the user interface and experience.
- Fixing bugs and optimizing performance.

---

## Setting Up Your Development Environment

Before you start contributing, you need to set up your local development environment. Follow the steps below to get started:

### Step 1: Clone the Repository

First, clone the OERchains repository from GitHub:

```bash
git clone https://github.com/ParkHealth/OERchains.git
cd OERchains
```

### Step 2: Install Dependencies

OERchains has dependencies for both **Node.js** and **Python**. Here’s how to install them:

#### For Python:

```bash
pip install -r requirements.txt
```

#### For Node.js:

Make sure you have **Node.js v16+** installed. Then run:

```bash
npm install
```

### Step 3: Set Up Environment Variables

Some configurations may require environment variables for your local setup. Create a `.env` file in the root of the repository based on `.env.example`, and add your configuration details.

```bash
cp .env.example .env
```

Edit the `.env` file to add your local configurations.

---

## Code Structure

The OERchains codebase is organized into several directories, each serving a specific purpose:

- **`/docs`**: Documentation files for developers and users.
- **`/src`**: Main source code for the application.
- **`/contracts`**: Smart contract code used for the decentralized blockchain-based system.
- **`/tests`**: Unit and integration tests for the application.
- **`/public`**: Static assets such as images and assets for the front-end.
- **`/scripts`**: Helper scripts for setting up the environment, running the tests, or interacting with the blockchain.

---

## How to Contribute

OERchains is a community-driven project, and we welcome contributions from everyone! To contribute to OERchains:

1. **Fork the Repository**: Click the "Fork" button at the top of the [OERchains GitHub repository](https://github.com/ParkHealth/OERchains).
   
2. **Create a New Branch**: Make sure to create a new branch for each feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**: Edit the code, write new features, or fix bugs.

4. **Write Tests**: If you are adding new features, ensure that you write tests to verify that your code works correctly.

5. **Submit a Pull Request**: Once you’re done with your changes, push them to your fork and open a pull request on GitHub.
   ```bash
   git push origin feature/your-feature-name
   ```

Before submitting your pull request, please make sure to:

- Follow the [coding standards](./docs/community/CONTRIBUTING.md).
- Ensure that all tests pass.
- Provide a clear description of the changes you made.

---

## Building and Running Locally

To test and run OERchains locally, follow these steps:

### Step 1: Start the Development Server

For the front-end, run the following command to start a local server:

```bash
npm run dev
```

This will start the app on [http://localhost:3000](http://localhost:3000).

### Step 2: Deploy a Local Blockchain (Optional)

For testing the blockchain integration, you may want to deploy a local instance of the Ethereum network using **Ganache** or **Hardhat**. 

To deploy using **Hardhat**:

```bash
npx hardhat node
```

Then deploy your contracts:

```bash
npx hardhat run scripts/deploy.js --network localhost
```

---

## Testing and Quality Assurance

We use a combination of **unit tests** and **integration tests** to ensure code quality and functionality. Here's how you can run the tests:

### Step 1: Install Test Dependencies

```bash
npm install --save-dev mocha chai
```

### Step 2: Run the Tests

To run the tests, use the following command:

```bash
npm test
```

### Step 3: Write Tests

When adding new features or fixing bugs, make sure to write tests to verify that your changes work correctly. Place your tests in the `/test` directory. Tests should follow the structure of existing tests and use **Mocha** and **Chai** for assertions.

---

## Deploying Changes

Once your changes have been reviewed and approved, the next step is deployment. Depending on the type of changes (smart contract updates, front-end changes, etc.), deployment may vary.

### For Smart Contracts:
- Deploy the updated contract to the blockchain using Hardhat or Truffle.
- Ensure that all contract interactions are tested on a test network before deploying to the mainnet.

### For Front-End Changes:
- Build the production version of the front-end:
  ```bash
  npm run build
  ```
- Deploy the built version to a hosting platform like Netlify or Vercel.

---

## Code of Conduct

All contributors must abide by our [Code of Conduct](./CODE_OF_CONDUCT.md). We are committed to creating a welcoming and inclusive environment for all participants.

---

Thank you for contributing to **OERchains**! We appreciate your efforts to help build a decentralized, open educational ecosystem that empowers educators, students, and content creators around the world.

For more information, please check out the [OERchains GitHub Repository](https://github.com/ParkHealth/OERchains).