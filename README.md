# Healthcare Chatbot with AutoGen Multi-Agent Collaboration



## Overview

This project demonstrates a **Healthcare Chatbot** powered by OpenAI GPT-4 using the [AutoGen](https://github.com/microsoft/autogen) framework. It features **multi-agent collaboration** where two AI agents work together to provide health advice:

- **HealthcareBot**: Provides symptom guidance and general health tips.
- **FactCheckerBot**: Verifies the medical accuracy of HealthcareBot's responses to ensure safety and reliability.

The chatbot is wrapped in a simple Python interface and can be integrated with a frontend such as [Gradio](https://gradio.app) for an interactive web UI.

---

## Features

- Multi-agent AI conversation with role-based collaboration.
- Friendly and professional healthcare advice.
- Fact-checking for safer responses.
- Easy to extend with additional agents or UI frameworks.
- Sample code for terminal-based interaction and Gradio UI.

---

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key
- Install dependencies:

```bash
pip install autogen openai gradio

