function load_car_models(company_id,car_model_id){
      var company=document.getElementById(company_id);
      var car_model=document.getElementById(car_model_id);
      {% for company in companies %}
        if (company.value=="{{company}}"){
            {% for model in car_models %}
                {% if company in model %}
                    var newOption=document.createElement("Option");
                    newOption.value="{{model}}";
                    newOption.innerHTML="{{model}}";
                    car_model.options.add(newOption)
                {% endif %}

            {% endfor %}
        }

      {% endfor %}
    }