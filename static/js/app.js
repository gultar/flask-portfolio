const runFileSystemCommand = (cmd, args=[]) =>{
    try{
        console.log('Okay')
      const commandResult = window.FileSystem[cmd](...args)
      return commandResult
    }catch(e){
      console.log(e)
      return { error:e.message }
    }
}

const exec = async (cmd, args=[], pointerId) =>{
    return runFileSystemCommand(cmd, [...args])
}


const makeTerminalWindow = async () =>{
    const termContainer = document.querySelector("#main-container")
    const terminal = new Terminal("1","1")
    terminal.init()
}

window.exec = exec

setTimeout(()=>{
    makeTerminalWindow()
}, 200)
