import SirioAPI # Import the Server logic
from SN_PyDepends import * # Refactor this soon and make it a proper python module damn it!

async def Process_Request(Client_Request, Client_Address):
    return Client_Request # Since this is an echo server, we just send back the Client's request

def Routine():
    DoNothing()