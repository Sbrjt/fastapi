async function fetchApi(url, { body, method, headers } = {}) {
	const res = await fetch(url, {
		method: method || (body ? 'POST' : 'GET'),
		body: JSON.stringify(body),
		headers: {
			...(body && { 'Content-Type': 'application/json' }),
			...headers,
		},
	})

	const type = res.headers.get('content-type')

	let json = null,
		text = null

	if (type?.includes('application/json')) {
		json = await res.json()
	} else {
		text = await res.text()
	}

	if (!res.ok) {
		console.log(json || text)
	}

	return { res, json, text }
}

function formData(e) {
	return Object.fromEntries(new FormData(e.target).entries())
}

export { fetchApi, formData }
