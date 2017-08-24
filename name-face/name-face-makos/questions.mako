<row>
    <qid><![CDATA[${starting_question_id}]]></qid>
    <parent_qid><![CDATA[0]]></parent_qid>
    <sid><![CDATA[${survey_id}]]></sid>
    <gid><![CDATA[${starting_group_id}]]></gid>
    <type><![CDATA[T]]></type>
    <title><![CDATA[intro]]></title>
    <question><![CDATA[
        <p>Welkom bij dit onderzoek naar de vraag of je bij een gezicht de juiste voornaam kunt kiezen.</p>

<p>Eerst vragen we een paar persoonlijke gegevens (leeftijd, geslacht, opleiding).
Daarna krijg je steeds een gezicht te zien met daarbij 4 voornamen.
    Aan jou de taak om de voornaam te selecteren die volgens jou het beste bij het gezicht past.</p>

        <p>Aan het einde van de test krijg je te horen of je beter dan kans de juiste voornaam bij een gezicht kunt kiezen.</p>

        <p>Veel succes!</p>

<script src="${name_js_file_ref}"></script><script src="${main_js_file_ref}"></script>
        <link rel="stylesheet" type="text/css" href="${intro_question_css_file_ref}">
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
<%

    group_id = starting_group_id+ 1
    leeftijd_question_id = starting_question_id +1
    gender_question_id = starting_question_id + 2
    education_question_id = starting_question_id + 3
%>

<row>
    <qid><![CDATA[${gender_question_id}]]></qid>
    <parent_qid>0</parent_qid>
    <sid><![CDATA[${survey_id}]]></sid>
    <gid><![CDATA[${group_id}]]></gid>
    <type>L</type>
    <title>Geslacht</title>
    <question><![CDATA[Geslacht: <link rel="stylesheet" type="text/css" href="${personal_questions_css_file_ref}">]]></question>
    <preg/>
    <help/>
    <other>Y</other>
    <mandatory>Y</mandatory>
    <question_order>2</question_order>
    <language>en</language>
    <scale_id>0</scale_id>
    <same_default>0</same_default>
    <relevance>1</relevance>
</row>
<row>
    <qid><![CDATA[${education_question_id}]]></qid>
    <parent_qid>0</parent_qid>
    <sid><![CDATA[${survey_id}]]></sid>
    <gid><![CDATA[${group_id}]]></gid>
    <type>L</type>
    <title>opleiding</title>
    <question><![CDATA[Wat is je hoogst genoten opleiding? <link rel="stylesheet" type="text/css" href="${personal_questions_css_file_ref}">]]></question>
    <preg/>
    <help/>
    <other>Y</other>
    <mandatory>Y</mandatory>
    <question_order>3</question_order>
    <language>en</language>
    <scale_id>0</scale_id>
    <same_default>0</same_default>
    <relevance>1</relevance>
</row>

<row>
    <qid><![CDATA[${leeftijd_question_id}]]></qid>
    <parent_qid>0</parent_qid>
    <sid><![CDATA[${survey_id}]]></sid>
    <gid><![CDATA[${group_id}]]></gid>
    <type>N</type>
    <title>leeftijd</title>
    <question><![CDATA[Wat is je leeftijd? <link rel="stylesheet" type="text/css" href="${personal_questions_css_file_ref}">]]></question>
    <preg/>
    <help/>
    <other>N</other>
    <mandatory>Y</mandatory>
    <question_order>1</question_order>
    <language>en</language>
    <scale_id>0</scale_id>
    <same_default>0</same_default>
    <relevance>1</relevance>
    <modulename/>
</row>
% for i in range(1, len(questions) + 1):
    <%
    id = starting_question_id + i + 3
    group_id = starting_group_id + i + 1
    %>
    <row>
    <qid><![CDATA[${id}]]></qid>
    <parent_qid><![CDATA[0]]></parent_qid>
    <sid><![CDATA[${survey_id}]]></sid>
    <gid><![CDATA[${group_id}]]></gid>
    <type><![CDATA[T]]></type>
    <title><![CDATA[vr${id}]]></title>
    <question><![CDATA[
        <p>Welke voornaam past het best bij het gezicht?</p>
        <script src="${main_js_file_ref}">
</script>
        <link rel="stylesheet" type="text/css" href="${css_file_ref}">
<style type="text/css">.textarea{
    display: None;
  }

</style>
<script>
selection =  {INSERTANS:${survey_id}X${starting_group_id}X${starting_question_id}}
id = "v${i}";
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
<%
    last_question_id = starting_question_id + len(questions) + 4
    last_question_group_id =  starting_group_id + len(questions) + 2
%>

<row>
    <qid><![CDATA[${last_question_id}]]></qid>
    <parent_qid>0</parent_qid>
    <sid><![CDATA[${survey_id}]]></sid>
    <gid><![CDATA[${last_question_group_id}]]></gid>
    <type>L</type>
    <title>Eindvraag</title>
    <question><![CDATA[Herkende je een van de mensen op de foto? <link rel="stylesheet" type="text/css" href=${personal_questions_css_file_ref}>]]></question>
    <preg/>
    <help/>
    <other>N</other>
    <mandatory>Y</mandatory>
    <question_order>1</question_order>
    <language>en</language>
    <scale_id>0</scale_id>
    <same_default>0</same_default>
    <relevance>1</relevance>
</row>
<%
    feedback_id = starting_question_id + len(questions) + 5
    feedback_group_id =  starting_group_id + len(questions) + 3
%>
<row>
    <qid><![CDATA[${feedback_id}]]></qid>
    <parent_qid>0</parent_qid>
    <sid><![CDATA[${survey_id}]]></sid>
    <gid><![CDATA[${feedback_group_id}]]></gid>
    <type>L</type>
    <title>Score</title>
    <question><![CDATA[
        <script src="${main_js_file_ref}"></script>
        <script src="${name_js_file_ref}"></script>
        <link rel="stylesheet" type="text/css" href="${score_css}">
        <script>
        answers = {
        % for i in range(1, len(questions) + 1):
            <%
                id = starting_question_id + i + 3
                group_id = starting_group_id + i + 1
            %>
            "v${i}": "{INSERTANS:${survey_id}X${group_id}X${id}}",
        % endfor
        }

        $(document).ready(function(){
	        showScore(questions, answers);
        })
        </script>
        ]]>
    </question>
    <preg/>
    <help/>
    <other>N</other>
    <mandatory>N</mandatory>
    <question_order>1</question_order>
    <language>en</language>
    <scale_id>0</scale_id>
    <same_default>0</same_default>
    <relevance>1</relevance>
</row>





