
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

export const Dropdown =({data, symbol, setSymbol}) =>
{ 

    return(
<FormControl size='small' color='info'>
  <InputLabel id="demo-simple-select-autowidth-label">Crypto</InputLabel>
  <Select
    labelId="demo-simple-select-autowidth-label"
    id="demo-simple-select-autowidth"
    value={symbol}
    label="Cryto"
    onChange={(event)=> setSymbol(event.target.value)}
  >
    {data.map((item)=> <MenuItem value={item}>{item?.toUpperCase()}</MenuItem>)}
  </Select>
</FormControl>
)
}
