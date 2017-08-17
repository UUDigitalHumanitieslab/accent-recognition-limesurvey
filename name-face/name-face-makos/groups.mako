<row>
    <gid><![CDATA[${starting_group_id}]]></gid>
    <sid><![CDATA[${survey_id}]]></sid>
    <group_name><![CDATA[Intro]]></group_name>
    <group_order><![CDATA[0]]></group_order>
    <description><![CDATA[<p>Welkom</p>
]]></description>
    <language><![CDATA[en]]></language>
    <randomization_group/>
    <grelevance/>
</row>
<%
    group_id =  starting_group_id + 1
%>
<row>
    <gid><![CDATA[${group_id}]]></gid>
    <sid><![CDATA[${survey_id}]]></sid>
    <group_name>Persoonlijke informatie</group_name>
    <group_order>1</group_order>
    <description/>
    <language>en</language>
    <randomization_group/>
    <grelevance/>
</row>
<%
    Q = 0
%>
% for i in range(starting_group_id + 2, starting_group_id + len(questions) + 2):
    <%
        Q += 1
    %>
<row>
    <gid><![CDATA[${i}]]></gid>
    <sid><![CDATA[${survey_id}]]></sid>
    <group_name><![CDATA[Q${Q}]]></group_name>
    <group_order><![CDATA[${i}]]></group_order>
    <description/>
    <language><![CDATA[en]]></language>
    <randomization_group/>
    <grelevance/>
</row>
% endfor