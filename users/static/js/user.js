$(document).ready(function () {
    $("#next1").on('click', function () {
        $('#step2').fadeIn('3000');

        $('#step1').css('display', 'none');
        $('#step2').css('display','grid');
        $('#steps').text('2');
        $('#stepText').html('<span>choose your password wisely...</span>');
    });

    $("#back2").on('click', function () {
        $('#step1').fadeIn('3000');
        $('#step1').css('display', 'grid');
        $('#step2').css('display','none');
        $('#stepText').html('<span>choose an username that can easily remembered...</span>');
        $('#steps').text('1');
    });

    $("#next2").on('click', function () {
        $('#step3').fadeIn('3000');
        $('#step2').css('display','none');
        $('#step3').css('display','grid');
        $('#stepText').html('<span>almost there...</span>');
        $('#steps').text('3');

        
        // $('#label1').css('padding-left', '50px');
        // $('#label2').css('padding-left', '0px');
        // $('#label3').css('padding-left', '0px');
        // $('#label4').css('padding-left', '50px');
        // $('#label5').css('padding-left', '0px');

        // $('#fname').css('margin-left', '50px');
        // $('#lname').css('margin-left', '0px');
        // $('#middlei').css('margin-left', '0px');
        // $('#email').css('margin-left', '50px');
        // $('#pnumber').css('margin-left', '0px');

        // $('#fname').css('margin-right', '25px');
        // $('#lname').css('margin-right', '25px');

        // $('#lname').css('width', '300px');
        // $('#fname').css('width', '300px');
        // $('#lname').css('width', '300px');
    });

    $("#back3").on('click', function () {
        $('#step2').fadeIn('3000');
        $('#step1').css('display', 'none');
        $('#step2').css('display','grid');
        $('#step3').css('display','none');
        $('#stepText').html('<span>choose your password wisely...</span>');
        $('#steps').text('2');
    });

    // choose 
    $("#one").on('click', function () {
        $('#one').css('background-color', 'var(--orange)')
        $('#two').css('background-color', 'white')
        $("#r1").prop("checked", true); 
        $("#r2").prop("checked", false); 
        $("#js").css("color", 'white'); 
        $("#jp").css("color", 'var(--dark)'); 
        $("#p1").css("color", 'var(--dark)'); 
        $("#p2").css("color", 'var(--blue)'); 
    });
    $("#two").on('click', function () {
        $('#two').css('background-color', 'var(--orange)')
        $('#one').css('background-color', 'white')
        $("#r2").prop("checked", true); 
        $("#r1").prop("checked", false); 
        $("#jp").css("color", 'white'); 
        $("#js").css("color", 'var(--dark)'); 
        $("#p2").css("color", 'var(--dark)'); 
        $("#p1").css("color", 'var(--blue)'); 
    });

    $('#btn-next').on('click', function () {
        $('#step1').css('display', 'grid');
        $('#con-circle').css('display', 'grid');
        $('#1st').css('display', 'none');
        $('#con-ba-su').css('display', 'none')
        
    });

    // console.log($("#one").attr("value", "Job Seeker"));
    // console.log($("#two").attr("value", "Job Provider"));
});
