import React from "react";
import ReactDOM from 'react-dom';
import aesjs from 'aes-js'

function Welcome(props) {
    return <h1>Привет, {props.name}</h1>
  }
  
  const element = <Welcome name="Алиса" />
  ReactDOM.render(
    element,
    document.getElementById('alice')
  );

function send(payload) {
  let xhr = new XMLHttpRequest();
  xhr.open("POST", '/crypto', true)

  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded")

  xhr.onreadystatechange = function() {
    if(xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
        let resp = JSON.parse(xhr.response)
        console.log(resp)
    }
  }
  xhr.send(payload)
}


send("action=get-message")
