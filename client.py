import requests
from typing import Optional




class Client():
  api_url = "https://api.roblox.com"
  def __init__(self, token: str = None):
    set_token(token)
    
  def set_token(self, token: Optional[str] = None) -> None:
      """
      Authenticates the client with the passed .ROBLOSECURITY token.
      This method does not send any requests and will not throw if the token is invalid.
      Arguments:
          token: A .ROBLOSECURITY token to authenticate the client with.
      """
      self._requests.session.cookies[".ROBLOSECURITY"] = token
      
  
  
  async def get_user(id: int, type: Optional[str] = "attributes"):
    """
    Gets a user by their id.
    
    Arguments:
      id: A int that is the users id.
      type: Type of data to return, json format or the atrributes.
    """
    r = requests.get(f"{api_url}/users/{id}")
    returndata = r.json()
    if type == "json":
      return returndata
    
ro = Client()
print(ro.get_user(2905665733, "json"))
    
    
