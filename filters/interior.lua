-- Interior design system mapping (phase 2) — pairs with latex/interior.tex.
-- Maps the manuscript's stable hooks to typeset environments (PDF only):
--   ## Decision Toolkit — Chapter N  -> DecisionToolkit panel
--   ## Key Takeaways                 -> KeyTakeaways panel
--   > ### Box N.X — Title            -> ChapterBox sidebar
--   single plain blockquote/chapter  -> PullQuote (signature line)
--   first ~2 paras of opening scene  -> OpeningScene treatment
-- EPUB keeps plain semantic structure.

if FORMAT ~= 'latex' then
  return {}
end

local function raw(tex)
  return pandoc.RawBlock('latex', tex)
end

local function header_text(h)
  return pandoc.utils.stringify(h.content)
end

local function tex_escape(s)
  return (s:gsub('[%%&#_{}$]', '\\%0'))
end

-- Panels: wrap the section under a hook heading until the next H<=2.
local function wrap_sections(blocks)
  local out = pandoc.List()
  local i = 1
  local n = #blocks
  while i <= n do
    local b = blocks[i]
    if b.t == 'Header' and b.level == 2 then
      local txt = header_text(b)
      local env = nil
      if txt:match('^Decision Toolkit') then env = 'DecisionToolkit'
      elseif txt:match('^Key Takeaways') then env = 'KeyTakeaways' end
      if env then
        out:insert(raw('\\begin{' .. env .. '}'))
        i = i + 1
        while i <= n and not (blocks[i].t == 'Header' and blocks[i].level <= 2) do
          out:insert(blocks[i])
          i = i + 1
        end
        out:insert(raw('\\end{' .. env .. '}'))
        goto continue
      end
    end
    out:insert(b)
    i = i + 1
    ::continue::
  end
  return out
end

-- Endnotes are a section heading followed by an endnotes list whose first
-- entry can be several lines long. Print the accumulated list immediately
-- below the manuscript heading, rather than waiting for the next chapter
-- hook; otherwise a chapter break can strand “Endnotes” on its own page.
local function protect_endnotes(blocks)
  local out = pandoc.List()
  for _, b in ipairs(blocks) do
    if b.t == 'Header' and b.level == 2 and header_text(b) == 'Endnotes' then
      local is_ch11_endnotes = b.identifier == 'ch11-endnotes'
      for _, class in ipairs(b.classes) do
        if class == 'ch11-endnotes' then is_ch11_endnotes = true end
      end
      if is_ch11_endnotes then
        out:insert(raw('\\clearpage'))
      else
        out:insert(raw('\\Needspace{16\\baselineskip}'))
      end
      out:insert(b)
      out:insert(raw('\\flushchapternotes'))
    else
      out:insert(b)
    end
  end
  return out
end

-- The PDF has a designed foreword injected before the automatic table of
-- contents (see latex/foreword.tex). Keep the Markdown foreword in the
-- book for EPUB, but omit its duplicate chapter from the PDF body.
local function drop_pdf_foreword(blocks)
  local out = pandoc.List()
  local skipping = false
  for _, b in ipairs(blocks) do
    if b.t == 'Header' and b.level == 1 then
      if header_text(b) == 'Foreword' then
        skipping = true
      else
        skipping = false
        out:insert(b)
      end
    elseif not skipping then
      out:insert(b)
    end
  end
  return out
end

-- Opening scene. Works whether quarto hands the filter one chapter file
-- (title injected as a top-level H1) or the merged book. For every H1
-- whose section (up to the next H1) contains a "Decision Toolkit" H2 —
-- i.e., every chapter — wrap the (optional scene-H2 +) first two
-- paragraphs after the H1 in the scene treatment.
local function section_is_chapter(blocks, i)
  for j = i + 1, #blocks do
    local b = blocks[j]
    if b.t == 'Header' and b.level == 1 then return false end
    if b.t == 'Header' and b.level == 2
       and header_text(b):match('^Decision Toolkit') then
      return true
    end
    if b.t == 'RawBlock' and b.text:match('DecisionToolkit') then
      return true
    end
  end
  return false
end

local function wrap_scenes(blocks)
  local out = pandoc.List()
  local n = #blocks
  local i = 1
  while i <= n do
    local b = blocks[i]
    out:insert(b)
    i = i + 1
    if b.t == 'Header' and b.level == 1 and section_is_chapter(blocks, i - 1) then
      -- pass through quarto's scaffolding (CodeBlock/RawBlock after the title)
      while i <= n and (blocks[i].t == 'CodeBlock' or blocks[i].t == 'RawBlock') do
        out:insert(blocks[i])
        i = i + 1
      end
      if i <= n and blocks[i].t == 'Header' and blocks[i].level == 2 then
        out:insert(blocks[i])
        i = i + 1
      end
      if i <= n and blocks[i].t == 'Para' then
        out:insert(raw('\\begin{OpeningScene}'))
        local paras = 0
        while i <= n and blocks[i].t == 'Para' and paras < 2 do
          out:insert(blocks[i])
          paras = paras + 1
          i = i + 1
        end
        out:insert(raw('\\end{OpeningScene}'))
      end
    end
  end
  return out
end

-- Boxes and pull quotes.
local function is_field_note(b)
  local first = b.content[1]
  if not (first and first.t == 'Para') then return false end
  local lead = first.content[1]
  return lead and lead.t == 'Strong'
         and pandoc.utils.stringify(lead.content):match('^Field note')
