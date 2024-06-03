@@ -3,5 +3,6 @@ WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
ENV DISABLE_AUTH True
ENV API_TYPE Empty
ENV DISABLE_AUTH False
CMD ["streamlit", "run", "main.py"]