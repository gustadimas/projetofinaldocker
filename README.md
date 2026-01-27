# Desafio Ambiente Docker

## 1) Visao geral
Este projeto mostra, de forma simples, o uso de IaC com Docker Compose.
Ele sobe uma API e um banco para demonstrar isolamento, redes e volume.

## 2) Infraestrutura como codigo
Servicos do `docker-compose.yml`:
- **api**: FastAPI com Dockerfile.
- **db**: PostgreSQL oficial.

## 3) Redes (isolamento)
- **public**: rede da API.
- **private**: rede do banco.

O banco fica apenas na `private` e nao expõe porta para o host.
A API acessa o banco pelo nome do servico: `db`.

## 4) Persistencia
O banco usa o volume `db_data`.
Isso guarda os dados mesmo se o container for recriado.

## 5) Seguranca / acesso controlado
- Usuario non-root no Dockerfile.
- Porta exposta somente da API (8080).
- `.env.example` sem senha real.
- `read_only`, `tmpfs`, `cap_drop` e `no-new-privileges` para reduzir riscos.

## 6) Como rodar (passo a passo)
Pre-requisito: Docker Desktop.

1) Copiar o template:
```bash
copy .env.example .env
```

2) Subir o compose:
```bash
docker compose up -d --build
```

3) Testar a API:
- Navegador: `http://localhost:8080/`
- PowerShell:
```powershell
Invoke-RestMethod http://localhost:8080/
Invoke-RestMethod http://localhost:8080/health
Invoke-RestMethod http://localhost:8080/info
```

Para parar:
```bash
docker compose down
```

## 7) O que poderia ser expandido
- Proxy (Traefik/Nginx)
- Portainer
- DevContainer