# Monkey Python

This project follows Thurston Ball's "Writing an Interpreter in Go" which can be found [here](https://interpreterbook.com).

This implmentation of the interpreter is written with python 3.11.

## Language Specification
program    := statement+
statement  := let
            | return
            | expression
let        := "let" identifier "=" expression ";"
return     := "return" expression ";"
identifier := [a-z, A-Z]+
expression := ?