# MCP Demo Project

This project demonstrates the use of multiple MCP (Multi-Channel Protocol) servers, including Playwright, Airbnb, and DuckDuckGo search integrations.

## Features
- Automated browser control with Playwright
- Airbnb data integration
- DuckDuckGo web search integration

## Setup

### 1. Clone the repository
```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2. Install dependencies
For Python:
```sh
pip install -r requirements.txt
```
For Node.js (if applicable):
```sh
npm install
```

### 3. Configuration
- Copy `browser_mcp.sample.json` to `browser_mcp.json` and edit as needed.
- Copy `.env.example` to `.env` and fill in your secrets (if required).

## Usage
Describe how to run your app here, e.g.:
```sh
python app.py
```

## File Structure
- `app.py` — Main application script
- `browser_mcp.json` — MCP server configuration
- `.env` — Environment variables (not committed)
- `.env.example` — Template for environment variables

## License
MIT
