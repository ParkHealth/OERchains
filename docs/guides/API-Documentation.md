# API Documentation for OERchains

Welcome to the **OERchains API Documentation**. This document provides detailed information about how to interact with the OERchains ecosystem through its RESTful API. Whether you're developing a front-end application, integrating with other platforms, or automating processes, this documentation will guide you through the available endpoints and functionality.

## Table of Contents
1. [Base URL](#base-url)
2. [Authentication](#authentication)
3. [Endpoints](#endpoints)
    - [Create OER](#create-oer)
    - [Retrieve OER](#retrieve-oer)
    - [Update OER](#update-oer)
    - [Delete OER](#delete-oer)
4. [Error Handling](#error-handling)
5. [Rate Limiting](#rate-limiting)
6. [FAQ](#faq)

---

## Base URL

The base URL for all API requests is:

```
https://api.oerchains.org/v1
```

All the endpoints described in this documentation are relative to this base URL.

---

## Authentication

The OERchains API uses **API Keys** for authentication. You can obtain an API key by registering an account with OERchains and following the process in the user dashboard.

To authenticate, include the API key in the `Authorization` header for all API requests.

### Example:

```bash
curl -X GET "https://api.oerchains.org/v1/oer/12345" \
     -H "Authorization: Bearer YOUR_API_KEY"
```

---

## Endpoints

### Create OER

**POST** `/oer`

This endpoint allows you to register a new Open Educational Resource (OER) in the OERchains system.

#### Request Body:
```json
{
    "title": "Blockchain for Beginners",
    "author": "John Doe",
    "license": "CC BY 4.0",
    "subject": "Blockchain",
    "media_url": "https://example.com/blockchain-for-beginners.pdf",
    "tags": ["Blockchain", "Education", "Introductory"]
}
```

#### Response:
```json
{
    "success": true,
    "message": "OER registered successfully",
    "oer_uuid": "d1b9b944-1a92-4c8b-b143-b021f7f85cbb"
}
```

---

### Retrieve OER

**GET** `/oer/{oer_uuid}`

This endpoint allows you to retrieve the metadata of a registered OER.

#### URL Parameters:
- `oer_uuid`: The unique identifier (UUID) for the OER.

#### Example Request:
```bash
curl -X GET "https://api.oerchains.org/v1/oer/d1b9b944-1a92-4c8b-b143-b021f7f85cbb" \
     -H "Authorization: Bearer YOUR_API_KEY"
```

#### Response:
```json
{
    "title": "Blockchain for Beginners",
    "author": "John Doe",
    "license": "CC BY 4.0",
    "subject": "Blockchain",
    "media_url": "https://example.com/blockchain-for-beginners.pdf",
    "tags": ["Blockchain", "Education", "Introductory"],
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
}
```

---

### Update OER

**PUT** `/oer/{oer_uuid}`

This endpoint allows you to update an existing OER's metadata.

#### URL Parameters:
- `oer_uuid`: The unique identifier (UUID) for the OER.

#### Request Body:
```json
{
    "title": "Advanced Blockchain Concepts",
    "author": "John Doe",
    "license": "CC BY 4.0",
    "subject": "Blockchain",
    "media_url": "https://example.com/advanced-blockchain.pdf",
    "tags": ["Blockchain", "Education", "Advanced"]
}
```

#### Response:
```json
{
    "success": true,
    "message": "OER updated successfully"
}
```

---

### Delete OER

**DELETE** `/oer/{oer_uuid}`

This endpoint allows you to delete a registered OER from the OERchains system.

#### URL Parameters:
- `oer_uuid`: The unique identifier (UUID) for the OER.

#### Example Request:
```bash
curl -X DELETE "https://api.oerchains.org/v1/oer/d1b9b944-1a92-4c8b-b143-b021f7f85cbb" \
     -H "Authorization: Bearer YOUR_API_KEY"
```

#### Response:
```json
{
    "success": true,
    "message": "OER deleted successfully"
}
```

---

## Error Handling

When an error occurs, the API will return an appropriate HTTP status code along with a JSON response that provides details about the error.

### Example Error Response:
```json
{
    "error": {
        "code": "400",
        "message": "Invalid OER UUID provided"
    }
}
```

Common HTTP status codes used:
- **200 OK**: Request was successful.
- **400 Bad Request**: The request was invalid.
- **401 Unauthorized**: Missing or invalid API key.
- **404 Not Found**: The requested OER does not exist.
- **500 Internal Server Error**: Something went wrong on the server.

---

## Rate Limiting

To ensure fair usage and prevent abuse, the OERchains API has rate limiting in place. By default, each API key is limited to 1000 requests per hour.

If you exceed the rate limit, you will receive a **429 Too Many Requests** response. You can check your remaining requests in the `X-RateLimit-Remaining` header.

---

## FAQ

### How do I get an API Key?

You can obtain an API key by signing up on the OERchains platform and following the instructions in your account dashboard.

### Can I use this API to create multiple OERs?

Yes, you can use the API to create as many OERs as needed. Each OER will be uniquely identified by a UUID.

### What happens if I delete an OER?

Once deleted, the OER is permanently removed from the OERchains registry. The data will not be recoverable.

---

For further assistance, please refer to our [GitHub Discussions](https://github.com/ParkHealth/OERchains/discussions) or contact us directly through our support channels.
