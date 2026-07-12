# TRC doc

---

# <a id="minimap"/> minimap

╠╦ [CLI usage](#cli)       <br>
┃┣╾ [-t](#cli_t)           <br>
┃┣╾ [-i](#cli_i)           <br>
┃┗╾ [-o](#cli_o)           <br>
╠╦ [control chars](#ctrl)  <br>
┃┗╾ [separator](#ctrl_sep) <br>
╠╦ [operator chars](#op)   <br>
┃┣╾ [subtitube](#op_sub)   <br>
┃┗╾ [erasure](#op_erasure)

---

# <a id="cli"/> CLI usage

```sh
python script.py \
 -t t.trc \
 -i i.txt \
 -o o.txt
```

[⛖](#minimap)

## <a id="cli_t"/> -t

[⛖](#minimap)

## <a id="cli_i"/> -i

[⛖](#minimap)

## <a id="cli_o"/> -o

[⛖](#minimap)

---

# <a id="ctrl"/> control chars

changes parser behaviors.

[⛖](#minimap)

## <a id="ctrl_sep"/> separator

```txt
(O)
:&:
(...)
```

separates operators.

- (O) : an operator
- (...) : repeates

[⛖](#minimap)

---

# <a id="op"/> operator chars

runs regex operations.

[⛖](#minimap)

## <a id="op_sub"/> subtitube

```txt
(S)
:=:
(R)
```

subtitubes texts.

- regex (S) : search pattern
- ref regex (R) : replacement

[⛖](#minimap)

## <a id="op_erasure"/> erasure

```txt
(S)
```

erases texts.

- regex (S) : search pattern

[⛖](#minimap)

---

[
░░░░░░░░░░░░░░░░░░░░░░░░░░<br>
░░░░████████░░████████░░░░<br>
░░██░░░░░░░░░░░░░░░░░░██░░<br>
░░██░░░░████░░████░░░░██░░<br>
░░██░░██░░░░░░░░░░██░░██░░<br>
░░██░░██░░░░██░░░░██░░██░░<br>
░░░░░░░░░░██░░██░░░░░░░░░░<br>
░░██░░██░░░░██░░░░██░░██░░<br>
░░██░░██░░░░░░░░░░██░░██░░<br>
░░██░░░░████░░████░░░░██░░<br>
░░██░░░░░░░░░░░░░░░░░░██░░<br>
░░░░████████░░████████░░░░<br>
░░░░░░░░░░░░░░░░░░░░░░░░░░
](#minimap)
