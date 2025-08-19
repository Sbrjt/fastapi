'use client'
import AddNotes from '@/components/AddNote'
import Login from '@/components/Login'
import Notes from '@/components/Notes'
import { useState } from 'react'

export default function page() {
	const [notes, setNotes] = useState([])

	return (
		<div style={{ padding: 20 }}>
			<Login setNotes={setNotes} />
			<hr />
			<AddNotes notes={notes} setNotes={setNotes} />
			<Notes notes={notes} setNotes={setNotes} />
		</div>
	)
}
