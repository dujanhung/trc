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

## <a id="cli_t"/> -t

## <a id="cli_i"/> -i

## <a id="cli_o"/> -o

---

# <a id="ctrl"/> control chars

changes parser behaviors.

## <a id="ctrl_sep"/> separator

```txt
(O)
:&:
(...)
```

separates operators.

- (O) : an operator
- (...) : repeates

---

# <a id="op"/> operator chars

runs regex operations.

## <a id="op_sub"/> subtitube

```txt
(S)
:=:
(R)
```

subtitubes texts.

- regex (S) : search pattern
- ref regex (R) : replacement

## <a id="op_erasure"/> erasure

```txt
(S)
```

erases texts.

- regex (S) : search pattern

---

[𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>
𒐦<br>](#minimap)
