// Style inventory for a rendered screen. It counts what a polish pass should
// control; it does not judge taste. Evaluate it in the page:
//   DevTools console: paste the file.
//   Playwright (Node):   await page.evaluate(fs.readFileSync(path, "utf8"))
//   Playwright (Python): page.evaluate(open(path, encoding="utf-8").read())
// Optional: set window.__inventoryRoot = "<css selector>" first to scope it.
(() => {
  const root = document.querySelector(window.__inventoryRoot || "body") || document.body;
  const canvas = document.createElement("canvas");
  canvas.width = canvas.height = 1;
  const ctx = canvas.getContext("2d", { willReadFrequently: true });
  const cache = new Map();
  const rgba = (value) => {
    if (!value || value === "none") return null;
    if (cache.has(value)) return cache.get(value);
    ctx.clearRect(0, 0, 1, 1);
    ctx.fillStyle = "#000";
    ctx.fillStyle = value;
    ctx.fillRect(0, 0, 1, 1);
    const [r, g, b, a] = ctx.getImageData(0, 0, 1, 1).data;
    const out = { r, g, b, a: a / 255 };
    cache.set(value, out);
    return out;
  };
  const hex = (c) => "#" + [c.r, c.g, c.b].map((v) => v.toString(16).padStart(2, "0")).join("");
  const lum = (c) => {
    const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
    return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b);
  };
  const ratio = (a, b) => { const [lo, hi] = [lum(a), lum(b)].sort((x, y) => x - y); return (hi + 0.05) / (lo + 0.05); };
  const sat = (c) => { const mx = Math.max(c.r, c.g, c.b) / 255, mn = Math.min(c.r, c.g, c.b) / 255, l = (mx + mn) / 2; return mx === mn ? 0 : (mx - mn) / (1 - Math.abs(2 * l - 1)); };
  const count = (map, key) => map.set(key, (map.get(key) || 0) + 1);
  const top = (map, n = 12) => [...map.entries()].sort((a, b) => b[1] - a[1]).slice(0, n).map(([value, uses]) => ({ value, uses }));
  const visible = (el) => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return r.width > 0 && r.height > 0 && s.visibility !== "hidden" && s.display !== "none"; };
  const ownText = (el) => [...el.childNodes].filter((n) => n.nodeType === 3).map((n) => n.textContent).join("").trim();
  const lineCount = (el) => {
    const tops = new Set();
    for (const n of el.childNodes) {
      if (n.nodeType !== 3 || !n.textContent.trim()) continue;
      const range = document.createRange();
      range.selectNodeContents(n);
      for (const r of range.getClientRects()) if (r.width > 0) tops.add(Math.round(r.top));
    }
    return tops.size;
  };
  const sample = (el) => (ownText(el) || el.getAttribute("aria-label") || el.tagName).slice(0, 40);

  // Nearest opaque background; gradients, images and translucency stay unresolved.
  const background = (el) => {
    for (let node = el; node && node.nodeType === 1; node = node.parentElement) {
      const s = getComputedStyle(node);
      if (s.backgroundImage && s.backgroundImage !== "none") return { unresolved: "gradient or image behind text" };
      const c = rgba(s.backgroundColor);
      if (c && c.a >= 0.99) return c;
      if (c && c.a > 0.01) return { unresolved: "translucent background" };
    }
    return rgba(getComputedStyle(document.body).backgroundColor) || { r: 255, g: 255, b: 255, a: 1 };
  };

  const sizes = new Map(), weights = new Map(), textColors = new Map(), families = new Map();
  const borders = new Map(), shadows = new Map(), radii = new Map();
  const warnings = { smallText: [], lowContrast: [], unresolvedContrast: 0, hangulBreaks: [], darkFilledControls: [], saturatedAreas: [] };
  const viewportArea = innerWidth * innerHeight;

  for (const el of [root, ...root.querySelectorAll("*")]) {
    if (!visible(el) || el.closest("svg")) continue;
    const s = getComputedStyle(el);
    const text = ownText(el);
    if (text) {
      const size = parseFloat(s.fontSize);
      count(sizes, size);
      count(weights, s.fontWeight);
      count(families, s.fontFamily.split(",")[0].replace(/["']/g, "").trim());
      const fg = rgba(s.color);
      if (fg) count(textColors, hex(fg));
      if (size < 13) warnings.smallText.push({ text: text.slice(0, 40), size });
      const bg = background(el);
      if (fg && !bg.unresolved) {
        const large = size >= 24 || (size >= 18.66 && Number(s.fontWeight) >= 700);
        const r = ratio(fg, bg);
        if (r < (large ? 3 : 4.5)) warnings.lowContrast.push({ text: text.slice(0, 40), ratio: Number(r.toFixed(3)), fg: hex(fg), bg: hex(bg), large });
      } else if (bg.unresolved) warnings.unresolvedContrast++;
      if (/[가-힣]/.test(text) && s.wordBreak !== "keep-all" && lineCount(el) > 1)
        warnings.hangulBreaks.push(text.slice(0, 40));
    }
    for (const side of ["Top", "Right", "Bottom", "Left"]) {
      const w = parseFloat(s[`border${side}Width`]), c = rgba(s[`border${side}Color`]);
      if (w > 0 && s[`border${side}Style`] !== "none" && c && c.a > 0) { count(borders, `${w}px ${s[`border${side}Style`]} ${hex(c)}@${c.a.toFixed(2)}`); break; }
    }
    if (s.boxShadow !== "none") count(shadows, s.boxShadow);
    if (s.borderTopLeftRadius !== "0px") count(radii, s.borderTopLeftRadius);
    const bg = rgba(s.backgroundColor);
    const rect = el.getBoundingClientRect();
    const control = el.matches("button, a, [role=button], [role=tab], .btn, input[type=submit]");
    const stop = (s.backgroundImage.match(/rgba?\([^)]*\)|#[0-9a-f]{3,8}\b|oklch\([^)]*\)/i) || [])[0];
    const fill = bg && bg.a > 0.5 ? bg : stop ? rgba(stop) : null;
    if (control && fill && fill.a > 0.5 && lum(fill) < 0.05) warnings.darkFilledControls.push(sample(el));
    if (bg && bg.a > 0.5 && sat(bg) > 0.35 && lum(bg) > 0.02 && lum(bg) < 0.8 && rect.width * rect.height > viewportArea * 0.03)
      warnings.saturatedAreas.push({ element: sample(el), color: hex(bg), share: Number((rect.width * rect.height / viewportArea).toFixed(3)) });
  }

  // Chart marks: radius spread, flat versus gradient fills, relation to plot size.
  const marks = { circleRadii: new Map(), flatRects: 0, gradientRects: 0, plots: [] };
  for (const svg of root.querySelectorAll("svg")) {
    const box = svg.getBoundingClientRect();
    if (box.width < 200 || box.height < 120) continue;
    const scale = box.width / (svg.viewBox.baseVal?.width || box.width);
    marks.plots.push({ width: Math.round(box.width), height: Math.round(box.height) });
    for (const c of svg.querySelectorAll("circle")) {
      const fill = c.getAttribute("fill") || "";
      if (fill === "transparent" || fill === "none" || fill.startsWith("url(#h")) continue;
      count(marks.circleRadii, Number((c.r.baseVal.value * scale).toFixed(1)));
    }
    for (const r of svg.querySelectorAll("rect")) {
      const fill = r.getAttribute("fill") || getComputedStyle(r).fill;
      if (!fill || fill === "none" || fill === "transparent") continue;
      fill.startsWith("url(") ? marks.gradientRects++ : marks.flatRects++;
    }
  }
  const barFills = new Map();
  for (const el of root.querySelectorAll("*")) {
    const r = el.getBoundingClientRect();
    if (el.closest("svg") || r.width < 6 || r.height < 6 || r.width > 80) continue;
    const s = getComputedStyle(el);
    const c = rgba(s.backgroundColor);
    const gradient = s.backgroundImage.startsWith("linear-gradient") || s.backgroundImage.startsWith("radial-gradient");
    if ((c && c.a > 0.5 && sat(c) > 0.4 && r.height > r.width * 0.8) || (gradient && r.height > r.width))
      count(barFills, gradient ? "gradient" : "flat");
  }

  return {
    scope: window.__inventoryRoot || "body",
    viewport: [innerWidth, innerHeight],
    text: {
      fontSizes: top(sizes, 20).sort((a, b) => a.value - b.value),
      distinctSizes: sizes.size,
      minSize: Math.min(...sizes.keys()),
      weights: top(weights),
      families: top(families, 6),
      distinctTextColors: textColors.size,
      textColors: top(textColors, 10),
    },
    surface: { borderStyles: top(borders, 10), distinctBorders: borders.size, shadows: top(shadows, 8), distinctShadows: shadows.size, radii: top(radii, 10) },
    chartMarks: { plots: marks.plots, circleRadii: top(marks.circleRadii), flatSvgRects: marks.flatRects, gradientSvgRects: marks.gradientRects, htmlBars: top(barFills) },
    warnings: {
      smallText: warnings.smallText.slice(0, 15), smallTextCount: warnings.smallText.length,
      lowContrast: warnings.lowContrast.slice(0, 15), lowContrastCount: warnings.lowContrast.length,
      unresolvedContrast: warnings.unresolvedContrast,
      hangulMayBreakMidWord: warnings.hangulBreaks.slice(0, 10), hangulMayBreakMidWordCount: warnings.hangulBreaks.length,
      darkFilledControls: warnings.darkFilledControls,
      saturatedAreas: warnings.saturatedAreas.slice(0, 10),
    },
    note: "Counts and flags only. Inspect the rendered screen; gradients, images and translucent layers leave contrast unresolved.",
  };
})()
