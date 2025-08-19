'use client'
import { fetchApi, formData } from '@/lib/utils'

function AddNote({ setNotes }) {
	async function addNote(e) {
		e.preventDefault()

		const note = formData(e)
		const { res } = await fetchApi('/api/note/add', { body: note })

		if (res.ok) {
			setNotes((prev) => [...prev, note])
		} else {
			window.alert('Please login!')
		}
	}

	return (
		<>
			<h2>Add note</h2>

			<form onSubmit={addNote}>
				<input placeholder='title' name='title' required />
				<br />
				<textarea name='content' required />
				<br />
				<button type='submit'>Add</button>
			</form>
		</>
	)
}

export default AddNote
