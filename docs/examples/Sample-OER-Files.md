# Sample OER Files for OERchains

This document provides sample Open Educational Resources (OER) files that are compatible with **OERchains**. These files demonstrate the types of educational content that can be integrated into the OERchains ecosystem, along with how they can be formatted for use with the platform.

The following examples represent various types of OERs that OERchains supports, including text-based documents, multimedia content, and interactive resources.

## Table of Contents
1. [Text-Based OER](#text-based-oer)
2. [Interactive Media OER](#interactive-media-oer)
3. [Multimedia OER](#multimedia-oer)
4. [OER Metadata Example](#oer-metadata-example)
5. [How to Submit OER Files to OERchains](#how-to-submit-oer-files-to-oerchains)

---

## Text-Based OER

### Example: Textbook on Blockchain

Here is an example of a text-based educational resource on **Blockchain**. This file would typically be a `.pdf`, `.txt`, or `.docx` format.

```plaintext
Title: Introduction to Blockchain
Author: Jane Smith
License: CC BY 4.0
Subject: Blockchain Technology
Grade Level: Advanced

Chapter 1: Understanding Blockchain Technology
- What is Blockchain?
- How Blockchain Works
- Blockchain Applications

Chapter 2: Blockchain in Education
- Benefits for Education
- Decentralized Learning Models
```

You can submit this resource in a text-based format or PDF. Ensure the metadata (author, title, license) is clearly marked for proper registration on the OERchains platform.

---

## Interactive Media OER

### Example: Blockchain Quiz

Interactive content, such as quizzes or simulations, can be submitted as HTML files, JSON-based interactive assessments, or packaged media that can run on a browser or mobile platform.

```html
<!-- Example HTML Quiz for Blockchain Basics -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Blockchain Quiz</title>
</head>
<body>
    <h2>Blockchain Knowledge Test</h2>
    <form id="quiz-form">
        <label for="question1">1. What is Blockchain?</label><br>
        <input type="radio" name="q1" value="a"> Distributed Ledger<br>
        <input type="radio" name="q1" value="b"> Centralized Database<br><br>

        <label for="question2">2. Who created Bitcoin?</label><br>
        <input type="radio" name="q2" value="a"> Satoshi Nakamoto<br>
        <input type="radio" name="q2" value="b"> Vitalik Buterin<br><br>

        <input type="submit" value="Submit">
    </form>

    <script>
        document.getElementById("quiz-form").onsubmit = function(event) {
            event.preventDefault();
            alert("Your answers have been submitted.");
        }
    </script>
</body>
</html>
```

This example demonstrates a basic interactive quiz. Users can submit their answers, and these responses could be recorded using a blockchain-based mechanism to verify participants’ learning progress.

## Multimedia OER

### Example: Blockchain Tutorial Video

For multimedia resources, such as tutorial videos or educational documentaries, these are typically submitted in formats like `.mp4`, `.avi`, or `.mov`.

Here is an example of how the OER metadata for a video might look:

```json
{
    "title": "Introduction to Blockchain",
    "author": "Blockchain Academy",
    "license": "CC BY 4.0",
    "subject": "Blockchain Technology",
    "grade_level": "Intermediate",
    "media_type": "Video",
    "media_url": "https://www.example.com/video.mp4"
}
```

This JSON file links to a tutorial video hosted on an external server. The metadata includes details about the resource such as the subject, grade level, and license type.

## OER Metadata Example

In addition to the educational content, each OER resource should have associated metadata. Below is a JSON example of metadata for an OER.

```json
{
    "title": "Blockchain Basics for Beginners",
    "author": "Alice Johnson",
    "license": "CC BY-SA 4.0",
    "subject": "Blockchain Technology",
    "grade_level": "Beginner",
    "keywords": ["Blockchain", "Distributed Ledger", "Cryptocurrency"],
    "media_url": "https://example.com/blockchain-basics.pdf"
}
```

Ensure that the metadata accurately describes the content and follows the standard format, allowing for easy querying and integration into the OERchains platform.

## How to Submit OER Files to OERchains

To submit your OER content to OERchains:

1. **Prepare your file(s)** – Ensure your OER is properly formatted with all necessary metadata.
2. **Upload to OERchains** – You can use the OERchains submission interface or submit your OER through a pull request on GitHub.
3. **Provide Metadata** – Include the metadata for each OER in JSON format, as shown above.
4. **Submit via GitHub** – All contributions to the OERchains project should be submitted via GitHub pull requests to ensure transparency and integrity.
   - [Submit a Pull Request](https://github.com/ParkHealth/OERchains/pulls)

## Conclusion

This document provides sample formats for various types of OER content that you can use in the **OERchains** ecosystem. By following these examples, you can ensure that your content is properly formatted, accompanied by the right metadata, and ready for submission to the platform.

We encourage contributions and welcome new OERs from the global education community. If you have any questions or need additional help with submitting OERs, feel free to contact us via our [GitHub Discussions](https://github.com/ParkHealth/OERchains/discussions).

Happy Learning, and thank you for supporting **OERchains**!