pip freeze > requirements.txt
chmod +x entrypoint.sh
docker exec -it django /bin/sh
tasks_group =  group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
tasks_group.apply_async()
task_chain = chain(tp3.s(), tp1.s(), tp2.s())
task_chain.apply_async()
docker compose exec django python manage.py shell
