# the MD regex converter language

# <code>◆◇</code>

```txt
◆
input texts
◇
```

represents an abitrary text content.

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

# <code>◙</code>

```
◙
◆
input texts
◇
```

represents a regex from the input file.

# <code>◘</code>

```
◘
◆
input texts
◇
```

represents a regex from the output file.

# <code>▼▲</code>

```txt
▼
▣
◙
◘
▲
```

represents an entry.

# <code>▶◀</code>

```txt
▶var_name◀
```

represents an abitrary variable.

> [!NOTE]
> - `var_name` must be `^[A-Za-z\_\-]{1-255}$`