Create a tsvector column for Full text search support: https://amitosh.medium.com/full-text-search-fts-with-postgresql-and-sqlalchemy-edc436330a0c


```sql
INSERT INTO category("id","name",owner_category, category_code, parent_id) Values (1,'C1', 'OT', 01, NULL)
INSERT INTO category("id","name",owner_category, category_code, parent_id) Values (2,'C2', 'OT', 012, 1);
INSERT INTO category("id","name",owner_category, category_code, parent_id) Values (3,'C3', 'OT', 013, 1);
INSERT INTO category("id","name",owner_category, category_code, parent_id) Values (4,'C4', 'OT', 0131, 3)

INSERT INTO category("name",owner_category, category_code, parent_id) Values ('C1', 'OT', 01, NULL)
INSERT INTO category("name",owner_category, category_code, parent_id) Values ('C2', 'OT', 012, 1);
INSERT INTO category("name",owner_category, category_code, parent_id) Values ('C3', 'OT', 013, 1);
INSERT INTO category("id","name",owner_category, category_code, parent_id) Values (5,'C4', 'OT', 0131, 3);



INSERT INTO brand("id", brand_name) Values (1, 'Aztec');
INSERT INTO brand("id", brand_name) Values (2, 'louis');
INSERT INTO brand("id", brand_name) Values (3, 'Afflister');

```

```bash
alembic revision --autogenerate -m 'first migration'
alembic upgrade head
```