# TO RUN

- First some configurations must be setup on docker-compose.yml

```
environment:
      - HOST=<host>
      - DATABASE=<database>
      - USER=<user>
      - PASSWORD=<password>
      - PORT=5432
      - CIDADE=<CIDADE>
      - ESTADO=<ESTADO>
      - ADMIN_USR=admin
      - ADMIN_PASS=<PASSWORD>
```

- Run:
  `docker-compose up`
