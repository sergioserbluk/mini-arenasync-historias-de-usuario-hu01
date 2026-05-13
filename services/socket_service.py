def emitir_estado(socketio, estado): #recibe socketio que es el objeto de la conexión y el estado que se quiere emitir
    socketio.emit("estado_actualizado", estado)
