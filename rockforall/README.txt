
####### CÓDIGOS REUTILIZADOS ######

// Formulário de criação da funcionaliade <criar momentos> no arquivo momentos.html //

<fieldset class="form-label-group form-group position-relative has-icon-left input-divider-left">
	<select name="cidade" class="form-control" id="basicSelect">
		<option>Onde foi ?</option>
		{% for id, cidade in momentos.cidade.field.choices %}
		<option value="{{ id }}">{{ cidade }}</option>
		{% endfor %}
	</select>
	<div class="form-control-position">
		<i class="fa fa-location-arrow" style="color: white;"></i>
	</div>
</fieldset>


<fieldset class="form-label-group form-group position-relative has-icon-left input-divider-left">
	<select name="estado" class="form-control" id="basicSelect">
		<option>UF</option>
		{% for id, estado in momentos.estado.field.choices %}
		<option value="{{ id }}">{{ estado }}</option>
		{% endfor %}
	</select>
	<div class="form-control-position">
		<i class="fa fa-globe" style="color: white;"></i>
	</div>
</fieldset>

############################################################################################################################

// Formulário de criação de anúncios


                                <fieldset class="form-label-group form-group position-relative has-icon-left input-divider-left">
                                    <select name="cidade_mora" class="form-control" id="basicSelect" required>
                                        <option>Cidade onde você reside ?</option>
                                        {% for id, cidade_mora in produtos.cidade_mora.field.choices %}
                                        <option value="{{ id }}">{{ cidade_mora }}</option>
                                        {% endfor %}
                                    </select>
                                    <div class="form-control-position">
                                        <i class="fa fa-location-arrow" style="color: white;"></i>
                                    </div>
                                </fieldset>

                                <fieldset class="form-label-group form-group position-relative has-icon-left input-divider-left">
                                    <select name="estado_mora" class="form-control" id="basicSelect" required>
                                        <option>UF</option>
                                        {% for id, estado_mora in produtos.estado_mora.field.choices %}
                                        <option value="{{ id }}">{{ estado_mora }}</option>
                                        {% endfor %}
                                    </select>
                                    <div class="form-control-position">
                                        <i class="fa fa-globe" style="color: white;"></i>
                                    </div>
                                </fieldset>
                            