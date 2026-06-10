# the regex converter language

## variants

### <code>◆◇</code>

```txt
◆
input texts
◇
```

represents an abitrary text content.

## keywords

### <code>▣</code>

```
▣
◆
metadata texts
◇
```

represents a metadata.

> [!NOTE]
> metadatas would be ignored at runtime.

### <code>◙</code>

```
◙
◆
input texts
◇
```

represents a regex from the input file.

### <code>◘</code>

```
◘
◆
input texts
◇
```

represents a regex from the output file.

## containers

### <code>▼▲</code>

```txt
▼
▣
◙
◘
▲
```

represents a container for entries.

## regexs

### <code>▶◀</code>

```txt
▶var_name◀
```

represents an abitrary variable regex.

> [!NOTE]
> - `var_name` must be `^[A-Za-z\_\-]{1-255}$`