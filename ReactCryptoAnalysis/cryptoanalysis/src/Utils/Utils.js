import dayjs from 'dayjs'
import utc from 'dayjs/plugin/utc'
import timezone from 'dayjs/plugin/timezone'

export const getCurrentDate =() => {
    const t = new Date();
    const date = ('0' + t.getUTCDate()).slice(-2);
    const month = ('0' + (t.getUTCMonth() +1)).slice(-2);
    const year = t.getUTCFullYear();
    return `${year}/${month}/${date}`;
  }



export const getCurrentDateTime = () => {
    let date = new Date();
    //return date.toISOString().replace("T"," ").substring(0, 19)
    return dayjs(date).format('YYYY-MM-DD hh:mm:ss')
} 


export const getDateInFormat = (date,fromat) =>
{
    let datenow = new Date();
    //example : dayjs().format('YYYY-MM-DD hh:mm:ss')
    return dayjs(date).format(fromat)
}