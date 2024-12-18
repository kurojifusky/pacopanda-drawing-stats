# PDS Server

> [!NOTE]
> Currently, the public APIs only accept `GET` requests. Any
> other request method will respond with `405 Method Not Allowed`
> or `403 Forbidden`.
>
> `👑` - only allowed to be pushed with an auth token

### Endpoints

- `GET /status`
- `GET /stats{?filters}`
- `GET /artworks`
- `GET /artwork{/title}`
- `GET /characters`
- `GET /character{?names}`
- `POST /new/character/` 👑
- `POST /new/artwork/` 👑
