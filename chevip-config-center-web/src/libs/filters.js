

var formatDate = function(value, format) {
  if (!(value instanceof Date)) {
    value = new Date(value)
  }
  return value.format(format)
}

var bgImg = function(path) {
  return {'background-image': `url("${encodeURI(path)}")`}
}

export { formatDate, bgImg }
