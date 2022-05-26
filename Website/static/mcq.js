alert("hello")

//Timer for each Question
                var total_seconds = 10 * 1;
                var c_minutes = parseInt(total_seconds / 60);
                var c_seconds = parseInt(total_seconds % 60);
                var timer;

                function CheckTime() {
                    if (total_seconds <= 0){
                        document.getElementById("quiz-time-left").innerHTML = 'Time Left: ' + c_minutes + ' minutes ' + c_seconds + ' seconds ';
                    }
                else{

                    document.getElementById("quiz-time-left").innerHTML = 'Time Left: ' + c_minutes + ' minutes ' + c_seconds + ' seconds ';   //the display statement
                    total_seconds = total_seconds - 1; //updating value of total seconds
                    c_minutes = parseInt(total_seconds / 60);  //updating the value of minute
                    c_seconds = parseInt(total_seconds % 60);  //updating the value of seconds
                    timer = setTimeout(CheckTime, 1000); //after every one second the function CheckTime will run
                }
                }                
                timer = setTimeout(CheckTime, 1000); //after every one second the function will run
                    class varimp{
                        static ts1 = 0;
                        static ts2 = 0;
                        static ts3 = 0;
                        static ts4 = 0;
                    }
                    

                    function startTimer1(){
                        
                        var cs = Math.round(varimp.ts1%60);
                        var cm = Math.round(varimp.ts1/60);
                        
                        function et1(){
                            document.getElementById("ShowTimer1").innerHTML = "Time Elapsed " + cm + " : " + cs + " ";
                            varimp.ts1 = varimp.ts1 + 1;
                            cm = Math.round(varimp.ts1/60);
                            cs = Math.round(varimp.ts1%60);
                            tmr1 = window.setTimeout(et1,1000);
                        }tmr1 = window.setTimeout(et1,1000);
                    }
                    function startTimer2(){
                        
                        var cs2 = Math.round(varimp.ts2%60);
                        var cm2 = Math.round(varimp.ts2/60);
                        
                        function et2(){
                            document.getElementById("ShowTimer2").innerHTML = "Time Elapsed " + cm2 + " : " + cs2 + " ";
                            varimp.ts2 = varimp.ts2 + 1;
                            cm2 = Math.round(varimp.ts2/60);
                            cs2 = Math.round(varimp.ts2%60);
                            tmr2 = window.setTimeout(et2,1000);
                        }tmr2 = window.setTimeout(et2,1000);
                    }
                    function startTimer3(){
                        
                        var cs3 = Math.round(varimp.ts3%60);
                        var cm3 = Math.round(varimp.ts3/60);
                        
                        function et3(){
                            document.getElementById("ShowTimer3").innerHTML = "Time Elapsed " + cm3 + " : " + cs3 + " ";
                            varimp.ts3 = varimp.ts3 + 1;
                            cm3 = Math.round(varimp.ts3/60);
                            cs3 = Math.round(varimp.ts3%60);
                            tmr3 = window.setTimeout(et3,1000);
                        }tmr3 = window.setTimeout(et3,1000);
                    }
                    function startTimer4(){
                        
                        var cs4 = Math.round(varimp.ts4%60);
                        var cm4 = Math.round(varimp.ts4/60);
                        
                        function et4(){
                            document.getElementById("ShowTimer4").innerHTML = "Time Elapsed " + cm4 + " : " + cs4 + " ";
                            varimp.ts4 = varimp.ts4 + 1;
                            cm4 = Math.round(varimp.ts4/60);
                            cs4 = Math.round(varimp.ts4%60);
                            tmr4 = window.setTimeout(et4,1000);
                        }tmr4 = window.setTimeout(et4,1000);
                    }
                    function stopTimer1(){
                        
                        if(document.getElementById('r11').checked == true){
                            document.getElementById('r12').disabled = true;
                            document.getElementById('r13').disabled = true;
                            document.getElementById('r14').disabled = true;  
                            window.clearTimeout(tmr1);
                        }
                        else if(document.getElementById('r12').checked == true){
                            document.getElementById('r11').disabled = true;
                            document.getElementById('r13').disabled = true;
                            document.getElementById('r14').disabled = true;  
                            window.clearTimeout(tmr1);
                        }
                        else if(document.getElementById('r13').checked == true){
                            document.getElementById('r12').disabled = true;
                            document.getElementById('r11').disabled = true;
                            document.getElementById('r14').disabled = true;  
                            window.clearTimeout(tmr1);
                        }
                        else if(document.getElementById('r14').checked == true){
                            document.getElementById('r12').disabled = true;
                            document.getElementById('r13').disabled = true;
                            document.getElementById('r11').disabled = true;  
                            window.clearTimeout(tmr1);
                        }
                    }

                    function stopTimer2(){
                        if(document.getElementById('r21').checked == true){
                            document.getElementById('r22').disabled = true;
                            document.getElementById('r23').disabled = true;
                            document.getElementById('r24').disabled = true; 
                            window.clearTimeout(tmr2); 
                        }
                        else if(document.getElementById('r22').checked == true){
                            document.getElementById('r21').disabled = true;
                            document.getElementById('r23').disabled = true;
                            document.getElementById('r24').disabled = true;  
                            window.clearTimeout(tmr2);
                        }
                        else if(document.getElementById('r23').checked == true){
                            document.getElementById('r22').disabled = true;
                            document.getElementById('r21').disabled = true;
                            document.getElementById('r24').disabled = true;  
                            window.clearTimeout(tmr2);
                        }
                        else if(document.getElementById('r24').checked == true){
                            document.getElementById('r22').disabled = true;
                            document.getElementById('r23').disabled = true;
                            document.getElementById('r21').disabled = true;  
                            window.clearTimeout(tmr2);
                        }
                    }

                    function stopTimer3(){
                        if(document.getElementById('r31').checked == true){
                            document.getElementById('r32').disabled = true;
                            document.getElementById('r33').disabled = true;
                            document.getElementById('r34').disabled = true;  
                            window.clearTimeout(tmr3); 
                        }
                        else if(document.getElementById('r32').checked == true){
                            document.getElementById('r31').disabled = true;
                            document.getElementById('r33').disabled = true;
                            document.getElementById('r34').disabled = true;  
                            window.clearTimeout(tmr3); 
                        }
                        else if(document.getElementById('r33').checked == true){
                            document.getElementById('r32').disabled = true;
                            document.getElementById('r31').disabled = true;
                            document.getElementById('r34').disabled = true;  
                            window.clearTimeout(tmr3); 
                        }
                        else if(document.getElementById('r34').checked == true){
                            document.getElementById('r32').disabled = true;
                            document.getElementById('r33').disabled = true;
                            document.getElementById('r31').disabled = true;  
                            window.clearTimeout(tmr3); 
                        }
                    }

                    function stopTimer4(){
                        if(document.getElementById('r41').checked == true){
                            document.getElementById('r42').disabled = true;
                            document.getElementById('r43').disabled = true;
                            document.getElementById('r44').disabled = true; 
                            window.clearTimeout(tmr4);  
                        }
                        else if(document.getElementById('r42').checked == true){
                            document.getElementById('r41').disabled = true;
                            document.getElementById('r43').disabled = true;
                            document.getElementById('r44').disabled = true;
                            window.clearTimeout(tmr4);   
                        }
                        else if(document.getElementById('r43').checked == true){
                            document.getElementById('r42').disabled = true;
                            document.getElementById('r41').disabled = true;
                            document.getElementById('r44').disabled = true;  
                            window.clearTimeout(tmr4); 
                        }
                        else if(document.getElementById('r44').checked == true){
                            document.getElementById('r42').disabled = true;
                            document.getElementById('r43').disabled = true;
                            document.getElementById('r41').disabled = true;  
                            window.clearTimeout(tmr4); 
                        }
                    }

                    function clearSelection1(){
                        var ele = document.getElementsByName("radio1");
                        for(var i=0;i<ele.length;i++)
                           ele[i].checked = false;
                        document.getElementById('r11').disabled = false;
                        document.getElementById('r12').disabled = false;
                        document.getElementById('r13').disabled = false;
                        document.getElementById('r14').disabled = false; 
                    }
                    function clearSelection2(){
                        var ele2 = document.getElementsByName("radio2");
                        for(var i=0;i<ele2.length;i++)
                           ele2[i].checked = false;
                        
                        document.getElementById('r21').disabled = false;
                        document.getElementById('r22').disabled = false;
                        document.getElementById('r23').disabled = false;
                        document.getElementById('r24').disabled = false; 
                    }
                    function clearSelection3(){
                        var ele3 = document.getElementsByName("radio3");
                        for(var i=0;i<ele3.length;i++)
                           ele3[i].checked = false;
                        
                        document.getElementById('r31').disabled = false;
                        document.getElementById('r32').disabled = false;
                        document.getElementById('r33').disabled = false;
                        document.getElementById('r34').disabled = false; 
                    }
                    function clearSelection4(){
                        var ele4 = document.getElementsByName("radio4");
                        for(var i=0;i<ele4.length;i++)
                           ele4[i].checked = false;
                        
                        document.getElementById('r41').disabled = false;
                        document.getElementById('r42').disabled = false;
                        document.getElementById('r43').disabled = false;
                        document.getElementById('r44').disabled = false; 
                    }
                    function store_t_data(){
                        document.getElementById('t1').value = varimp.ts1;
                        document.getElementById('t2').value = varimp.ts2;
                        document.getElementById('t3').value = varimp.ts3;
                        document.getElementById('t4').value = varimp.ts4;
                    }store_t_data();

//Timer ends here
                 
