# the regex-based converter language

## variants

<table><thread><tr><td>

# <code>◆◇</code>

```txt
◆
abitrary texts
◇
```

represents an abitrary text content.

</td></tr></thread><tbody><tr><td>

# <code>◨◧</code>

```txt
◨
list of texts
◧◉○
```

represents a list of texts.

<table><thread><tr><td>
attributes
</td><td>
description
</td></tr></thread><tbody><tr><td>
flag[1] <code>ul(n)</code>
</td><td>
construct an unordered list with <code>n</code> elements
</td></tr></tbody><thread><tr><td>
flag[1] <code>ol(n,t,s)</code>
</td><td>
construct an ordered list with <code>n</code> elements, type <code>t</code> and start with <code>s</code>
</td></tr></thread><tbody><tr><td>
flag[1] <code>row(n)</code>
</td><td>
construct a table with <code>n</code> row
</td></tr></tbody><thread><tr><td>
flag[1] <code>collumn(n)</code>
</td><td>
construct a table with <code>n</code> collumn
</td></tr></thread><tbody><tr><td>
flag[0] <code>delim(n)</code>
</td><td>
split strings with delimeter <code>n</code>
</td></tr></tbody></table>

</td></tr></tbody></table>

## keywords

<table><thread><tr><td>

# <code>▣</code>

```
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

```
◙
◆
input regexs
◇
```

represents a regex content from the input file.

</td></tr></tbody><thread><tr><td>

# <code>◘</code>

```
◘
◆
output regexs
◇
```

represents a regex content from the output file.

</td></tr></thread></table>

## containers

### <code>▼▲</code>

```txt
▼
▣
◙
◘
▲
```

represents an entry container.

## regexs

### <code>▶◀</code>

```txt
▶var_name◀
```

represents an abitrary variable regex.

> [!NOTE]
> - `var_name` must be `^[A-Za-z\_\-]{1-255}$`