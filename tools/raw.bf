// Bonfire Schema
// Layer 1

------types------

ok = Ok
error message:string = Error
vector count:int items:T = Vector<T>

layer layer:int = Layer
config max_file_size:int = Config
user first_name:string last_name:string about:string username:string badge:bool = User
dialog title:string = Dialog
chat title:string = Chat

inputUser user_id:int = InputUser
inputUserName username:string = InputUser

// typingActionEmpty = TypingAction
// typingAction = TypingAction

------functions------

help.getLayer = Layer
help.getConfig = Config

auth.signUp first_name:string last_name:string email:string code:string = User
auth.signIn email:string code:string = User
auth.import key:string = User

dialogs.get = Vector<Dialog>

chats.create title:string = Ok

users.get id:Vector<InputUser> = Vector<User>

usernames.check username:string = Ok
usernames.update username:string = Ok

messages.send chat_id:int text:string = Ok
// messages.setTyping action:TypingAction = Ok
