(function () {
    var dine = [
        { name: 'M记', isRain: true },
        { name: '木桶饭', isRain: true },
        { name: '明记', isRain: true },
        { name: '粥', isRain: true },
        { name: '牛王庄', isRain: false },
        { name: '筒骨粉', isRain: false }
    ],
        tempDine = [];
    function buildAndLoopDom() {
        var _html = '';
        $('.list').html('');
        dine.forEach((obj, i) => {
            var _dom = $(`<p class='select bounceInRight animated time-${i}'>${obj.name}<span name='${obj.name}'></span></p>`)
            $('.list').append(_dom);
        })
        tempDine = dine.concat([]);
        event();
    }
    function event() {
        $('.list p span').on('click', function () {
            var _name = $(this).attr('name');
            tempDine = tempDine.filter(function (obj) {
                return _name != obj.name;
            })
            $(this).parents().eq(0).addClass('hidden').removeClass('select');
        })
        $('.play').on('click', function () {
            console.log(tempDine);
            var _tianxuan = tempDine[Math.floor(Math.random() * tempDine.length)];
            $('.list').html('').append(`<p class='tianxuan tada animated'>${_tianxuan.name}</p>`);
            //特殊判断
            fuckMc();
            //重置与渲染
            $(this).html('回魂');
            $('.play').off('click').on('click', function () {
                buildAndLoopDom();
                $(this).html('一发入魂');
            })
        })
    }
    function fuckMc(para) {
        var date = new Date().getDay();
        var isRain = $('.rain').hasClass('checked');
        if (date == 4) {
            $('.list').html('').append(`<p class='tianxuan tada animated'>M记</p>`);
        } else if (isRain) {
            var _isRain = true;
            var time = 0;
            while (_isRain){
                time ++;
                var today = tempDine[Math.floor(Math.random() * tempDine.length)];
                _isRain = today.isRain;
                if (_isRain) {
                    $('.list').html('').append(`<p class='tianxuan tada animated'>${today.name}</p>`);
                }
                if (time <= 10) {
                    _isRain = !_isRain;
                } else {
                    console.log('随便来一发吧');
                }
            }
        }
    }

    buildAndLoopDom();
    $('.zwei-switch').on('click', function () {
        $(this).toggleClass('checked');
    })
})()




