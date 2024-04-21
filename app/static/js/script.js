$(document).ready(function (e) {
    $('#choose-file').on('submit',(function(e) {
        e.preventDefault(); // делаем отмену действия браузера и формируем ajax
        var formData = new FormData($('#choose-file')[0]);
        // данные с формы завернем в переменную для ajax
        $.ajax({
            type:'POST', // тип запроса
            url: '/', // куда будем отправлять, можно явно указать
            data:formData, // данные, которые передаем
            cache:false, // кэш и прочие настройки писать именно так (для файлов)
            // (связано это с кодировкой и всякой лабудой)
            contentType: false, // нужно указать тип контента false для картинки(файла)
            processData: false, // для передачи картинки(файла) нужно false
            success:function(data){ // в случае успешного завершения
                let img = document.createElement('img')
                img.src = 'data:image/png;base64,' + data
                let parrent = document.getElementsByClassName('result')[0]
                for (let index = 0; index < parrent.children.length; index++) {
                    parrent.children[0].remove()
                    
                }
                parrent.appendChild(img)
            },
            error: function(data){ // в случае провала
                console.log("Завершилось с ошибкой"); // сообщение об ошибке
                console.log(data); // и данные по ошибке в том числе
            }
        });
    }));
});