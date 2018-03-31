$(document).ready(function ()
{
    calculateBMI();
    hideSelected(['[name="KID_DETAILS"]', '[name="BMI"]', '[name="BSA"]', '[name="YEAR"]'])

    function hideSelected(array)
    {
        $.each(array, function (index, element)
        {
            $(element).parents('.input-field').hide();
        })
    }


    $('[name="height"]').on('input', calculateBMI);
    $('[name="weight"]').on('input', calculateBMI);



    $('#calculateBp').on('click', function ()
    {
        var firstBp = $('#id_bloodpressure1').val() ? $('#id_bloodpressure1').val().split('/') : '';
        var secondBp = $('#id_bloodpressure2').val() ? $('#id_bloodpressure2').val().split('/') : '';
        var thirdBp = $('#id_bloodpressure3').val() ? $('#id_bloodpressure3').val().split('/') : '';

        var checkForLowerDiastolic = Math.min(firstBp[1], secondBp[1], thirdBp[1]);


        var comboOfAll = [firstBp, secondBp, thirdBp];

        var finalArray = [];

        $(comboOfAll).each(function (i, k)
        {
            $(k).each(function (l, m)
            {

                if (l == 1 && k[1] == checkForLowerDiastolic) {
                    finalArray.push(k);
                }

            })
        })

        addSisandDiastolic = []

        $(finalArray).each(function (r, t)
        {
            var sum = parseInt(t[0]) + parseInt(t[1]);
            addSisandDiastolic.push(sum)
        })

        var indexOfHighValue = addSisandDiastolic.reduce(function (iMax, x, i, arr)
        {
            return x < arr[iMax] ? i : iMax;
        }, 0);

        $('[name="systolic"]').val((parseInt(finalArray[indexOfHighValue][0]) + parseInt(finalArray[indexOfHighValue][0])) / 2);
        $('#calculatedSystolic').text((parseInt(finalArray[indexOfHighValue][0]) + parseInt(finalArray[indexOfHighValue][0])) / 2);

        $('#calculatedDiastolic').text((parseInt(finalArray[indexOfHighValue][1]) + parseInt(finalArray[indexOfHighValue][1])) / 2);
        $('[name="diastolic"]').val((parseInt(finalArray[indexOfHighValue][1]) + parseInt(finalArray[indexOfHighValue][1])) / 2);

        $('#anthroSign').val('false');

    });


    function calculateBMI()
    {
        var calculateBMI = '0';
        var calculatedBSA = '0'
        var height = parseFloat($('[name="height"]').val());
        var weight = parseFloat($('[name="weight"]').val());
        if (height && height >= 75 && weight && Math.round(weight) > 9) {
            if (document.getElementById("calculatedBMI"))
                document.getElementById("calculatedBMI").textContent = formulaForBmi(height, weight).toFixed(2).toString();
            if (document.getElementById("calculatedBSA"))
                document.getElementById("calculatedBSA").textContent = formulaForBsa(height, weight).toFixed(2).toString();
            $('[name="bmi"]').val(formulaForBmi(height, weight).toFixed(2));
            $('[name="bsa"]').val(formulaForBsa(height, weight).toFixed(2));
            $('[name="year"]').val(new Date().getFullYear());
            $('[name="kiduid"]').val($('#uidDisplay').text());
        } else {
            $('#calculatedBMI').text(calculateBMI.toString());
            $('#calculatedBSA').text(calculatedBSA.toString());
        }
    }

    function formulaForBmi(height, weight)
    {
        return weight / ((height * height) / 100) * 100;
    }

    function formulaForBsa(height, weight)
    {
        return Math.sqrt([height * weight] / 3600)
    }

    $('.optionsOne').siblings('div').hide();

    $('.dentalFormHolder,.pediatricsFormHolder,.nutritionHolder,.optholContainer').find('input,select,textarea').addClass('form-control');

    $('.optionsOne select').on('change', function ()
    {
        if ($(this).find('option:selected').text() == ('Abnormal') || $(this).find('option:selected').text() == ('Present')) {
            $(this).parents('div.optionsOne').siblings('div').show();
        } else {
            $(this).parents('div.optionsOne').siblings('div').hide();
        }
    })

    $('.orthodonticMaloccilsionAbnormalitiesOtherTypes li').addClass('checkbox');
    $('.orthodonticMaloccilsionAbnormalitiesOtherTypes li input').removeClass('form-control');

    $('.provisionalDiagnosis select').on('change', function ()
    {

        $('.variousOptionsForProvisionals div').hide();
        if ($(this).find('option:selected').text() == 'CARIES') {
            $('.cariesTypes').show();
        }
        if ($(this).find('option:selected').text() == 'FRACTURED TOOTH/TEETH') {
            $('.fracturedOrCrackedTeethTypes').show();
        }
        if ($(this).find('option:selected').text() == 'ABNORMAL FRENUM') {
            $('.abnormalFrenum').show();
        }
        if ($(this).find('option:selected').text() == 'PERIODONTAL ABNORMALITY') {
            $('.prediodontalAbnormalities').show();
        }
        if ($(this).find('option:selected').text() == 'ORTHODONTIC/MALOCCLUSION ABNORMALITIES - OTHERS') {
            $('.orthodonticMaloccilsionAbnormalitiesOtherTypes').show();
        }
        if ($(this).find('option:selected').text() == 'HABITS') {
            $('.habitsTypes').show();
        }
        if ($(this).find('option:selected').text() == 'ORTHODONTIC/MALOCCLUSION ABNORMALITIES') {
            $('.orthodonticMaloccilsionAbnormalitiesTypes').show();
        }
    })

    $('.provisionalDiagnosis select').removeAttr('required');
    $('[name="childuid"]').val($('#uidDisplay').text());

    if ($('.formFilledMessage').length == 1) {
        $('body').addClass('formFilledContainer');
    }
    $('.changeEyeProblem select').on('change', function ()
    {
        if ($(this).val() !== 'none') {
            $(this).parent('div').siblings('div').show()
        } else {
            $(this).parent('div').siblings('div').hide()
        }
    })
    $('.finaladvices select').on('change', function ()
    {
        if ($(this).val() === 'others') {
            $(this).parent('div').siblings('div').show()
        } else {
            $(this).parent('div').siblings('div').hide()
        }
    })

    // using jQuery
    function getCookie(name)
    {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $('#getTheAnthoDetails').on('click', function ()
    {
        var csrftoken = getCookie('csrftoken');

        $('.anthroFormQuestion,.showAfterAjaxCallAnthroDetails').hide();
        $('.loader').removeClass('loaderHide')

        $.ajax({
            url: 'http://127.0.0.1:8000/littleStar/dummyAjaxCall/',
            type: 'POST', // This is the default though, you don't actually need to always mention it
            data: { csrfmiddlewaretoken: csrftoken, kiduid: $('#uidDisplay').text() },

            success: function (data)
            {
                var localJson = JSON.parse(data);
                $(localJson).each(function (i, k)
                {
                    $('.showAfterAjaxCallAnthroDetails input').each(function (key, value)
                    {
                        if ($(this).attr('name') !== 'csrfmiddlewaretoken') {
                            $(value).val(k.fields[$(value).attr('name')]);
                        }

                    })
                })

                $('.showAfterAjaxCallAnthroDetails').show();
                $('.loader').addClass('loaderHide')


                var chartData = {
                    datasets: [{
                        label: '3rd Percentile',
                        backgroundColor: 'rgba(255, 255, 255, 0.0)',
                        borderColor: 'rgba(0, 119, 290, 0.6)',
                        data: [{ x: 1, y: 10 }, { x: 2, y: 12 }, { x: 3, y: 18 }, { x: 4, y: 5 }, { x: 5, y: 25 }, { x: 6, y: 30 }]
                    },
                    {
                        label: '50th Percentile',
                        backgroundColor: 'rgba(255, 255, 255, 0.0)',
                        borderColor: 'rgba(120, 0, 190, 0.6)',
                        data: [{ x: 1, y: 8 }, { x: 2, y: 9 }, { x: 3, y: 16 }, { x: 4, y: 8 }, { x: 5, y: 12 }, { x: 6, y: 20 }]
                    },
                    {
                        label: '99th Percentile',
                        backgroundColor: 'rgba(255, 255, 255, 0.0)',
                        borderColor: 'rgba(0, 200, 10, 0.6)',
                        data: [{ x: 1, y: 10 }, { x: 2, y: 5 }, { x: 3, y: 26 }, { x: 4, y: 18 }, { x: 5, y: 19 }, { x: 6, y: 10 }]
                    }]
                };

                var originalController = Chart.controllers.line;
                Chart.controllers.line = Chart.controllers.line.extend({
                    draw: function ()
                    {
                        originalController.prototype.draw.call(this, arguments);
                        drawLabels(this);
                    }
                });

                function drawLabels(t)
                {
                    ctx.save();
                    ctx.font = Chart.helpers.fontString(12, Chart.defaults.global.defaultFontStyle, Chart.defaults.global.defaultFontFamily);
                    ctx.fillStyle = 'red';
                    ctx.textBaseline = 'bottom';

                    var chartInstance = t.chart;
                    var datasets = chartInstance.config.data.datasets;
                    datasets.forEach(function (ds, index)
                    {
                        var label = ds.label;
                        var meta = chartInstance.controller.getDatasetMeta(index);
                        var len = meta.data.length - 1;
                        //console.log(ds, meta.data[len]._model);    
                        var xOffset = meta.data[len]._model.x + 10;
                        var yOffset = meta.data[len]._model.y;
                        ctx.fillText(label, xOffset, yOffset);
                    });
                    ctx.restore();
                }


                var ctx = document.getElementById("myChart").getContext("2d");
                var myBar = new Chart(ctx, {
                    type: 'line',
                    data: chartData,
                    options: {
                        legend: { display: false },
                        scales: {
                            xAxes: [{
                                type: 'linear',
                                scaleLabel: { display: true, labelString: 'Age' }
                            }],
                            yAxes: [{
                                ticks: { min: 0 },
                                scaleLabel: { display: true, labelString: 'MUAC' }
                            }]
                        },
                        layout: {
                            padding: {
                                left: 0,
                                right: 60,
                                top: 20,
                                bottom: 0
                            }
                        }
                    }
                });



            },
            failure: function (data)
            {
                alert('Got an error dude');
            }
        });

    })


})
