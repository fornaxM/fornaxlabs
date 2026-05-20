FROM nginx:alpine

# Copy site files
COPY . /usr/share/nginx/html

# Copy nginx config template (uses $PORT injected by Railway)
COPY nginx.conf /etc/nginx/templates/default.conf.template

EXPOSE 8080
