# 🚀 Web App de Análisis y Forecasting de Ventas 📊

¡Bienvenido al repositorio de una poderosa herramienta de Data Mining y Forecasting para análisis de ventas en la industria agrícola! 🌾🐄🐖🐓

Esta aplicación utiliza Flask, SQLAlchemy y Prophet para predecir ventas y analizar materiales necesarios en el futuro. Además, presenta una interfaz web interactiva para la visualización de datos históricos y proyecciones.

## 🌟 Características Principales

✅ Carga y almacenamiento de datos históricos de ventas en una base de datos SQLite.  
✅ Forecasting de ventas utilizando el modelo Prophet para predecir unidades vendidas.  
✅ Cálculo automatizado de materiales necesarios (alimentos y recursos) por animal.  
✅ Interfaz interactiva con visualización dinámica de gráficos y datos.  
✅ Endpoints REST que devuelven datos en formato JSON para facilitar la integración.

## 🛠️ Tecnologías Utilizadas

- **Backend:** Flask + SQLAlchemy + SQLite
- **Ciencia de Datos:** Prophet + Pandas
- **Frontend:** HTML5, CSS3 (archivos de template: index.html, forecasting.html, materials.html)
- **Interactividad:** Gráficos interactivos integrados en la web

## 📂 Estructura del Proyecto

```
📦 Proyecto
├── .venv/ # Entorno virtual
├── templates/ # Archivos HTML
│ ├── index.html # Página principal
│ ├── forecasting.html # Visualización de pronósticos
│ └── materials.html # Visualización de materiales necesarios
├── Supermix_Sales_data.csv # Datos históricos de ventas
├── Combined_Sales_Data_forecast.csv # Resultados de forecasting
├── app.py # Código principal de la aplicación
├── knn_model.pkl # Modelo KNN (si es relevante)
├── requirements.txt # Librerías necesarias
└── README.md # Documentación del proyecto

bash
Copy
Edit
```

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/crime-prevention-system.git
cd crime-prevention-system
```

Set up a virtual environment:
```
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
Install dependencies:
```

pip install -r requirements.txt
Run the application:

python app.py
Access the dashboard at: http://127.0.0.1:5000
```

🔥 Fire Detection Example

🔫 Gun Detection Example

🗣️ Voice-to-Text Alert Example

🎯 Project Goals
Enhance public safety by detecting threats earlier.

Help law enforcement and security teams act proactively.

Reduce casualties and crime incidents with smart AI monitoring.

🤝 Contribution
Contributions are welcome! 🎉
Feel free to open issues, suggest improvements, or submit pull requests.

📄 License
This project is licensed under the MIT License. 📜

🚨 Disclaimer
This system is intended to assist and not replace human security personnel.
False positives/negatives are possible depending on model accuracy and conditions.
