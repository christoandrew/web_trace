FROM redis

COPY redis.conf /usr/local/etc/redis/redis.conf
COPY redisearch.so /usr/local/etc/redis/redisearch.so

CMD ["redis-server", "/usr/local/etc/redis/redis.conf", "--requirepass root"]