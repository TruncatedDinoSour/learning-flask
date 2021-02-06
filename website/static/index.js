console.warn('[ CUTENESS ALERT ] too much cuteness! stop being so cute >:(')
function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteID: noteId })
    }).then((_res) => {
        window.location.href = '/';
    });
}