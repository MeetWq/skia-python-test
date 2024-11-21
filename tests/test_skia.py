
import pytest


def test_import_skia():
    import skia

    print("test")


def test_import_skia_textlayout():
    from skia import textlayout

    print("test")


def test_skia_paragraph():
    from skia import Surfaces, ImageInfo, AlphaType
    from skia import textlayout
    from skia import ColorBLACK, ColorWHITE, FontMgr, FontStyle, Paint, Unicodes, kPNG

    paint = Paint()
    paint.setAntiAlias(True)
    paint.setColor(ColorBLACK)

    style = textlayout.TextStyle()
    style.setFontSize(30.0)
    style.setForegroundPaint(paint)

    font_collection = textlayout.FontCollection()
    font_collection.setDefaultFontManager(FontMgr())
    para_style = textlayout.ParagraphStyle()
    builder = textlayout.ParagraphBuilder.make(para_style, font_collection, Unicodes.ICU.Make())
    builder.pushStyle(style)
    builder.addText("test")

    paragraph = builder.Build()
    paragraph.layout(500.0)

    surface = skia.Surfaces.MakeRasterN32Premul(500, 500)
    canvas = surface.getCanvas()
    canvas.clear(ColorWHITE)
    paragraph.paint(canvas, 0, 0)

    surface.flushAndSubmit()
    image = surface.makeImageSnapshot()
    image.save("test.png", kPNG)

    print("test")
