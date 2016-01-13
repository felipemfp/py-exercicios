# Implementar uma função que formate uma lista de tuplas como tabela HTML.

def to_table_html(it, formatted = True):
    table_html = "<table>"
    if formatted: table_html += "\n"
    for item in it:
        if formatted: table_html += "\t"
        table_html += "<tr>"
        if formatted: table_html += "\n"
        for element in item:
            if formatted: table_html += "\t\t"
            table_html += "<td>{0}</td>".format(element)
            if formatted: table_html += "\n"
        if formatted: table_html += "\t"
        table_html += "</tr>"
        if formatted: table_html += "\n"
    table_html += "</table>"

    return table_html


if __name__ == "__main__":
    it = [("Membro", "Função"),
          ("Felipe", "Desenvolvedor Front-End"),
          ("Francisco", "Desenvolvedor Back-End"),
          ("Paulo", "Designer de Interface")]
    print(to_table_html(it))


# <table>
# 	<tr>
# 		<td>Membro</td>
# 		<td>Função</td>
# 	</tr>
# 	<tr>
# 		<td>Felipe</td>
# 		<td>Desenvolvedor Front-End</td>
# 	</tr>
# 	<tr>
# 		<td>Francisco</td>
# 		<td>Desenvolvedor Back-End</td>
# 	</tr>
# 	<tr>
# 		<td>Paulo</td>
# 		<td>Designer de Interface</td>
# 	</tr>
# </table>