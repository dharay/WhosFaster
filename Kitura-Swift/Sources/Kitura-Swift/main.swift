import Kitura
//import cfactorial

func fib(n: Int) -> Int{
    if n == 0 || n == 1{
        return n
    } else {
        return fib(n:n-1) + fib(n: n-2)
    }
}


let router = Router()

router.get("/") { request, response, next in
    response.send("Hello world! from Kitura!")
    next()
}

router.get("/fib/:amt") { request, response, next in
    guard let amtString = request.parameters["amt"],
        let amt = Int(amtString),
        amt >= 0
    else {
        let _ = response.send(status: .badRequest)
        return next()
    }
    response.send("\(fib(n: amt))")
    next()
}

router.get("/c/fib/:amt") { request, response, next in
    guard let amtString = request.parameters["amt"],
        let amt = Int(amtString),
        amt >= 0
    else {
        let _ = response.send(status: .badRequest)
        return next()
    }
    response.send("not implemented")
    next()
}



Kitura.addHTTPServer(onPort: 8080, with: router)
Kitura.run()
