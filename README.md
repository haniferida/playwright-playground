# Playwright Playground

Portfolio-ready end-to-end automation project built to demonstrate clean test architecture, reusable Page Object Model (POM), and cross-language test implementation with Playwright.

## Overview

This repository contains two implementations of the same Google Search test flow:

- **Python + pytest + Playwright**
- **TypeScript + Playwright Test**

The goal is to show scalable testing patterns (fixtures, POM, clear assertions, and maintainable project structure), not just a single passing script.

## Highlights

- Reusable **Page Object Model** for page actions and assertions
- Isolated test setup using fixtures/context
- Robust locator strategy for Google Search elements
- Resilient assertions that handle real-world behavior (including challenge pages)
- Clean separation between framework setup, page objects, and test specs

## Tech Stack

- Playwright
- Python + pytest
- TypeScript + Playwright Test

## Project Structure

```text
.
├── conftest.py
├── pages/
│   ├── base_page.py
│   └── google_search_page.py
├── tests/
│   └── test_example.py
└── playwright-ts/
    ├── playwright.config.ts
    ├── tsconfig.json
    ├── pages/
    │   ├── basePage.ts
    │   └── googleSearchPage.ts
    └── tests/
        └── google-search.spec.ts
```

## Run Python Suite

```bash
pytest -q
```

## Run TypeScript Suite

```bash
cd playwright-ts
npm install
npx playwright install chromium
npm test
```

## Why This Project

This project is part of my QA Automation portfolio to demonstrate:

- writing maintainable UI automation with POM
- building scalable test foundations for growing suites
- implementing the same business flow across different testing stacks