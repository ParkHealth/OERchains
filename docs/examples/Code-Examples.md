# Code Examples for OERchains

This document provides code examples to help developers interact with and contribute to the **OERchains** ecosystem. Whether you're looking to build on top of OERchains, integrate with the platform, or contribute directly to its development, these code samples will provide you with a solid foundation.

## Table of Contents
1. [Basic Setup](#basic-setup)
2. [Integrating OERchains with Blockchain](#integrating-oerchains-with-blockchain)
3. [Working with OER Metadata](#working-with-oer-metadata)
4. [Querying OER Data](#querying-oer-data)
5. [Contributing to OERchains](#contributing-to-oerchains)

## Basic Setup

To get started with developing for OERchains, you'll need to clone the repository and set up your development environment. Here’s how to do it:

### Step 1: Clone the Repository

```bash
git clone https://github.com/ParkHealth/OERchains.git
cd OERchains
```

### Step 2: Install Dependencies

You’ll need to have **Node.js** and **Python 3.x** installed. After cloning the repository, install the necessary dependencies:

For Python dependencies:

```bash
pip install -r requirements.txt
```

For Node.js dependencies:

```bash
npm install
```

### Step 3: Running the Local Development Server

To start the development server, run the following command:

```bash
npm run dev
```

Your local instance of OERchains will be running on `http://localhost:3000`.

---

## Integrating OERchains with Blockchain

OERchains is built on a decentralized blockchain protocol. Here’s an example of how you might interact with the blockchain to register a new educational resource (OER).

### Step 1: Initialize Web3

```javascript
const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');
```

### Step 2: Create a Smart Contract

```javascript
const contractABI = [ /* ABI array here */ ];
const contractAddress = '0xYourSmartContractAddress';

const contract = new web3.eth.Contract(contractABI, contractAddress);
```

### Step 3: Register OER

Here’s how you can register a new OER on the blockchain using the smart contract.

```javascript
const account = '0xYourAccountAddress';
const privateKey = 'yourPrivateKey';

const data = {
  title: 'Introduction to Blockchain',
  author: 'John Doe',
  license: 'CC BY 4.0',
  metadata: { 
    subject: 'Blockchain', 
    grade: 'Advanced'
  }
};

const dataHash = web3.utils.sha3(JSON.stringify(data));

const tx = contract.methods.registerOER(dataHash);

const gas = await tx.estimateGas({ from: account });
const gasPrice = await web3.eth.getGasPrice();

const signedTx = await web3.eth.accounts.signTransaction(
  {
    to: contractAddress,
    data: tx.encodeABI(),
    gas,
    gasPrice,
  },
  privateKey
);

const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
console.log('Transaction Receipt:', receipt);
```

## Working with OER Metadata

OERchains supports metadata for educational resources. Here’s how to interact with OER metadata.

### Step 1: Example Metadata Structure

Each OER on OERchains is associated with metadata that includes details like the resource’s title, subject, and license.

```json
{
  "title": "Blockchain for Beginners",
  "author": "Jane Smith",
  "license": "CC BY-SA 4.0",
  "subject": "Blockchain",
  "grade": "Beginner",
  "keywords": ["blockchain", "education", "open-source"]
}
```

### Step 2: Register Metadata

When adding metadata to an OER, the metadata is stored on-chain for transparency and traceability.

```javascript
const registerMetadata = async (metadata) => {
  const metadataHash = web3.utils.sha3(JSON.stringify(metadata));
  
  const tx = contract.methods.registerMetadata(metadataHash);
  const gas = await tx.estimateGas({ from: account });
  const gasPrice = await web3.eth.getGasPrice();

  const signedTx = await web3.eth.accounts.signTransaction(
    {
      to: contractAddress,
      data: tx.encodeABI(),
      gas,
      gasPrice,
    },
    privateKey
  );

  const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
  console.log('Metadata Transaction Receipt:', receipt);
};
```

## Querying OER Data

Once OER metadata is stored on the blockchain, you can query it using the OERchains APIs or directly via smart contract calls.

### Step 1: Query by Title

To find an OER by its title, you can call the smart contract method like this:

```javascript
const title = 'Blockchain for Beginners';

contract.methods.getOERByTitle(title).call()
  .then(result => {
    console.log('OER Data:', result);
  })
  .catch(err => {
    console.error('Error fetching OER:', err);
  });
```

### Step 2: Query by Author

You can also query OERs by their author or other metadata fields:

```javascript
const author = 'Jane Smith';

contract.methods.getOERByAuthor(author).call()
  .then(result => {
    console.log('OER Data by Author:', result);
  })
  .catch(err => {
    console.error('Error fetching OER by author:', err);
  });
```

## Contributing to OERchains

We welcome contributions to OERchains! Whether you're fixing bugs, adding new features, or improving documentation, your contributions are valuable.

To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes (`git checkout -b feature-name`).
3. Make your changes and commit them.
4. Push to your fork (`git push origin feature-name`).
5. Submit a pull request to the main repository.

For detailed guidelines on contributing, see our [CONTRIBUTING.md](https://github.com/ParkHealth/OERchains/blob/main/docs/community/CONTRIBUTING.md).


We hope these examples help you get started with the OERchains project. If you have any questions or need further assistance, feel free to reach out via our [Discussions](https://github.com/ParkHealth/OERchains/discussions) page.

Happy coding!
