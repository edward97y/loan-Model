# Loan Approval Prediction API

A production-ready **FastAPI** application that serves a **pre-trained Machine Learning model** for loan approval prediction.

The model is loaded **once at application startup**, ensuring high performance and scalability.

This project focuses on **correct ML deployment architecture**, not just building a model.

---

## Features

- FastAPI backend
- Pre-trained ML pipeline (no training inside API)
- Input validation using **Pydantic**
- Model loaded once using **lifespan**
- Clean request/response structure
- Designed to handle many requests without server failure
- Ready for Dockerization (planned)

---

---

## 📥 Input Schema

The API expects a **JSON** request with the following fields:

```json
{
  "no_of_dependents": 2,
  "education": "Graduate",
  "self_employed": "No",
  "income_annum": 500000,
  "loan_amount": 200000,
  "loan_term": 360,
  "cibil_score": 750,
  "residential_assets_value": 1000000,
  "commercial_assets_value": 0,
  "luxury_assets_value": 0,
  "bank_asset_value": 200000
}

Client Request
      ↓
Input Validation (Pydantic)
      ↓
Preprocessing (inside ML pipeline)
      ↓
Model Inference
      ↓
Prediction Response


