-- Kindle EPUB profile: retain the source's vector diagrams for readers while
-- directing Kindle conversion to high-resolution PNG equivalents.
if FORMAT ~= 'epub' then return {} end
function Image(image)
  image.src = image.src:gsub('^/assets/diagrams/(.+)%.svg$', '/assets/kindle/diagrams/%1.png')
  image.src = image.src:gsub('^assets/diagrams/(.+)%.svg$', 'assets/kindle/diagrams/%1.png')
  return image
end
