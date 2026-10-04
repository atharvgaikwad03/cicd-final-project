# CI/CD Final Project

## Project Name: OpenShift CI/CD Pipeline with GitHub Actions and Tekton

**Author:** Atharv Gaikwad  
**GitHub:** https://github.com/atharvgaikwad03  
**Course:** IBM DevOps and Software Engineering Professional Certificate  
**Assignment:** Final Project – CI/CD Pipeline Implementation

---

## Project Overview

This project demonstrates a complete CI/CD pipeline using:
- **GitHub Actions** for automated linting and unit testing
- **Tekton Pipelines** for task-based automation on OpenShift
- **OpenShift** for container build and deployment

The application is a simple Python Flask counter service that maintains a hit counter using Redis.

---

## Repository Structure

```
cicd-final-project/
├── .github/
│   └── workflows/
│       └── workflow.yml       # GitHub Actions CI workflow
├── .tekton/
│   └── tasks.yml              # Tekton pipeline tasks
├── tests/
│   └── test_counter.py        # Unit tests using nose
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Container image definition
└── README.md                  # Project documentation
```

---

## CI/CD Pipeline Steps

### GitHub Actions Workflow
1. **Lint with flake8** – Checks Python code style and syntax errors
2. **Run unit tests with nose** – Executes all unit tests and reports coverage

### Tekton Pipeline
1. **cleanup** – Removes previous workspace artifacts
2. **git-clone** – Clones the source repository
3. **flake8** – Lints Python source code
4. **nose** – Runs unit tests
5. **buildah** – Builds the container image
6. **deploy** – Deploys the application to OpenShift

---

## Application Description

The application is a Python Flask-based hit counter service:
- Endpoint `GET /` returns a welcome message
- Endpoint `GET /counter` increments and returns the visit count
- Backed by a Redis database
- Runs on port **8000**

---

## How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
flask run --port=8000

# Run tests
nosetests --with-spec --spec-color
```

---

## OpenShift Deployment

The pipeline is configured to:
1. Pull source from GitHub
2. Lint and test the code
3. Build a container image using Buildah
4. Push to the OpenShift internal registry
5. Deploy to the OpenShift cluster

---

## License

This project is part of IBM's Coursera DevOps course curriculum and is for educational purposes.
