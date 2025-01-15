# Sample Smart Contract for OERchains

This document provides a sample **smart contract** written in **Solidity** that could be used within the **OERchains** ecosystem. The smart contract facilitates the management of **Open Educational Resources (OERs)** by enabling transparent licensing, attribution, and fair usage of educational materials on the blockchain.

The sample contract showcases how educators, content creators, and institutions can register their OERs and interact with the OERchains network using a decentralized approach.

## Table of Contents
1. [Overview](#overview)
2. [Smart Contract Code](#smart-contract-code)
3. [How It Works](#how-it-works)
4. [Deployment Instructions](#deployment-instructions)
5. [Testing the Smart Contract](#testing-the-smart-contract)

## Overview

The goal of this smart contract is to provide a simple yet effective way to register OERs on the blockchain, allowing users to:

- Register educational resources (documents, videos, quizzes, etc.)
- Associate the resources with a unique identifier (UUID)
- Attach metadata such as title, author, license, and subject
- Track the usage of the content
- Ensure the educational resources are used according to the specified license terms

## Smart Contract Code

Below is a simplified version of a smart contract for registering OERs. This contract includes basic functionalities for storing OER metadata on the Ethereum blockchain.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract OERRegistry {

    // Struct to store OER metadata
    struct OER {
        string title;
        string author;
        string license;
        string subject;
        string mediaUrl;
        uint timestamp;
    }

    // Mapping to store OERs by their UUID
    mapping(bytes32 => OER) public oerRegistry;

    // Event to log the registration of a new OER
    event OERRegistered(bytes32 indexed oerUUID, string title, string author);

    // Function to register a new OER
    function registerOER(
        string memory _title,
        string memory _author,
        string memory _license,
        string memory _subject,
        string memory _mediaUrl
    ) public returns (bytes32) {
        bytes32 oerUUID = keccak256(abi.encodePacked(_title, _author, block.timestamp));
        
        oerRegistry[oerUUID] = OER({
            title: _title,
            author: _author,
            license: _license,
            subject: _subject,
            mediaUrl: _mediaUrl,
            timestamp: block.timestamp
        });

        emit OERRegistered(oerUUID, _title, _author);

        return oerUUID;
    }

    // Function to retrieve OER details by UUID
    function getOER(bytes32 _oerUUID) public view returns (string memory, string memory, string memory, string memory, string memory, uint) {
        OER memory oer = oerRegistry[_oerUUID];
        return (oer.title, oer.author, oer.license, oer.subject, oer.mediaUrl, oer.timestamp);
    }
}
```

This contract provides the following functionality:

- **registerOER**: This function allows anyone to register an OER by providing metadata such as the title, author, license, subject, and media URL. It then generates a unique identifier (UUID) for the OER using the keccak256 hash function.
  
- **getOER**: This function allows users to retrieve the metadata of an OER by its UUID.

- **Event Logging**: The contract emits an event `OERRegistered` whenever a new OER is registered, making it easier to track all the OERs in the system.

## How It Works

### Registering OERs

1. **Metadata Submission**: When a user wants to register an OER, they provide metadata such as the title, author, license, subject, and media URL.
   
2. **UUID Generation**: The contract uses the `keccak256` hash function to generate a unique identifier (UUID) for the resource. The UUID ensures that each OER is uniquely identifiable on the blockchain.

3. **Storing Data**: The metadata, along with the generated UUID, is stored in the contract’s `oerRegistry` mapping. This mapping associates each UUID with an OER’s metadata.

4. **Event Emission**: The contract emits an `OERRegistered` event, logging the registration of the OER on the blockchain.

### Retrieving OERs

- **Querying**: Users can query the OER registry by providing the UUID. The contract will return the stored metadata associated with the UUID.

## Deployment Instructions

To deploy this smart contract on the Ethereum network (or any other EVM-compatible chain), follow these steps:

1. **Install Prerequisites**:
   - Install [Node.js](https://nodejs.org/) if you don't have it already.
   - Install [Truffle](https://www.trufflesuite.com/truffle) or [Hardhat](https://hardhat.org/).
   
2. **Deploy the Contract**:
   - Set up a Truffle or Hardhat project.
   - Copy the contract code into your project's `contracts` directory.
   - Write a migration script for the contract deployment.
   - Deploy it using your preferred Ethereum network (testnet or mainnet).

3. **Verify Deployment**:
   - Once deployed, use the contract’s address to interact with it.
   - You can use web3.js or ethers.js to interact with the contract from a frontend application.

## Testing the Smart Contract

To test the functionality of the smart contract locally, you can follow these steps:

1. **Install Ganache**: Ganache is a personal Ethereum blockchain for testing. You can use it to simulate the Ethereum network locally.

2. **Write Tests**: In your Truffle or Hardhat project, write tests using the Mocha framework to verify that the smart contract behaves as expected. Example tests might include:
   - Registering an OER and checking that the UUID is returned.
   - Retrieving the metadata of a registered OER.

3. **Run Tests**: Use Truffle or Hardhat to run your tests on the local Ganache network.

Example test script (in JavaScript using Mocha):

```javascript
const OERRegistry = artifacts.require("OERRegistry");

contract("OERRegistry", accounts => {
    it("should register a new OER", async () => {
        const oerRegistry = await OERRegistry.deployed();
        
        const title = "Blockchain Basics";
        const author = "John Doe";
        const license = "CC BY 4.0";
        const subject = "Blockchain";
        const mediaUrl = "https://example.com/blockchain-basics.pdf";
        
        const oerUUID = await oerRegistry.registerOER(title, author, license, subject, mediaUrl);
        const oerData = await oerRegistry.getOER(oerUUID);
        
        assert.equal(oerData[0], title, "Title should match");
        assert.equal(oerData[1], author, "Author should match");
        assert.equal(oerData[2], license, "License should match");
    });
});
```

## Conclusion

This sample smart contract demonstrates how to register OERs on the Ethereum blockchain using a decentralized system. By using smart contracts, **OERchains** aims to ensure transparency, fairness, and traceability for educational resources shared across the platform. With this contract, OER creators can have greater control over their content, and consumers can trust that the educational resources are legitimate and properly attributed.

Feel free to modify and extend this contract to meet the specific needs of your OER projects!

For more information, please refer to the [OERchains Documentation](https://github.com/ParkHealth/OERchains) or reach out via our [GitHub Discussions](https://github.com/ParkHealth/OERchains/discussions).
