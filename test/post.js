import fs from 'fs'
import fetch from 'node-fetch'

const url = 'http://0.0.0.0:61112'

const body = {
    audio_name: 'input.slk',
    audio_data: "data:audio/silk;base64," + fs.readFileSync('input.slk', 'base64')
};
const response = await fetch(url + '/api/audio/', {
    body: JSON.stringify(body),
    method: 'post',
    headers: { 'Content-Type': 'application/json' } // eslint-disable-line
}); // eslint-disable-line
const data = await response.json()
console.log(data) // eslint-disable-line