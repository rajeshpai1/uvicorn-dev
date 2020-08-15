async def app(scope, receive, send):
	assert scope['type'] == 'http'
	await send({
		'type': 'http.response.start',
		'status': 200,
		'port': 300,
		'headers': [
			[b'content-type', b'text/plain'],
		]
	})
	await send({
		'type': 'http.response.body',
		'body': b'Hello, world!',
	})
