// This JS function will take care of when the user delete notes
function deleteNote(noteId) {
    fetch ("/delete-note", {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}