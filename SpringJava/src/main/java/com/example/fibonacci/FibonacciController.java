package com.example.fibonacci;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class FibonacciController {

    @RequestMapping("/")
    public String index() {
        return "Greetings from Spring Boot!";
    }

    @RequestMapping(value = "/fib/{num}", method = RequestMethod.GET, produces = "application/json")
    @ResponseBody
    public int getFiboSum(@PathVariable("num") int num) {
        return fiboSum(num);
    }

    private int fiboSum(int num) {
        if (num == 0 || num == 1) {
            return 1;
        } else {
            return fiboSum(num - 1) + fiboSum(num - 2);
        }
    }
}
