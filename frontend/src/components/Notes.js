'use client'
import { fetchApi } from '@/lib/utils'
import { useEffect } from 'react'

function Notes({ notes, setNotes }) {
	useEffect(() => {
		getNotes()
	}, [])

	async function getNotes() {
		const { res, json } = await fetchApi('/api/note/all')

		if (res.ok) {
			setNotes(json)
		}
	}

	return (
		<>
			{notes.map(({ content, title, id }) => (
				<p key={id}>
					{title}
					<br />
					{content}
				</p>
			))}
		</>
	)
}

export default Notes
