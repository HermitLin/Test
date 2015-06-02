    switchfun : function (fieldname, val) {
        switch (fieldname) {
            case 'soot_carry_on_measure' :
                //營業面積
                switch (val) {
                    case 0 :
                        return '小於25坪'
                    case 1 : 
                        return '25～70坪'
                    case 2 : 
                        return '大於70坪'
                    default
                        return 'Error'

                }  

            case 'aaa' :
            case 'soot_smell_in_the_kitchen' :
                //逸散性油煙味
                switch (val) {
                    case 0 :
                        return '無'
                    case 1 : 
                        return '微'
                    case 2 : 
                        return '輕'
                    case 3 : 
                        return '重'
                    default
                        return 'Error'
                }
            case 'soot_see_emission' :
                // 油煙排放目測
                switch (val) {
                    case 0 :
                        return '無'
                    case 1 : 
                        return '少'
                    case 2 : 
                        return '中'
                    case 3 : 
                        return '多'
                    default 
                        return 'Error'
                }
            default : 
                return 'Something Error!'
        }   

        switch (fieldname) {
            case '' : 
                switch (val) {
                    case '' : 
                }

        }
    }







    switch (fieldname) {
        case '' : 
            switch (val) : {
                case '' :

                    return
            }

    }






