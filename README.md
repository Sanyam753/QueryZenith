
# 📊 QueryZenith - Interactive SQL Query Chatbot

Welcome to **QueryZenith**! This project is a Streamlit application that allows users to interact with a MySQL database through a chat interface. Powered by the capabilities of the `langchain` library and the `ChatGroq` model, QueryZenith enables seamless and intuitive SQL query generation and execution.

## 🚀 Features

- **Interactive SQL Querying**: Chat with the application to generate and execute SQL queries.
- **Data Visualization**: Display data insights through charts and tables.
- **Multiple CSV Uploads**: Upload and chat with multiple CSV files.
- **Environment Configuration**: Load environment variables securely using dotenv.

## 🛠️ Technologies Used

- **Streamlit**: Web interface
- **Pandas**: Data manipulation
- **LangChain**: Language model interactions
- **ChatGroq**: Model for language processing
- **dotenv**: Environment variable management

## 📋 Requirements

- Python 3.7+
- Required Python libraries (see `requirements.txt`)

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/queryzenith.git
   cd queryzenith
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   Create a `.env` file in the project root and add your environment variables:

   ```dotenv
   GROQ_API_KEY=your_groq_api_key
   ```

## 📊 Usage

1. **Run the Streamlit application**:

   ```bash
   streamlit run app.py
   ```

2. **Upload your CSV files** via the sidebar and interact with the data by entering queries.

## 📁 File Structure

```
queryzenith/
├── .env.example
├── app.py
├── chatbot.py
├── requirements.txt
└── README.md
```

- **`.env.example`**: Example environment file.
- **`app.py`**: Main application file.
- **`chatbot.py`**: Chatbot implementation.
- **`requirements.txt`**: List of dependencies.
- **`README.md`**: Project documentation.

## 📝 Example Queries

- **Basic SQL Query**: "Show me the top 10 products by sales."
- **CSV Interaction**: "What is the total revenue for Tokyo in 2023?"

## 🌟 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## 📞 Support

If you have any questions or need further assistance, feel free to open an issue or contact the project maintainer at sanyamsankhala13@gmail.com.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using QueryZenith! We hope it makes your SQL querying experience seamless and enjoyable. 😊

