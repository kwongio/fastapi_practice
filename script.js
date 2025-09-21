import http from 'k6/http';

export const options = {
    vus : 10,
    duration: '10s'
}

export default function () {
    const url = "http://localhost:8000"
    http.get(url + "/explorer");
}
