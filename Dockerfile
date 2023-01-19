FROM python:3.9.15

ENV data=TRUE
RUN pip install numpy waitress flask tflite-runtime requests tensorflow

WORKDIR /app

COPY ["predict.py", "cancer_model.tflite", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--port=9696", "predict:app"]