<row>
    <qid><![CDATA[${starting_question_id}]]></qid>
    <parent_qid><![CDATA[0]]></parent_qid>
    <sid><![CDATA[${survey_id}]]></sid>
    <gid><![CDATA[${starting_group_id}]]></gid>
    <type><![CDATA[T]]></type>
    <title><![CDATA[intro]]></title>
    <question><![CDATA[Welkom bij deze survey<script src="${name_js_file_ref}"></script><script src="${main_js_file_ref}"></script>
<style type="text/css">.textarea{
    display: None;
  }
</style>
<script>
$(document).ready(function(){
       	selection = makeSelection(Questions)
        str = JSON.stringify(selection)
        str = addSpaces(str)
		$('.textarea').val(str)
})
</script>]]></question>
    <preg/>
    <help/>
    <other><![CDATA[N]]></other>
    <mandatory><![CDATA[N]]></mandatory>
    <question_order><![CDATA[0]]></question_order>
    <language><![CDATA[en]]></language>
    <scale_id><![CDATA[0]]></scale_id>
    <same_default><![CDATA[0]]></same_default>
    <relevance><![CDATA[1]]></relevance>
    <modulename/>
</row>
% for i in range(1, len(questions) + 1):
    <%
    id = starting_question_id + i
    group_id = starting_group_id + i
    %>
    <row>
    <qid><![CDATA[${id}]]></qid>
    <parent_qid><![CDATA[0]]></parent_qid>
    <sid><![CDATA[${survey_id}]]></sid>
    <gid><![CDATA[${group_id}]]></gid>
    <type><![CDATA[T]]></type>
    <title><![CDATA[vr${id}]]></title>
    <question><![CDATA[<script src="${main_js_file_ref}">
</script>
        <link rel="stylesheet" type="text/css" href=${css_file_ref}>
<style type="text/css">.textarea{
    display: None;
  }

</style>
<script>
selection =  {INSERTANS:${survey_id}X${starting_group_id}X${starting_question_id}}
id = "v${i}"
$(document).ready(function(){
	generateQuestion(id, selection[id])
})
</script>]]></question>
    <preg/>
    <help/>
    <other><![CDATA[N]]></other>
    <mandatory><![CDATA[Y]]></mandatory>
    <question_order><![CDATA[1]]></question_order>
    <language><![CDATA[en]]></language>
    <scale_id><![CDATA[0]]></scale_id>
    <same_default><![CDATA[0]]></same_default>
    <relevance><![CDATA[1]]></relevance>
    <modulename/>
</row>
% endfor