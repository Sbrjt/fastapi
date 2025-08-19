'use client'
import { fetchApi, formData } from '@/lib/utils'
import { useEffect, useState } from 'react'

function Login({ setNotes }) {
	const [user, setUser] = useState()

	useEffect(() => {
		getUser()
	}, [])

	async function getUser() {
		const { res, json } = await fetchApi('/api/auth/me')

		if (res.ok) {
			console.log(json)

			setUser(json)
		}
	}

	const handleLogin = async (e) => {
		e.preventDefault()

		const user = formData(e)

		const { res, json } = await fetchApi('/api/auth/login', {
			body: user,
		})

		if (res.ok) {
			setUser(json)

			const { json: notes } = await fetchApi('/api/note/all')
			setNotes(notes)
		} else {
			alert('Login failed')
		}
	}

	const handleLogout = async () => {
		const { res } = await fetchApi('/api/auth/logout')

		if (res.ok) {
			setNotes([])
			setUser()
		}
	}

	return (
		<>
			{user ? (
				<>
					<p>Hello {user.email}! 👋🏻</p>
					<button type='button' onClick={handleLogout}>
						Logout
					</button>
				</>
			) : (
				<>
					<h2>Login</h2>
					<form onSubmit={handleLogin}>
						<input type='email' placeholder='email' name='email' required />
						<br />
						<input
							type='password'
							placeholder='password'
							name='password'
							required
						/>
						<br />
						<button type='submit'>Login</button>
					</form>
				</>
			)}
		</>
	)
}

export default Login
