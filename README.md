# RotaCerta

Protótipo de mobilidade para Campinas com backend FastAPI e frontend React.

## Estado atual

O código integra o Google Maps para autocompletar endereços e consultar rotas alternativas, incluindo combinações de subrotas.
A origem da consulta está fixa no COTUCA no backend. A interface desenha a primeira rota retornada.

Avaliação de segurança com dados de ocorrências, iluminação e denúncias, além de contas de usuários, faz parte da proposta e ainda não está implementada.

## Executar o backend

Na raiz do repositório:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
python -m uvicorn main:app --reload --port 8000
```

Configure `GOOGLE_MAPS_API_KEY` em `backend/.env`. A integração utiliza Google Routes e Places.
A documentação fica em http://localhost:8000/docs.
No Windows, ative o ambiente com `.venv\Scripts\activate`.

## Executar o frontend

Em outro terminal, a partir da raiz:

```bash
cd frontend
cp .env.example .env
npm ci
npm run dev
```

Configure `VITE_GOOGLE_MAPS_API_KEY` com uma chave para Google Maps JavaScript API.
Use http://localhost:5173, origem permitida pelo CORS do backend.
As consultas aos serviços do Google dependem de APIs habilitadas e podem gerar cobrança.

Variáveis `VITE_*` ficam visíveis no navegador: restrinja a chave de frontend por sites e APIs permitidas no Google Cloud. Use uma chave separada no backend e não publique os arquivos `.env`.
Chaves anteriormente versionadas devem ser substituídas no Google Cloud; removê-las dos arquivos atuais não as remove do histórico.

## Organização

| Caminho | Responsabilidade |
| --- | --- |
| `backend/main.py` | Aplicação FastAPI e CORS |
| `backend/routes/maps.py` | Endpoints de mapas |
| `backend/services/services_maps.py` | Consulta e combinação de rotas |
| `backend/schemas/` | Contratos das respostas |
| `frontend/src/components/` | Componentes React |
| `frontend/index.html` | Inicialização do Google Maps |
| `backend/.env.example` e `frontend/.env.example` | Modelos de configuração |

## Endpoints

| Método | Caminho | Função |
| --- | --- | --- |
| GET | `/maps/autocomplete/{endereco}` | Sugestões de endereços |
| GET | `/maps/route/{destino}` | Rotas a partir da origem fixa |

## Verificações do frontend

```bash
cd frontend
npm run lint
npm run build
```

## Próximos passos

- Permitir que o usuário escolha a origem.
- Revisar o contrato de coordenadas entre backend e frontend.
- Implementar critérios de segurança com fontes de dados documentadas.
- Adicionar testes e tratamento de falhas dos serviços externos.
