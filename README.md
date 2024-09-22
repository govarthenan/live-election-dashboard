# 🗳️ Live Election Dashboard

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white)
![Ruff](https://img.shields.io/badge/Ruff-v0.1.0-purple?logo=ruff&logoColor=white)
![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-4.9%2B-green?logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.0%2B-blue?logo=plotly&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-2.0%2B-orange?logo=plotly&logoColor=white)

A real-time election results dashboard that uses web scraping and data visualization techniques to display live updates.

## 🚀 Features

- **Live Updates**: Refreshes data every 60 seconds
- **Interactive Chart**: Visualizes vote counts and percentages
- **Responsive Design**: Works on desktop and mobile devices
- **Easy to Use**: Simple setup and execution

## 📊 Preview

[Insert a screenshot or GIF of your dashboard here]

## 🛠️ Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/govarthenan/live-election-dash.git
   cd live-election-dash
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Running the Application

To run the Live Election Dashboard, ensure you acitvated the virtual environment and then run the following command:

```
python main.py
```

Open your web browser and navigate to `http://localhost:8050` to view the live dashboard.

## 🔧 Configuration

You can modify the number of candidates displayed by changing the `num_pairs` parameter in the `scrape_data()` function call within `live-chart.py`:
```python
data = scrape_data(num_pairs=5) # Change this number to scrape more or fewer pairs
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/govarthenan/live-election-dash/issues).

## 📝 License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

## 👨‍💻 Author

**Govarthenan Rajadurai**

- GitHub: [@govarthenan](https://github.com/govarthenan)
- Email: govarthenan@gmail.com

## 🙏 Acknowledgements

- [Dash](https://dash.plotly.com/) for the interactive web application framework
- [Plotly](https://plotly.com/python/) for the beautiful charts
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for web scraping capabilities

---

Made with ❤️ and Python