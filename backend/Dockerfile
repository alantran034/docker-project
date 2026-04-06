FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DATABASE_URL=postgresql://postgres1:FSHxbpNTO2K3TOYQ44RDUXD0XbqYL0be@dpg-d79ukln5r7bs738376ag-a.singapore-postgres.render.com/postgres1_5b72

EXPOSE 8000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]