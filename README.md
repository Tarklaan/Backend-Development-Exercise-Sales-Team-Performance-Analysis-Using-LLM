# Backend-Development-Exercise-Sales-Team-Performance-Analysis-Using-LLM
# Sales Team Performance Analysis Using LLM

This Django-based backend system uses a Large Language Model (LLM) to analyze sales data and provide feedback on both individual sales representatives and overall team performance. It includes RESTful API endpoints for data ingestion, performance feedback, team assessment, and trend analysis.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Run Instructions](#run-instructions)
- [API Endpoints](#api-endpoints)
- [Using the APIs with Postman](#using-the-apis-with-postman)
- [Environment Variables](#environment-variables)

## Project Overview

This project is designed to provide actionable insights into sales performance using machine learning models and GPT-based LLMs. The backend is built with Django and leverages RESTful APIs for data ingestion, feedback generation, and trend analysis.

### Features
- **Data Ingestion**: Load sales data via a CSV file.
- **Performance Feedback**: Generate LLM-driven feedback for individual sales representatives.
- **Team Performance Assessment**: Analyze the overall performance of the sales team.
- **Performance Trends**: Get insights into sales performance trends over time.

## Technologies Used

- **Django**: Web framework for building the backend.
- **Django REST Framework (DRF)**: For creating RESTful APIs.
- **OpenAI API**: To integrate the LLM for generating insights.
- **Postman**: For testing the API endpoints.
- **Python**: The main programming language.

## Setup and Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtualenv (optional but recommended)
- OpenAI API Key

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repository/sales-analysis-llm.git
   cd sales-analysis-llm
