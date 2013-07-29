from twisted.web import server, resource
from twisted.internet import reactor, ssl
import datetime

P = '\
<html>\
<head>\
<title>Secure Dead Drop</title>\
</head>\
<body>\
<table>\
<form action="display.php" method="post">\
<tr>\
<td>Enter Secured Text:</td>\
</tr>\
<tr>\
<td><form method="post"><textarea name="message" cols="50" rows="10"></textarea></form></td>\
</tr>\
</table>\
<table>\
<tr>\
<td><input type="submit" value="Submit" /></td><br />\
<td><input type="reset" value="Clear" /></td><br />\
</tr>\
</table>\
</body>\
</html>\
'
messages = "/path/to/messages/file"


def saveMessage(string,IP):
  f = open(messages,'a')
  timeStamp = datetime.datetime.now().isoformat(' ')
  f.write(timeStamp+" : "+ IP +" : "+string+"\n")
  f.close()


class Simple(resource.Resource):
  isLeaf = True
  def render(self, request):
    IP = request.getClientIP()
    html = ""
    extra = ""
    html += "<html>"
    html += "<title>DDD</title></html>"
    html += "<h1>DDD</h1>"
    html += """<table><tr>For those of you familiar with the books of Orson Scott Card, there 
    is some interesting technology in his universe. Besides tablets called "desks"<br>
    he has anonymous email and digital dead drops for passing information securely 
    in a one-way fashion. This is my attempt at that.<tr></table> """
    field_value = request.args.get('Field', '')
    button_val = request.args.get('name_submit','')	
    form = """
    <FORM ACTION="default.cgi" METHOD="POST" ENCTYPE="application/x-www-form-urlencoded">
    <P><TEXTAREA NAME="Field" COLS="50" ROWS="10"></TEXTAREA><BR>
    <INPUT TYPE="SUBMIT" NAME="name_submit" VALUE="Submit"></INPUT>
    </FORM>
    """
    if button_val == ['Submit']:
      saveMessage(field_value[0],IP)
      extra += "<html><h2>Submitted Encrypted Message:</h2></html>"
      extra += field_value[0]+"<br>"
      extra += "<h3>From IP address " + IP + "</h3>"
    return html + form + extra

sslContext = ssl.DefaultOpenSSLContextFactory('keys/server.pem','keys/ca.pem')
site = server.Site(Simple())
reactor.listenSSL(8083, site, contextFactory = sslContext)

#reactor.listenTCP(8083, site)
reactor.run()
