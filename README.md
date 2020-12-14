## Egglang
Egglang is a simple toy language and interpreter built using python. This is a sort of learning exercise to understand how some of these lower level concepts function. The lexer and parser were written using a library called RPLY, which is pretty much a direct port of PLY. I followed a lecture by Alex Gaynor to get a base idea of how an interpreter functions and an outline for this project. You can find that [here](https://www.youtube.com/watch?v=LCslqgM48D4). 

### Goals:
Currently I have all the moving parts finished, but I'd like to add variables, strings, if else statements and while loops before i consider this really completed. Currently I can just add numbers together

### How it works:
If you're interested in how an interpreter works, i'd recommend watching the video linked above. This isn't the only way an interpreter can be built but just one possible way. If you want to step through my code, start with the lexer, then the parser and the ast, then the bytecode compiler and finally the actual interpreter. There's comments in each file to direct you, and if you trace everything from the main file, you should be able to understand what's going on. I found it difficult to learn all these moving parts as I couldnt really find well commented code (go figure) for an interpreter written in python using the same library.
