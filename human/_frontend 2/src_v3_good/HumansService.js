import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class HumansService{

//    constructor(){}


    getHumans() {
        const url = `${API_URL}/api/humans/`;
        return axios.get(url).then(response => response.data);
    }
    getHumansByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getHuman(pk) {
        const url = `${API_URL}/api/humans/${pk}`;
        return axios.get(url).then(response => response.data);
    }
//    deleteHuman(human){
//        const url = `${API_URL}/api/humans/${human.pk}`;
//        return axios.delete(url);
//    }
//    createHuman(human){
//        const url = `${API_URL}/api/humans/`;
//        return axios.post(url,human);
//    }
//    updateHuman(human){
//        const url = `${API_URL}/api/humans/${human.pk}`;
//        return axios.put(url,human);
//    }
}