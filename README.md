# Audio Enabled Morse Code Converstion and Wireless Transmission


This project enables wireless communication of Morse code messages between two Arduino devices. It converts audio input into text, encodes the text in Morse code, and wirelessly transmits it using RF modules. The project is designed to showcase the integration of Arduino, RF modules, and Python libraries for speech recognition.

## Table of Contents

- [Introduction](#introduction)
- [Tools Used](#tools-used)
- [How It Works](#how-it-works)
- [Circuit Diagram](#circuit-diagram)
- [Programs](#programs)
- [Testing](#testing)
- [Conclusion](#conclusion)

## Introduction

The project's primary goal is to transmit Morse code messages wirelessly between two Arduino devices. It achieves this by converting audio input into text using Python's Speech Recognition Library, encoding the text into Morse code, and transmitting it wirelessly using RF modules. 

## Tools Used

- **Arduino Nano:** Used as the transmitter for sending Morse code messages wirelessly.
- **Arduino UNO:** Acts as the receiver for receiving Morse code messages.
- **RF Module (433MHz):** Enables wireless communication between the Arduino Nano and Arduino UNO.
- **Radio Head Library:** Facilitates wireless data transmission.
- **Buzzer:** Used to audibly represent Morse code signals.
- **Arduino IDE:** Used for programming the Arduino Nano and Arduino UNO.
- **PySerial:** Enables serial port communication with external devices.
- **Python's Speech Recognition Library:** Converts audio input into text for encoding.

## How It Works

1. **Audio Input:** The Python script waits for audio input from the user and converts it into text using the Speech Recognition Library.

2. **Text to Morse Code:** The text is converted into Morse code using a custom Morse code conversion algorithm.

3. **Serial Communication:** The encoded message is transferred to the Arduino Nano from the Python script.

4. **Transmitting and Receiving Signal:** The Arduino Nano transmits the message to the Arduino UNO via RF modules for wireless communication.

5. **Buzzer Output:** The Arduino UNO beeps a buzzer to represent the Morse code, consisting of dots and dashes.




Visit this link for the brief explanation of this IOT project : https://docs.google.com/document/d/1entEEynCJG4Q3eZZdChxzb7-V0Vi__WptiCsg8n5ZFs/edit?usp=sharing
