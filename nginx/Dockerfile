FROM nginx:1.25-alpine


RUN mkdir -p /code/static && \
    mkdir -p /code/media && \
    chmod -R 755 /code

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]