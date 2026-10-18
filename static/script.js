const chatForm=document.getElementById("chatForm");
const questionInput=document.getElementById("questionInput");
const conversation=document.getElementById("conversation");
const sendButton=document.getElementById("sendButton");
const pages={
    chat:document.getElementById("chatPage"),
    about:document.getElementById("aboutPage"),
    help:document.getElementById("helpPage")
};
function showPage(pageName){
    Object.entries(pages).forEach(([name,page])=>{
        page.hidden=name!=pageName;
    });
    document.querySelectorAll(".nav-link").forEach(button=>{
        button.classList.toggle("active",button.dataset.page==pageName);
    });
}
document.querySelectorAll("[data-page]").forEach(button=>{
    button.addEventListener("click",event=>{
        event.preventDefault();
        showPage(button.dataset.page);
    });
});
document.querySelectorAll("[data-question]").forEach(button=>{
    button.addEventListener("click",()=>{
        questionInput.value=button.dataset.question;
        showPage("chat");
        sendQuestion();
    });
});
function addTypingIndicator() {
    const row=document.createElement("article");
    row.className="message-row assistant-row";
    const bubble=document.createElement("div");
    bubble.className="message assistant-message";
    bubble.textContent="Finding an answer...";
    row.appendChild(bubble);
    conversation.appendChild(row);
    conversation.scrollTop=conversation.scrollHeight;
    return row;
}
function addMessage(text,sender="assistant",isError=false){
    const row=document.createElement("article");
    row.className=`message-row ${
        sender==="user"?"user-row":"assistant-row"
    }`;
    const avatar=document.createElement("div");
    avatar.className=`avatar ${
        sender==="user"?"user-avatar":"assistant-avatar"
    }`;
    avatar.textContent=sender==="user"?"●" : "✳";
    avatar.setAttribute("aria-hidden","true");
    const bubble=document.createElement("div");
    bubble.className=`message ${
        sender==="user"?"user-message":"assistant-message"
    }`;
    if(isError){
        bubble.classList.add("error-message");
    }
    bubble.textContent=text;
    row.append(avatar,bubble);
    conversation.appendChild(row);
    conversation.scrollTop=conversation.scrollHeight;
    return row;
}
async function sendQuestion() {
    const question = questionInput.value.trim();
    if (!question||sendButton.disabled){
        return;
    }
    addMessage(question,"user");
    questionInput.value="";
    questionInput.style.height="auto";
    sendButton.disabled=true;
    const loadingMessage=addTypingIndicator();
    try {
        const response=await fetch("/chat", {
            method:"POST",
            headers:{
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question:question
            })
        });

        const data=await response.json().catch(() => ({}));
        if (!response.ok) {
            addMessage(
                data.error || "Something went wrong. Please try again.",
                "assistant",
                true
            );
            return;
        }
        const answer=typeof data.answer==="string"? data.answer.trim(): "";
        if(answer){
            addMessage(answer, "assistant");
        }else{
            addMessage(
                "The backend did not return an answer. Please check your Flask backend.",
                "assistant",
                true
            );
        }

    }catch(error){
        addMessage(
            "Unable to connect to the server. Please check that Flask is running.",
            "assistant",
            true
        );
        console.error("Chat error:", error);
    } finally {
        loadingMessage.remove();
        sendButton.disabled = false;
        questionInput.focus();
    }
}
chatForm.addEventListener("submit",event=>{
    event.preventDefault();
    sendQuestion();
});

questionInput.addEventListener("keydown",event => {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        chatForm.requestSubmit();
    }
});
questionInput.addEventListener("input",() => {
    questionInput.style.height = "auto";
    questionInput.style.height =Math.min(questionInput.scrollHeight, 150) + "px";
});
showPage("chat");
