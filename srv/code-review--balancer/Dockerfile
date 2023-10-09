FROM nginx:1.24-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./src/code_review__balancer/nginx.conf /etc/nginx/conf.d
COPY ./src/code_review__web/static /docker_app/src/code_review__web/static
COPY ./src/code_review__web/data /docker_app/src/code_review__web/data