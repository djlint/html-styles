# HtmlStyles

Python port of npm package [html-styles](https://www.npmjs.com/package/html-styles).

List of known HTML tag default styles.

## What is this?

This is a list of default styles for HTML tags as defined by [W3C specification](https://www.w3.org/TR/html5/rendering.html).


## Install

```sh
pip install html-styles
```

## Use

```py
from HtmlStyles import html_styles
from itertools import chain


def get_tag_style(style):

    return dict(
        chain(
            *map(
                dict.items,
                [
                    {y: x["style"].get(style) for y in x["selectorText"].split(",")}
                    for x in list(
                        filter(lambda x: x["style"].get(style) is not None, html_styles)
                    )
                ],
            )
        )
    )


print(get_tag_style("display"))

print(get_tag_style("white-space"))
```

Yields:

```py
{'[hidden]': 'none', ' area': 'none', ' base': 'none', ' basefont': 'none', ' datalist': 'none', ' head': 'none', ' link': 'none', ' meta': 'none', '\nnoembed': 'none', ' noframes': 'none', ' param': 'none', ' rp': 'none', ' script': 'none', ' source': 'none', ' style': 'none', ' template': 'none', ' track': 'none', ' title': 'none', 'embed[hidden]': 'inline', 'input[type=hidden i]': 'none', 'html': 'block', ' body': 'block', 'address': 'block', ' blockquote': 'block', ' center': 'block', ' div': 'block', ' figure': 'block', ' figcaption': 'block', ' footer': 'block', ' form': 'block', ' header': 'block', ' hr': 'block', '\nlegend': 'block', ' listing': 'block', ' main': 'block', ' p': 'block', ' plaintext': 'block', ' pre': 'block', ' xmp': 'block', 'dialog:not([open])': 'none', 'slot': 'contents', 'ruby': 'ruby', 'rt': 'ruby-text', 'article': 'block', ' aside': 'block', ' h1': 'block', ' h2': 'block', ' h3': 'block', ' h4': 'block', ' h5': 'block', ' h6': 'block', ' hgroup': 'block', ' nav': 'block', ' section': 'block', 'dir': 'block', ' dd': 'block', ' dl': 'block', ' dt': 'block', ' ol': 'block', ' ul': 'block', 'li': 'list-item', 'table': 'table', 'caption': 'table-caption', 'colgroup': 'table-column-group', ' colgroup[hidden]': 'table-column-group', 'col': 'table-column', ' col[hidden]': 'table-column', 'thead': 'table-header-group', ' thead[hidden]': 'table-header-group', 'tbody': 'table-row-group', ' tbody[hidden]': 'table-row-group', 'tfoot': 'table-footer-group', ' tfoot[hidden]': 'table-footer-group', 'tr': 'table-row', ' tr[hidden]': 'table-row', 'td': 'table-cell', ' th': 'table-cell', ' td[hidden]': 'table-cell', ' th[hidden]': 'table-cell', 'table > form': 'none', ' thead > form': 'none', ' tbody > form': 'none', ' tfoot > form': 'none', ' tr > form': 'none', 'fieldset': 'block'}
{'listing': 'pre', ' plaintext': 'pre', ' pre': 'pre', ' xmp': 'pre', 'pre[wrap]': 'pre-wrap', 'nobr': 'nowrap', 'nobr wbr': 'normal', 'td[nowrap]': 'nowrap', ' th[nowrap]': 'nowrap', 'table': 'initial', 'textarea': 'pre-wrap'}
```
## License

[GPL][license] © Riverside Healthcare
Ported from `html-styles` [MIT][license] © [Mario Nebl](https://github.com/marionebl)

[license]: LICENSE