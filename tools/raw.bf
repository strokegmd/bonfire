// Bonfire Schema
// Layer 1

------types------

ok = Ok
error message:string = Error
vector count:int items:T = Vector<T>

layer layer:int = Layer
authorization auth_key:bytes user:User = Authorization
config max_file_size:int = Config
dialog title:string = Dialog
chat title:string = Chat

inputUser user_id:int = InputUser
inputUserName username:string = InputUser

username username:string = Username

user user_id:int first_name:string last_name:string about:string username:string boost:bool usernames:Vector<Username> = User

// typingActionEmpty = TypingAction
// typingAction = TypingAction

------functions------

help.getLayer = Layer
help.getConfig = Config

auth.sendCode email:string = Ok
auth.signUp first_name:string last_name:string email:string code:string = Authorization
auth.signIn email:string code:string = Authorization
auth.import auth_key:bytes = Authorization

dialogs.get = Vector<Dialog>

chats.create title:string = Ok

users.get id:Vector<InputUser> = Vector<User>

account.checkUsername username:string = Ok
account.updateUsername username:string = Ok
account.addUsername username:string = Ok

messages.send chat_id:int text:string = Ok
// messages.setTyping action:TypingAction = Ok
