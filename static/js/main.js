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

                var ctx = document.getElementById("myChart");
                var myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        datasets: [{
                            label: '3rd Percentile',
                            data: [11.7, 11.9, 12.2, 12.3, 12.4, 12.5, 12.5, 12.6, 12.6, 12.7, 12.7, 12.7, 12.7, 12.8, 12.8, 12.8, 12.9, 12.9, 13, 13, 13.1, 13.1, 13.2, 13.2, 13.3, 13.3, 13.3, 13.4, 13.4, 13.5, 13.5, 13.5, 13.6, 13.6, 13.6, 13.6, 13.7, 13.7, 13.7, 13.7, 13.8, 13.8, 13.8, 13.8, 13.8, 13.9, 13.9, 13.9, 13.9, 13.9, 14, 14, 14, 14, 14.1, 14.1, 14.1, 14.1],
                            // Changes this dataset to become a line
                            type: 'line',
                            radius: 0,
                            borderColor: ['#e6da48'],
                            background: '#e6da48',
                            fill: false,
                        },

                        {
                            label: '15th Percentile',
                            fill: false,
                            radius: 0,
                            data: [12.5, 12.8, 13, 13.1, 13.3, 13.3, 13.4, 13.5, 13.5, 13.5, 13.5, 13.6, 13.6, 13.6, 13.7, 13.7, 13.7, 13.8, 13.8, 13.9, 13.9, 14, 14, 14.1, 14.1, 14.2, 14.2, 14.3, 14.3, 14.4, 14.4, 14.4, 14.5, 14.5, 14.5, 14.6, 14.6, 14.6, 14.6, 14.7, 14.7, 14.7, 14.8, 14.8, 14.8, 14.8, 14.9, 14.9, 14.9, 14.9, 15, 15, 15, 15, 15.1, 15.1, 15.1, 15.1]
                        }, {
                            label: '50th Percentile',
                            fill: false,
                            borderColor: ['#1bbe10'],
                            radius: 0,
                            data: [13.5, 13.8, 14.1, 14.2, 14.4, 14.5, 14.5, 14.6, 14.6, 14.6, 14.7, 14.7, 14.7, 14.8, 14.8, 14.8, 14.9, 14.9, 15, 15, 15.1, 15.2, 15.2, 15.3, 15.3, 15.4, 15.4, 15.5, 15.5, 15.6, 15.6, 15.7, 15.7, 15.7, 15.8, 15.8, 15.8, 15.9, 15.9, 15.9, 16, 16, 16, 16.1, 16.1, 16.1, 16.2, 16.2, 16.2, 16.3, 16.3, 16.3, 16.4, 16.4, 16.4, 16.5, 16.5, 16.5]
                        },
                        {
                            label: '85th Percentile',
                            fill: false,
                            borderColor: ['#f66464'],
                            radius: 0,
                            data: [14.6, 14.9, 15.2, 15.4, 15.5, 15.6, 15.7, 15.8, 15.8, 15.9, 15.9, 15.9, 16, 16, 16, 16.1, 16.1, 16.2, 16.2, 16.3, 16.4, 16.4, 16.5, 16.6, 16.6, 16.7, 16.7, 16.8, 16.9, 16.9, 17, 17, 17.1, 17.1, 17.1, 17.2, 17.2, 17.3, 17.3, 17.4, 17.4, 17.4, 17.5, 17.5, 17.6, 17.6, 17.6, 17.7, 17.7, 17.8, 17.8, 17.8, 17.9, 17.9, 18, 18, 18.1, 18.1]
                        },
                        {
                            label: '97th Percentile',
                            fill: false,
                            radius: 0,
                            borderColor: ['#fa2020'],
                            data: [15.5, 15.9, 16.2, 16.4, 16.5, 16.7, 16.7, 16.8, 16.9, 16.9, 16.9, 17, 17, 17.1, 17.1, 17.2, 17.2, 17.3, 17.3, 17.4, 17.5, 17.5, 17.6, 17.7, 17.8, 17.8, 17.9, 18, 18, 18.1, 18.2, 18.2, 18.3, 18.3, 18.4, 18.4, 18.5, 18.5, 18.6, 18.6, 18.7, 18.7, 18.8, 18.8, 18.9, 18.9, 19, 19, 19.1, 19.1, 19.2, 19.2, 19.3, 19.3, 19.4, 19.4, 19.5, 19.5]
                        },

                        {
                            label: 'MUAC vs Age',
                            backgroundColor: 'rgba(0,0,0,0.7)',
                            borderColor: '#fff',
                            borderWidth: 1,
                            radius: 5,
                            type: 'bubble',
                            data: [
                                {
                                    y: parseInt(localJson[0].fields.midupperarmcircumference),
                                    x: parseInt($('.convertedAge').text()) * 12
                                }
                            ]
                        }
                        ],

                        labels: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

                    },
                    options: {
                        legend: {
                            position: 'right'
                        },
                        responsive: true,

                        tooltips: {
                            enabled: false
                        },
                        scales: {

                            yAxes: [{
                                scaleLabel: {
                                    display: true,
                                    labelString: 'MUAC in cms'
                                },
                                gridLines: {
                                    display: false
                                }
                            }],
                            xAxes: [{
                                scaleLabel: {
                                    display: true,
                                    labelString: 'Age in months'
                                },
                                gridLines: {
                                    display: false
                                },
                                ticks: {
                                    autoSkip: false,
                                    callback: function (value, index, values)
                                    {
                                        if (value % 12 === 0) {
                                            return value;
                                        }
                                    }
                                }
                            }],
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
