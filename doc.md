# the regex-based converter language

## description

## example

### regex converter file

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
◧▰delim('\n')▱
that's all the pots
◇
◘
◆
broken-pot-names: [
◨
'▶a◀',
◧▰delim(',\n')▱
]
◇
▲
```

### input file

```txt
there are 3 rocks,
they broke 5 pots.

look.
pot 1 is broken.
pot 5 is broken.
that's all the pots.
```

### output file

```yml
rocks-count: 3
broken-pots-count: 5
broken-pot-names: [
'pot 1',
'pot 5'
]
```

___

# doc contents

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

represents a keyword container.

</td></tr></thread><tbody><tr><td>

# <code>◆◇</code>

```txt
◆
abitrary text container
◇
```

represents an abitrary text container.

</td></tr></tbody><thread><tr><td>

# <code>▰▱</code>

```txt
▰flag1(),flag2(),...▱
```

represents a flag container.

</td></tr></thread></table>

## regex methods

<table><thread><tr><td>

# <code>▶◀</code>

```txt
▶var_name◀
```

represents a regex variable.

> [!NOTE]
> - `▶◀` are not unique, and can't be sent across different `▼▲`.
> - `▶◀` from `◘` must exist in `▶◀` from `◙`. otherwise, it would result in `𒐪` being added in output file.

</td></tr></thread><tbody><tr><td>

# <code>◨◧</code>

```txt
◨
list of texts
◧▰delim(',')▱
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
construct a MD ordered list with <code>n</code> elements, type <code>t</code> and start with <code>s</code>
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
split an abitrary text with delimeter <code>n</code>
</td></tr></tbody></table>

</td></tr></tbody></table>