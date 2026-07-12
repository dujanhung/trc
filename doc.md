# TRC doc

---

# minimap

╠╦ CLI usage       <br>
┃┣╾ -t             <br>
┃┣╾ -i             <br>
┃┗╾ -o             <br>
╠╦ control chars   <br>
┃┗╾ separator      <br>
╠╦ operator chars  <br>
┃┣╾ subtitube      <br>
┃┗╾ erasure

---

# CLI usage

```sh
python script.py \
 -t t.trc \
 -i i.txt \
 -o o.txt
```

## -t

## -i

## -o

---

# control chars

changes parser behaviors.

## separator

```txt
(O)
:&:
(...)
```

separates operators.

- (O) : an operator
- (...) : repeates

---

# operator chars

runs regex operations.

## subtitube

```txt
(S)
:=:
(R)
```

subtitubes texts.

- regex (S) : search pattern
- ref regex (R) : replacement

## erasure

```txt
(S)
```

erases texts.

- regex (S) : search pattern
