import './chatBot.css';
import { useEffect, useState } from 'react';
import {IoMdSend}  from 'react-icons/io';
import {BiBot,BiUser} from 'react-icons/bi';

function Basic(){
    const [chat,setChat] = useState([]);
    const [inputMessage,setInputMessage] = useState('');
    const [recipientId,setRecipientId] = useState('');
    const [recommendButton,setRecommendButton] = useState('');
    const [botTyping,setbotTyping] = useState(false);

    
   useEffect(()=>{
   
        console.log("called");
        const objDiv = document.getElementById('messageArea');
        objDiv.scrollTop = objDiv.scrollHeight;
        
    
    },[chat])

    const handleButtonClick=(evt)=>{
        evt.preventDefault();
        const name = "Khai Do";
        const request_temp = {sender : "user", sender_id : name , msg : recommendButton[2].title};
        
        if(recommendButton[2].payload !== ""){
            
            setChat(chat => [...chat, request_temp]);
            setbotTyping(true);
            
            rasaAPI(recommendButton[2].payload);
            setRecommendButton('');
        }
        else{
            if(recommendButton[2].url !== ""){
            
                setbotTyping(true);
                
                const response_temp = {sender: "bot",recipient_id : "default",msg: recommendButton[2].url};
                setChat(chat => [...chat, {sender: "bot",recipient_id : "default",msg: recommendButton[2].url}]);
                console.log(response_temp)
                setRecommendButton('');
            }else{
                window.alert("Please enter valid message");
            }
            
        }
        
    }


    const handleSubmit=(evt)=>{
        evt.preventDefault();
        const name = "Khai Do";
        const request_temp = {sender : "user", sender_id : name , msg : inputMessage};
        
        if(inputMessage !== ""){
            
            setChat(chat => [...chat, request_temp]);
            setbotTyping(true);
            setInputMessage('');
            rasaAPI(inputMessage);
        }
        else{
            window.alert("Please enter valid message");
        }
        
    }


    const rasaAPI = async function handleClick(msg) {
    
        //chatData.push({sender : "user", sender_id : name, msg : msg});
        

          await fetch('http://localhost:5005/webhooks/rest/webhook', {
            method: 'POST',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
              'charset':'UTF-8',
            },
            credentials: "same-origin",
            body: JSON.stringify({ "message": msg }),
        })
        .then(response => response.json())
        .then((response) => {
            if(response){
                response.forEach((temp) => {
                    const recipient_id = temp["recipient_id"];
                    const recipient_msg = temp["text"];        
                    const recipient_custom = temp["custom"];        
                    
                    const response_temp = {sender: "bot",recipient_id : recipient_id,msg: recipient_msg};
                    setRecipientId(recipient_id);
                    setbotTyping(false);
                    setRecommendButton(recipient_custom);
                    setChat(chat => [...chat, response_temp]);
                })
                
               // scrollBottom();

            }
        }) 
    }


    const stylecard = {
        maxWidth : '35rem',
        border: '1px solid black',
        paddingLeft: '0px',
        paddingRight: '0px',
        borderRadius: '30px',
        boxShadow: '0 16px 20px 0 rgba(0,0,0,0.4)'

    }
    const styleHeader = {
        height: '4.5rem',
        borderBottom : '1px solid black',
        borderRadius: '30px 30px 0px 0px',
        backgroundColor: '#8012c4',

    }
    const styleFooter = {
        //maxWidth : '32rem',
        borderTop : '1px solid black',
        borderRadius: '0px 0px 30px 30px',
        backgroundColor: '#8012c4',
        
        
    }
    const styleBody = {
        paddingTop : '10px',
        height: '28rem',
        overflowY: 'a',
        overflowX: 'hidden',
        
    }

    return (
      <div>
        {/* <button onClick={()=>rasaAPI("shreyas","hi")}>Try this</button> */}
        

        <div className="container">
        <div className="row justify-content-center">
            
                <div className="card" style={stylecard}>
                    <div className="cardHeader text-white" style={styleHeader}>
                        <h1 style={{marginTop:'0px'}}>Tư vấn tuyển sinh</h1>
                        {botTyping ? <h6>Bot đang nhập....</h6> : null}
                        
                    </div>
                    <div className="cardBody" id="messageArea" style={styleBody}>
                        
                        <div className="row msgarea">
                            {chat.map((user,key) => (
                                <div key={key}>
                                    {user.sender==='bot' ?
                                        (
                                            
                                            <div className= 'msgalignstart'>
                                                <BiBot className="botIcon"  /><h5 className="botmsg">{user.msg}</h5>
                                            </div>
                                        
                                        )

                                        :(
                                            
                                            <div className= 'msgalignend'>
                                                <h5 className="usermsg">{user.msg}</h5><BiUser className="userIcon" />
                                            </div>
                                        )
                                    }
                                </div>
                            ))}
                            
                        </div>
                
                    </div>
                    <div className="cardFooter text-white" style={styleFooter}>
                        <div className="row">
                            <form style={{display: 'flex'}} onSubmit={handleSubmit}>
                                <div className="col-10" style={{paddingRight:'0px'}}>
                                    {recommendButton ? <button onClick={handleButtonClick}>{recommendButton[0].title}</button> : null}
                                    <input onChange={e => setInputMessage(e.target.value)} value={inputMessage} type="text" className="msginp"></input>
                                </div>
                                <div className="col-2 cola">
                                    <button type="submit" className="circleBtn" ><IoMdSend className="sendBtn" /></button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            
        </div>
        </div>

      </div>
    );
}
  
export default Basic;
