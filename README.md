# Cine Norte Django

Aplicacion web del lado del servidor para la cartelera del cine Cine Norte.

## Ejecutar el proyecto

1. Crear y activar el entorno virtual:

   ```powershell
   py -3.13 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Instalar las dependencias:

   ```powershell
   pip install -r requirements.txt
   ```

3. Ejecutar las migraciones de Django:

   ```powershell
   python manage.py migrate
   ```

4. Iniciar el servidor:

   ```powershell
   python manage.py runserver
   ```

Visita `http://127.0.0.1:8000/` en el navegador.