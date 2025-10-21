import axios from 'axios'
import express from 'express'

const app = express()
app.use(express.json())

app.get("/", async (req, res) => {
  const response = await axios.get("http://10.255.255.254:2038/data")
  const data = response.data
  res.status(200).json({data: data["atomic_field_measurement"]})
})

app.listen(2101, () => {
  console.log('Mass stabilizer service running on port 2101')
})