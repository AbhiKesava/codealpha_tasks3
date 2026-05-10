# codealpha_tasks3
# Secure Coding Review

This project demonstrates a secure coding review of a Python login application.

## Objectives

- Identify security vulnerabilities
- Learn secure coding practices
- Perform manual code review
- Apply remediation techniques
- Improve application security

---

## Vulnerabilities Identified

| Vulnerability | Risk |
|---|---|
| Hardcoded Credentials | High |
| Plaintext Passwords | High |
| Missing Input Validation | Medium |
| No Account Lockout | Medium |

---

## Tools Used

- Python
- Bandit
- Static Analysis
- Manual Inspection

---

## Project Files

```text
secure-coding-review/
│
├── vulnerable_app.py
├── secure_app.py
├── README.md
├── screenshots/
│   ├── vulnerable-code.png
│   ├── bandit-scan.png
│   └── secure-code.png
└── report/
    └── secure_coding_review_report.pdf
