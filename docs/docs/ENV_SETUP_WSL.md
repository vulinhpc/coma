# 🖥️ ENV SETUP — WSL Ubuntu (Windows 10)

## 1) WSL

```bash
wsl --install -d Ubuntu-22.04
wsl --set-version Ubuntu-22.04 2
```

## 2) Node & pnpm

```bash
sudo apt update && sudo apt install -y curl git build-essential
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
corepack enable && corepack prepare pnpm@9 --activate
```

## 3) PostgreSQL 16

```bash
sudo apt install -y postgresql postgresql-contrib
sudo service postgresql start
sudo -u postgres psql -c "CREATE USER coma WITH PASSWORD 'coma';"
sudo -u postgres psql -c "CREATE DATABASE coma OWNER coma;"
```

## 4) .env (local)

```
DATABASE_URL=postgres://coma:coma@localhost:5432/coma
CLERK_PUBLISHABLE_KEY=...
CLERK_SECRET_KEY=...
CLOUDINARY_URL=cloudinary://<key>:<secret>@<cloud_name>
```

## 5) Chạy

```bash
pnpm install
pnpm db:generate && pnpm db:migrate
pnpm dev
```
