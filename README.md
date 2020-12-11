## Egglang
Egglang is a simple toy language and interpreter built using python. This is a sort of learning exercise to understand how some of these lower level concepts function. The lexer and parser were written using a library called RPLY, which is pretty much a direct port of PLY. I followed a lecture by Alex Gaynor to get a base idea of how an interpreter functions and an outline for this project. You can find that [here](https://www.youtube.com/watch?v=LCslqgM48D4). 

### Goals:
Currently I have the lexer, parser, the AST and the bytecode compiler finished. All it can really do right now is add numbers together, but once I write the actual bytecode interpreter, things _should_ become a lot easier. I'd like to add variables, strings, if else statements and while loops before i consider this really completed.

### How it works:
If you're interested in how an interpreter works, i'd recommend watching the video linked above. This isn't the only way an interpreter can be built but just one possible way. If you want to step through my code, start with the lexer, then the parser and the ast, then the bytecode compiler and finally the actual interpreter. I'll add comments to all the files so you can get an idea of whats going on.
