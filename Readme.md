# Flask Speech Recognition Web App

This is a Flask-based web application for speech recognition. It allows users to upload audio files, which are then processed using the SpeechRecognition library to convert the speech into text and return the transcript.

## Features

- Flask web application to serve as a frontend for audio file uploads.
- Converts speech to text using the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library.
- Handles file uploads for audio recognition.
- Containerized using Docker for easy deployment.
- Integrated with GitHub Actions for CI/CD automation.

## Functionality

1. **Home Page**: The home page allows users to upload audio files.
2. **Speech Recognition**: Uses Google’s Speech Recognition API to convert audio to text.
3. **Error Handling**: Displays appropriate messages if the speech cannot be identified or if there is an error during the request.

## Tech Stack

- Python 3.9
- Flask 2.x
- SpeechRecognition 3.x
- Docker (for containerized deployment)
- GitHub Actions (for CI/CD automation)

## Installation

### Prerequisites

- Python 3.9+
- pip

### Install Dependencies

Ensure that Python and pip are installed, and then run the following command to install the required dependencies:


