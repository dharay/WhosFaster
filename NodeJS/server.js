


const express = require("express")
const app = express()
app.get("/", function (req, res) {
	res.send("Hello World")
})

function fibboSum(num) {
	// console.log("value of num in test() " + num)
	if (num <= 1) return 1;
	return fibboSum(num - 1) + fibboSum(num - 2);
}

app.get("/fib/:num", function (req, res) {
	res.send("Sum: " + fibboSum(req.params.num))
})
app.listen(3000)