FROM nginx:1.25-alpine


RUN rm /etc/nginx/conf.d/default.conf


COPY nginx.conf /etc/nginx/conf.d/default.conf


RUN mkdir -p /code/static && \
    mkdir -p /code/media && \
    chmod -R 755 /code

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]