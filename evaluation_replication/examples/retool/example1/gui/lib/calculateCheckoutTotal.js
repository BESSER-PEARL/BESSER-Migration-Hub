const price = parseInt({{textInput30.value}})
const discount_percent = parseInt({{textInput31}}.value)
const total = price - (price * discount_percent /100)
return(total)
