
const datepickers = document.querySelectorAll('.datepicker')

for(const dp of datepickers){
    dp.addEventListener('change', (event) => {
       $.post('/home/set_date', {
           due_date: event.target.value,
           id: dp.id
       })
    });
}
