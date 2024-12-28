# 👔 Recomendador de Ropa con Machine Learning 🤖

## Descripción del Proyecto 🌟
Este proyecto está diseñado para facilitar la tediosa tarea de buscar ropa en paginas FastFashion, Aunque tengan muchos productos es complejo y toma tiempo encontrar algo que nos guste.

Sube fotos de las camisas que te gusten, Dale click al modelo para que aprenda tus gustos, y deja que nuestro sistema haga el trabajo duro. Utilizando **web scraping** y **machine learning**, este proyecto analiza tus preferencias y te recomienda camisas que puede que te encantarán, proporcionando detalles como precios y enlaces. 

---

## Estructura del Proyecto 🗂️

```
├───app
│   ├───static               # Archivos estáticos (CSS, JS, imágenes)
│   └───templates            # Plantillas HTML para la interfaz web
├───base_de_datos            # Archivos relacionados con la gestión de datos
├───datos
│   ├───imagenes             # Imágenes de camisas subidas por los usuarios, mientras aun siga en produccion
│   └───procesador           
├───modelos                  # Modelos de machine learning entrenados
├───scrapper
│   └───edgedriver_win64     
│       └───Driver_Notes     
└───tests                    # Pruebas del sistema
```

---

## Características Clave ✨

- **Autenticación**: Login y registro de usuarios para garantizar una experiencia personalizada.
- **Gestor de Imágenes**: Subida de fotos para registrar las preferencias del usuario.
- **Análisis con Machine Learning**: Estudio de tus gustos basado en colores, estilos y patrones.
- **Recomendaciones Dinámicas**: Obtén sugerencias únicas con enlaces y precios actualizados.
- **Web Scraping**: Extracción de información de páginas populares de moda como Bershka y H&M.

---

## Requisitos del Sistema 🛠️

1. **Python 3.10+**
2. Instalacion de requirements.txt

---

## Instalación 🚀

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Jiuby/recomendador-camisas.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd recomendador-camisas
   ```
3. Configura un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

---

## Uso 📋

1. Ejecuta el servidor local:
   ```bash
   python api.py
   ```
2. Ve a [http://localhost:5000/api/camisas](ttp://localhost:5000/api/camisas) en tu navegador.
3. Por el momento solo se puede ver la API al momento de ejecutar los archivos de webScrapping y el proceso ETL de estos

---

## Contribución 🤝

Cualquier apoyo hasta este proyecto me seria de muy gran ayuda, ya que para mi es complejo dedicarme a cada apartado del proyecto (DataScience,BackEnd,DevOps,FrontEnd)

---


## Contacto 📧

Cualquier duda o sugerencia, no dudes en contactarme:
- **GitHub**: [Jiuby](https://github.com/Jiuby)
- **Email**: [juane8w@gmail.com](mailto:juane8w@gmail.com)

Este proyecto es realizado para demostrar mis conocimientos en las areas de 
Ciencia de datos
BackEnd
Ingenieria de datos

