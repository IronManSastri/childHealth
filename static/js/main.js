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

    function calculateBMI()
    {
        var calculateBMI = '0';
        var calculatedBSA = '0'
        var height = parseFloat($('[name="height"]').val());
        var weight = parseFloat($('[name="weight"]').val());
        if (height && height >= 75 && weight && Math.round(weight) > 9) {
            document.getElementById("calculatedBMI").textContent = formulaForBmi(height, weight).toFixed(2).toString();
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

    $('.dentalFormHolder,.pediatricsFormHolder').find('input,select').addClass('form-control');

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
})