end

local function map_blockquotes(blocks)
  -- first pass: count plain single-para blockquotes between H1s (chapters)
  local out = pandoc.List()
  local plain_count = {}
  local chapter = 0
  for _, b in ipairs(blocks) do
    if b.t == 'Header' and b.level == 1 then chapter = chapter + 1 end
    if b.t == 'BlockQuote' then
      local first = b.content[1]
      local is_box = first and first.t == 'Header' and first.level == 3
                     and header_text(first):match('^Box%s')
      if not is_box and not is_field_note(b)
         and #b.content == 1 and b.content[1].t == 'Para' then
        plain_count[chapter] = (plain_count[chapter] or 0) + 1
      end
    end
  end
  chapter = 0
  for _, b in ipairs(blocks) do
    if b.t == 'Header' and b.level == 1 then chapter = chapter + 1 end
    if b.t == 'BlockQuote' then
      local first = b.content[1]
      local is_box = first and first.t == 'Header' and first.level == 3
                     and header_text(first):match('^Box%s')
      if is_field_note(b) then
        out:insert(raw('\\begin{FieldNote}'))
        for _, blk in ipairs(b.content) do out:insert(blk) end
        out:insert(raw('\\end{FieldNote}'))
      elseif is_box then
        local txt = header_text(first)
        local label, title = txt:match('^(Box%s+[%w.]+)%s*[—–%-]*%s*(.*)$')
        out:insert(raw(string.format('\\begin{ChapterBox}{%s}{%s}',
          tex_escape(label or txt), tex_escape(title or ''))))
        for k = 2, #b.content do out:insert(b.content[k]) end
        out:insert(raw('\\end{ChapterBox}'))
      elseif #b.content == 1 and b.content[1].t == 'Para'
             and (plain_count[chapter] or 0) == 1 then
        -- the chapter's one signature line -> pull quote
        out:insert(raw('\\begin{PullQuote}'))
        out:insert(b.content[1])
        out:insert(raw('\\end{PullQuote}'))
      else
        out:insert(b)  -- content blockquote: keep default styling
      end
    else
      out:insert(b)
    end
  end
  return out
end

-- Render reader-facing placeholders in red in every PDF edition so they
-- cannot be mistaken for final publication copy. [MOVING] flags inline;
-- bracketed placeholders wrap the complete bracketed run.
local function starts_placeholder(text)
  return text:match('^%[PLACEHOLDER') or text:match('^%[AUTHOR')
      or text:match('^%[MOVING') or text:match('^%[PUBLIC')
      or text:match('^%[TODO') or text:match('^%[TBD')
      or text:match('^%[TBC') or text:match('^%[ISBN')
end

local function flag_placeholders(inls)
  local out = pandoc.Inlines{}
  local collecting = false
  for _, el in ipairs(inls) do
    if not collecting and el.t == 'Str'
       and starts_placeholder(el.text) then
      collecting = true
      out:insert(pandoc.RawInline('latex', '\\textcolor{placeholderred}{'))
    end
    if el.t == 'Str' and el.text:match('%[MOVING%]') and not collecting then
      out:insert(pandoc.RawInline('latex', '\\textcolor{placeholderred}{'))
      out:insert(el)
      out:insert(pandoc.RawInline('latex', '}'))
    else
      out:insert(el)
    end
    if collecting and el.t == 'Str' and el.text:match('%]') then
      out:insert(pandoc.RawInline('latex', '}'))
      collecting = false
    end
  end
  if collecting then out:insert(pandoc.RawInline('latex', '}')) end
  return out
end

local function has_class(el, class)
  for _, candidate in ipairs(el.classes) do
    if candidate == class then return true end
  end
  return false
end

-- A few tables have a specific reader function and need different density
-- from the book's ordinary reference tables. Keep that treatment local,
-- semantic in Markdown, and absent from EPUB's content structure.
local function map_special_divs(blocks)
  local out = pandoc.List()
  for _, b in ipairs(blocks) do
    if b.t == 'Div' and has_class(b, 'opportunity-table') then
      out:insert(raw('\\begingroup\\fontsize{7.6}{9.4}\\selectfont'
        .. '\\setlength{\\tabcolsep}{2.6pt}\\renewcommand{\\arraystretch}{1.08}'))
      for _, child in ipairs(b.content) do out:insert(child) end
      out:insert(raw('\\endgroup'))
    elseif b.t == 'Div' and has_class(b, 'worksheet-table') then
      out:insert(raw('\\BookWorksheetTableBegin'))
      for _, child in ipairs(b.content) do out:insert(child) end
      out:insert(raw('\\BookWorksheetTableEnd'))
    elseif b.t == 'Div' and has_class(b, 'about-author') then
      out:insert(raw('\\begin{AuthorNote}'))
      for _, child in ipairs(b.content) do out:insert(child) end
      out:insert(raw('\\end{AuthorNote}'))
    else
      out:insert(b)
    end
  end
  return out
end

function Pandoc(doc)
  local blocks = drop_pdf_foreword(doc.blocks)
  blocks = protect_endnotes(blocks)
  blocks = wrap_sections(blocks)
  blocks = wrap_scenes(blocks)
  blocks = map_blockquotes(blocks)
  blocks = map_special_divs(blocks)
  doc.blocks = blocks
  doc = doc:walk({Inlines = flag_placeholders})
  return doc
end
