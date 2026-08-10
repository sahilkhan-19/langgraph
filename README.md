# LangGraph Learning Hub

A comprehensive collection of LangGraph examples and tutorials demonstrating various patterns and techniques for building AI applications with language models.

## 📚 Overview

This repository contains interactive Jupyter notebooks showcasing different LangGraph concepts and workflows. LangGraph is a library for building stateful, multi-actor applications with LLMs, combining the power of language models with robust application logic.

### What is LangGraph?

LangGraph enables you to:
- Build complex AI workflows and agents
- Implement conditional logic and branching
- Handle parallel execution patterns
- Create stateful conversations and interactions
- Orchestrate multiple LLM calls efficiently

---

## 📂 Project Structure

```
langgraph/
├── README.md                    # This file
├── .gitignore                  # Git ignore rules
├── .env                        # Environment variables (not in git)
├── requirements.txt            # Python dependencies
├── venv/                       # Virtual environment
│
├── bmi.ipynb                   # BMI calculation example
├── conditional.ipynb           # Basic conditional flows
├── conditional_llm.ipynb       # Conditional logic with LLM
├── parallel_simple.ipynb       # Simple parallel execution
├── parallel_llm.ipynb          # Parallel LLM workflows
├── prompt_chaining.ipynb       # Sequential prompt chaining
└── simplel_llm.ipynb           # Simple LLM integration
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd langgraph
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   **Windows (PowerShell):**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   venv\Scripts\activate.bat
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

---

## 📖 Notebook Guide

### Basic Examples

| Notebook | Description | Level |
|----------|-------------|-------|
| **simplel_llm.ipynb** | Introduction to LLM integration | Beginner |
| **bmi.ipynb** | BMI calculation workflow | Beginner |
| **prompt_chaining.ipynb** | Sequential multi-step prompts | Intermediate |

### Control Flow

| Notebook | Description | Level |
|----------|-------------|-------|
| **conditional.ipynb** | Basic conditional routing | Intermediate |
| **conditional_llm.ipynb** | LLM-driven decision making | Intermediate |

### Advanced Patterns

| Notebook | Description | Level |
|----------|-------------|-------|
| **parallel_simple.ipynb** | Parallel execution basics | Advanced |
| **parallel_llm.ipynb** | Complex parallel workflows | Advanced |

---

## 🔧 Usage

### Running Notebooks

1. **Start Jupyter**
   ```bash
   jupyter notebook
   ```

2. **Navigate to a notebook** and open it in your browser

3. **Execute cells** sequentially with `Shift + Enter`

### Key Concepts Demonstrated

- **State Management**: Track data across workflow steps
- **Graph Structures**: Define nodes and edges for workflows
- **Conditional Routing**: Route execution based on conditions
- **Parallel Processing**: Execute multiple steps concurrently
- **LLM Integration**: Incorporate language models into workflows

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
# OpenAI API Configuration
OPENAI_API_KEY=your_api_key_here

# LangSmith Configuration (optional)
LANGSMITH_API_KEY=your_langsmith_key
LANGSMITH_TRACING=true

# Other API Keys
ANTHROPIC_API_KEY=your_anthropic_key

# LangGraph Settings
LOG_LEVEL=INFO
```

> **Note:** Never commit `.env` files to git. Add them to `.gitignore`.

---

## 📦 Dependencies

Key packages used in this project:

- **langgraph** - Core workflow orchestration
- **langchain** - Language model framework
- **openai** - OpenAI API client
- **jupyter** - Interactive notebooks
- **python-dotenv** - Environment variable management

For a complete list, see `requirements.txt`

---

## 🎯 Learning Path

**Recommended order for learning:**

1. Start with `simplel_llm.ipynb` to understand basic LLM calls
2. Explore `prompt_chaining.ipynb` for sequential workflows
3. Try `conditional.ipynb` and `conditional_llm.ipynb` for branching logic
4. Advance to `parallel_simple.ipynb` and `parallel_llm.ipynb`
5. Apply concepts to `bmi.ipynb` or create your own workflows

---

## 💡 Tips & Tricks

### Debugging Workflows
- Use `.invoke()` to execute graphs with detailed output
- Enable logging to see workflow execution steps
- Check state transitions between nodes

### Performance Optimization
- Use parallel execution for independent steps
- Batch API calls when possible
- Cache results to avoid redundant calls

### Best Practices
- Keep nodes focused and single-purpose
- Use clear naming for nodes and edges
- Add error handling for API calls
- Document your workflow logic

---

## 🤝 Contributing

Contributions are welcome! To add new examples:

1. Create a new notebook with a clear, descriptive name
2. Add documentation and comments
3. Update this README with your notebook
4. Test thoroughly before committing

---

## 📚 Additional Resources

- [LangGraph Documentation](https://python.langchain.com/docs/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Jupyter Notebook Guide](https://jupyter-notebook.readthedocs.io/)

---

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## ⚠️ Disclaimer

These examples are for educational purposes. When using LLMs in production:
- Handle errors gracefully
- Implement proper logging and monitoring
- Be aware of API costs
- Follow rate limiting guidelines
- Implement proper authentication and authorization

---

## 🎓 Author

Created for learning and demonstrating LangGraph capabilities.

**Last Updated:** August 2026

---

## 📞 Support

For issues, questions, or suggestions:
- Check existing documentation
- Review notebook examples
- Refer to official LangGraph docs
- Open an issue in the repository

---

**Happy Learning! 🚀**
