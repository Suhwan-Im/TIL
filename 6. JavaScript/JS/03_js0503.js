axios
  .get('https://jsonplaceholder.typicode.com/users')
  .then((res) => {
    console.log(res.data);
    return res.data
  })
  .then((rlt) => {
    console.log(rlt);
  })
  .catch((err) => {
    console.log(err)
  })