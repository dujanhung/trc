```md

# RECL - the regex-based converter language

# description

the regex-based converter language (RECL) is a file format that designated to convert files via regex.

# features

## reusable alphabet

unlike hardcoded regex alphabets, users could swap out default RECL alphabets with different ones.

## human-readable language

users no longer deal with complex alienated regex languages. instead, an easy human-readable RECL language takes place to improve readability.

## no indentations required

unlike XML, RECL language don't use indentation, which is safe for clipboards and line-wrapping textbox UIs.

___

# example

## RECL file

```txt
▼
▣
◆
the situation
◇
◙
◆
there are ▶a◀ rocks,
they broke ▶b◀ pots.
◇
◘
◆
rocks-count: ▶a◀
broken-pots-count: ▶b◀
◇
▲
▼
▣
◆
the looks
◇
◙
◆
look.
◨
▶a◀ is broken.
◧▰delim(◑\n◐)▱
that's all the pots.
◇
◘
◆
broken-pot-names: [
◨
'▶a◀'
◧▰delim(◑,\n◐)▱
]
◇
▲
```

## input file

```txt
there are 3 rocks,
they broke 5 pots.

unaffected-texts: 999

look.
pot 1 is broken.
pot 5 is broken.
that's all the pots.
```

## output file

```yml
rocks-count: 3
broken-pots-count: 5

unaffected-texts: 999

broken-pot-names: [
'pot 1',
'pot 5'
]
```

___

# CLI usage

## install depencies

```sh
pkg install python
pip install rich
```

## run

```sh
python script.py -a alphabet.json -i input.md -o output.md
```

<table><thread><tr><td>
flag
</td><td>
description
</td></tr></thread><tbody><tr><td>
<code>-a</code>
</td><td>
filepath to a JSON file containing a RECL alphabet
</td></tr></tbody><thread><tr><td>
<code>-i</code>
</td><td>
filepath to input file
</td></tr></thread><tbody><tr><td>
<code>-o</code>
</td><td>
filepath to output file
</td></tr></tbody></table>

___

# RECL doc contents

## keywords

<table><thread><tr><td>

# <code>▣</code>

```txt
▣
◆
metadata texts
◇
```

represents a metadata.

> [!NOTE]
> metadatas would be ignored at runtime.

</td></tr></thread><tbody><tr><td>

# <code>◙</code>

```txt
◙
◆
input regexs
◇
```

represents a regex content from the input file.

</td></tr></tbody><thread><tr><td>

# <code>◘</code>

```txt
◘
◆
output regexs
◇
```

represents a regex content from the output file.

</td></tr></thread></table>

## containers

<table><thread><tr><td>

# <code>▼▲</code>

```txt
▼
▣
◙
◘
▲
```

represents a scope.

> [!IMPORTANT]
> **only use multiple of this container to split scope and organize contents**. too many may increase file size and harm readability. too few may pollute contents with inconsistent hardcoded texts.

</td></tr></thread><tbody><tr><td>

# <code>◆◇</code>

```txt
◆
abitrary text container
◇
```

represents an abitrary text container.

</td></tr></tbody><thread><tr><td>

# <code>◑◐</code>

```txt
◑literal text container◐
```

represents a literal text container.

</td></tr></thread><tbody><tr><td>

# <code>▰▱</code>

```txt
▰flag1(),flag2(),...▱
```

represents a flag container.

> [!NOTE]
> unless otherwised noted, `▰▱` can't be left empty. the ones shown in this doc are for visual purposes.

</td></tr></tbody></table>

## regex methods

> [!NOTE]
> unless othetwise noted:
> - regex methods are not unique, and can't be sent across different `▼▲`.
> - regex methods from `◘` must exist in the ones from `◙`. otherwise, it would result in `𒐪` being added in the output file.

<table><thread><tr><td>

# <code>▶◀</code>

```txt
▶var_name◀
```

represents a regex variable.

</td></tr></thread><tbody><tr><td>

# <code>◨◧</code>

```txt
◨
list of texts
◧▰▱
```

represents an infinite repetitive structure of an abitrary text, a MD list, or a MD table.

<table><thread><tr><td>
attributes
</td><td>
index (begins with <code>1</code>)
</td><td>
description
</td></tr></thread><tbody><tr><td>
<code>ul(n)</code>
</td><td>
<code>1</code>
</td><td>
construct a MD unordered list with <code>n</code> elements
</td></tr></tbody><thread><tr><td>
<code>ol(n,t,s)</code>
</td><td>
<code>1</code>
</td><td>
construct a MD ordered list with <code>n</code> elements, type <code>t</code>, and start with <code>s</code>
</td></tr></thread><tbody><tr><td>
<code>row(n)</code>
</td><td>
<code>1</code>
</td><td>
construct a MD table with <code>n</code> row
</td></tr></tbody><thread><tr><td>
<code>collumn(n)</code>
</td><td>
<code>1</code>
</td><td>
construct a MD table with <code>n</code> collumn
</td></tr></thread><tbody><tr><td>
<code>delim(n)</code>
</td><td>
<code>1</code>
</td><td>
construct a list of abitrary texts with delimeter <code>n</code>
</td></tr></tbody></table>

</td></tr></tbody></table>

```