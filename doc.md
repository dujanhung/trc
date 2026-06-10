# the regex converter language

## variants

<table><tr><td>

𒐪𒐪𒐪𒐪𒐪

<details>

# <code>◆◇</code>

```txt
◆
abitrary texts
◇
```

represents an abitrary text content.

</details>

𒐪𒐪𒐪𒐪𒐪

</td><td>

𒐪𒐪𒐪𒐪𒐪

# <code>◨◧</code>

```txt
◨
list of texts
◧◉○
```

represents a list of texts.


## attributes

- `row()`
- `collumn()`
- `table()`

𒐪𒐪𒐪𒐪𒐪

</td></tr></table>

## keywords

<table><tr><td>

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

</td><td>

# <code>◙</code>

```
◙
◆
input regexs
◇
```

represents a regex content from the input file.

</td><td>

# <code>◘</code>

```
◘
◆
output regexs
◇
```

represents a regex content from the output file.

</td></tr></table>

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