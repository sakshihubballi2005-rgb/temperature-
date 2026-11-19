const http = require ('http')

name = 'Sakshi'
dep = 'BCA'
http.createServer ((req,resp) => {
    resp.setHeader ("Content - Type", "text/html");
    // resp.write ("</2> Hello Students </2>")
    resp.write(`<html>
        <head>
        <title> Server Response </title>
        </head>
        <body>
        <h1> Server Response Page </h1>
        <h2> Name : `+name+` </h2>
        <h2> Department : `+dept+` </h2>
        <h2> `+new Date()+` </h2>
        </body>
        </html>`)
    resp.end ('Ending Server')
}) .listen(8060)