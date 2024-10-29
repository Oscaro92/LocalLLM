# Local LLM
![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat&logo=langchain&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) ![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat&logo=ollama&logoColor=white)

A chat with an LLM locally and offline.

## 🔧 Installation

Clone the repository
```shell
git clone https://github.com/Oscaro92/LocalLLM.git
cd LocalLLM
```

Create a virtual environment
```shell
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

Install dependencies
```shell
pip install -r requirements.txt
```

## ⚙️ Configuration

Add Ollama on your machine (with [Docker](https://www.docker.com/))

```shell
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

Run a model (example with llama3.2)
```shell
docker exec -it ollama ollama run llama3.2
```

## 🚀 Usage

```shell
streamlit run chat.py
```

## 📁 Project Structure

```
mail-agent/
├── chat.py             # Chat 
├── llm.py              # LLM tool
├── requirements.txt    # Dependencies
├── .env                # Environment variables
└── README.md           # Documentation
```

## 📝 License

This project is licensed under the MIT License.
