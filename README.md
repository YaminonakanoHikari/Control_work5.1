# Blog API

## Эндпоинты

- GET /api/v1/posts/ — список постов
- GET /api/v1/posts/1/ — подробный пост
- POST /api/v1/posts/ — создать пост (только авторизованный)
- POST /api/v1/posts/1/comments/ — добавить комментарий

curl http://127.0.0.1:8000/api/v1/posts/
curl -X POST http://127.0.0.1:8000/api/v1/posts/ \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-H "Content-Type: application/json" \
-d '{"title":"Мой пост","body":"Текст","is_published":true}'
