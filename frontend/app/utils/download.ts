export async function downloadFile(link: string) {
  const { data } = await useFetch<Blob | MediaSource>(link, {
    method: 'get',
    body: null,
    responseType: 'blob'
  });

  if (data.value) {
    const fileURL = window.URL.createObjectURL(data.value);
    const a = document.createElement('a');
    a.href = fileURL;
    a.download = link;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(fileURL);
  }
}
