# introduction

TRC (Text Regex Converter) is a regex transformation language.

TRC could convert TXT-to-TXT, TXT-to-MD, and other variants.

---

# features

## alphabets

TRC could handle custom alphabets that defined in a JSON file.

## io

TRC read the input file and write the output file.

## lifecycles

TRC could do pre-process and post-process.

## variants

TRC could handle arbitrary and literal text.

## flags

TRC could handle flag containers, like a list of Python methods.

## memory visibility

TRC restricts memory visibility via scope containers and named capturing operators.

## memory management

TRC could send data from and to many operators.

beside internal memory, TRC could handle external memory, such as:
- load references from other TRC files
- copy-and-paste contents from multiple external files to the output file

## arbitrary lists generator

TRC could generate arbitrary lists.

## HTML tags generator

TRC could generate common HTML tags in MD, such as:
- `<ul>`
- `<ol>`
- horizontal `<table>`
- vertical `<table>`

---

# purpose

in maintainance enviroment, TRC is used where:

- contents are repetitive and structured
- regex transformations are common
- manual conversion becomes unsafe
- templates must be reusable across many files

---

# application

TRC is commonly used for:

- API documentation
- wiki
- digital book
- digital newspaper
- other structured texts

---

# why TRC exists?

## improve conversion performance

### before

- many days
- low accuracy
- expensive

### after

- several seconds
- high accuracy
- cheap

## improve health for maintainers

### before

- finger pain
- weakness
- headache

### after

- simple one-click action
- full of energy
- relaxed mind

## clean contents

### before

- typos
- mismatches
- broken HTML tags

### after

- no typos
- no mismatches
- proper HTML tags

---

# TRC syntax doc

the full TRC syntax documentation is in the doc file.

---

# composition

the TRC processor itself is a Python script.

a TRC transformation is made of:

- alphabet (alphabet.json) : defines symbols for TRC syntax
- template (template.trc) : defines transformation rules
- input (input.txt) : input content
- output (output.txt) : output content

> [!NOTE]
> file extensions are optional.

---

# script workflows

```txt
parse CLI arguments
⬇️
read alphabet file
⬇️
read template file
⬇️
read input file
⬇️
run core functions
⬇️
write output file
```

---

# minimal example

a TRC transformation typically looks like:

<table><tr><td>

# TRC alphabet

use built-in fallback.

# TRC file

```txt
▼
◙
◆
there are ▶a◀ rocks.
◇
◘
◆
rocks-count: ▶a◀
◇
▲
```

# input file

```txt
there are 3 rocks.
```

# output file

```yml
rocks-count: 3
```

</td></tr></table>